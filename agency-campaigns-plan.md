# RecurPost: Agency-Only Acquisition Plan (Search, Remarketing, PMax)

Plan date: 26 Nov 2026. Companion to `google-search-ads-plan.md`.

**Build files** (Google Ads Editor format) are in `google-ads-build/agency/`:
- `keywords.csv`: 96 unique keywords across 4 campaigns.
- `negatives.csv`: 100+ agency-specific negatives.
- `responsive-search-ads.csv`: 22 RSAs; headlines ≤30, descriptions ≤90, all checked.
- `assets.csv`: sitelinks, callouts, a structured snippet and price assets.
- `keyword-planner-seed-list.txt`: paste into Keyword Planner to pull volumes.
- `build_agency.py`: regenerates everything.

**Confidence labels:**
- **[Certain]** = Mixpanel "Production Analytics" or the live recurpost.com pages (checked 26 Nov 2026).
- **[Likely]** = strong inference.
- **[Guessing]** = needs validation. All CPCs are guesses until you share Keyword Planner data.

---

## 1. The uncomfortable truths first

1. **[Certain] Agency customers are a small market for RecurPost today.**
   - In six months (May–Oct 2026), 94 people selected an Agency plan worldwide, and 43 paid within 30 days. That is **~7 paying agency customers a month from all channels combined.**
   - The US supplied 20 of them (~3 a month).
   - An agency-only campaign is a precision play, not a volume play. A realistic early goal is **+3 to +5 agency customers a month**, which would roughly double US agency acquisition.
2. **[Certain] Only ~3% of signups in the US/UK/CA/AU end up on an Agency plan** (22 of 757 within 30 days). The campaign only pays back if its signups choose Agency far more often than that (section 4). This is the number that decides success, and you can measure it within 6 weeks.
3. **[Certain] Nothing in the product currently shows that a new signup is an agency.**
   - About 47% of signups create or edit a workspace, but only 2% of those go on to an Agency plan.
   - Inviting collaborators happens too rarely to use (18 users in six months in these markets).
   - The **"Start Agency trial" button sends people to the same signup URL as every other plan, with no plan parameter** (checked on the live pricing page).
   - So Google has nothing agency-specific to optimise toward. **Fixing this is the first job** (section 6). Without it, Google will optimise toward cheap Starter signups whatever your keywords say.
4. **"Only real agency owners" cannot be enforced through targeting.** Google has no reliable "agency owner" audience. Agency-only comes from three things together: agency-intent keywords, negatives that remove small businesses and service-seekers, and bidding on an agency-qualified conversion. Audiences help only as observation signals and for remarketing.
5. **[Likely] PMax is the wrong tool right now** (section 11). It optimises to the easiest conversion, which here is a Starter signup in a cheap market, and it needs far more conversions than agency volume can supply.
6. **Google RSAs accept at most 4 descriptions,** not 5. Five are written below. The main ad group runs two RSAs that rotate them, so all five are used.

---

## 2. Which countries to target

Agency plan selections in the 6 months to 26 Oct 2026, and how many paid within 30 days [Certain]:

| Country | Agency plan selections | Paid within 30 days | Paid rate | Decision |
|---|---|---|---|---|
| **United States** | 25 | 20 | **80%** | **Tier 1: launch, ~65% of budget** |
| **United Kingdom** | 4 | 4 | 100% | **Tier 2: launch** |
| **Canada** | 3 | 3 | 100% | **Tier 2: launch** (with the UK) |
| Singapore | 2 | 2 | 100% | Tier 3: paused test (tiny sample) |
| Netherlands | 2 | 2 | 100% | Tier 3: paused test; English ads work for Dutch agencies [Likely] |
| Australia | 1 | 0 | 0% | Tier 3: paused test; strong overall paid rate (22%) but no agency evidence yet |
| New Zealand | 2 | 0 | 0% | Exclude for now |
| UAE | 1 | 0 | 0% | **Exclude**: no agency evidence |
| India | 24 | 3 | 12.5% | **Exclude**: agencies select the plan but rarely pay |
| Japan, Germany, others | 1–3 each | 0–1 | — | Exclude (language and volume) |
| **All countries** | 94 | 43 | 46% | |

**Takeaways:**
- **The US is the agency market:** 47% of all paying agency customers.
- The **US, UK and Canada together are 63%** (27 of 43).
- Every non-US country has fewer than 5 agency customers, so treat Tier 2 and 3 as experiments.
- Agency buyers pay about 2 days after choosing the plan, on average. Once someone picks Agency, the decision is nearly made.

---

## 3. Campaign architecture

| # | Campaign | Type | Geo | Daily budget | Targeting | Status |
|---|---|---|---|---|---|---|
| A | `RP \| Search \| Agency \| US` | Search | US | **$70** | Agency keywords, audiences in **Observation** | On |
| B | `RP \| Search \| Agency \| UK-CA` | Search | UK, CA | **$30** | Same | On |
| C | `RP \| Search \| Agency \| AU-SG-NL` | Search | AU, SG, NL | $10 | Same | **Paused** until week 6 |
| D | `RP \| Search \| Agency RLSA \| US-UK-CA` | Search | US, UK, CA | **$10** | Generic scheduler keywords, **shown only to agency-intent remarketing lists** (Targeting) | On once the lists reach serving size |
| E | `RP \| Demand Gen \| Agency Remarketing \| US-UK-CA` | Demand Gen (YouTube, Shorts, Discover, Gmail, Display) | US, UK, CA | **$15** | Agency-intent remarketing lists (Targeting) | On once the lists reach serving size |
| | **Total** | | | **$125/day ≈ $5,250 over 6 weeks** | | |

**If you also run the earlier Search plan:** remove its "Agency" ad group from C2/C4, so the two campaigns don't bid against each other on the same terms. Brand stays in the earlier plan's C1.

**Settings for A–D:**
- Search Network only; Search Partners off; Display expansion off.
- Location option: "Presence: people in or regularly in".
- Language: English.
- Auto-applied recommendations off; broad match off.
- Tracking template: `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}&src=gads_agency`

---

## 4. Unit economics (what "working" means)

Agency plan: $79/month ($948 first year), or $790/year on yearly billing (2 months free) [Certain, live pricing page].

| Metric | US | UK + CA |
|---|---|---|
| Agency plan selected → paid | 80% [Certain] | ~100% on 7 people [Certain, tiny sample] |
| Break-even cost per **paying agency customer** (12-month payback) | **$948** | **$948** |
| Break-even cost per **Agency plan selection** | ~$760 | ~$760 (use the US rate until there is data) |
| Target cost per Agency plan selection (70% of break-even) | **~$530** | **~$530** |

**The question that decides success:** what share of signups from these campaigns choose the Agency plan?

| Agency-plan rate among campaign signups | Break-even cost per signup | Verdict at a guessed $10–15 CPC and 10% click→signup ($100–150 per signup) [Guessing] |
|---|---|---|
| 3% (today's average for these markets) | ~$23 | Fails |
| 10% | ~$76 | Fails |
| **20%** | **~$152** | **Breaks even** |
| 30% | ~$228 | Profitable |

[Guessing] Agencies probably churn less than solo users. If you accept a 24-month payback for agencies, every break-even figure doubles. Decide this before launch, because it changes the kill thresholds.

**Week-6 check:** if fewer than ~15% of campaign signups are agency-qualified (section 6), tighten keywords and landing pages before spending more.

---

## 5. Keywords

The full list is in `google-ads-build/agency/keywords.csv`, with phrase and exact match only. Each ad group lands on an existing page [Certain].

| Ad group | Intent | Example keywords | Landing page |
|---|---|---|---|
| **Agency Software** (18 kw) | Agency looking for a tool | "social media management tool for agencies", "social media scheduler for agencies", "agency social media management software", "smm agency software", [social media management for agencies] | `/use-cases/agencies/` |
| **Multi-Client Management** (11) | The agency's core job | "manage multiple social media accounts for clients", "social media dashboard for multiple clients", "connect client social accounts without password" | `/use-cases/agencies/` |
| **Client Approvals** (8) | Agency-only feature | "social media approval workflow", "client approval social media posts", "shareable social media calendar for clients" | `/features/collaborate/approval-workflow/` |
| **White-Label Reporting** (8) | Agency-only feature | "white label social media reports", "branded social media reports for clients", "automated social media reports for clients" | `/features/measure/brand-logo-white-label-reports/` |
| **Agency Competitor Switch** (40) | Agencies on agency tools | "sendible alternative", "agorapulse alternative", "socialpilot alternative", "vista social alternative", "planable alternative", "heyorca alternative", "hootsuite alternative for agencies", "sprout social for agencies" | `/compare/alternatives/<tool>/` per keyword |
| **Agency Plan Pricing** (5) | Ready to buy | "social media management software for agencies pricing", "affordable social media tool for agencies" | `/plans-and-pricing/` |
| **RLSA: Generic Scheduler** (8, campaign D only) | Generic terms, but only for known agency-intent visitors | "social media scheduler", "social media management tool", "hootsuite alternative" | `/use-cases/agencies/` |

**Left out on purpose:**
- **Freelancer keywords.** The pricing page positions Personal for freelancers, so these would pull in Personal buyers.
- **"social media marketing agency" phrasing.** Those searchers want to hire an agency.
- **"white label social media services".** Those searchers are agencies reselling services, not looking for software.

**Negatives** (`negatives.csv`, phrase match, shared set on A–D). They cover:
- hiring or buying agency services (services, packages, reseller, panel, outsourcing);
- starting an agency (how to start, business plan, name ideas, contract, proposal, courses, jobs);
- **non-agencies** (small business, solopreneur, personal brand, creator, influencer, for my business);
- wrong products (advertising, PPC, SEO, CRM, project management, followers);
- existing users (login, support, cancel, coupon).

### Keyword volume: yes, please share it
Paste `google-ads-build/agency/keyword-planner-seed-list.txt` (96 keywords) into **Keyword Planner → Get search volume and forecasts**. Set locations to US, UK, Canada, Australia, Singapore and Netherlands, set the language to English, and break down by location. Export:
- average monthly searches;
- competition;
- top-of-page bid (low and high range).

With that I will:
1. drop keywords under ~10 searches a month, or move them into phrase-match parents;
2. set CPC caps per ad group from the top-of-page bid range;
3. re-check the budget split against the real CPCs.

---

## 6. Conversion tracking: make "agency" visible to Google (week 0, blocks launch)

**Engineering tasks:**
1. **Pass the plan choice.** Add `?plan=agency` to every "Start Agency trial" button and every CTA on agency pages. Store it on the user at signup.
2. **Ask one onboarding question:** "Who do you manage social media for?" with the options:
   - My own business;
   - Clients, as an agency;
   - Clients, as a freelancer.

   Follow it with "How many clients?" for the client options.
3. **Fire `agency_qualified`** when any of these happen:
   - the signup came from `plan=agency`;
   - onboarding answer = agency, or client count ≥ 3;
   - a 6th social account is connected (above the Personal plan's limit of 5);
   - the Agency plan is selected.
4. **Fire `demo_booked`** from `social.recurpost.com/book-demo/`, carrying the click ID.
5. **Upload offline conversions** to Google Ads using the stored click ID (`gclid`/`gbraid`/`wbraid`) and hashed email, as set out in the earlier plan's section 8.

**Conversion actions:**

| Conversion | Fires | Role (Phase 1–2) | Value | Click window |
|---|---|---|---|---|
| **Agency-qualified signup** | `agency_qualified` (first time) | **Primary** | $150 | 30 days |
| **Demo booked** | `demo_booked` | **Primary** | $200 | 30 days |
| Agency plan selected | `plan_selected` with plan containing "Agency" | Secondary; primary in Phase 3 | $760 | 60 days |
| Agency paid | First `transactions` after Agency plan selected | Secondary (reporting) | Actual first payment × 12 | 60 days |
| Any signup | `account_created` | Secondary (diagnostic) | $0 | 30 days |

---

## 7. Search ads

### Main RSA (Agency Software ad group)

**15 headlines (≤30 characters):**

| # | Headline | Chars |
|---|---|---|
| 1 | Social Media Tool for Agencies | 30 |
| 2 | Built for Agencies, From $79 | 28 |
| 3 | A Workspace for Every Client | 28 |
| 4 | White-Label Client Reports | 26 |
| 5 | Client Approval Workflow | 24 |
| 6 | No-Password Client Onboarding | 29 |
| 7 | 20 Social Accounts for $79/mo | 29 |
| 8 | Shareable Client Calendars | 26 |
| 9 | Automated Client Reports | 24 |
| 10 | Roles & Permissions Built In | 28 |
| 11 | Free 14-Day Agency Trial | 24 |
| 12 | No Credit Card to Start | 23 |
| 13 | Switch Without Losing Queues | 28 |
| 14 | Recycle Evergreen Client Posts | 30 |
| 15 | Save 2 Months With Yearly | 25 |

**5 descriptions (≤90 characters).** RSA 1 uses D1–D4 and RSA 2 uses D2–D5:
1. Give every client its own workspace, approval flow and white-label reports. From $79/mo.
2. Clients connect accounts without sharing passwords and approve posts by link. Free trial.
3. 20 social accounts and 3 users on the Agency plan. Add accounts for $4/mo as you grow.
4. Schedule, recycle and report across 10 networks for every client from one dashboard.
5. Switching tools? Move over without losing queues, libraries or approvals. No card needed.

**Each other ad group** swaps 2–3 headlines for its own angle (all in the CSV):
- **Approvals:** "Clients Approve Posts by Link", "Internal & Client Approvals".
- **White-label:** "Reports With Your Agency Logo", "Scheduled Client Reports".
- **Competitor:** "Switching Agency Tools?", "Compare Before You Renew".
- **Pricing:** "Agency Plan: $79/Month", "$4/mo Per Extra Account", "Yearly: 2 Months Free".
- **Multi-client:** "Manage Every Client Account", "One Inbox for Every Client".

**Every claim comes from the live pricing or agency page:**
- $79/month, 20 social accounts, 3 users, a separate workspace per client;
- internal and external approval workflow, password-free client onboarding;
- white-label analytics reports, automated scheduled client reports, shareable calendars;
- roles and permissions;
- $4 per extra account, $20 per extra teammate, yearly billing with 2 months free;
- migration without losing queues, libraries or approvals.

**Not claimed:** "unlimited", ratings, or competitor names in ad text.

**Pinning:** pin nothing at launch. After 3 weeks, consider pinning "Social Media Tool for Agencies" to position 1, to discourage clicks from non-agencies.

### Sitelinks (≤25 characters; descriptions ≤35)

| Sitelink | Description 1 | Description 2 | URL |
|---|---|---|---|
| Agency Plan & Pricing | 20 accounts and 3 users, $79/mo | Yearly billing: 2 months free | `/plans-and-pricing/` |
| RecurPost for Agencies | A separate workspace per client | Built for client work | `/use-cases/agencies/` |
| White-Label Reports | Reports with your agency logo | Scheduled client reports | `/features/measure/brand-logo-white-label-reports/` |
| Client Approval Workflow | Clients approve posts by link | Internal and external review | `/features/collaborate/approval-workflow/` |
| Roles & Permissions | Control who can do what | Team and client access | `/features/collaborate/roles-and-permissions/` |
| Shared Client Calendar | View-only link for clients | Clients comment, no login | `/features/collaborate/shared-calendar/` |
| Switch to RecurPost | Keep queues and libraries | Move without losing approvals | `/migrate/` |
| Book a Product Demo | See the agency workflow live | Ask about your client setup | `social.recurpost.com/book-demo/` |

### Other assets
- **Callouts (≤25):** No Credit Card Needed · 14-Day Free Trial · A Workspace Per Client · White-Label Reports · Client Approval Links · No-Password Onboarding · Automated Client Reports · Roles & Permissions · 2 Months Free on Yearly · iOS & Android Apps.
- **Structured snippet:** header "Service catalog": Client workspaces; Approval workflow; White-label reports; Shared calendars; Social inbox; Evergreen recycling.
- **Price asset:** Agency plan $79/mo · Agency yearly $790/yr · Extra social account $4/mo · Extra teammate $20/mo.
- **Lead form asset (optional, A only):** "Book a product demo", asking for name, work email and number of clients. This is useful for agencies that want a call before a trial. Route leads to sales within one business day.
- **Image assets:** a screenshot of the client approval link and of a white-label report, if design can supply them.

---

## 8. Keywords only, or keywords plus audience segments?

**Short answer: use keywords for targeting and audiences for observation.** The one exception is campaign D, where audiences do the targeting.

| Campaign | Who sees the ads | Audience setting | Why |
|---|---|---|---|
| **A, B, C** (agency keywords) | Anyone searching agency-intent terms | **Observation** | The keywords already express agency intent. Adding Targeting would cut an already small volume, and Google's audience data cannot reliably identify agency owners |
| **D (RLSA)** | Only people on agency-intent remarketing lists | **Targeting** | Generic terms like "social media scheduler" are too broad for strangers. For someone who already viewed agency pages or started an Agency trial, the same search is high intent |
| **E (Demand Gen)** | Only agency-intent remarketing lists | **Targeting** | Display and YouTube have no keyword intent, so the audience is the targeting |

**Segments to add in Observation on A–C:**
- the remarketing lists from section 9;
- **In-market:** Advertising & Marketing Services; Business Productivity Software;
- **Custom segment:** people who searched for Sendible, Agorapulse, SocialPilot, Vista Social, Planable, or "white label social media reports";
- **Detailed demographics, if available in your account:** Industry → Advertising & marketing; Company size → small [Likely available].

After 4 weeks, check whether any segment converts to agency-qualified at ≥2× the rest. Smart Bidding uses these signals automatically once they are added; there is no need to set bid adjustments.

---

## 9. Remarketing audiences: how to build them

### 9.1 Plumbing (week 0)
1. **Google tag on both domains** (recurpost.com and social.recurpost.com). Link GA4 to Google Ads with audience sharing on.
2. **GA4 events to create:**
   - `agency_cta_click`: any click on "Start Agency trial" or the agency-page CTAs;
   - `demo_page_view`: `/book-demo/`;
   - `demo_booked`;
   - `agency_page_engaged`: two or more agency pages, or 60+ seconds on one;
   - `agency_qualified` (section 6), sent from the app with `user_id`.
3. **Customer Match from Mixpanel cohorts.** Use Mixpanel's Google Ads cohort sync if it is enabled; otherwise upload a hashed CSV weekly. Customer Match requires account eligibility (good policy and payment history, enough account age and spend) [Likely]. Check Audience Manager. If the account is not eligible, build the same lists as GA4 audiences using `user_id`.

### 9.2 The lists

| # | List | Built from | Membership | Use |
|---|---|---|---|---|
| R1 | **Agency plan selected, not paid** | Mixpanel cohort → Customer Match (or GA4) | 30 days | Hottest. D + E. Message: "Finish setting up your agency workspace" |
| R2 | **Agency trial started, not paid** | `agency_qualified` without a payment | 30 days | D + E |
| R3 | **Demo page visitors who didn't book** | GA4: `demo_page_view` without `demo_booked` | 30 days | D + E |
| R4 | **Clicked "Start Agency trial" but no account created** | GA4: `agency_cta_click` without `account_created` | 30 days | D + E. Pairs with the signup-form fixes |
| R5 | **Engaged with agency pages** | GA4: `agency_page_engaged`, or views of `/use-cases/agencies/`, approval, white-label, roles, shared-calendar pages | 90 days | D + E |
| R6 | **Viewed agency-competitor comparisons** | GA4: `/compare/alternatives/` pages for sendible, agorapulse, socialpilot, vista-social, planable, statusbrew, heyorca | 90 days | D + E |
| R7 | **YouTube engagers** | Link the RecurPost YouTube channel: viewers of agency-workflow videos, subscribers | 180 days | E |
| **R-ALL** | **Agency intent (any of R1–R7)** | Combined segment | — | Default targeting for D and E while the lists are small |

**Exclusions on every campaign:**
- current paying Agency customers (Customer Match);
- all other paying customers (they are an upsell job, not acquisition);
- `/signin/` and app dashboard visitors (existing users);
- careers and job page visitors;
- everyone outside the target countries (campaign geo).

### 9.3 List size and reach
- [Likely] A list needs roughly 100+ active users before it serves on Search, YouTube or Display. Check the "Size" column in Audience Manager after 2 weeks.
- [Certain] Agency lists will be small: R1 grows by only ~8 people a month worldwide. That is why D and E start on the **combined R-ALL list**, and why the budgets are small ($10 and $15 a day).
- **Don't widen reach with "optimized targeting".** It pushes the ads to people outside your lists, which breaks "agency only".

### 9.4 Demand Gen creative (campaign E)
- **Formats:**
  - 15–30 second vertical and horizontal videos for YouTube in-stream and Shorts;
  - image ads for Discover, Gmail and Display;
  - square and landscape screenshots.
- **Three messages, one each, served in rotation:**
  1. **Client separation:** "A separate workspace for every client." Screen recording of switching between client workspaces.
  2. **Approvals without logins:** a client approving a post by link, then the shareable calendar.
  3. **Reports under your brand:** a white-label report with an agency logo. Close: "Agency plan $79/mo · 20 accounts · 14-day free trial".
- **Proof:** use a case study only if the customer is an agency and has agreed to be named. Check the case-study pages before using one.
- **Bidding:** start with Maximize Clicks with a CPC cap. Switch to Maximize Conversions on agency-qualified + demo booked once 15+ conversions are recorded.
- **Exclusions:** content for children, games apps (Display), and sensitive content categories.

---

## 10. Bidding plan

| Phase | When | Search A–C | RLSA D | Demand Gen E | Gate |
|---|---|---|---|---|---|
| **1. Control** | Weeks 1–3 | **Manual CPC** with caps from Keyword Planner (placeholder: US $15, UK/CA $10) [Guessing] | Manual CPC at 60% of the A caps | Maximize Clicks, CPC cap $2 | ≥15 primary conversions (agency-qualified + demo) per campaign |
| **2. Learn** | Weeks 4–8 | **Maximize Conversions** on agency-qualified + demo booked | Same | Same | ≥30 primary conversions in 30 days |
| **3. Efficiency** | When the gate is met | **Target CPA**, starting at the trailing actual CPA, then down 10% every 2 weeks | Same | Same | ≥30 Agency plan selections in 30 days across A+B |
| **4. Value** | Probably not at this budget | Maximize Conversion Value / tROAS with Agency plan selected as primary | — | — | — |

**Why Manual CPC first:**
- Agency keywords are narrow and expensive.
- Maximize Clicks hunts for the cheapest clicks, which are often off-intent.
- At ~1–3 conversions a week, automated bidding has nothing to learn from yet.

**Rules for changes:**
- After switching bid strategy, change nothing else for 7 days except adding negatives.
- Change budgets by at most 20% a step.

### Decision rules

| Trigger | Action |
|---|---|
| Keyword spend ≥ $300 with 0 agency-qualified signups | Pause |
| Ad group: after ≥15 signups, fewer than 15% are agency-qualified | Wrong audience: tighten match types, add negatives, check the landing page |
| Campaign: cost per Agency plan selection ≤ $530 and losing >20% impression share to budget | Budget +20% per week |
| Week 6: UK-CA cost per agency-qualified signup > 1.5× US | Cut B to $15/day; consider switching on C instead |
| Week 6: A and B on target | Switch on C (AU-SG-NL) at $10/day for 6 weeks |
| Weeks 10–12: cost per paying agency customer > 2× $948 (or 2× your agreed payback figure) | Stop that market; keep remarketing only |

---

## 11. Should you also try Performance Max?

**Not now.** Revisit in about 3 months if the gates below are met.

**Why not:**
1. **Too few conversions.** PMax needs a steady flow of conversions to optimise ([Likely] 30–50 a month). Agency buyers come to ~7 a month from all channels.
2. **It optimises to the easiest conversion.** Pointed at signups, it will find cheap Starter and Personal signups and non-agency audiences. Audience signals in PMax are hints, not targeting, so you cannot make it agency-only.
3. **It competes with your Search campaigns.** PMax also serves on Search and can take over your brand and agency queries, which blurs what is working.
4. **It reports less.** You see less about placements and queries than in Search and Demand Gen, which makes "agency only" hard to verify.

**When to test PMax (all must be true):**
- Agency-qualified signups ≥ 30 a month, with offline conversion import working;
- Agency plan selected imported with value;
- Search A+B profitable for 2 months.

**How to test it then:**
- 10–15% of budget;
- value-based bidding (tROAS) on Agency plan selected;
- brand exclusions and account-level negative keywords;
- customer lists excluded;
- the new-customer acquisition goal on;
- audience signals from R-ALL and current Agency customers.

**Better first step beyond Search:** campaign E (Demand Gen remarketing). It reaches YouTube and Display with audience control you can verify.

---

## 12. Timeline

| Week | Work | Owner |
|---|---|---|
| **0** | `?plan=agency` on CTAs; onboarding question; `agency_qualified` and `demo_booked` events; offline upload; GA4 events and audiences; Customer Match check; **Keyword Planner export → CPC caps**; import the CSVs | Dev, Analytics, Marketing |
| **1** | Launch A and B on Manual CPC. Search terms review Monday and Thursday | Marketing |
| **2** | Check list sizes; launch D and E if R-ALL is large enough | Marketing |
| **3–4** | Negatives round 2; switch to Maximize Conversions where ≥15 conversions | Marketing |
| **6** | Check the agency-qualified rate (target ≥15–20%); decide on C | Marketing, Founder |
| **8–12** | Target CPA if the gate is met; paid-agency readout; scale or stop per market | Marketing, Founder |

---

## 13. Open questions

1. **Payback for agencies:** 12 or 24 months? This doubles or halves every threshold.
2. **Keyword Planner export** for the seed list (section 5): this sets the CPC caps and the final keyword list.
3. **Engineering capacity** for section 6 in week 0. Without `agency_qualified`, run A and B on Manual CPC only, and judge them on Agency plan selections in Mixpanel.
4. **Agency case studies:** is any published case study an agency that agreed to be named?
