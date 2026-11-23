"""Generate Google Ads Editor import CSVs for the RecurPost Search plan."""
import csv, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
B = "https://recurpost.com"

C_BRAND = "RP | Search | Brand | US-UK-CA-AU"
C_US_HI = "RP | Search | NB High-Intent | US"
C_US_CORE = "RP | Search | NB Core | US"
C_INTL_HI = "RP | Search | NB High-Intent | UK-CA-AU"
C_TEST = "RP | Search | NB Test | AE-SG (paused)"

COMPETITORS = {
    "hootsuite": "hootsuite", "buffer": "buffer", "sprout social": "sprout-social",
    "later": "later", "meetedgar": "meetedgar", "socialbee": "socialbee",
    "agorapulse": "agorapulse", "sendible": "sendible", "socialpilot": "socialpilot",
    "planoly": "planoly", "publer": "publer", "loomly": "loomly",
    "smarterqueue": "smarterqueue", "coschedule": "coschedule", "metricool": "metricool",
}

# (ad group, final url, [(keyword, match)])
def comp_keywords():
    rows = []
    for name, slug in COMPETITORS.items():
        url = f"{B}/compare/alternatives/{slug}/"
        # "buffer" and "later" are ambiguous words, so qualify them with "app"
        q = f"{name} app" if name in ("buffer", "later") else name
        rows += [(f"{q} alternative", "Phrase", url),
                 (f"{q} alternatives", "Phrase", url),
                 (f"apps like {name}", "Phrase", url),
                 (f"cheaper than {q}", "Phrase", url)]
    rows += [("social media scheduler alternative", "Phrase", f"{B}/compare/alternatives/"),
             ("switch social media scheduler", "Phrase", f"{B}/migrate/")]
    return rows

HIGH_INTENT = {
    "Competitor Alternatives": (f"{B}/compare/alternatives/", None),  # keyword-level URLs
    "Evergreen & Recycle": (f"{B}/features/schedule/evergreen-content-marketing/", [
        ("recycle social media posts", "Phrase"), ("evergreen content scheduler", "Phrase"),
        ("evergreen social media posts", "Phrase"), ("repost old social media posts", "Phrase"),
        ("recurring social media posts", "Phrase"), ("auto repost social media", "Phrase"),
        ("social media content library", "Phrase"), ("evergreen post scheduler", "Exact"),
        ("schedule recurring posts", "Phrase"), ("reshare old posts automatically", "Phrase")]),
    "Small Business": (f"{B}/use-cases/smbs/", [
        ("social media scheduler for small business", "Phrase"),
        ("social media management for small business", "Phrase"),
        ("small business social media tool", "Phrase"),
        ("social media posting tool for small business", "Phrase"),
        ("schedule social media posts for my business", "Phrase"),
        ("affordable social media scheduler", "Phrase"),
        ("cheap social media scheduler", "Phrase"),
        ("social media scheduler for solopreneurs", "Phrase")]),
    "Agency": (f"{B}/use-cases/agencies/", [
        ("social media management tool for agencies", "Phrase"),
        ("social media scheduler for agencies", "Phrase"),
        ("agency social media management software", "Phrase"),
        ("social media tool for agencies", "Phrase"),
        ("manage multiple social media accounts for clients", "Phrase"),
        ("social media management for multiple clients", "Phrase"),
        ("white label social media reports", "Phrase"),
        ("white label social media scheduler", "Phrase"),
        ("social media client approval tool", "Phrase"),
        ("social media approval workflow", "Phrase")]),
    "Google Business Profile": (f"{B}/schedule-google-business-profile-posts/", [
        ("schedule google business profile posts", "Phrase"),
        ("google business profile post scheduler", "Phrase"),
        ("schedule google my business posts", "Phrase"),
        ("google business posts multiple locations", "Phrase"),
        ("multi location social media management", "Phrase")]),
    "Bulk Scheduling": (f"{B}/features/schedule/bulk-scheduling/", [
        ("bulk schedule social media posts", "Phrase"),
        ("bulk upload social media posts", "Phrase"),
        ("csv social media scheduler", "Phrase"),
        ("schedule a month of social media posts", "Phrase")]),
}

CORE = {
    "Core Scheduler": (f"{B}/plans-and-pricing/", [
        ("social media scheduling tool", "Exact"), ("social media scheduler", "Exact"),
        ("social media management software", "Exact"), ("social media management tool", "Exact"),
        ("schedule posts on multiple platforms", "Exact"), ("social media posting tool", "Exact"),
        ("best social media scheduler", "Exact"), ("social media planner app", "Exact"),
        ("post to all social media at once", "Exact")]),
}

BRAND = {
    "Brand": (f"{B}/", [("recurpost", "Exact"), ("recurpost", "Phrase"),
                        ("recur post", "Phrase")]),
    "Brand Pricing & Reviews": (f"{B}/plans-and-pricing/", [
        ("recurpost pricing", "Phrase"), ("recurpost review", "Phrase"),
        ("recurpost reviews", "Phrase"), ("recurpost plans", "Phrase")]),
}

kw_rows = []
def add_groups(campaign, groups):
    for ag, (url, kws) in groups.items():
        if ag == "Competitor Alternatives":
            for k, m, u in comp_keywords():
                kw_rows.append([campaign, ag, k, m, u])
        else:
            for k, m in kws:
                kw_rows.append([campaign, ag, k, m, url])

add_groups(C_BRAND, BRAND)
add_groups(C_US_HI, HIGH_INTENT)
add_groups(C_US_CORE, CORE)
add_groups(C_INTL_HI, HIGH_INTENT)
add_groups(C_TEST, {k: v for k, v in HIGH_INTENT.items()
                    if k in ("Competitor Alternatives", "Evergreen & Recycle", "Small Business")})

with open(f"{OUT}/keywords.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad Group", "Keyword", "Criterion Type", "Final URL"])
    w.writerows(kw_rows)

# ---------- Negatives (shared list, phrase match) ----------
NEG = {
    "Hiring an agency": ["agency near me", "near me", "hire", "hiring an agency", "services",
                         "company", "companies", "consultant", "outsource", "quote",
                         "marketing agency near me", "smm agency", "smm panel"],
    "Ads, not organic posting": ["advertising", "ads manager", "facebook ads", "google ads",
                                 "ppc", "paid social", "boost post", "ad agency"],
    "Learning, not buying": ["course", "courses", "certification", "certificate", "training",
                             "tutorial", "what is", "definition", "meaning", "examples",
                             "ideas", "tips", "pdf", "book", "degree", "class", "how to become"],
    "Jobs": ["jobs", "job", "salary", "career", "careers", "internship", "resume", "remote"],
    "Free-only / low intent": ["crack", "apk", "mod", "free download", "template", "templates",
                               "open source", "github"],
    "Existing users of other tools": ["login", "log in", "sign in", "support", "customer service",
                                      "phone number", "cancel", "refund", "down", "not working",
                                      "promo code", "coupon", "discount code"],
    "Out of scope": ["meta business suite", "creator studio", "instagram followers",
                     "buy followers", "likes", "bot", "spy", "hack"],
}
with open(f"{OUT}/negatives.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Shared Set", "Theme", "Keyword", "Criterion Type", "Apply to"])
    for theme, words in NEG.items():
        for word in words:
            w.writerow(["RP Shared Negatives", theme, word, "Negative Phrase",
                        "All non-brand campaigns"])
    # brand-campaign-specific negatives
    for word in ["login", "log in", "sign in", "support", "cancel"]:
        w.writerow(["(campaign-level)", "Existing customers", f"recurpost {word}",
                    "Negative Phrase", C_BRAND])

# ---------- RSAs ----------
COMMON = ["Free 14-Day Trial, No Card", "Plans From $9/Month", "Recycle Your Best Posts",
          "Post to 10 Social Networks", "One Calendar, All Networks",
          "AI Captions & Images Built In", "Bulk Scheduling Built In",
          "Evergreen Content Libraries"]

ADS = {
    "Small Business": dict(
        h=["Social Scheduler for SMBs", "Manage Your Own Social Media", "Set It Once, Keep Posting",
           "Schedule Google Business Posts", "Simple Social Media Planning",
           "Reply From One Social Inbox", "Keep Your Feed Active"] + COMMON,
        d=["Plan, schedule and recycle posts for your business on 10 networks. From $9/month.",
           "Try it free for 14 days with no credit card. Connect your accounts and fill your calendar.",
           "Evergreen libraries re-share your best posts automatically, so your feed never goes quiet.",
           "Write captions and images with built-in AI, then bulk schedule weeks of posts at once."],
        p=("small-business", "scheduler")),
    "Agency": dict(
        h=["Social Media Tool for Agencies", "Manage Every Client Account",
           "Client Workspaces & Approvals", "White-Label Client Reports", "All Clients, One Calendar",
           "Client Approval Links", "Agency Plan From $79/Month", "Reports With Your Logo",
           "Roles & Permissions Built In", "One Inbox for All Clients",
           "Free 14-Day Trial, No Card", "Recycle Your Best Posts", "Post to 10 Social Networks",
           "Bulk Scheduling Built In", "AI Captions & Images Built In"],
        d=["Client workspaces, approval links and white-label reports in one social media tool.",
           "Schedule, approve and report for every client from one dashboard. Free 14-day trial.",
           "Recycle evergreen posts for each client and keep every calendar full with less work.",
           "Roles and permissions keep clients and teammates in their lane. No credit card needed."],
        p=("agencies", "clients")),
    "Competitor Alternatives": dict(
        h=["Switching Social Media Tools?", "Compare Before You Renew", "Side-by-Side Comparison",
           "See How to Switch", "Try Our Pricing Calculator", "Client Approvals & Reports",
           "Reply From One Social Inbox"] + COMMON,
        d=["See how RecurPost compares on features and price, then try it free for 14 days.",
           "Plans from $9/month with evergreen recycling, AI captions and client approvals.",
           "Connect your accounts and start scheduling today. No credit card needed for the trial.",
           "Post to Facebook, Instagram, LinkedIn, X, TikTok, YouTube, Pinterest and more."],
        p=("compare", "alternatives")),
    "Evergreen & Recycle": dict(
        h=["Evergreen Content Scheduler", "Auto-Reshare Evergreen Posts", "Set It Once, Keep Posting",
           "Content Libraries That Repeat", "Never Run Out of Posts", "Recurring Social Media Posts",
           "Keep Your Feed Active", "Import Posts From RSS", "Free 14-Day Trial, No Card",
           "Plans From $9/Month", "Recycle Your Best Posts", "Post to 10 Social Networks",
           "AI Captions & Images Built In", "Bulk Scheduling Built In", "One Calendar, All Networks"],
        d=["Build evergreen libraries and RecurPost re-shares your best posts on a schedule you set.",
           "Keep every profile active without writing new posts daily. Free 14-day trial, no card.",
           "Works with Facebook, Instagram, LinkedIn, X, TikTok, Pinterest, Google Business and more.",
           "Plans from $9/month. Bulk upload, RSS import and AI captions fill your libraries fast."],
        p=("evergreen", "recycle")),
    "Google Business Profile": dict(
        h=["Schedule Google Business Posts", "GBP Post Scheduler", "Manage Multiple Locations",
           "Google Business + Social", "Keep Every Location Active", "Plan Posts for Every Location",
           "Multi-Location Scheduling"] + COMMON,
        d=["Schedule Google Business Profile posts with Facebook, Instagram and more in one place.",
           "Keep every location's profile fresh with recurring posts. Free 14-day trial, no card.",
           "Plans from $9/month. Bulk schedule and recycle posts across all your business locations.",
           "Write posts with built-in AI and schedule them to every location from one dashboard."],
        p=("google-business", "posts")),
    "Bulk Scheduling": dict(
        h=["Bulk Schedule Social Posts", "Upload Weeks of Posts at Once", "Bulk Upload & Schedule",
           "Import Posts From RSS", "Plan a Month in One Sitting", "Reply From One Social Inbox",
           "Client Approvals & Reports"] + COMMON,
        d=["Upload a batch of posts, set the times and let RecurPost publish across 10 networks.",
           "Bulk scheduling, RSS import and evergreen recycling. Try free for 14 days, no card.",
           "Plans from $9/month for your own brand, or client workspaces for agencies.",
           "Write captions and images with built-in AI, then schedule them all in one go."],
        p=("bulk", "scheduling")),
    "Core Scheduler": dict(
        h=["Social Media Scheduler", "Schedule Posts Everywhere", "Social Media Management Tool",
           "Plan, Schedule & Recycle", "Reports With Your Logo", "Client Approvals & Reports",
           "Reply From One Social Inbox"] + COMMON,
        d=["Plan, schedule and recycle posts on 10 social networks from one calendar. From $9/month.",
           "Try it free for 14 days with no credit card. Built for solo brands and agencies alike.",
           "Evergreen libraries re-share your best posts automatically, so your feed never goes quiet.",
           "AI captions, bulk scheduling, approvals and white-label reports in one simple tool."],
        p=("plans", "pricing")),
    "Brand": dict(
        h=["RecurPost Official Site", "RecurPost Plans From $9/Month", "Start Your RecurPost Trial",
           "Social Inbox, Reports & More", "Client Approvals & Reports", "Reports With Your Logo",
           "Reply From One Social Inbox"] + COMMON,
        d=["Plan, schedule and recycle posts on 10 social networks. Free 14-day trial, no card.",
           "Plans from $9/month for your own brand, or client workspaces for agencies.",
           "Evergreen libraries, AI captions, bulk scheduling, approvals and white-label reports.",
           "Start your free 14-day trial today. No credit card needed."],
        p=("official", "")),
}
ADS["Brand Pricing & Reviews"] = dict(ADS["Brand"], p=("pricing", "plans"))

errors = []
ad_rows = []
for campaign, groups in [(C_BRAND, BRAND), (C_US_HI, HIGH_INTENT), (C_US_CORE, CORE),
                         (C_INTL_HI, HIGH_INTENT), (C_TEST, HIGH_INTENT)]:
    for ag, (url, _) in groups.items():
        if campaign == C_TEST and ag not in ("Competitor Alternatives", "Evergreen & Recycle",
                                             "Small Business"):
            continue
        a = ADS[ag]
        h, d = a["h"], a["d"]
        if len(h) != 15 or len(d) != 4 or len(set(h)) != 15:
            errors.append(f"{ag}: {len(h)} headlines ({len(set(h))} unique), {len(d)} descriptions")
        for x in h:
            if len(x) > 30: errors.append(f"H>30 ({len(x)}): {x}")
        for x in d:
            if len(x) > 90: errors.append(f"D>90 ({len(x)}): {x}")
        for x in a["p"]:
            if len(x) > 15: errors.append(f"Path>15: {x}")
        ad_rows.append([campaign, ag, "Responsive search ad", url, a["p"][0], a["p"][1]] + h + d)

with open(f"{OUT}/responsive-search-ads.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad Group", "Ad type", "Final URL", "Path 1", "Path 2"]
               + [f"Headline {i}" for i in range(1, 16)]
               + [f"Description {i}" for i in range(1, 5)])
    w.writerows(ad_rows)

# ---------- Assets ----------
SITELINKS = [("Plans & Pricing", "/plans-and-pricing/", "Starter, Personal and Agency", "Free 14-day trial, no card"),
             ("For Small Businesses", "/use-cases/smbs/", "Manage your own social media", "Plans from $9/month"),
             ("For Agencies", "/use-cases/agencies/", "Client workspaces and approvals", "White-label reports"),
             ("Evergreen Recycling", "/features/schedule/evergreen-content-marketing/", "Re-share your best posts", "Libraries that repeat"),
             ("Compare Alternatives", "/compare/alternatives/", "Side-by-side comparisons", "Features and pricing"),
             ("White-Label Reports", "/features/measure/brand-logo-white-label-reports/", "Reports with your logo", "Built for client work"),
             ("Switch to RecurPost", "/migrate/", "Move from your current tool", "See how switching works"),
             ("Bulk Scheduling", "/features/schedule/bulk-scheduling/", "Upload posts in batches", "Fill weeks in one sitting")]
CALLOUTS = ["No Credit Card Needed", "14-Day Free Trial", "Evergreen Post Recycling",
            "Client Approval Links", "White-Label Reports", "AI Captions & Images",
            "10 Social Networks", "Bulk Scheduling", "Social Inbox"]
with open(f"{OUT}/assets.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Asset type", "Text", "Description line 1", "Description line 2", "Final URL", "Level"])
    for t, u, d1, d2 in SITELINKS:
        if len(t) > 25: errors.append(f"Sitelink>25: {t}")
        for x in (d1, d2):
            if len(x) > 35: errors.append(f"SL desc>35: {x}")
        w.writerow(["Sitelink", t, d1, d2, B + u, "Account"])
    for c in CALLOUTS:
        if len(c) > 25: errors.append(f"Callout>25: {c}")
        w.writerow(["Callout", c, "", "", "", "Account"])
    for plan, price, desc in [("Starter", "9", "2 social accounts"), ("Personal", "25", "Up to 5 accounts"),
                              ("Agency", "79", "Client workspaces")]:
        w.writerow(["Price", f"{plan} | USD {price} per month", desc, "", B + "/plans-and-pricing/", "Account"])

print(f"keywords: {len(kw_rows)} rows, ads: {len(ad_rows)}")
print("ERRORS:" if errors else "All length checks passed")
for e in errors: print("  ", e)
