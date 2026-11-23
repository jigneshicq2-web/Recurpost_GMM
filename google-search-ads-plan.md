# RecurPost: Google Search Campaign Plan (v2, detailed)

Plan date: 23 Nov 2026. Replaces v1 of this file. Builds on `recurpost-conversion-experiments.md`.

**Build files** (Google Ads Editor import format) are in `google-ads-build/`:
- `keywords.csv`: 294 keywords, each with its landing page.
- `negatives.csv`: the shared negative list.
- `responsive-search-ads.csv`: 18 RSAs (15 headlines and 4 descriptions each; lengths checked).
- `assets.csv`: sitelinks, callouts and price assets.
- `build_ads.py`: regenerates all four files.

**Confidence labels:**
- **[Certain]** = from RecurPost's Mixpanel project ("Production Analytics"), the live site, or the earlier audit.
- **[Likely]** = strong inference.
- **[Guessing]** = assumption to validate. Every cost-per-click (CPC) number is a guess, because Keyword Planner was not reachable from here.

**Mixpanel queries used** (signups 15 May–20 Oct 2026, 30-day conversion window):
- signup → paid, broken down by country;
- signup → social account connected → paid;
- signup → first post → paid;
- signup → plan selected → paid;
- plan selected by country and plan.

---

## 0. What changed from v1, and why

v1 used RecurPost's blended signup→paid rate of 7.3%. **[Certain] That number is misleading for this campaign**, because it is dragged down by markets you will not target:

| Market | Signups | Paid within 30 days | Signup → paid |
|---|---|---|---|
| **United Kingdom** | 101 | 28 | **27.7%** |
| **United States** | 443 | 88 | **19.9%** |
| Australia | 32 | 7 | 21.9% |
| Canada | 47 | 8 | 17.0% |
| Singapore | 10 | 1 | 10% (too few to judge) |
| UAE | 22 | 1 | 4.5% (too few to judge) |
| India | 804 | 9 | 1.1% |
| Vietnam | 258 | 1 | 0.4% |
| All countries | 2,229 | 167 | 7.0% |

This has three consequences:
1. **Paid search in the US and UK is roughly 3× more viable than v1 said.** Break-even cost per signup is about $60, not $30 (section 3).
2. **Your geo choice needs to change** (section 4).
3. **Your agency-keyword emphasis needs to change** (section 1, point 2).

---

## 1. The uncomfortable truths first

1. **[Certain] UAE and Singapore are the weakest evidence in your market list. Canada and Australia are proven and missing.**
   - UAE and Singapore together produced 32 signups and 2 paying customers in five months.
   - Canada and Australia produced 79 signups and 15 paying customers (19%).
   - **I disagree with targeting UAE and Singapore at launch,** because there is no evidence they pay and their search volume is small.
   - **Instead:** launch US, UK, Canada and Australia. Keep UAE + Singapore as a paused test campaign, switched on only with a capped budget and a kill rule (section 6).
   - **The risk in your approach:** splitting a ~$150/day budget across two weak markets slows learning in the two that pay.
2. **[Certain] English-market buyers are mostly small accounts, not agencies.** Of plan selections:
   - **US:** Starter 44%, Personal 43%, Agency 13%.
   - **UK:** Starter 65%, Personal 28%, Agency 7%.
   - **Canada + Australia:** 1 Agency selection out of 35.

   Agency keywords are still worth running, because each Agency customer is worth $79/month. But the **volume** in these markets is small businesses and solo marketers. The plan therefore leads with small-business, evergreen and competitor-switcher intent.
3. **[Certain] The homepage tells small businesses it is not for them.** It reads "for people who manage many accounts, not one" and "Not the best fit when… you need only one or two Meta accounts". It must not be the landing page for non-agency ads. RecurPost already has `/use-cases/smbs/`, `/features/schedule/evergreen-content-marketing/` and 40+ `/compare/alternatives/…` pages. Every ad group below lands on a matching page.
4. **[Certain] You cannot bid on purchases directly at this budget, but there is a strong early signal.**
   - **Every paying customer in these markets first connected a social account.** 69% of signups connect one, on average ~7 hours after signup, and 30% of those who connect go on to pay.
   - Paid conversions arrive on average ~8 days after signup.
   - So **"social account connected" is the conversion to bid on.** It is fast, plentiful, and a near-necessary step to purchase.
   - "Account signup" stays as a secondary, reporting-only conversion.
   - This is how you get "optimise for purchases" without starving the algorithm.
5. **[Certain] Paid clicks still land on a signup form that loses 58% of the visitors who reach it** (from the earlier audit). Shipping Google one-click signup (Experiment 1) raises the return on every dollar here.
6. **[Guessing] US CPCs for these terms are likely $3–10.** At a $6 CPC, signups break even only if ≥10% of clicks sign up. That is achievable on high-intent terms and unlikely on generic ones. That is why generic "core" terms get a separate, capped campaign.

---

## 2. Objective

**Goal:** new paying subscriptions from Google Search in US/UK/CA/AU, at a cost no higher than 12 months of the customer's revenue (assumed payback target; change it and the numbers in section 3 scale linearly).

**Primary KPI:** cost per paying customer (30-day), by market.

**Bidding KPI:** cost per social-account-connected signup.

**Early warning KPI:** the share of ad-sourced signups that connect a social account. The baseline is 69% [Certain]. **If paid search signups connect at below 55%, the traffic is low quality**, whatever the cost per signup says.

---

## 3. Unit economics and targets

**Average plan value per paying customer** uses list prices (Starter $9, Personal $25, Agency $79), monthly billing, and each market's plan mix [Certain mix]:
- US: ~$25/month
- UK: ~$18/month
- Canada + Australia: ~$19/month

Annual-plan discounts and churn are ignored [Guessing].

| Market | First-year value | Signup → paid | **Break-even cost per signup** | **Break-even cost per account-connected** | **Target CPA (account-connected, 70% of break-even)** | Break-even cost per paying customer |
|---|---|---|---|---|---|---|
| US | $300 | 19.9% | **$60** | **$90** | **$63** | $300 |
| UK | $221 | 27.7% | **$61** | **$66–88**¹ | **$47** | $221 |
| CA + AU | $230 | 19.0% | **$44** | **$69** | **$47** | $230 |

¹ The 30% connected→paid rate is the blended rate for all four markets. The UK's rate is probably higher, given its signup→paid rate. Use $47 until UK data comes in.

**Budget sizing.** Six weeks needs:
- ~60 US signups;
- ~40 UK/CA/AU signups;
- brand coverage.

Expected result: ~20 paying customers [Guessing, assumes ad-sourced trials convert at the market average]. That is enough for a first cost-per-paid read.

---

## 4. Account structure

| # | Campaign | Geo | Daily budget | Ad groups | Status at launch |
|---|---|---|---|---|---|
| C1 | `RP \| Search \| Brand \| US-UK-CA-AU` | US, UK, CA, AU | **$15** | Brand; Brand Pricing & Reviews | On |
| C2 | `RP \| Search \| NB High-Intent \| US` | US | **$60** | Competitor Alternatives; Evergreen & Recycle; Small Business; Agency; Google Business Profile; Bulk Scheduling | On |
| C3 | `RP \| Search \| NB Core \| US` | US | **$25** | Core Scheduler (exact match only) | On, with CPC cap |
| C4 | `RP \| Search \| NB High-Intent \| UK-CA-AU` | UK, CA, AU | **$45** | Same as C2 | On |
| C5 | `RP \| Search \| NB Test \| AE-SG` | UAE, Singapore | $8 | Competitor; Evergreen; Small Business | **Paused** (optional, section 6) |
| | **Total** | | **$145/day (~$6,100 over 6 weeks)** | | |

**Why it is split this way:**
- Generic "core" terms get their own capped campaign, so they cannot eat the high-intent budget.
- Brand is isolated so it cannot make non-brand results look profitable.
- UK, Canada and Australia share one campaign, because each alone is too small to train bidding. Check the per-country split in the Locations report weekly.

**Settings for every campaign:**

| Setting | Value | Why |
|---|---|---|
| Networks | Google Search only. **Search Partners off, Display off** | Partner/Display traffic dilutes quality |
| Locations | As above. **"Presence: people in or regularly in your locations"** | The default "presence or interest" serves ads to India and elsewhere |
| Excluded locations | None needed with Presence; add India and Vietnam if they show up in the Locations report | 1% paid rate there [Certain] |
| Language | English | |
| Ad schedule | All hours for the first 4 weeks; review hour/day data after that | Too little data to cut sooner |
| Devices | All. Review mobile after 4 weeks | The signup form is weaker on mobile (earlier audit) |
| Auto-applied recommendations | **Off** | Prevents automatic broad match and budget raises |
| Broad match | **Off** until Phase 3 | |
| Ad rotation | Optimise | |
| Tracking template | `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}&src=gads` | Lets Mixpanel separate paid search from the CTA tests |

---

## 5. Ad groups, keywords and landing pages

Full list: `google-ads-build/keywords.csv`. Phrase and exact match only.

| Ad group | Intent | Example keywords | Landing page [Certain, live] | Expected buyer |
|---|---|---|---|---|
| **Competitor Alternatives** | Switchers, highest intent | "hootsuite alternative", "apps like sprout social", "cheaper than buffer app", "meetedgar alternatives" (15 competitors) | `/compare/alternatives/<competitor>/` set per keyword; `/migrate/` for "switch…" | All plans |
| **Evergreen & Recycle** | RecurPost's differentiator, likely lowest CPC [Guessing] | "recycle social media posts", "evergreen content scheduler", "recurring social media posts" | `/features/schedule/evergreen-content-marketing/` | Starter / Personal |
| **Small Business** | The main English-market buyer | "social media scheduler for small business", "affordable social media scheduler" | `/use-cases/smbs/` | Starter / Personal |
| **Agency** | Low volume, high value | "social media tool for agencies", "white label social media reports", "social media approval workflow" | `/use-cases/agencies/` | Agency |
| **Google Business Profile** | Niche many competitors under-serve [Likely] | "schedule google business profile posts", "multi location social media management" | `/schedule-google-business-profile-posts/` | Personal / Agency |
| **Bulk Scheduling** | Power users | "bulk schedule social media posts", "csv social media scheduler" | `/features/schedule/bulk-scheduling/` | Personal / Agency |
| **Core Scheduler** (C3 only) | Generic, expensive | [social media scheduler], [social media management software] | `/plans-and-pricing/` | Mixed |
| **Brand** (C1 only) | Navigational | [recurpost], "recurpost pricing", "recurpost review" | Homepage / pricing | Mixed |

**Removed from your original idea:**
- "advertising" terms;
- "social media marketing" as a broad theme;
- "agency" terms phrased as hiring intent ("social media marketing agency").

These are now negatives.

**Negatives** (`google-ads-build/negatives.csv`): one shared list of 70+ phrase-match terms on all non-brand campaigns. It covers:
- hiring an agency;
- running ads;
- courses and education;
- jobs;
- free downloads and templates;
- login/support/cancel for other tools;
- follower-buying.

The brand campaign also excludes "recurpost login / sign in / support / cancel", because those searchers are existing users.

---

## 6. Optional UAE + Singapore test (C5)

Switch it on only if you specifically want to test these markets. Rules:
- Budget $8/day, high-intent ad groups only.
- **Stop after $600 spend** if:
  - cost per account-connected is above $94 (2× the international target); **or**
  - there is not at least one plan selection.
- Do not merge it into C4. The two paying customers it has to go on would be lost inside the UK/CA/AU data.

---

## 7. Ads and assets

Full copy: `google-ads-build/responsive-search-ads.csv` and `assets.csv`. All headlines are ≤30 characters, descriptions ≤90 and paths ≤15.

**Claims used, all taken from the live site or audit:**
- 14-day free trial, no credit card;
- plans from $9/month; Agency $79/month;
- 10 networks;
- evergreen libraries;
- AI captions and images;
- bulk scheduling and RSS import;
- client approvals, white-label reports, roles and permissions, social inbox.

**Before launch, have someone confirm:** that the social inbox and AI tools are included on Starter, and that prices are shown as monthly billing.

**Not used, on purpose:**
- Competitor names in ad text. Google can restrict them on a trademark complaint, especially in the UK.
- Ratings (unverified).
- "Unlimited" claims.

**Each ad group has its own angle:**
- **Small Business:** "Manage Your Own Social Media", "Plans From $9/Month", "Set It Once, Keep Posting".
- **Agency:** "Client Workspaces & Approvals", "White-Label Client Reports", "Agency Plan From $79/Month".
- **Competitor:** "Switching Social Media Tools?", "Compare Before You Renew", "See How to Switch".
- **Evergreen:** "Auto-Reshare Evergreen Posts", "Never Run Out of Posts", "Content Libraries That Repeat".

**Assets (account level):**
- **8 sitelinks:** Pricing, SMBs, Agencies, Evergreen, Compare, White-Label, Migrate, Bulk.
- **9 callouts.**
- **Price asset:** Starter $9, Personal $25, Agency $79.
- **Optional:** add the logo and business name assets in the account.

**Pinning:** pin nothing at launch. After 3 weeks, if one ad group's "Free 14-Day Trial, No Card" or price headline clearly outperforms, pin it to position 2 in that ad group only.

---

## 8. Measurement setup (week 0; launch is blocked until this is done)

### 8.1 Conversion actions

| Conversion action | Source | Fires when | Category | Phase 1 role | Count | Click window | Value |
|---|---|---|---|---|---|---|---|
| **Social account connected** | Offline import (server) or server-side tag | First successful social account connection within 7 days of signup (Mixpanel `specific_sa_modified` [Likely]; confirm it means "connected") | Qualified lead | **Primary** | One | 30 days | US $90 / Intl $66, or a flat $75 |
| Account signup | Google tag on signup success + enhanced conversions | `account_created` | Sign-up | Secondary | One | 30 days | $0 |
| First post scheduled | Offline import | First `one_off_post_modified` (34% of signups; 40% of these pay) | Qualified lead | Secondary | One | 30 days | — |
| Plan selected | Offline import | `plan_selected` (25% of signups; 81% of these pay, ~7 days after signup) | Converted lead | Secondary (Phase 3 candidate) | One | 60 days | Plan first-year value |
| **Paid subscription** | Offline import | First `transactions` | Purchase | Secondary (reporting) | One | 60 days | Actual first payment × 12 |

**Why "social account connected" and not signup:**
- **[Certain]** Signups that never connect an account essentially never pay (129 of 130 payers in these markets connected first).
- It filters out tire-kickers, yet still fires for 69% of signups within hours. Google can therefore learn from it inside the 6-week window.

### 8.2 Engineering checklist

1. **One Google tag** on `recurpost.com` and `social.recurpost.com`, with auto-tagging on and the conversion linker on. Test that a `gclid` from an ad click is still present when `/new-user-registration-signup/` loads.
2. **At `account_created`, store on the user record:** `gclid`, `gbraid`, `wbraid`, signup timestamp, hashed email, and `utm_*`/`src`.
3. **Enhanced conversions for leads:** send the hashed email with the signup conversion.
4. **Offline upload job (daily):** for users with a stored click ID or email, upload "Social account connected", "First post scheduled", "Plan selected" and "Paid subscription", each with its timestamp and value. Use the Google Ads API, scheduled CSV uploads, or Segment's Google Ads Conversions destination.
5. **Consent Mode v2** on both domains. Without it, UK conversions are under-counted and bidding there is starved.
6. **Mixpanel:** persist `utm_source/medium/campaign/term` and `src=gads` onto the user profile at signup, so there is one view of ad-sourced cohorts.
7. **QA:** run a test click → signup → connect account → confirm each conversion appears in Google Ads within 24–48 hours.

---

## 9. Audiences (Observation mode only)

Add to C2, C3, C4 and C5:
- **Remarketing:** all visitors (30 days), signup-page visitors who did not sign up (30 days), pricing-page visitors (30 days).
- **Customer Match exclusion:** current paying customers, plus trial users from the last 30 days.
- **In-market:** Business Services > Advertising & Marketing Services; Business Productivity Software.
- **Custom segment:** people who searched competitor names, "social media scheduler", or "evergreen content".

Review conversion rate by segment at week 4. Do **not** switch any segment to Targeting: it shrinks a campaign that is already volume-limited.

---

## 10. Bidding phases and gates

| Phase | When | Bidding | Primary conversion | Gate to move on |
|---|---|---|---|---|
| **1. Collect data** | Weeks 1–2 | **Maximize Clicks** with max CPC caps: C2/C4 $8, C3 $6, C1 $2 [Guessing; raise if impression share lost to rank is >50%] | Social account connected | ≥15 account-connected conversions in the campaign |
| **2. Learn** | Weeks 3–6 | **Maximize Conversions** (no target) | Social account connected | ≥30 conversions in 30 days **and** cost stable for 2 weeks |
| **3. Control cost** | Week 7+ | **Target CPA**: US $63, Intl $47 (section 3). Set it at the trailing 30-day CPA first, then step down 10% every 2 weeks | Social account connected | — |
| **4. Optimise for revenue** (only if volume allows) | When a campaign reaches ≥30 plan selections in 30 days (≈$300+/day spend) | **Maximize Conversion Value → target ROAS** | Plan selected (with plan value) | — |

**Change discipline:** after a bid-strategy switch, change nothing (budget, keywords or bids) for 7 days, except adding negatives. Change budgets by at most 20% at a time.

---

## 11. Optimisation cadence

| When | Task | Rule |
|---|---|---|
| **Daily, weeks 1–2** (10 min) | Spend pacing, disapprovals, conversion tracking alive | If no signups have been recorded for 48 hours while clicks continue, assume tracking broke and pause |
| **Mon + Thu, weeks 1–3; weekly after** | Search terms report | Add a negative for any term with no relevance. Add an exact keyword for any converting term not yet in the list |
| **Weekly (Monday)** | Keyword and ad group review | Apply the decision rules below |
| **Weekly** | Mixpanel reconciliation | Compare Google-reported signups and connections with Mixpanel ad-sourced cohorts. A gap over 20% means a tracking problem |
| **Every 2 weeks** | Ad copy | Replace "Low"-rated headlines; keep 15 per ad |
| **Week 4** | Audience, device, hour-of-day and location review | Adjust bids only where the gap is ≥30% with ≥20 conversions |
| **Week 6** | Phase gate review | Section 10 |
| **Weeks 10–12** | Paid-customer readout | Scale/kill (below) |

### Decision rules (agree before launch)

**Keyword:**
- **Pause** if spend ≥ 2× the market's break-even cost per signup with 0 signups (US $120; UK/CA/AU $90).
- **Lower bids 20%** if cost per account-connected > 1.5× target after ≥5 conversions.

**Ad group:**
- After ≥20 signups, if the share of signups that connect an account is below 55%, the traffic is low quality. Tighten match types, add negatives, and check the landing page before spending more.

**Core campaign (C3):** after 4 weeks, pause it if cost per account-connected is > 1.5× the C2 average. Move its budget to C2.

**Market (within C4):** after 6 weeks, if one country's cost per account-connected is > 1.5× the others, lower its bid adjustment by 30%.

**Scale:** if a campaign's cost per account-connected is ≤ target and it is losing >20% impression share to budget, raise its budget 20% per week while CPA stays within 15%.

**Paid readout, weeks 10–12, per market:**

| Cost per paying customer vs break-even | Action |
|---|---|
| ≤ 1.0× | Scale |
| 1.0–2.0× | Keep, cut weakest ad groups, re-check after the signup-form fix |
| > 2.0× | Stop non-brand in that market, **unless** Experiment 1 (Google one-click signup) has not shipped yet; re-test after it does |

---

## 12. Weekly report template

| Campaign / Market | Spend | Clicks | CTR | Avg CPC | Signups | Click→signup | Account-connected | Connected % of signups | Cost per connected | vs target | Plan selected | Paid (30d, lagged) | Cost per paid | vs break-even |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 Brand | | | | | | | | | | | | | | |
| C2 US High-Intent | | | | | | | | | | | | | | |
| C3 US Core | | | | | | | | | | | | | | |
| C4 UK | | | | | | | | | | | | | | |
| C4 CA | | | | | | | | | | | | | | |
| C4 AU | | | | | | | | | | | | | | |
| **Non-brand total** | | | | | | | | | | | | | | |

Report brand separately, and never blend it into non-brand totals. Show paid customers by signup cohort week, since they arrive ~8 days after signup on average.

---

## 13. How this fits with the remarketing campaign

- **Geo:** restrict remarketing to US/UK/CA/AU (plus UAE/SG only if C5 runs). **[Certain]** 36% of signups are from India and convert to paid at 1%. A global "all visitors" list will spend most of its budget there.
- **Exclusions:** paying customers (Customer Match / `transactions` audience).
- **Best list:** signed up but did not connect a social account within 3 days. That is the step every payer passes through, and 31% of signups stall before it.
- **Keep the budgets separate** from Search, so each channel's results can be read on their own. When you judge Search, compare the cost per paid customer with and without view-through credit from remarketing.

---

## 14. Timeline and owners

| Week | Work | Owner |
|---|---|---|
| **0** | Section 8 tracking build and QA; confirm the meaning of the social-account-connected event; Keyword Planner CPC check (adjust CPC caps); confirm feature claims; import the build files into Ads Editor; Customer Match upload | Dev + Analytics + Marketing |
| **1** | Launch C1–C4 on Maximize Clicks; daily checks; first search-terms pass on Thursday | Marketing |
| **2** | Negatives round 2; tracking reconciliation with Mixpanel | Marketing + Analytics |
| **3** | Switch campaigns past 15 conversions to Maximize Conversions | Marketing |
| **4** | Audience/device/location review; C3 Core keep-or-pause decision | Marketing |
| **5–6** | Ad copy refresh; Phase 3 gate check | Marketing |
| **7–9** | Target CPA; budget shifts within the 20% rule | Marketing |
| **10–12** | Paid readout by market; scale / fix / stop; decide on C5 and Phase 4 | Marketing + Founder |

---

## 15. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| `gclid` lost between `recurpost.com` and `social.recurpost.com` | Medium | High (no offline conversions, so bidding is blind) | Week 0 QA test; enhanced conversions as backup |
| Ad-sourced trials pay at a lower rate than the market average | Medium | High | Watch the connected-account rate from week 2; paid readout weeks 10–12 |
| CPCs above the break-even range | Medium | High | Keyword Planner check in week 0; Core isolated and capped |
| Small-business clicks land on the agency-focused homepage | Low (fixed by the page mapping) | Medium | Every ad group has its own landing page |
| 58% signup-form drop-off | Certain | High | Ship Experiment 1; read paid results before and after it |
| Competitor-term trademark complaints | Low–Medium | Low | No competitor names in ad text |
| Low UK consent rate under-counts conversions | Medium | Medium | Consent Mode v2 |
| Paid traffic contaminates the homepage/signup A/B tests | Medium | Medium | `src=gads` parameter; segment test results by source |
| Budget too small to exit learning | Medium | Medium | Bid on the higher-volume account-connected event; don't split budgets further |

---

## 16. What NOT to do

- Don't make Purchase the bidding goal at this budget. Use "social account connected" until a campaign has ≥30 plan selections in 30 days.
- Don't target UAE/Singapore ahead of Canada/Australia without a test budget and a kill rule.
- Don't send non-agency ads to the homepage.
- Don't use "advertising" or generic "social media marketing" keywords, or Audience Targeting in Search.
- Don't turn on Search Partners, Display, broad match or auto-applied recommendations at launch.
- Don't use "presence or interest" location targeting.
- Don't blend brand into non-brand results.
- Don't change bid strategy, budget and keywords in the same week.
- Don't judge Search before 30-day paid data exists (week 10+). Use cost per account-connected as the interim decision metric.

---

## 17. Open questions

1. **Payback target:** is 12 months right? Every target in section 3 scales with it.
2. **Budget:** is ~$145/day for 6 weeks available? At half that, drop C3 Core and run C1, C2 and C4 only.
3. **Event meaning:** does `specific_sa_modified` mean "account connected successfully", or does it also fire on edits and disconnects? Engineering should confirm, or add a clean `social_account_connected` server event, before it becomes the bidding conversion.
4. **Billing mix:** what share of payers choose annual billing, and at what discount? This changes the first-year values.
