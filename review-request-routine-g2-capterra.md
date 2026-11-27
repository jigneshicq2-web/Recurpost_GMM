# G2 & Capterra Review-Request Routine (Customer Success)

Owner: Customer Success lead · Supporting: Marketing (links, tracking, on-site badges) · Status: Draft v1 · 2026-11-27

---

## 1. Where we stand

| Platform | Reviews | Rating | Last review | Days without a review (as of 2026-11-27) |
|---|---|---|---|---|
| G2 | 65 | 4.5 | 2026-04-29 | ~212 |
| Capterra | 170 | 4.7 | 2026-03-09 | ~263 |

**Diagnosis**
- The problem is **how recent the reviews are, not how many there are.** No new reviews for 7–9 months tells buyers and platform rankings that the product is stagnant or customers are leaving. [Likely] G2's Grid/seasonal reports and Capterra's Shortlist give extra weight to recent reviews, so the old reviews are counting for less every month.
- G2 is the weaker profile: fewer reviews and a lower rating, so each new review moves its average more. Capterra is part of the Gartner Digital Markets network (Capterra, GetApp, Software Advice), so [Likely] one Capterra review shows up on all three sites.
- **Our attribution is blind.** We can't say which platform sends signups. Fix this first (section 3). Otherwise we'll keep guessing at where to put effort.

## 2. Targets (first 90 days: Dec 2026 – Feb 2027)

| Metric | Target |
|---|---|
| New G2 reviews | 30 (65 → 95) |
| New Capterra reviews | 15 (170 → 185) |
| Freshness | At least 1 new review per platform every 2 weeks, without exception |
| Asks sent | ~300 total (assumes a 15% ask→review rate [Guessing]; adjust after week 4) |
| Average rating | Hold Capterra at ≥4.6, move G2 toward 4.6 |
| Negative-review response time | < 48 hours, 100% |

**Routing rule:** each ask links to **one platform only**. Two links split attention and lower completion.
- Default for the next 90 days: **G2** (it's stalest and lowest, so the gains are biggest).
- Send to **Capterra** instead when: the customer is a small business, solo user or agency owner who found us via Capterra/GetApp, OR they already have a G2 review, OR the 2-week Capterra freshness floor is at risk.
- Reconsider the split at day 45, using the referral data from section 3.

## 3. Fix tracking first (Marketing, week 1)

Referral visits from g2.com and capterra.com should show up in GA4 even without UTMs. If they don't, the platforms are probably stripping the referrer (`rel="noreferrer"` or a redirect).

1. **Check first:** GA4 → Reports → Acquisition → Traffic acquisition → set *Session source* to contain `g2` / `capterra`, last 12 months. Write down what you find.
2. **Add UTM links to the profile website/CTA fields** in each vendor portal:
   - G2: `https://recurpost.com/?utm_source=g2&utm_medium=referral&utm_campaign=g2_profile`
   - Capterra: `https://recurpost.com/?utm_source=capterra&utm_medium=referral&utm_campaign=capterra_profile`
   - If you run paid listings (Capterra PPC / G2 Buyer Intent), give those a separate `utm_medium=cpc`.
3. **Confirm signup is a GA4 key event.** Without it, UTMs only measure traffic, not signups.
4. **Also tag the review-request links in our own emails** (`utm_source=cs_email&utm_campaign=review_ask_g2`) so we can count clicks per template.
5. Optional: add "How did you hear about us?" to signup/onboarding with G2 and Capterra as options. This catches people who searched for us after reading reviews, which UTMs miss.

## 4. Triggers: who gets asked and when

Choose customers by **what they've done in the product**, never by sentiment survey results (see section 8).

| # | Trigger | Signal | Sent by | Template |
|---|---|---|---|---|
| T1 | Activation milestone | Paid account, ≥30 days active, and has used the core workflow (e.g. ≥1 recurring library/schedule running, ≥N posts published) | Automated email from CSM's name | A |
| T2 | Support win | Ticket marked *solved*, customer rated support ≥4/5 or said thanks | CSM, within 24h | B |
| T3 | Requested feature shipped | Customer on the request list for a feature that just launched | CSM | C |
| T4 | Renewal / upgrade | Annual renewal processed or plan upgrade | Automated | A |
| T5 | Live call | Onboarding/QBR call where the customer praises the product without being prompted | CSM asks on the call, sends link right after | Call script |

**Exclusions (don't ask)**
- Trial users, or accounts less than 30 days old
- Accounts with an open ticket, an escalation, a failed payment, or a cancellation request
- Anyone asked in the last 180 days, or who already reviewed on that platform
- Internal, partner, affiliate, or employee accounts (both platforms count these as conflicts of interest)

## 5. Cadence & ownership

- **Weekly quota:** each CSM sends 15 asks per week (T2 + T5 manually, T1/T4 automated). With 2 CSMs plus automation that's roughly 300 in 90 days. Scale up or down with headcount.
- **Sequence:** Ask → one reminder on day 5 → stop. Never a third touch.
- **Weekly 15-minute review (Monday):** CS lead checks the tracker: asks sent, reviews posted, any negative reviews, freshness floor status.
- **Monthly:** share new quotes with Marketing for the signup/pricing pages and the "Wall of love".

## 6. Incentive policy

Both platforms allow incentives **if they're offered to everyone you ask, whatever they say, and disclosed.**

- Offer: **$25 Amazon gift card (or local equivalent) for a published review**, positive or negative. Say exactly that in the email.
- Pay out only after the platform publishes the review. Platforms reject short or low-effort reviews, so we don't pay for those.
- Budget: 45 reviews × $25 ≈ **$1,125 for 90 days**.
- Before launching, check the current incentive rules in the G2 and Capterra vendor portals. Both run their own gift-card review campaigns, which may be cheaper and handle compliance for us. Use theirs if available.
- **Be clear about what this buys:** incentives increase review *volume*. They do not produce signups directly. Signups come later and indirectly, through better ranking/badges on the platforms and review quotes on our own pages. Judge this on review count and freshness in Q1. Judge signups only after the UTM data from section 3 has been collecting for about 60 days.

## 7. Email templates

Placeholders: `{{first_name}}`, `{{csm_name}}`, `{{milestone}}`, `{{feature}}`, `{{review_link}}`.
Review links (replace with the exact URLs from each vendor portal):
- G2: `https://www.g2.com/products/recurpost/take_survey`
- Capterra: `https://www.capterra.com/reviews/<PRODUCT_ID>/RecurPost` *(get the exact link from the Capterra vendor portal)*

Keep emails as plain text, sent from the CSM's own name. No banners.

### Template A — Milestone / renewal (T1, T4)
**Subject:** {{first_name}}, quick favor? (2 min)

> Hi {{first_name}},
>
> You've been using RecurPost for a while now ({{milestone}}). Thanks for sticking with us.
>
> Would you share an honest review of your experience on G2? Other agencies and small teams rely on these reviews when choosing a tool, and your feedback goes straight to our product team.
>
> 👉 {{review_link}}
>
> It takes about 3 minutes. As a thank-you, we'll send a $25 gift card for any published review, positive or critical.
>
> Thanks,
> {{csm_name}}
> Customer Success, RecurPost

### Template B — After a solved ticket (T2)
**Subject:** Glad we got that sorted

> Hi {{first_name}},
>
> Glad we got that fixed for you. If you have 3 minutes, an honest review of RecurPost on G2 would really help us:
>
> 👉 {{review_link}}
>
> Any published review gets a $25 gift card from us as a thank-you, whatever you write.
>
> {{csm_name}}

### Template C — Feature you asked for has shipped (T3)
**Subject:** You asked, we built it: {{feature}}

> Hi {{first_name}},
>
> A while back you asked for {{feature}}. It's live now. [1-line how-to / link]
>
> If RecurPost has been useful to you, would you leave an honest review on G2? It helps other teams find us, and it tells us which features to prioritize next.
>
> 👉 {{review_link}}
>
> $25 gift card for any published review, as a thank-you.
>
> {{csm_name}}

### Reminder (day 5, reply in the same thread)
> Hi {{first_name}}, just bumping this in case it got buried. Here's the link again: {{review_link}}. No worries if now's not a good time.

### CSM call script (T5)
> "That's really good to hear. Would you be open to saying that in a quick review on G2? It helps other agencies who are evaluating tools. I'll email you the link right after this call. It takes about three minutes, and we send a $25 gift card for any review that's published."

Send Template A within 1 hour of the call, with the first line changed to mention the call.

## 8. Compliance rules (do not break these)

1. **No review gating.** Never send an NPS/CSAT survey and then send the review link only to promoters. Triggers are behaviour-based (section 4). [Likely] G2 and Capterra policies, and [Certain] the FTC's 2024 rule on fake reviews (16 CFR Part 465), prohibit suppressing or filtering for negative sentiment.
2. **Incentives can't depend on sentiment** and must be disclosed in the ask.
3. **No reviews from employees, family, partners, or affiliates.**
4. **Never write, edit, or "suggest" review text.** You may suggest *topics* ("what problem it solved, what you'd improve").
5. **One link, one platform, one ask plus one reminder.**

## 9. Handling negative reviews

- Reply publicly within 48h: acknowledge, don't argue, take it offline ("I've emailed you directly").
- Open a ticket and assign the CSM. If the issue gets fixed, the CSM may ask *once* whether they'd update their review. Never pressure them, and never tie it to an incentive.
- Log the theme in the tracker. If the same issue shows up in 3 or more reviews, flag it to Product.

## 10. Tracker

Use `review-request-tracker-template.csv` (import into Google Sheets). Columns:

`date_asked, customer_name, account_id, plan, csm, trigger (T1–T5), platform (G2/Capterra), template, reminder_sent (Y/N), review_posted (Y/N), date_posted, rating, incentive_paid (Y/N), quote_usable_for_site (Y/N), notes`

Weekly KPIs (calculate in the sheet): asks sent · reviews posted · ask→review % by trigger and by template · avg rating of new reviews · days since last review per platform · incentive spend.

## 11. Week-1 launch checklist

- [ ] Marketing: run the GA4 referral check; add UTM URLs to both vendor profiles; confirm signup key event (section 3)
- [ ] CS lead: get the exact review links from both vendor portals; check for platform-run gift-card campaigns (section 6)
- [ ] CS lead: build the exclusion list and pull the first T1 batch (paid, ≥30 days, active) (section 4)
- [ ] CS ops: set up T1/T4 automated emails and the day-5 reminder in the email tool
- [ ] Finance: approve the $1,125 incentive budget and how payouts are handled
- [ ] CSMs: 15-minute briefing on triggers, script, and compliance rules (sections 4, 7, 8)
- [ ] Send the first 30 asks by end of week 1, choosing the most engaged accounts first
- [ ] Marketing: fix the duplicate/inconsistent testimonial attribution flagged in `recurpost-conversion-experiments.md`, and plan to replace it with real G2/Capterra quotes plus a rating badge once fresh reviews come in
