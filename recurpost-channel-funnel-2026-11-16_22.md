# RecurPost Channel Funnel: Week of 16–22 Nov 2026

Source: Mixpanel "Production Analytics" (2504932). The baseline is the cohort from 1 Jun to 22 Oct 2026, converted to a weekly figure (÷ 20.6 weeks). Definitions are unchanged from `recurpost-channel-funnel-baseline.md`.

Confidence labels: **[Certain]** = a query result. **[Likely]** = a strong inference. **[Guessing]** = an assumption.

**How to compare:** last week's users have had only 1–7 days to convert, so every rate below uses a **1-day conversion window**, for both last week and the baseline. The 30-day baselines in the main report don't apply to a week this recent. The numbers in brackets are 95% confidence intervals. **z** is a two-proportion z-test against the baseline; |z| ≥ 1.96 means p < 0.05.

---

## The uncomfortable truths first

1. **[Certain] On a like-for-like basis, the headline "118 signups (+25% vs baseline)" is probably not real growth.**
   - Since the week of 26 Oct, `account_created` has fired only server-side (`analytics-php`). The client-side web, iOS and Android events stopped (weekly counts: Oct 19: 9 php; Oct 26: 185; Nov 2: 141; Nov 9: 89; Nov 16: 118).
   - Signups that pass through the tracked signup page fell to **56 last week**, against a **baseline of 62 a week (−10%)**.
   - In the baseline, 83% of web signups passed through the signup page. Last week only 54% did.
   - **[Likely]** The new server-side event counts accounts the old one didn't, such as team-member invites or other non-form signups. That would inflate signups and depress activation, which is exactly the pattern below.
   - Confirm with engineering what triggers the php `account_created` event.
2. **[Certain] Visit→signup from the marketing site fell to 34.6%, against a 43.4% baseline (z = −1.99, borderline significant).** Traffic held exactly at baseline (133 vs 133 a week). The drop is on the signup form, not upstream.
3. **[Certain] Web activation fell to 55.8%, against a 65.7% baseline (z = −2.06, significant).** It is either a real regression or the counting change in point 1. Resolve point 1 before treating it as a product problem.
4. **[Certain] The iOS/Android split is no longer available.** The server-side event only carries `device_type`: web or mobile.

---

## 1. Funnel, 16–22 Nov vs baseline (1-day conversion window)

### Traffic → signup (web, signup page)

| Channel | Traffic: last week | Traffic: baseline/wk | Visit→Signup: last week | Visit→Signup: baseline | z |
|---|---:|---:|---:|---:|---:|
| From recurpost.com | **133** | 133 | **34.6%** (27–43) | 43.4% (42–45) | **−1.99** |
| All other referrers ¹ | 82 | 54 | 12.2% (7–21) | 8.4% (7–10) | +1.17 |
| **Total web, signup page** | **215** | 187 | **26.0%** (21–32) | 33.3% (32–35) | **−2.19** |

¹ Derived by subtraction (total minus recurpost.com).

### Signup → activation → paid

| Channel | Signups: last week | Signups: baseline/wk | Signup→Activated: last week | Signup→Activated: baseline | z | Paid ≤1 day: last week | Paid ≤1 day: baseline |
|---|---:|---:|---:|---:|---:|---:|---:|
| Web: via signup page, from recurpost.com | 46 | 58 | **73.9%** (60–84) | 66.4% (64–69) | +1.06 | 3 | ~2.4/wk |
| **Web: all** (`device_type = web`) | **104** | 75 | **55.8%** (46–65) | 65.7% (63–68) | **−2.06** | 4 (3.8%) | 3.4% |
| **Mobile app** (`device_type = mobile`) | **14** | 19 | **7.1%** (1–31) | 24.5% (21–29) | −1.50 | 0 | 0% |
| **All channels** | **118** | 94 | **50.0%** (41–59) | 57.3% (55–59) | −1.55 | 4 (3.4%) | 2.7% |

**Paid to date** (any time since signup, out of a possible 1–7 days): **6 customers** from last week's cohort. The 30-day baseline is about 6.7 paying customers a week, but most payments arrive after the 14-day trial ends. Read last week's paid number on **20 Dec**, when the cohort reaches 30 days.

### UTM-tagged traffic
Last week's volume was too small to report. The baseline is about 3 tagged visits a week, and last week was in line.

---

## 2. Read-out

| Signal | Verdict | Confidence |
|---|---|---|
| Marketing-site traffic to signup | Flat (133 vs 133) | [Certain] |
| Signup-form conversion (recurpost.com visitors) | **Down 9 points**, borderline significant | [Certain] data / [Likely] real |
| Total signups | Up 25% on the raw count, but **down 10% on the like-for-like measure** (signup-page-attributed) | [Likely] the raw count is inflated by the tracking change |
| Web activation | Down 10 points, significant | [Likely] mostly the tracking change; partly real is possible |
| Activation of signup-page users | Up (74% vs 66%), not significant | [Certain] |
| Mobile activation | 1 of 14; too small to read | [Certain] |
| Early paid conversion | In line with baseline | [Certain] (n = 4) |

**Bottom line:** [Likely] it was a flat-to-slightly-weak week. Traffic held, the signup form converted worse, and the users who did come through the form activated normally. The apparent rise in signups and fall in activation are best explained by the late-October change to how `account_created` is tracked, not by user behaviour.

## 3. Actions this week (ranked)

1. **Find out what fires the server-side `account_created`** and add a `signup_method` / `source` property (form, google, team_invite, app) so that invites can be excluded. Until then, report **signup-page-attributed signups** (56) as the like-for-like weekly KPI.
2. **Check the signup form for breakage, 16–22 Nov.** A 9-point drop with flat traffic suggests something like a captcha, validation or deploy issue. Check the error logs and run a manual test on mobile and desktop.
3. **Re-baseline after the tracking fix.** The Jun–Oct baselines for signups and activation are not comparable with server-side counts.
4. **Read the paid conversion for this cohort on 20 Dec** (30-day maturity).

## Saved Mixpanel queries

- Signups by platform, weekly: https://mixpanel.com/project/2504932/view/3046188/app/insights#L13qtAYgj7n1
- Last week, from recurpost.com (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#qYh38fdWBUUU
- Baseline, from recurpost.com (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#263YPtH1WeEG
- Last week, all external web (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#MiazWPGU3btm
- Baseline, all external web (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#dgZmBK57wGXq
- Last week, web signups (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#5TiSNufpjrZ4
- Baseline, web signups (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#wdfXxDLiPKCU
- Last week, mobile signups (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#mnymMcbatxFa
- Baseline, mobile signups (1-day): https://mixpanel.com/project/2504932/view/3046188/app/insights#Mj1BFy3heFtZ
- Last week, all signups (30-day, paid to date): https://mixpanel.com/project/2504932/view/3046188/app/insights#QW1GKK1vbght
