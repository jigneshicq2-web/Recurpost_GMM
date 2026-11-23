# RecurPost Funnel by Acquisition Channel (GA4 + Mixpanel)

Sources:
- GA4 property "RecurPost--GooglePlusPages" (158056940), pulled through Windsor.ai.
- Mixpanel "Production Analytics" for activation, because GA4 has no web activation event.

**Baseline:** ISO weeks 23–42 (1 Jun – 18 Oct 2026), reported as a weekly mean or median. **Last week:** ISO week 47 (16–22 Nov 2026).

Confidence labels: **[Certain]** = a query result. **[Likely]** = a strong inference. **[Guessing]** = an assumption.

## Stage definitions

| Stage | GA4 / Mixpanel definition | Channel scope |
|---|---|---|
| **Traffic** | New users on `recurpost.com` (hostname filter) | Session default channel group |
| **Signup** | GA4 key event `Web_Sign_Up` (on `social.recurpost.com`) | First-user default channel group |
| **Activation** | Mixpanel `specific_sa_modified` with `actions = added` (not in GA4 for web) | **Blended only**; can't be split by channel |
| **Paid** | GA4 key event `purchase` (FastSpring checkout) | First-user default channel group |

---

## The uncomfortable truths first

1. **[Certain] GA4's "purchase" is not "new paying customer".**
   - GA4 records about 15.4 purchases a week. Mixpanel's new-signup cohort produces about 6.7 paying customers a week.
   - GA4 therefore also counts upgrades, plan changes and add-ons from existing customers.
   - **Use GA4 purchases as a revenue-activity signal, not as signup→paid conversion.** For cohort paid conversion, Mixpanel remains the source.
2. **[Certain] "Direct" traffic has tripled since early October, but signups haven't followed.**
   - Direct new users per week: about 1,300 (median, Jun–Sep), then 2,683 (wk 41), 3,602 (wk 42), 5,530 (wk 45) and 3,755 last week.
   - Direct signups fell from 34 a week to 24.
   - The Direct visit→signup rate fell from 2.1% to 0.64% (z = −6.2).
   - **[Likely]** This is low-quality or bot traffic, or a paid/partner source missing its UTMs. It is not real demand. Until it is filtered, it makes every blended traffic metric meaningless.
3. **[Certain] GA4 contains bot spikes that would corrupt a mean-based baseline.**
   - Organic Social: 2,492 / 3,182 / 12,018 new users in weeks 33–35, against a median of about 255.
   - Referral: 544 new users last week, against a median of about 33, with 3 signups.
   - The traffic baselines below use **medians** for that reason.
4. **[Certain] Organic Search, the largest real channel, is declining.**
   - New users: 1,475 a week (median) → 1,113–1,242 a week for the last 4 weeks (**−17%**).
   - Signups: 28.5 a week → 22–24 (**−20%**).
   - The conversion rate is unchanged (1.79% vs 1.84%, z = −0.1). This is a traffic or SEO problem, not a conversion problem.
5. **[Certain] Since week 43, purchases credited to first-touch Organic Search have dropped to 0**, against a baseline of 4.3 a week, while Direct still records purchases. **[Likely]** That pattern suggests an attribution break, such as a checkout-domain or cross-domain change in late October, rather than a real collapse. Verify it in GA4's cross-domain settings.

---

## 1. Funnel by channel: last week vs baseline

| Channel | New users: LW | New users: baseline (median/wk) | Signups: LW | Signups: baseline (mean/wk) | Visit→Signup: LW | Visit→Signup: baseline | Purchases ¹: LW | Purchases ¹: baseline/wk |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Organic Search** | 1,230 | 1,475 | **22** | 29.9 | 1.79% | 1.84% | 0 | 4.3 |
| **Direct** ² | 3,755 | 1,312 | **24** | 33.9 | **0.64%** | 2.13% | 10 | 8.7 |
| **Organic Social** | 328 | 256 | 6 | 4.6 | 1.8% | ~2.0% ³ | 0 | 1.0 |
| **Paid Search + PMax** | 83 | ~4 (launched wk 43) | 3 | 0.6 | 3.6% | n/a | 0 | 0 |
| **AI Assistant** (ChatGPT etc.) | 54 | 46 | 4 | 1.2 | 7.4% | 2.6% | 0 | 0.15 |
| **Paid Social** | 0 | 44 | 0 | 2.8 | — | 1.1% | 0 | 0 |
| **Referral** | 544 ⁴ | 33 | 3 | 0.6 | 0.55% | 0.8% | 0 | 1.3 |
| **Other / Unassigned** | 174 | 21 | 3 | 0.3 | — | — | 0 | 0.05 |
| **Total** | **6,168** | ~3,900 | **65** | **70.9** | 1.05% | 1.70% | **10** | **15.4** |

¹ GA4 `purchase`, which includes existing-customer upgrades and add-ons (see truth #1).
² Inflated by suspected non-human or untagged traffic since week 41.
³ Median-based. The mean is distorted by the bot spikes in weeks 33–35.
⁴ A one-week spike, probably referral spam.

**Activation (Mixpanel, blended, 1-day window):** last week 50.0% (59/118) vs 57.3% baseline. On the like-for-like web view, 55.8% vs 65.7% (z = −2.06). It can't be split by channel until the channel is passed into Mixpanel (see the next steps).

### Paid Search test (weeks 43–46)

| Week | New users | Signups (Paid Search + Cross-network + Paid Other) | Visit→Signup | Purchases |
|---|---:|---:|---:|---:|
| 43 | 458 | 14 | 3.1% | 0 |
| 44 | 855 | 43 | 5.0% | 0 |
| 45 | 469 | 35 | 7.5% | 0 |
| 46 | 38 | 6 | — | 0 |
| 47 (LW) | 83 | 3 | 3.6% | 0 |

- **[Certain]** Paid Search converted visitors to signups at 3–7.5%. That is 2–4× Organic Search (1.8%), and it was the best-converting meaningful channel in the period.
- **[Certain]** Volume collapsed in week 46. **[Likely]** The campaign was paused or its budget was cut.
- **[Certain]** It has 0 GA4 purchases so far. The week-44 cohort reaches day 30 around 2 Dec. **Don't judge Paid Search on paid conversion before mid-December.**
- Ad spend isn't connected in Windsor, so CAC can't be calculated. The only connected Meta account belongs to a different business.

---

## 2. Baseline scorecard per channel (the numbers to beat each week)

| Channel | New users/wk (median) | Signups/wk (mean) | Visit→Signup | Watch threshold |
|---|---:|---:|---:|---|
| Organic Search | 1,475 | 29.9 | 1.84% | < 1,300 new users or < 22 signups |
| Direct | 1,312 (pre-October) | 33.9 | 2.13% | Rate < 1.5% suggests junk traffic |
| Organic Social | 256 | 4.6 | ~2.0% | n/a (small) |
| AI Assistant | 46 | 1.2 | 2.6% | n/a (small, growing) |
| Paid Search | — (new) | — | 3–7.5% (wks 43–45) | Set after a full month of spend |
| **Total signups (GA4)** | — | **70.9** | — | **< 60** |
| **Total purchases (GA4)** | — | **15.4** | — | **< 10** |

**[Certain]** Two independent sources agree on signup volume. GA4 shows **65 signups vs a 70.9 baseline (−8%)**. Mixpanel's signup-page-attributed count shows 56 vs 62 (−10%). The higher server-side Mixpanel count (118) is the outlier.

---

## 3. Read-out for 16–22 Nov

1. **[Certain] Real signups were down about 8–10%**, confirmed by both GA4 and Mixpanel.
2. **[Certain] The drop comes from Organic Search volume (−23% vs baseline) and Direct (−29%).** It is not caused by conversion on the main organic channel.
3. **[Likely] The Paid Search pause explains the fall from 123 signups (week 44) and 84 (week 45) back to the baseline.** Paid Search added about 35–43 signups a week while it ran.
4. **[Certain] AI Assistant traffic converts at 7.4%** (z = +2.1, small sample). It is the best organic channel per visitor and worth an inexpensive content investment.
5. **[Certain] Purchases (10) were below baseline (15.4)**, with first-touch Organic Search purchases at 0 for a fifth straight week. Check the attribution first (truth #5).

## 4. What NOT to do

- **Don't report "traffic +58% vs baseline".** It is driven by Direct and Referral junk.
- **Don't kill or scale Paid Search on current data.** Its signup rate is strong, but there is no purchase evidence yet and no spend data.
- **Don't use GA4 purchases ÷ GA4 signups as a paid conversion rate.** The numerator includes existing customers.

## 5. Next steps (ranked)

1. **Diagnose the Direct surge** (1–2 hours). In GA4, break down Direct since week 41 by landing page, country, device and engagement time. If it is bot traffic, add an internal/bot traffic filter. If it comes from untagged campaigns such as email or partners, add UTMs.
2. **Verify cross-domain tracking** across recurpost.com, social.recurpost.com and the FastSpring checkout domain. Purchases dropping to 0 for Organic Search since week 43 is the symptom.
3. **Decide on Paid Search with data.** Connect Google Ads to Windsor to get CAC. Hold the campaign at a fixed budget for 4 weeks and judge it on signup→paid in Mixpanel 30 days after each cohort.
4. **Send the GA4 first-user channel into Mixpanel** on `account_created`, via a cookie or the `client_id`. That unlocks activation and true paid conversion by channel, which neither tool gives on its own today.
5. **Investigate the Organic Search decline** (−17% for 4 weeks). Check Search Console for lost queries and pages. This is the largest channel by revenue at baseline.

## Data notes

- Windsor connector: `googleanalytics4`, account 158056940. Weekly aggregates were built from daily rows.
- Traffic is filtered to `hostname = recurpost.com` so that logged-in app usage on `social.recurpost.com` is excluded.
- Signups and purchases use the **first-user** channel because they often happen days after the first visit. Traffic uses the **session** channel, so the visit→signup ratios mix scopes and are **[Likely]** directionally correct, not exact.
