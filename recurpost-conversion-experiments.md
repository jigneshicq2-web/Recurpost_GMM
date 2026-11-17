# RecurPost: Two High-Impact Signup Conversion Experiments

Audit date: 17 Nov 2026. Sources: live pages (recurpost.com, /plans-and-pricing/, social.recurpost.com/new-user-registration-signup/) rendered at desktop 1440×900 and iPhone 13; RecurPost Mixpanel project "Production Analytics" (account_created, email_confirmed, plan_selected, transactions, Segment "Loaded a Page" on social.recurpost.com).

Confidence labels: **[Certain]** = observed on the page or in Mixpanel. **[Likely]** = strong inference. **[Guessing]** = assumption that needs validation.

**Not available:** page-level traffic for recurpost.com. The marketing site is not tracked in Mixpanel, and the Similarweb lookup failed because the account has run out of credits. Every test duration below is derived from signup-page and signup volumes, not from homepage or pricing sessions. Validate the durations against GA4 (G-1QQJJSLQGH) before launch.

---

## The uncomfortable truths first

1. **[Certain] The biggest measurable leak is after the homepage and pricing pages, on the signup form.** Between 1 Aug and 15 Nov 2026, 2,122 unique users reached the signup page from recurpost.com. Only 898 of them (42%) produced `account_created` within 7 days, and only about 18% within 1 day. All homepage and pricing CTAs go to this single form, which has:
   - no Google or social sign-on;
   - a 6-rule password policy;
   - a phone field;
   - a Cloudflare captcha.
2. **[Certain] The homepage is written for a minority of plan choosers.**
   - The hero says *"Social media management for people who manage many accounts, not one,"* and a section says RecurPost is *"Not the best fit when… you need only one or two Meta accounts."*
   - Over the last 6 months, `plan_selected` events break down as Personal 917 (50%), Starter 455 (25%) and Agency 454 (25%).
   - Starter is the 2-account plan, so the homepage explicitly disqualifies the group behind 1 in 4 plan selections.
   - **[Likely]** By list price, Agency still carries about half of new plan revenue, so this is a volume-versus-value trade-off and needs a test rather than an opinion.
3. **[Certain] At about 100 signups a week (2,607 `account_created` uniques over the last 6 months), RecurPost cannot reliably detect small lifts on homepage tests that use signups as the metric.** Detecting a 20% relative lift needs about 420 signups per arm. Plan for big swings, or use a leading metric to make decisions.
4. **[Likely] Signup volume fell from 660 in May to 400–460 a month from June onward.** I could not confirm when the agency-first homepage went live. If the two coincide, Experiment 2 matters more. Check your CMS or deploy history.
5. **[Certain] Attribution is currently impossible between the homepage and the pricing page.** The signup page's referrer arrives as `https://recurpost.com/` with no path. This is consistent with a strict-origin referrer policy. Fix it before running either test (see E1).

---

## A. Executive summary

### Conversion opportunities found

| # | Opportunity | Page | Evidence | Confidence |
|---|---|---|---|---|
| 1 | Signup form abandonment: 58% of visitors who reach the form from recurpost.com don't create an account within 7 days. No Google sign-on, 6-rule password, phone field, captcha. | Signup page | Mixpanel funnel + page markup | [Certain] data / [Likely] cause |
| 2 | Agency-only hero framing excludes Starter and Personal buyers (~75% of plan selections). The H1 tag holds a category label, and the visible headline is an H2. | Homepage | Page copy + `plan_selected` mix | [Certain] / [Likely] impact |
| 3 | Plan intent is lost. "Start Starter / Personal / Agency trial" all point to the same URL with no plan parameter. The signup page then shows a generic headline ("The complete social media management tool") and an agency testimonial. | Pricing → Signup | CTA hrefs | [Certain] |
| 4 | Mobile pricing is buried. A 75-word intro (with a link sending users back to the homepage) pushes the first plan CTA to about 1,190px, roughly 1.8 screens down on a 664px viewport. On desktop, the floating "Ask anything about RecurPost…" bar sits over the Personal and Agency trial buttons at the 900px fold. | Pricing | Screenshots + element positions | [Certain] |
| 5 | Trust and expectation inconsistencies: the same testimonial is credited to "Claire Bell, Agency Owner" (signup page) and "Claire Hall · Freelance PR Consultant" (pricing page). The nav says "Sign Up For Free" while the FAQ says "There is no permanent free plan." | Signup, pricing, nav | Page text | [Certain] |

**Fix these now; they don't need a test:**
- **#5:** correct the testimonial attribution. Wrong attribution is a credibility risk and possibly an endorsement-compliance risk.
- **#4, desktop:** keep the floating chat bar from covering CTAs. This is a defect, not a hypothesis.

### The two experiments to prioritise

1. **Signup page + add "Continue with Google" one-click signup → expected +10–25% relative form completion, which is roughly +10–20% total signups [Guessing, benchmark-based].**
2. **Homepage + replace the agency-only hero headline and subheadline with one that includes solo users and small businesses while keeping agencies → expected −5% to +20% relative signups, with a plan-mix guardrail [Guessing].**

---

## B. Experiment 1: Google one-click signup

**Page:** `https://social.recurpost.com/new-user-registration-signup/`. Every "Sign Up For Free" and "Start 14-day free trial" CTA on the homepage and pricing page lands here, so this one test improves conversion from both priority pages at once.

### Current problem (observed)
- **[Certain]** Fields: Full name, Email, Phone (optional, with the note "Our team may contact you…"), and Password. The password needs 8–20 characters, 1 uppercase, 1 lowercase, 1 number, 1 symbol and no spaces. Then a Cloudflare Turnstile captcha.
- **[Certain]** There is no Google, Microsoft or other social sign-on. The markup has no OAuth button, and the only Google references are analytics and fonts.
- **[Certain]** Only 42% of recurpost.com-referred visitors to this page create an account within 7 days (898 of 2,122, Aug–Nov 2026).
- **[Certain]** About 15% of new accounts never confirm their email: `email_confirmed` 483 vs `account_created` 570 over 30 days.

### Hypothesis
Visitors who click a trial CTA have already decided to try RecurPost. They drop off because of the effort and the moment of doubt at the form: inventing a password that meets six rules, typing details on mobile, and then confirming an email. One-click Google signup removes the password, the typing and the email-confirmation step for the main sign-in provider among SMBs and agencies. **If** we add "Continue with Google" above the email form, **then** form completion rises, **because** the cost of the final step falls to one click. Intent stays the same: the user still chose to start a trial.

### Proposed change (one variable)
- **Control (A):** the current page.
- **Variant (B):** the current page plus a full-width **"Continue with Google"** button (official Google style) as the first element under "14-day free trial – no credit card needed". Then add a divider, "or sign up with email", and keep the existing form exactly as it is below.
- Google signups skip password creation and email confirmation (the address is already verified by Google). The captcha can be skipped for OAuth because Google has already verified the user.
- **Do not change** the headline, testimonial, phone field or password rules in this test. Those are separate hypotheses (see the backlog).

### Expected lift
- **[Guessing]** +10% to +25% relative form completion (42% → about 46–52%). Every signup passes through this page, so that is about +10–20% total signups.
- The range is a benchmark from B2B SaaS SSO rollouts, not a RecurPost-specific forecast.
- Upside case: if Google users skip email verification, activated accounts rise more than raw signups, because confirmation loss is about 15% today.

### Success metrics
- **Primary:** successful account signup, measured as `account_created` per unique signup-page visitor within 7 days.
- **Secondary:**
  - signup completion rate: submits ÷ form starts (first field focus or Google click);
  - signup initiation rate: form starts ÷ page views;
  - email-confirmed or activated rate: first social account connected via `add_specific_sa_clicked` / `specific_sa_modified` within 7 days;
  - trial-to-paid: `plan_selected` within 14 days and `transactions` within 30 days.
- **Guardrails:**
  - trial-to-paid must not fall by more than 15% relative (baseline: 7.3% of accounts transact within 30 days; 106 of 1,461, Jul–Oct cohort);
  - the share of new accounts from personal versus business email domains;
  - spam or duplicate accounts.

### Testing plan
- **Split:** 50/50 server-side or edge split on the signup page, sticky per visitor (cookie). Exclude `?invited` team-invite traffic.
- **Sample:** 42% baseline, 80% power, α = 0.05:
  - about 550 visitors per arm to detect +20%;
  - about 980 per arm to detect +15%.
- **Duration:** about 600–700 eligible visitors a month **[Likely, from Mixpanel]**:
  - **minimum 6–8 weeks** for a ≥20% effect, and at least 2 full business cycles;
  - 10–12 weeks if you need to detect +15%;
  - 30-day trial-to-paid readout after that.
- **Segments:** new vs returning visitor; desktop vs mobile; traffic source via `utm_*` and the new `src` CTA parameter (E1); country, especially the US/UK/EU vs India/rest-of-world split; persona from onboarding.
- **Implementation complexity:** **Medium.** Requires:
  - Google OAuth client and consent screen;
  - account creation and merge for existing emails;
  - `signup_method` set to `google` or `email` (the property exists in Mixpanel but is currently null);
  - Segment `identify`/`alias` on the new path.
- **Key risks:**
  - lower lead data, because the phone number is lost on the Google path; sales follow-up then relies on onboarding;
  - Google Workspace admins blocking third-party apps;
  - a higher share of gmail.com tire-kickers (watch trial-to-paid);
  - OAuth verification review lead time.

**Why this is priority #1:**
- It is the only test where RecurPost has the volume to read a result in under 2 months, because of the 42% baseline at the bottom of the funnel.
- It lifts conversion from both priority pages at once.
- The intent is already proven: these users clicked a trial CTA.
- It carries little brand or positioning risk.

---

## C. Experiment 2: An inclusive hero headline

**Page:** `https://recurpost.com/` (homepage hero, above the fold).

### Current problem (observed)
- **[Certain]** The visible headline is *"Social media management for people who manage **many** accounts, not one."* ("many" is underlined). The subhead names "agencies, freelancers, and teams managing multiple accounts".
- **[Certain]** The hero visual is a client switcher (Northwind / Lumen Co / Bloom / +9) with a client-approval card.
- **[Certain]** Further down, the page says it is "Not the best fit when… you need only one or two Meta accounts."
- **[Certain]** RecurPost's own plan data shows 75% of plan selections are Starter (2 accounts) or Personal (5 accounts), with Personal the single most-chosen plan.
- **[Certain]** The `<h1>` element is the category tag "RecurPost: Social Media Management Software & Scheduler", not the value proposition.
- **[Likely]** A small business, creator or solo marketer reading the first screen concludes "this is for agencies" and leaves or goes to a competitor before reaching the Starter ($9) and Personal ($25) options.

### Hypothesis
The hero filters out the visitors who make up most plan selections. **If** the headline and subheadline speak to "from your own brand to 50 client accounts", **then** more SMB and solo visitors start a trial, **because** they will recognise themselves in the first five seconds. Agencies keep a clear reason to stay through the subheadline and the agency-specific hero visual.

### Proposed change (one variable: hero headline and subheadline copy only)
- **Control (A):** the current headline and subheadline.
- **Variant (B):**
  - **Headline:** *"Plan, schedule and recycle your best posts across every social account. From your own brand to 50 clients."*
  - **Subheadline:** *"One calendar for Facebook, Instagram, LinkedIn, X, TikTok, YouTube, Pinterest, Google Business Profile, Threads and Bluesky. Solo owners start at $9/month; agencies get client workspaces, approval links and white-label reports."*
- **Unchanged:** CTA copy ("Start 14-day free trial"), "No credit card required", the hero visual, the H1 tag, the "Not the best fit" section and everything below the hero. That keeps the read on one variable: audience scope of the value proposition.
- **[Likely]** "Recycle your best posts" is also RecurPost's historical differentiator (the brand name, evergreen libraries, `recurring_post_modified` and `library_modified` among the most-used product events). Including it keeps the variant from being a generic "social scheduler" line. If you want a pure audience test, use *"Plan and schedule posts across every social account. From your own brand to 50 clients."*

### Expected lift
- **[Guessing]** −5% to +20% relative visitor-to-signup on homepage traffic. The negative end is real: agencies may respond less to a broader message.
- **[Guessing]** The plan mix is likely to shift toward Starter and Personal. That is why revenue per visitor, not signups alone, decides the winner.

### Success metrics
- **Primary:** successful account signup per unique homepage visitor (attributed via the `src=home_*` CTA parameter, see E1).
- **Leading or decision metric:** hero CTA click-through, i.e. homepage visitor → signup page load. Its base rate is several times higher than signup, so it reaches significance much faster.
- **Secondary:**
  - CTA CTR (hero, mid-page and footer separately);
  - signup initiation rate;
  - signup completion rate;
  - "Book a demo" CTR, which should not drop for agencies;
  - scroll depth to the pricing teaser;
  - pricing-page visits from the homepage.
- **Quality and guardrails:**
  - `plan_selected` mix by `plan_name`;
  - trial-to-paid at 30 days;
  - **expected new MRR per 1,000 homepage visitors**, the decision metric for a winner;
  - Agency-plan selections must not drop by more than 10% relative.

### Testing plan
- **Split:** 50/50, server-side or edge rendering of the hero block. Avoid client-side flicker, because it biases toward control. Keep the same URL and canonical tag (this is SEO-safe A/B testing; no cloaking).
- **Sample:** **[Guessing, needs GA4]**
  - at a 2% homepage visitor-to-signup rate, +20% needs about 21,000 visitors and about 420 signups per arm;
  - +25% needs about 14,000 and about 280.
- **Duration:** with about 100 signups a week site-wide, of which perhaps 40–60% start on the homepage **[Guessing]**:
  - a signup-powered read takes 10–20 weeks;
  - **so run for a fixed 6 weeks and decide on hero CTA click-through plus revenue per visitor**, treating signups as confirmatory;
  - pre-register this rule before launch.
- **Segments:**
  - new vs returning, because returning visitors already know the positioning and dilute the effect;
  - device, because on iPhone-sized screens the current hero CTA sits at y≈712 against a 664px viewport, just below the fold;
  - traffic source (organic brand vs non-brand vs paid vs referral);
  - geography, since SMB share is likely higher outside the US.
- **Implementation complexity:** **Low** for copy and an edge split; Low–Medium once CTA source tagging is added.
- **Key risks:**
  - an agency-heavy segment converting less (watch the demo CTR and Agency mix);
  - a lower blended ARPU even if signups rise;
  - SEO, if the headline is swapped in crawled HTML for a long time (keep the H1 unchanged and the test time-boxed);
  - a test interaction with Experiment 1 if both run at once (see E3).

**Why this is priority #2:**
- It is the only open question on the homepage backed by RecurPost's own data: positioning versus who actually buys.
- It affects the largest traffic pool.
- Either result is valuable: it validates the agency repositioning or reverses it.
- It is cheap to run.
- It ranks below Experiment 1 because its result will be slower and noisier.

---

## D. Experiment comparison

| | Exp 1: Google one-click signup | Exp 2: Inclusive hero headline |
|---|---|---|
| Page | Signup page (shared by homepage and pricing CTAs) | Homepage hero |
| Change | Add "Continue with Google" above the email form | Rewrite hero headline and subheadline to include solo users and SMBs |
| Hypothesis type | Friction removal at peak intent | Audience and positioning fit |
| Expected lift | +10–25% form completion → about +10–20% total signups [Guessing] | −5% to +20% homepage signups; plan mix shifts [Guessing] |
| Primary metric | `account_created` / signup-page visitor (7-day) | `account_created` / homepage visitor; decide on CTA CTR + revenue per visitor |
| Statistical power | Good (42% baseline) | Weak on signups at current volume |
| Effort | Medium (OAuth, identity, analytics) | Low (copy + edge split) |
| Duration | 6–8 weeks + 30-day paid readout | 6 weeks fixed, pre-registered decision rule |
| Downside risk | Low (lead-data loss, possibly lower quality) | Medium (ARPU, agency signal) |
| Priority | **#1** | **#2** |

---

## E. Implementation recommendations

### E1. Analytics prerequisites (week 0; block launch until done)
1. **CTA source tagging.** Append `?src=<page>_<location>` to every signup link, for example:
   - `home_hero`, `home_mid`, `home_footer`, `nav`;
   - `pricing_starter`, `pricing_personal`, `pricing_agency`, `pricing_footer`.

   Persist `src` and `utm_*` into the `Loaded a Page` and `account_created` properties. Today, Mixpanel cannot tell homepage signups from pricing signups.
2. **Funnel events on the signup page.** Add the following as Segment track calls, carrying `experiment_id` and `variant`:
   - `signup_form_viewed`;
   - `signup_form_started` (first field focus or Google click);
   - `signup_submitted`;
   - `signup_failed` (with the failure reason: password rule, captcha, duplicate email).
3. **Populate `signup_method`** (`email` / `google` / `team_invite`). The property exists but is null for over 99% of signups.
4. **Cross-domain identity.** Confirm that the Segment `anonymousId` from recurpost.com carries over to social.recurpost.com and is aliased at signup, so both experiments can be tied to the visitor's first touch. The marketing site currently doesn't send page views to Mixpanel at all; only the knowledge base does.
5. **Exposure events.** Fire `$experiment_started` (`Experiment name`, `Variant name`) so Mixpanel's experiment breakdowns work.
6. **Agree the definition of "qualified signup"** before launch. Suggested: email confirmed **and** at least 1 social account connected within 7 days.

### E2. Build
- **Exp 1:** a backend engineer (OAuth + account merge), a frontend engineer (button + divider), QA on the existing-email, Workspace-blocked and mobile in-app browser cases, and a privacy/terms review of the Google consent screen. Estimate: 1–2 sprints including Google verification.
- **Exp 2:** copywriter sign-off on the variant, a frontend engineer for the edge or server-side split of the hero block (Cloudflare Worker or similar; not a client-side tool, to avoid flicker), and an SEO check that the H1 and canonical tag are unchanged. Estimate: 2–4 days.

### E3. Sequencing
- **Run both at once with independent randomisation.** Exp 2 changes who arrives at the signup page; Exp 1 changes how many of them complete it. Check the interaction (Exp 2 variant × Exp 1 variant) at readout.
- **If engineering can only take one, ship Exp 1 first.**
- Do not change pricing or signup-page copy during either test.

### E4. Decision rules (agree before launch)
- **Exp 1:** ship if the primary metric is significantly up at p < 0.05 **and** 30-day trial-to-paid is not down by more than 15% relative.
- **Exp 2:** ship B if hero CTA CTR is significantly up **and** expected new MRR per 1,000 homepage visitors is up or flat with Agency selections down by no more than 10%. If signups rise but MRR per visitor falls, keep A and test a segmented hero instead (an SMB variant for non-brand organic and SMB keywords, agency for the rest).

### E5. Backlog (next tests or fixes, in rank order)
1. **Plan-aware signup (Pricing → Signup).** Pass `?plan=agency&billing=monthly` from pricing CTAs. Show "You're starting your 14-day Agency trial: $79/mo after the trial, no card now" on the signup page, and pre-select the plan in `/onboarding-plan-selection/`. Targets trial-to-paid (the `no_plan_selected` event exists). Run it after Exp 1, because both touch the signup page.
2. **Mobile pricing above the fold.** Cut the 75-word intro to one line, remove the "start on the RecurPost homepage" exit link, and get the first plan CTA into the first screen.
3. **Password rule relaxation** (minimum length only, with a strength meter) and **dropping the phone field**. Test these separately after Exp 1.
4. **Nav CTA consistency.** "Sign Up For Free" vs "Start 14-day free trial": align the wording to the trial to stop free-plan expectations.

### Open questions for your team
- When did the "many accounts, not one" hero go live? Does it line up with the drop from 660 signups (May) to about 450 a month (June onward)?
- What are the monthly GA4 sessions for `/` and `/plans-and-pricing/`, and the share of signups from each? These numbers turn the Exp 2 duration from a guess into a plan.
- Is cross-domain Segment identity configured between recurpost.com and social.recurpost.com?
