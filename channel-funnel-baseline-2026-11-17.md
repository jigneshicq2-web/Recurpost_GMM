# RecurPost: traffic, signups, activation and paid by channel, against baseline

Snapshot date: 17 Nov 2026. Live version (re-runs the Mixpanel, Meta and Sheets queries when opened): https://claude.ai/artifact/XNNbFm9sP9nNkk84J7ddUf

**Windows.** Current = 19/20 Oct to 15/16 Nov 2026 (4 weeks). Baseline = 27 Jul to 18/19 Oct 2026 (12-week weekly average). The snapshot figures below come from queries run on 17 Nov, and their date edges differ by about one day from the live dashboard's.

**Confidence labels.** [Certain] = queried directly. [Likely] = strong inference. [Guessing] = assumption.

## Read this first: what the data cannot tell you

1. **[Certain] You cannot compute CAC by channel today.**
   - Google Ads spend is not reachable from this session. The Windsor connector (GA4 + Google Ads) failed to connect, there is no GA4 connector, and BigQuery has no credentials.
   - The Marketing KPI Tracker, where CPL and CAC were meant to live, is empty: its Channel Input and Weekly Input tabs have no rows since September.
   - The Leadership Scorecard (the Odoo KPI report) has no spend, CPL or CAC rows.
2. **[Certain] Mixpanel's UTM properties are empty on 100% of signups.** This covers `initial_utm_*` and `$initial_referring_domain`. Channel was rebuilt from the `refer_url` user property, which stores the landing URL.
   - About 31% of current signups have no landing URL. 53% of those are mobile-app signups.
3. **[Certain] 13 signups between 26 Oct and 8 Nov are internal tests.** Their landing URL contains `gtm_debug`, so they inflate the late-October spike.
4. **[Certain] The scorecard does not match Mixpanel.**
   - "New trial signups" averages about 147 a week over the last 4 weeks, against about 133 `account_created` uniques in Mixpanel.
   - The scorecard's activation figures run 26 to 29%, against 23% for the same definition in Mixpanel.
   - Agree one definition for each before using either as a target.

## Company funnel

| Metric | Baseline / wk | Current / wk | Change |
|---|---|---|---|
| Signup-page visitors (Mixpanel; GA4 unavailable) | 199 | 280 | +41% |
| Signups (`account_created` uniques) | 92 | 133 (129 excluding tests) | +44% |
| Activated within 7 days (first post), % of cohort | 21.1% | 23.1% | +2.0 pts |
| Activated users | 19 | 34 | +75% |
| New paying customers (first `order.completed`) | 11.6 | 14.3 | +23% |
| Signup → paid within 30 days | 7.3% | 6.8% (cohorts still maturing) | n/a |

## By channel

| Channel | Signups/wk baseline | Signups/wk current | Share now | Activation 7d B → C | Signup→paid 30d B → C |
|---|---|---|---|---|---|
| Website (homepage, pricing, SEO pages) | 60 | 51 | 39% | 25% → 35% (homepage only) | 9.0% → 10.9%* (homepage only) |
| Unattributed (no landing URL) | 26 | 41 | 31% | 14% → 22% | 1.8% → n/a |
| Google Ads (Search + PMax) | 0.8 | 26.5 | 20% | 0% (n=10) → 12% | n/a → 2.8%* |
| ChatGPT Ads (new) | 0 | 4.5 | 3% | n/a → 0% (n=18) | n/a → 0%* |
| AI search, organic (chatgpt.com etc.) | 1.8 | 4.5 | 3% | 29% → 38% | 9 paid customers since Jul, the best payer rate |
| Meta Ads (website traffic) | 1.8 | 0.5 | <1% | 5% (n=21) | 0 paid customers since Jul |
| Instagram organic (bio link) | 1.0 | 1.3 | 1% | 0% | 1 paid customer since Jul |
| Internal test (`gtm_debug`) | 0 | 3.3 | 2% | 0% | Exclude |

\* These current cohorts are still inside the 30-day window, so treat the rate as a floor.

### Spend, CPL and CAC

- **Meta, RecurPost ad account [Certain].** ₹4,529 (27–31 Jul) plus ₹1,909 (Aug) bought 118 leads, about ₹55 per lead. Spend was ₹0 from September to November.
- **Meta lead forms, 1–13 Sep [Certain, from the Paid Ads Performance Report sheet].** This ran in another account, which the connector cannot read.
  - ₹26,792 spent, 155 leads, CPL ₹173.
  - 90 qualified leads, ₹298 per qualified lead.
  - Paid and revenue columns are blank.
  - The Lead Tracker showed all 147 leads with no owner at its last update.
  - Meta CAC: **not measurable**. Zero Meta-tagged users in Mixpanel paid between Jul and Nov.
- **Google Ads: spend not connected.** CAC = spend ÷ 3 paid customers so far from the current cohort.

### Sales funnel (Leadership Scorecard, Odoo)

| KPI | Baseline avg (Aug 3 – Oct 19) | Current avg (Oct 26 – Nov 16) |
|---|---|---|
| Demos completed / wk | ~21 | ~20 |
| Demo show rate | ~49% | ~52% |
| Demo → win rate (trailing) | ~4% | ~8% (volatile) |
| New MRR closed, India | ~₹9.2k / wk | ~₹9.6k / wk (last week ₹623) |

## Interpretation

- **[Certain] Signup growth comes mostly from Google Ads, which started around 19 Oct.** Google Ads signups activate at about one-third of the homepage rate (12% vs 35%) and pay at about one-quarter (2.8% vs 10.9%, both immature).
- **[Likely] Some of it is cannibalisation.** Website signups fell about 15% (60 → 51 a week) as Google Ads rose. Performance Max is probably capturing brand and organic demand. This needs a brand-exclusion test to confirm.
- **[Certain] Activation improved across channels.** The homepage went from 25% to 35% and unattributed from 14% to 22%. This is product or CS-driven, not ad-driven.
- **[Certain] AI search is the highest-quality channel per signup, but it is small.**

## Actions, ranked

1. **Get Google Ads spend into reporting this week.** Reconnect Windsor or export from Google Ads. Judge the channel on paid customers and activated users, not signups.
2. **Run a brand-term exclusion in Performance Max** and compare website signups with and without it.
3. **Fix attribution.**
   - Persist UTMs on `account_created` and the user profile.
   - Tag the mobile-app install source.
   - Filter `gtm_debug` and internal accounts out of every KPI.
4. **Pause ChatGPT Ads** until it produces activated users.
5. **Don't restart Meta lead forms** until each lead is email-matched to a RecurPost account and Odoo outcome, so CPL can become CAC.
6. **Retire or automate the Marketing KPI Tracker.** A manual tracker that nobody fills gives false confidence.
