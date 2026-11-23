# Why paid-ad signups activate at about half the rate of everyone else

Analysis date: 23 Nov 2026. Source: Mixpanel project "Production Analytics" (2504932). Window: signup-page visits from 23 May to 8 Nov 2026, with a 14-day conversion window.

Labels: **[Certain]** = read directly from Mixpanel. **[Likely]** = strong inference. **[Guessing]** = needs validation.

---

## 0. Read this first: Mixpanel cannot see paid traffic today

- **[Certain]** All 2,548 signups in the window have `initial_utm_source` / `initial_utm_medium` set to the literal string `"undefined"`.
- **[Certain]** Every signup has Marketing Channel = "Direct" and an unset `$initial_referring_domain`.
- **[Certain]** Only 11 users in 6 months have a page load with `utm_medium=cpc`, and only 1 has a `gclid` in the URL.

UTMs and click IDs are lost between recurpost.com and social.recurpost.com, and the profile setter writes `String(undefined)`.

I could not find where the "10% vs 24%" figure came from. To reproduce it, I identified paid users through a side channel: the GA cross-domain linker (`_gl=`) on the signup-page URL. That linker carries a `_gcl_aw` cookie only when the visitor arrived from a Google Ads click.
- This catches **Google Ads only**. Meta ads are running (`utm_source=Meta Ads` / `ig` with numeric campaign IDs, and 96 users with `fbclid`) but cannot be isolated.
- Sample sizes are small: 270 paid signup-page visitors and 70 paid signups.

## 1. The gap, reproduced

Activation here means a first post (`one_off_post_modified`) within 14 days of signup.

| Step | Paid (Google Ads, `_gcl_aw`) | Everyone else |
|---|---|---|
| Signup-page visitors | 270 | 5,182 |
| → account created | 26% (70) | 34% (1,767) |
| Account → social account connected | 53% | 68% |
| Connected → first post | 27% | 41% |
| **Account → first post (activation)** | **14% (10/70)** | **28% (491/1,767)** |
| Account → plan selected | 4% | 9% |
| Account → `sa_connect_failed` | 9% | 10% |

**[Certain]** The gap shows up at both post-signup steps (connect, then post). Connection failures are the same for both groups, so this is not an OAuth or technical bug.
**[Likely]** A 95% confidence interval on 10/70 is roughly 7–24%. The direction is solid; the exact size is not.

## 2. Root causes, ranked

### Cause 1: Paid spend is concentrated in a low-intent India segment
| Segment | Share of paid signups | Paid activation | Organic activation, same country |
|---|---|---|---|
| India | 63% (44/70) | **9%** (4/44) | 25% (177/705) |
| United States | 23% (16/70) | 31% (5/16) | 41% (129/314) |

- **[Certain]** Paid India users submit the signup form an average of **83 seconds** after the page loads. Organic India users take about 4,300 seconds (about 70 minutes).
- **[Certain]** 96% of paid India signup-page visitors create an account (organic India: 87%), yet only 9% post.
- Taken together, sign-up is effortless while intent is low.
- **[Likely]** The campaigns are buying cheap, fast form-fills (students, job seekers, free-tool searchers) rather than buyers.
- **[Guessing]** The Google Ads conversion action is `account_created` / signup. If so, Smart Bidding is being rewarded for exactly this behaviour and will keep finding more of it. **Verify this in Google Ads first; it decides whether Fix 2 is the main lever.**

Country mix alone accounts for part of the gap. Paid users still trail organic users within the same country, so targeting quality is the larger factor.

### Cause 2: Paid "agency / for others" signups stall after connecting one account
| Persona (`persona_group`) | Paid activation | Organic activation |
|---|---|---|
| `for_others` (agency/freelancer) | **8%** (2/26) | 25% (48/192) |
| `own_brand` | 23% (6/26) | 44% (46/105) |
| `exploring` | 25% (2/8) | 37% (22/60) |

- **[Certain]** Paid `for_others` users reach the connect step (58%), but only 13% of connectors then post.
- **[Likely]** An agency user signing up from an ad has no client accounts connected and often has no access to them yet. The onboarding asks them to connect accounts and schedule a post, so they connect their own test profile and stop.
- The homepage and ads lean agency-first (see `recurpost-conversion-experiments.md`), so paid traffic over-indexes on this persona: 37% of paid signups against about 11% of organic signups.

### Cause 3: The time to a first post is long for everyone, and paid users have the least patience
- **[Certain]** Connected → first post takes about 1.1 days on average for organic users and about 1.4 days for paid users. Only 27% of paid connectors ever post.
- **[Likely]** Nothing in onboarding gets a user to a scheduled post in the same session. This affects every user, but low-intent paid users drop out first.

### Ruled out
- **Social-account connection errors:** same rate (9% vs 10%).
- **Signup-form friction:** paid users complete the form *faster* and at a *higher* rate per visitor in India. Making the form easier will not fix paid activation, and could make quality worse.

---

## 3. The fixes I will make

Ordered by dependency, then by expected impact.

### Fix 1: Repair paid attribution (week 1; blocks measuring everything else)
1. On recurpost.com, capture `utm_*`, `gclid`, `gbraid`, `wbraid` and `fbclid` on landing, then append them to every signup CTA link (or store them in a first-party cookie on `.recurpost.com`).
2. On social.recurpost.com, read those values at signup. Write them to the profile as `initial_utm_*`, `initial_gclid` and `initial_fbclid`, using **set-once** semantics, and add them to the `account_created` event.
3. Fix the setter that writes the string `"undefined"`: skip null or undefined values instead of stringifying them. Backfill is not possible, so accept the history gap.
4. Rebuild the Marketing Channel custom property on the corrected fields.
5. **Done when:** at least 95% of signups that carry `_gcl_aw` in their linker also carry `initial_utm_medium=cpc` or a `gclid`, for 2 consecutive weeks.

### Fix 2: Optimize ad bidding for activation, not signup (week 1–2)
1. Create a new Google Ads conversion action, "Activated: first post scheduled". Send it via offline conversion import or server-side enhanced conversions, keyed on the stored `gclid`, when `one_off_post_modified` first fires within 14 days.
2. Make it the **primary** bidding conversion. Demote "signup" to secondary/observation.
3. Do the same for Meta with a Conversions API custom event.
4. **Why:** if bidding rewards signups, the 83-second India form-fills are the cheapest conversions and the algorithm will keep buying them. Changing the goal fixes targeting continuously. Hand-tuned exclusions don't.
5. **Risk:** conversion volume drops about 5×, roughly 1–2 Google conversions a week at current spend. That is below Smart Bidding's comfort zone. If volume is too thin, use "connected a social account" (about 2× more frequent) as the primary goal until volume allows.

### Fix 3: Stop the India paid leak now (this week, no engineering)
1. Split India into its own campaign with its own budget and a target CPA based on **activated** users, not signups.
2. Until Fix 2 has 4+ weeks of data, cut India paid budget by about 50% and move it to the US/UK/CA/AU campaigns, where paid activation (31% US) is closer to organic levels.
3. Pull the search-terms report for India and add negatives for job, free, student, course, template, download and "free tool" style queries.
4. **Do not** cut India entirely. Organic India activates at 25%, so the market can produce activators; the paid targeting is what's broken.

### Fix 4: An agency onboarding path that doesn't need client access on day one (2–3 sprints; A/B test)
For users with `persona_group = for_others`:
1. After persona selection, offer **"Invite your client to connect their account"** (a shareable connect link). This replaces "connect your accounts" as the only option.
2. Pre-load a **demo client workspace** with a sample calendar, so the user can schedule and preview a post before real client access exists.
3. Give credit for the first post to the user's own brand account if they have one: "Start with your own agency's page."
4. **Test:** a 50/50 split on `for_others`, all channels. The primary metric is first post within 14 days; the guardrail is first-week churn.
5. **[Guessing]** Expected effect: paid `for_others` activation from 8% to 15–20%. The sample is small, so judge it on the combined organic and paid `for_others` cohort (about 50 a month).

### Fix 5: First post in the same session as connecting an account (1 sprint; A/B test, benefits everyone)
1. Immediately after the first `specific_sa_modified`, open the composer with an AI-drafted post for that account (the `ai_post_modified` flow exists) and default the schedule to the next best time slot.
2. Fire a 24-hour email or in-app nudge if a user has connected an account but not posted.
3. **Target:** connected → first post from 41% to 50% overall, and from 27% to 40% for paid.

### Fix 6: Message match from ad to landing page (after Fix 1, so it can be measured)
- Send paid clicks to a campaign-specific landing page (agency keywords → agency page; "scheduler" keywords → SMB page). Pass `?plan=` and `?persona=` through to signup, so onboarding skips questions the ad already answered.
- I've ranked this last because the data shows the problem is after signup, not before it.

---

## 4. What not to do
- **Don't scale paid spend** until Fix 2 is live. Every extra dollar buys more 9%-activation signups.
- **Don't run the Google one-click signup test on paid traffic alone** as a fix for this problem. It would make sign-up even easier for a segment that already signs up too easily.
- **Don't judge paid campaigns on CPA per signup.** Report cost per activated user and 30-day trial-to-paid by campaign.

## 5. How we'll know it worked (review 6 weeks after Fix 1 ships)
| Metric | Today | 6-week target |
|---|---|---|
| Signups with paid attribution captured | ~0% | ≥95% of `_gcl_aw` signups |
| Paid activation (first post ≤14d) | 14% | ≥20% |
| Paid India share of paid signups | 63% | ≤40% |
| Cost per activated paid user | unknown (no attribution) | baseline set in week 2, −30% by week 6 |

## 6. Open questions that would change this plan
1. Where does the "10% vs 24%" number come from, and how is "activation" defined there? This analysis uses first post within 14 days and gets 14% vs 28%.
2. What is the primary conversion action in Google Ads and Meta today? If it is already activation-based, Fix 2 drops out and Fix 3 becomes the lead.
3. What share of paid spend goes to India, and to which campaigns? (Campaign IDs seen: 24361769993, 24373482924, 24395739243.)

## Appendix: Mixpanel reports used
- Paid funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#9CnDGHJL1Nrz
- Non-paid funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#E71BJ7jszbqF
- Paid by country: https://mixpanel.com/project/2504932/view/3046188/app/insights#hR2PYktBz4zg
- Paid by persona: https://mixpanel.com/project/2504932/view/3046188/app/insights#mLUZhcpqULoa
- Non-paid by persona: https://mixpanel.com/project/2504932/view/3046188/app/insights#Q2rdPKuo3VXW
