# RecurPost: Google Search Campaign Plan (Paid Signup Activations)

Plan date: 23 Nov 2026. Builds on `recurpost-conversion-experiments.md` (same funnel data and confidence labels).

**[Certain]** = from RecurPost data or the live pages in the earlier audit. **[Likely]** = strong inference. **[Guessing]** = assumption that needs validation (CPCs especially: pull Keyword Planner numbers before launch).

---

## 1. The uncomfortable truths first

1. **[Likely] Generic "social media management" search traffic will probably not pay back at RecurPost's current funnel.**
   - Only **7.3% of new accounts pay within 30 days** [Certain, Jul–Oct cohort], and the blended plan is about **$34.5/month** (50% Personal $25, 25% Starter $9, 25% Agency $79) [Certain mix, list prices].
   - At a $6 CPC and an 8% click-to-signup rate [Guessing], a signup costs ~$75 and a paying customer ~$1,030: a **~30-month payback** on the blended plan.
   - **So the plan only works if it skews to high-intent, high-value searches** (agency, competitor-switcher, evergreen/recycle) and keeps expensive head terms on a short leash.
2. **[Certain] Optimising for purchases as the primary goal from day one will starve Google's bidding.** RecurPost has ~100 signups a week site-wide and ~7 paid conversions per 100 signups, so a new campaign will produce single-digit purchases a month. Smart Bidding needs roughly 15–30+ conversions in 30 days to work [Likely, Google guidance]. Also note: in Google Ads a **"secondary" conversion action does not influence bidding at all.** "Purchase primary, signup secondary" means the algorithm learns only from the rare purchase.
3. **[Certain] The purchase happens 14+ days after the click, inside the app** (14-day trial, no card). Google cannot see it unless you import it (GCLID / enhanced conversions + offline upload). Without that, "optimise for purchases" is not possible at all.
4. **[Certain] Paid clicks will land on the same signup form that loses 58% of visitors who reach it** (no Google sign-on, 6-rule password, phone field, captcha). Every dollar of Search spend is taxed by that leak. Shipping Experiment 1 (Google one-click signup) raises the ROI of this campaign more than any keyword choice.
5. **Two of your targeting ideas will attract the wrong people:**
   - **"Advertising" keywords:** RecurPost is not an ad-buying tool. These searchers want to run ads or hire someone to. Exclude them.
   - **"Agency" keywords:** "social media marketing agency" is searched mostly by people looking to **hire** an agency, not by agencies looking for a tool [Likely]. Target agency-*tool* intent instead ("social media tool for agencies", "white label social media reports").
   - **"Interested in social media marketing":** Search is driven by keywords, not interests. Use audiences only in **Observation** mode to learn and adjust bids, not to target.
6. **[Likely] Adding UAE and Singapore adds conversions at the margin, not volume.** They are small English-language search markets. Search volume is not your bottleneck; qualified-click-to-paid conversion is. Keep them, but don't let them share a budget with the US, where CPCs and volume behave differently.
7. **"Monitor and adjust" is not a plan.** Write the kill and scale thresholds down before launch (section 8), or the campaign will drift on gut feel.

---

## 2. Objective and the numbers that decide success

**Objective:** new paid subscriptions from Google Search at a payback period RecurPost accepts.

**Assumption (change it if wrong):** target payback ≤ 12 months on first-year revenue.

| Keyword theme | Expected plan | Break-even cost per **paid** customer (12 mo) | Break-even cost per **signup** (× 7.3%) |
|---|---|---|---|
| Agency intent | Agency $79 | ~$950 | **~$69** |
| Competitor switchers | Mixed, skews Personal/Agency [Guessing] | ~$500 | **~$37** |
| Core category / SMB | Blended $34.5 | ~$415 | **~$30** |

[Guessing] These assume search-sourced trials convert at the site average of 7.3%. High-intent search traffic often converts better; measure it, then recalculate. Churn and annual-plan discounts are ignored.

**Funnel KPIs to report weekly:**

| Stage | Metric | Owner of the data |
|---|---|---|
| Click | CTR, CPC, search impression share | Google Ads |
| Signup | Cost per `account_created` | Google Ads (imported) + Mixpanel |
| Activation | Cost per activated trial (email confirmed + ≥1 social account connected within 7 days) | Mixpanel → Google Ads import |
| Paid | Cost per `transactions` within 30/45 days, plan mix | Mixpanel → Google Ads offline import |
| Payback | (Cost per paid) ÷ (avg monthly plan value) | Spreadsheet |

---

## 3. Measurement setup (week 0; do not launch without it)

1. **Google tag on both `recurpost.com` and `social.recurpost.com`**, same tag ID, auto-tagging on, conversion linker enabled. Confirm the `gclid` survives the hop to the signup subdomain.
2. **Store `gclid` / `gbraid` / `wbraid` and the hashed email on the user record at signup.** This is what lets you attribute a purchase 14–30 days later.
3. **Enhanced conversions for leads** on the signup form (hashed email).
4. **Offline conversion import for "Activated trial" and "Paid"** from Mixpanel/Segment (Segment's Google Ads conversions destination, or a daily scheduled upload). Send plan value with "Paid".
5. **Conversion windows:** click-through window **60 days** for Paid (14-day trial plus decision time), 30 days for Signup and Activated.
6. **Consent Mode v2** on both domains. Without it, UK conversions will be under-reported.
7. **Populate `signup_method` and persist `utm_*` + `src`** (already in the audit's E1). Paid traffic must be separable from organic in Mixpanel.

**Conversion actions:**

| Action | Phase 1 (weeks 1–6) | Phase 2 (once ≥30 primary conv / 30 days per campaign and Paid import verified) | Value |
|---|---|---|---|
| Signup (`account_created`) | **Primary** | Primary | $30 (= 7.3% × ~$415 expected first-year value) |
| Activated trial | **Primary** | Primary | Set from your activated→paid rate (pull from Mixpanel) [Guessing ~$60–80] |
| Paid (`transactions`) | Secondary (observe) | **Primary** | First-year plan value: Starter $108, Personal $300, Agency $948 |

[Likely] Value-based bidding with these values is how you get "optimise for purchases" without starving the algorithm. It steers toward agency buyers automatically, because their conversions are worth 9× a Starter's.

---

## 4. Campaign structure

Three campaigns. More would split an already small conversion volume.

| Campaign | Geo | Ad groups | Share of budget |
|---|---|---|---|
| **C1 Brand** | US, UK, UAE, SG | RecurPost brand terms | 10% |
| **C2 Non-brand US** | US | Agency, Competitor, Evergreen/Recycle, Core | 60% |
| **C3 Non-brand Intl** | UK, UAE, SG | Agency, Competitor, Evergreen/Recycle (Core only if C2 Core proves profitable) | 30% |

**Settings for every campaign:**
- Search Network only. **Search Partners off, Display expansion off.**
- Location option: **"Presence: people in or regularly in"**, not "presence or interest".
- Language: English (add Arabic as a language setting for UAE only if you have Arabic ads; otherwise English only).
- **Auto-applied recommendations off.** Broad-match and budget recommendations will be pushed at you; ignore them until Phase 2.
- Brand is a separate campaign so it cannot inflate the non-brand results. Report non-brand alone.

**Budget [Guessing, set your own]:** to judge cost per signup you need ~50 signups per non-brand campaign; to get a first read on cost per paid you need ~100–150 signups in total. At ~$50–75 per signup that is **~$6,000–9,000 over 6 weeks (~$150–200/day)**. Below ~$60/day, run only C2 Agency + Competitor and C1 Brand.

---

## 5. Keywords

Start with **exact and phrase match only.** Broad match comes in Phase 2, paired with value-based bidding and a mature negative list.

### Ad group: Agency intent (highest value, highest priority)
- [social media management tool for agencies]
- [social media scheduler for agencies]
- "agency social media management software"
- "social media tool for agencies"
- "white label social media reporting"
- "white label social media scheduler"
- "social media client approval tool"
- "manage multiple social media accounts for clients"
- "social media management for multiple clients"

### Ad group: Competitor switchers
- "hootsuite alternative", "buffer alternative", "sprout social alternative", "later alternative", "meetedgar alternative", "agorapulse alternative", "socialbee alternative"
- "cheaper than hootsuite", "hootsuite vs buffer", "best hootsuite alternatives"
- Do **not** put competitor brand names in ad text; Google may restrict it on a trademark complaint, especially in the UK.

### Ad group: Evergreen / Recycle (RecurPost's differentiator, likely lower CPC)
- "recycle social media posts"
- "evergreen content scheduler"
- "evergreen social media posts tool"
- "repost old social media posts automatically"
- "social media content library scheduler"
- "recurring social media posts"

### Ad group: Core category (expensive; cap it)
- [social media scheduling tool]
- [social media management software]
- [social media scheduler]
- [schedule posts on multiple platforms]
- [social media posting tool]
- Run with a max CPC cap or a portfolio bid limit. Pause any keyword that spends 2× the break-even signup cost ($60) without a signup.

### Brand (C1)
- [recurpost], "recurpost pricing", "recurpost review"
- Exclude "recurpost login" / "recurpost sign in": those are existing users.

### Shared negative list (apply to all non-brand campaigns from day 1)
- **Hiring an agency:** agency near me, hire, services, company, consultant, freelancer for, outsource, quote
- **Ads, not social posting:** advertising, ads manager, facebook ads, google ads, ppc, paid social
- **Learning, not buying:** course, certification, training, tutorial, what is, definition, examples, ideas, tips, pdf, book, degree
- **Jobs:** jobs, job, salary, career, internship, hiring, resume
- **Free-only / low intent:** free download, crack, apk, template, templates
- **Existing users of other tools:** hootsuite login, buffer login, sprout login, support, customer service, cancel
- **Wrong platform fit (review first):** meta business suite, creator studio

Review the search-terms report twice a week for the first 3 weeks and add negatives every time.

---

## 6. Audiences (Observation only, never Targeting)

Add to every non-brand campaign so you can see and bid on differences without narrowing reach:
- **Remarketing lists (RLSA):** all site visitors (30 days); signup-page visitors who did not create an account (30 days); pricing-page visitors.
- **Customer Match exclusions:** current paying customers and active trials (stop paying for people you already have).
- **In-market:** Business Services → Advertising & Marketing Services; Business Software.
- **Custom segment:** people who searched competitor and "social media scheduler" terms.

After 3–4 weeks, if a segment shows ≥2× conversion rate, it will be weighted by Smart Bidding in Phase 2. **Do not switch to Targeting:** it cuts volume on a campaign that is already volume-constrained.

The separate remarketing campaign you are planning should **exclude** people who already converted to paid, and run its own budget so it does not cannibalise the read on Search.

---

## 7. Ads and landing pages

**Message match is the main lever, because the homepage is written for agencies** ("for people who manage many accounts, not one") [Certain]. Sending SMB or core-category clicks there sends them to a page that tells them it is not for them.

| Ad group | Landing page |
|---|---|
| Agency | Homepage, or an agency page (client workspaces, approvals, white-label) |
| Competitor | A comparison page (RecurPost vs [tool]); if none exists, the pricing page |
| Evergreen / Recycle | The evergreen/recycle feature page |
| Core category | Pricing page, **not** the agency homepage |

**RSA starter copy** (verify character counts in the editor; check every feature claim against the live product):

*Agency ad group, headlines (≤30):*
- Social Media Tool for Agencies
- Client Workspaces & Approvals
- White-Label Client Reports
- All Clients, One Calendar
- Recycle Your Best Posts
- Free 14-Day Trial, No Card

*Agency ad group, descriptions (≤90):*
- Schedule, approve and report for every client from one dashboard. Free 14-day trial.
- Plan posts for Facebook, Instagram, LinkedIn, TikTok and more. No credit card needed.

*Competitor ad group, headlines:*
- Switching Social Media Tools?
- Plans From $9/Month
- Recycle Evergreen Posts
- Free 14-Day Trial, No Card

*Core / SMB ad group, headlines:*
- Schedule Posts Everywhere
- Plans From $9/Month
- Recycle Your Best Posts
- One Calendar, All Networks

Use sitelinks (Pricing, Agency features, Evergreen library, Compare), callouts (No credit card, 14-day trial, Client approvals) and a price extension with the three plans.

---

## 8. Bidding, phases and decision rules

### Phase 1: Learn (weeks 1–6)
- **Bidding:** Maximize Clicks with a max CPC cap for the first ~2 weeks (until ≥15 signups per campaign), then **Maximize Conversions** on Signup + Activated trial.
- **Weekly decisions (pre-agreed):**
  - Pause a keyword that spends **2× its ad group's break-even signup cost** with zero signups.
  - Pause an ad group with signup cost **> 1.5× break-even** after ≥20 signups.
  - Shift budget toward the ad group with the lowest cost per **activated** trial (not per signup).
  - If C3 (UK/UAE/SG) cost per activated trial is >1.5× C2 after 4 weeks, cut C3 to UK only.

### Phase 2: Optimise for paid (from week 7, if gates are met)
**Gates:** Paid offline import verified (Google Ads shows imported paid conversions that match Mixpanel ±10%), and ≥30 primary conversions in 30 days per campaign.
- Switch to **Maximize Conversion Value** with all three actions primary and the values in section 3.
- After another 4–6 weeks of stable data, add a **target ROAS** set from your payback target.
- Only then test **broad match** in one ad group, with the negative list in place.

### Scale or kill (week 10–12 readout, once 30-day paid data exists)
- **Scale** (raise budget 20–30% per week) the campaigns and ad groups where cost per paid ≤ break-even and impression share lost to budget > 20%.
- **Kill** non-brand Search if blended cost per paid is > 2× break-even **after** the signup-form fix (Experiment 1) has shipped. Before that fix, the test is penalised by a known 58% form leak.

---

## 9. What NOT to do

- Don't make Purchase the only primary conversion in Phase 1. The campaign will not exit learning.
- Don't target "advertising" or generic "social media marketing" terms. They bring course-seekers, job-seekers and people hiring agencies.
- Don't use Audience Targeting in Search. Observation only.
- Don't turn on Search Partners, Display expansion, or broad match at launch.
- Don't use "presence or interest" location targeting. It serves ads to people outside your four countries.
- Don't mix brand and non-brand in one campaign or report. Brand will make non-brand look profitable.
- Don't judge on Google's reported signups alone. Reconcile with Mixpanel `account_created` and `transactions` weekly.
- Don't change the homepage or signup page mid-flight without logging it. Paid traffic also flows into Experiments 1 and 2 from the audit, so segment those test results by `utm_source=google / utm_medium=cpc`.

---

## 10. Timeline

| Week | Work |
|---|---|
| 0 | Tracking (section 3), negative lists, landing-page mapping, Keyword Planner CPC check, Mixpanel check of paid conversion by country |
| 1–2 | Launch C1 + C2 (+ C3 if budget allows). Maximize Clicks with CPC cap. Search-terms review twice a week |
| 3–6 | Maximize Conversions on Signup + Activated. Weekly pause/shift rules |
| 7 | Phase 2 gate check. Switch to value-based bidding if gates are met |
| 10–12 | First 30-day paid readout. Scale / restructure / kill decision |

---

## Open questions that change the plan

1. **What payback period or target cost per paid customer is acceptable?** Every threshold above depends on it (assumed: 12 months).
2. **What is the monthly test budget?** Below ~$60/day, run Agency + Competitor + Brand only.
3. **Which countries do paying customers come from today?** If US/UK/UAE/SG convert to paid below the site average in Mixpanel, the geo choice needs revisiting before spend, not after.
4. **Do comparison pages and an evergreen/recycle feature page exist?** If not, they are the cheapest way to improve Quality Score and conversion rate on the two best ad groups.
