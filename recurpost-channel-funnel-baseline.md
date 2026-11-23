# RecurPost: Funnel by Channel, With Baselines

Built 23 Nov 2026 from Mixpanel project "Production Analytics" (2504932).

Confidence labels: **[Certain]** = a direct query result. **[Likely]** = a strong inference. **[Guessing]** = an assumption.

## Definitions

| Stage | Event definition |
|---|---|
| **Traffic** | Unique users who load the web signup page (`Loaded a Page`, path contains `new-user-registration-signup`). Loads referred from `social.recurpost.com` are excluded; these are mostly post-verification reloads. |
| **Signup** | `account_created` |
| **Activation** | `specific_sa_modified` with `actions = added`, meaning the first social account is connected |
| **Paid** | `transactions` with an `event_type` containing `completed` (`subscription.charge.completed` / `order.completed`) |

- **Cohort:** users who entered the funnel between 1 Jun and 22 Oct 2026, so every user has a full 30-day window.
- **Conversion window:** 30 days from the first step. That covers the 14-day trial plus the first charge.
- **Ranges:** the numbers in brackets are 95% confidence intervals (Wilson method). **Use these ranges as the baseline, not the point estimate.**

---

## The uncomfortable truths first

1. **[Certain] The data can't report true acquisition channels (Google, Meta, organic, referral) today.**
   - 71% of signup-page traffic arrives with the referrer `https://recurpost.com/`, so the original source is lost at the marketing site.
   - The marketing site isn't tracked in Mixpanel.
   - The user properties `$initial_referring_domain` and `initial_utm_*` are empty for 1,938 of the 1,939 signups.
   - UTMs appear on fewer than 0.1% of page loads.
   - So the funnel below splits by the channels the data *can* see: web vs iOS app vs Android app, the referrer before the signup page, and UTM-tagged visits.
2. **[Certain] The connected Meta Ads account (Windsor, "Pro Start Me") is not RecurPost's.**
   - Its campaigns are UAE/India lead-gen and WhatsApp campaigns, and it shows zero registrations.
   - Paid-social CAC therefore can't be computed. If RecurPost runs paid ads, that account isn't connected.
3. **[Certain] The mobile apps bring in 20% of signups but only 4% of paying customers.**
   - Web signup→paid is 8.6%; iOS is 1.9% and Android is 1.1%.
   - **[Likely]** Part of this gap is a measurement problem. Some iOS `account_created` events use device UUIDs as `distinct_id`, so later server-side events may not link. Fix identity before you treat the gap as fully real.
4. **[Certain] Tracking changed in October 2026.**
   - Server-side `account_created` (`analytics-php`) began firing: 164 users in October, up from 0 earlier.
   - Over the same month, client-side web signups dropped from about 330 to 228.
   - Blended totals are unaffected, but the October web row below is undercounted. Don't read it as a web decline.

---

## 1. Funnel by channel (cohort 1 Jun – 22 Oct 2026)

| Channel | Traffic | Signups | Visit→Signup | Activated | Signup→Activated | Paid | Activated→Paid | **Signup→Paid** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Web: from recurpost.com** | 2,745 | 1,207 | **44.0%** (42.1–45.8) | 821 | **68.0%** (65.3–70.6) | 118 | **14.4%** (12.1–16.9) | **9.8%** (8.2–11.6) |
| **Web: all other referrers** ¹ | 1,116 | 96 | **8.6%** (7.1–10.4) | 69 | ~72% | 7 | ~10% | ~7% |
| **Web: total (signup page)** | 3,861 | 1,303 | **33.7%** (32.3–35.3) | 890 | **68.3%** | 125 | **14.0%** | **9.6%** |
| **iOS app** | n/a ² | 207 | n/a | 71 | **34.3%** (28.2–41.0) | 4 | 5.6% (2.2–13.6) | **1.9%** (0.8–4.9) |
| **Android app** | n/a ² | 189 | n/a | 37 | **19.6%** (14.5–25.8) | 2 | 5.4% (1.5–17.7) | **1.1%** (0.3–3.8) |
| **All channels (blended)** | — | **1,939** | — | 1,150 | **59.3%** (57.1–61.5) | 139 | **12.1%** (10.3–14.1) | **7.2%** (6.1–8.4) |

¹ Derived by subtracting the recurpost.com row from the web total. **[Likely]** close, but not exact, because a user can appear in both rows.
² App-store traffic isn't in Mixpanel. Use App Store Connect or Google Play Console impressions and installs for this stage.

**Web signups counted by `account_created` (analytics.js)** run 1,532 → 1,041 activated (68.0%) → 132 paid (8.6% signup→paid). This matches the signup-page view above.

### UTM-tagged visits (1 Jan – 22 Oct 2026, a longer window because volume is tiny)

| `utm_source` | Visits | Signups | Visit→Signup | Activated | Paid |
|---|---:|---:|---:|---:|---:|
| RecurPostKB (knowledge base) | 153 | 17 | 11.1% (7.1–17.1) | 14 | **5** |
| ig (Instagram) | 67 | 17 | 25.4% (16.5–36.9) | 6 | 0 |
| Blog | 74 | 1 | 1.4% | 0 | 0 |
| All other UTM sources (about 60) | 350 | 1 | ~0% | 1 | 0 |
| **Total UTM-tagged** | **644** | **36** | **5.6%** | **21** | **5** |

**[Certain]** These sample sizes are too small to support budget decisions. They are directional only. The knowledge base is the only tagged source that produced paying customers.

---

## 2. Baseline scorecard (the numbers to beat)

Weekly volumes use 20.6 weeks (1 Jun – 22 Oct).

| Metric | Baseline | Weekly volume | Watch threshold ³ |
|---|---|---|---|
| Signup-page visit → signup, from recurpost.com | **44%** (42–46) | ~133 visitors → ~59 signups | < 40% |
| Signup → activated, web | **68%** (66–70) | ~51 activated | < 63% |
| Signup → activated, iOS | **34%** (28–41) | ~3.4 activated | n/a (too small) |
| Signup → activated, Android | **20%** (15–26) | ~1.8 activated | n/a (too small) |
| Activated → paid, web | **12.7%** (10.8–14.8) | ~6.4 paid | < 10% |
| Signup → paid, blended | **7.2%** (6.1–8.4) | ~94 signups → ~6.7 paid | < 6% |
| Signups per month, blended | **434** (range 395–457, Jun–Oct) | ~94 | < 390 |
| Mobile share of signups | **20%** | ~19 | — |

³ A watch threshold is roughly the lower bound of the 95% interval. A month below it is unlikely to be noise. **[Likely]** Monthly reads of paid conversion carry ±3–4 points of noise at this volume, so judge paid trends on rolling 8–12-week windows.

---

## 3. What this tells you

1. **[Certain] The web funnel is healthy after signup.** 68% activate and about 1 in 7 activated users pay. The biggest web leak is still the signup form: 56% of visitors arriving from recurpost.com don't create an account. This supports Experiment 1, Google one-click signup, in `recurpost-conversion-experiments.md`.
2. **[Certain] Visitors who reach the signup page from anywhere other than recurpost.com convert at 8.6%, one-fifth the rate of those coming from the marketing site.** **[Likely]** These are mostly low-intent arrivals: blog and help-centre links, bookmarks and sign-in confusion. Ruling this out takes UTM/`src` tagging.
3. **[Certain] The apps underperform at activation, not only at payment.**
   - iOS loses 66% of signups and Android 80% before a social account is connected.
   - **[Guessing]** Possible causes include the OAuth connect flow on mobile and the `sa_connect_failed` event (354 events in the last 30 days).
   - Check `sa_connect_failed` split by `mp_lib` before investing in app acquisition.
4. **[Likely] Taken at face value, mobile users are worth about one-fifth of a web signup.** Don't scale app-store acquisition until identity is fixed and this gap is re-measured.

## 4. What NOT to do

- **Don't allocate marketing budget by channel from this data.** "recurpost.com" is not a channel. It is where every channel ends up after the source is lost.
- **Don't compare October web numbers with earlier months** until the client-side/server-side `account_created` duplication is reconciled.
- **Don't treat the UTM table as channel ROI.** It has 5 paying customers in total.

## 5. Next steps to make this a true channel funnel (ranked)

1. **Persist first-touch source across domains** (1–2 days of engineering).
   - On recurpost.com, capture `utm_*`, `gclid`/`fbclid` and `document.referrer` into a first-party cookie, scoped to `.recurpost.com`.
   - Read the cookie on social.recurpost.com and send it with `account_created`.
   - Set it as `initial_utm_*` / `initial_referrer` with `$set_once`.
   - This is the single change that unlocks every channel split above.
2. **Add the marketing site to Mixpanel** (the Segment `page` call already exists for the knowledge base) so that the Traffic stage counts real sessions, not signup-page loads.
3. **Fix mobile identity.** Call `identify(user_id)` in the iOS and Android SDKs at signup and login so that app signups link to server-side activation and transaction events. Then re-measure the mobile rows.
4. **Reconcile `account_created`.** Choose a single source of truth (server-side) and stop the client-side duplicate, or tag it with `source = client` and exclude it.
5. **Connect the right ad accounts** (RecurPost's Google Ads and Meta) in Windsor so that spend → signup → paid gives a CAC per channel.
6. **Rebuild this report** after 6–8 weeks of clean data, with the channel defined as `initial_utm_source` grouped into Paid Search, Paid Social, Organic Search, Direct, Referral, Email and App Store.

## Saved Mixpanel queries (reproducible)

- Web funnel, signup page from recurpost.com: https://mixpanel.com/project/2504932/view/3046188/app/insights#YcC5TNZWhKvG
- Web funnel, all external referrers: https://mixpanel.com/project/2504932/view/3046188/app/insights#QtWRuTY7EmfU
- Web signup funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#nGf53HvSPeUC
- iOS funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#dbKmAC9xsvK5
- Android funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#U15y9p7u7H2N
- UTM funnel: https://mixpanel.com/project/2504932/view/3046188/app/insights#9cpjGoD4uV7e
- Signups by platform, monthly: https://mixpanel.com/project/2504932/view/3046188/app/insights#wf9csrMMUD9a
