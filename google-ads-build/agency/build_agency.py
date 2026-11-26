"""Generate Google Ads Editor CSVs for the RecurPost agency-only Search campaigns.

Usage: python3 build_agency.py <output_dir>
"""
import csv, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
B = "https://recurpost.com"

C_US = "RP | Search | Agency | US"
C_UKCA = "RP | Search | Agency | UK-CA"
C_TEST = "RP | Search | Agency | AU-SG-NL (test, paused)"
C_RLSA = "RP | Search | Agency RLSA | US-UK-CA"

AGENCY_PAGE = f"{B}/use-cases/agencies/"

GROUPS = {
    "Agency Software": (AGENCY_PAGE, [
        ("social media management tool for agencies", "Phrase"),
        ("social media management software for agencies", "Phrase"),
        ("social media management platform for agencies", "Phrase"),
        ("social media scheduler for agencies", "Phrase"),
        ("social media scheduling tool for agencies", "Phrase"),
        ("social media software for agencies", "Phrase"),
        ("social media tool for agencies", "Phrase"),
        ("social media tools for agencies", "Phrase"),
        ("best social media tool for agencies", "Phrase"),
        ("social media tool for marketing agencies", "Phrase"),
        ("social media planner for agencies", "Phrase"),
        ("agency social media management software", "Phrase"),
        ("agency social media scheduler", "Phrase"),
        ("agency social media tool", "Phrase"),
        ("social media agency software", "Phrase"),
        ("social media agency tools", "Phrase"),
        ("smm agency software", "Phrase"),
        ("social media management for agencies", "Exact"),
    ]),
    "Multi-Client Management": (AGENCY_PAGE, [
        ("manage multiple social media accounts for clients", "Phrase"),
        ("social media management for multiple clients", "Phrase"),
        ("manage clients social media accounts", "Phrase"),
        ("social media tool for multiple clients", "Phrase"),
        ("multi client social media management", "Phrase"),
        ("social media dashboard for multiple clients", "Phrase"),
        ("schedule posts for multiple clients", "Phrase"),
        ("manage multiple brands social media", "Phrase"),
        ("social media client management software", "Phrase"),
        ("client workspaces social media", "Phrase"),
        ("connect client social accounts without password", "Phrase"),
    ]),
    "Client Approvals": (f"{B}/features/collaborate/approval-workflow/", [
        ("social media approval workflow", "Phrase"),
        ("social media content approval tool", "Phrase"),
        ("social media post approval software", "Phrase"),
        ("client approval social media posts", "Phrase"),
        ("social media approval tool for clients", "Phrase"),
        ("shareable social media calendar for clients", "Phrase"),
        ("client social media calendar tool", "Phrase"),
        ("social media calendar with client approval", "Phrase"),
    ]),
    "White-Label Reporting": (f"{B}/features/measure/brand-logo-white-label-reports/", [
        ("white label social media reports", "Phrase"),
        ("white label social media reporting tool", "Phrase"),
        ("white label social media management tool", "Phrase"),
        ("white label social media scheduler", "Phrase"),
        ("white label social media analytics", "Phrase"),
        ("branded social media reports for clients", "Phrase"),
        ("social media client reporting tool", "Phrase"),
        ("automated social media reports for clients", "Phrase"),
    ]),
    "Agency Competitor Switch": (None, None),  # keyword-level URLs below
    "Agency Plan Pricing": (f"{B}/plans-and-pricing/", [
        ("social media management software for agencies pricing", "Phrase"),
        ("agency social media tool pricing", "Phrase"),
        ("affordable social media tool for agencies", "Phrase"),
        ("cheap social media scheduler for agencies", "Phrase"),
        ("social media scheduler price per client", "Phrase"),
    ]),
}

# Agency-focused competitors that have a RecurPost comparison page
COMPETITORS = {"sendible": "sendible", "agorapulse": "agorapulse", "socialpilot": "socialpilot",
               "vista social": "vista-social", "planable": "planable", "statusbrew": "statusbrew",
               "heyorca": "heyorca", "contentstudio": "contentstudio", "loomly": "loomly",
               "sked social": "sked-social", "eclincher": "eclincher"}

def competitor_rows():
    rows = []
    for name, slug in COMPETITORS.items():
        url = f"{B}/compare/alternatives/{slug}/"
        rows += [(f"{name} alternative", "Phrase", url), (f"{name} alternatives", "Phrase", url),
                 (f"cheaper than {name}", "Phrase", url)]
    for big, slug in (("hootsuite", "hootsuite"), ("sprout social", "sprout-social")):
        url = f"{B}/compare/alternatives/{slug}/"
        rows += [(f"{big} alternative for agencies", "Phrase", url),
                 (f"{big} for agencies", "Phrase", url)]
    rows.append(("switch social media tool agency", "Phrase", f"{B}/migrate/"))
    return rows

RLSA = {"Generic Scheduler (agency-intent visitors only)": (AGENCY_PAGE, [
    ("social media scheduler", "Phrase"), ("social media management tool", "Phrase"),
    ("social media scheduling tool", "Phrase"), ("social media management software", "Phrase"),
    ("social media management platform", "Phrase"), ("hootsuite alternative", "Phrase"),
    ("sprout social alternative", "Phrase"), ("buffer app alternative", "Phrase")])}

kw_rows, seeds = [], []
def add(campaign, groups):
    for ag, (url, kws) in groups.items():
        if ag == "Agency Competitor Switch":
            for k, m, u in competitor_rows():
                kw_rows.append([campaign, ag, k, m, u]); seeds.append(k)
        else:
            for k, m in kws:
                kw_rows.append([campaign, ag, k, m, url]); seeds.append(k)

for c in (C_US, C_UKCA, C_TEST):
    add(c, GROUPS)
add(C_RLSA, RLSA)

with open(f"{OUT}/keywords.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad Group", "Keyword", "Criterion Type", "Final URL"])
    w.writerows(kw_rows)

uniq = list(dict.fromkeys(seeds))
with open(f"{OUT}/keyword-planner-seed-list.txt", "w") as f:
    f.write("\n".join(uniq) + "\n")

# ---------------- negatives ----------------
NEG = {
    "Hiring or buying agency services": ["near me", "hire", "hiring", "services", "service", "company",
        "companies", "consultant", "consulting", "packages", "package", "outsourcing", "outsource",
        "fulfillment", "reseller", "resell", "smm panel", "panel", "quote", "rates", "cost of hiring"],
    "Starting or running an agency (not buying software)": ["how to start", "start a", "starting a",
        "business plan", "name ideas", "names", "contract", "proposal", "proposal template",
        "for sale", "franchise", "course", "courses", "certification", "training", "tutorial",
        "what is", "definition", "examples", "salary", "jobs", "job", "career", "internship"],
    "Not agencies (keep this campaign agency-only)": ["small business", "for small businesses",
        "solopreneur", "personal brand", "personal use", "creator", "creators", "influencer",
        "student", "students", "church", "for my business"],
    "Wrong product": ["advertising", "ads manager", "facebook ads", "google ads", "ppc", "seo",
        "website builder", "crm", "invoice", "invoicing", "time tracking", "project management",
        "buy followers", "followers", "likes", "bot"],
    "Low intent or existing users": ["free download", "crack", "apk", "open source", "github",
        "login", "log in", "sign in", "support", "customer service", "cancel", "refund",
        "coupon", "promo code", "not working"],
}
with open(f"{OUT}/negatives.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Shared Set", "Theme", "Keyword", "Criterion Type", "Apply to"])
    for theme, words in NEG.items():
        for word in words:
            w.writerow(["RP Agency Negatives", theme, word, "Negative Phrase", "All agency Search campaigns"])

# ---------------- RSAs ----------------
H_CORE = ["Social Media Tool for Agencies", "Built for Agencies, From $79", "A Workspace for Every Client",
          "White-Label Client Reports", "Client Approval Workflow", "No-Password Client Onboarding",
          "20 Social Accounts for $79/mo", "Shareable Client Calendars", "Automated Client Reports",
          "Roles & Permissions Built In", "Free 14-Day Agency Trial", "No Credit Card to Start",
          "Switch Without Losing Queues", "Recycle Evergreen Client Posts", "Save 2 Months With Yearly"]
D_ALL = ["Give every client its own workspace, approval flow and white-label reports. From $79/mo.",
         "Clients connect accounts without sharing passwords and approve posts by link. Free trial.",
         "20 social accounts and 3 users on the Agency plan. Add accounts for $4/mo as you grow.",
         "Schedule, recycle and report across 10 networks for every client from one dashboard.",
         "Switching tools? Move over without losing queues, libraries or approvals. No card needed."]

def swap(base, new):
    """Replace the last len(new) headlines of base with ad-group-specific ones, keep 15 unique."""
    out = [h for h in base if h not in new]
    return (new + out)[:15]

ADS = {
    "Agency Software": [dict(h=H_CORE, d=D_ALL[:4], p=("agencies", "client-work")),
                        dict(h=H_CORE, d=D_ALL[1:], p=("agency-plan", "trial"))],
    "Multi-Client Management": [dict(h=swap(H_CORE, ["Manage Every Client Account", "One Inbox for Every Client",
                                                     "All Clients, One Dashboard"]), d=D_ALL[:4],
                                     p=("agencies", "clients"))],
    "Client Approvals": [dict(h=swap(H_CORE, ["Clients Approve Posts by Link", "Internal & Client Approvals",
                                              "Comment-Ready Client Calendar"]),
                              d=[D_ALL[1], D_ALL[0],
                                 "Route posts through internal and client review stages before they go live.",
                                 D_ALL[2]], p=("approvals", "clients"))],
    "White-Label Reporting": [dict(h=swap(H_CORE, ["Reports With Your Agency Logo", "Scheduled Client Reports",
                                                   "Branded Reports for Clients"]),
                                   d=["Send clients scheduled analytics reports under your own agency brand.",
                                      D_ALL[0], D_ALL[2], D_ALL[1]], p=("white-label", "reports"))],
    "Agency Competitor Switch": [dict(h=swap(H_CORE, ["Switching Agency Tools?", "Compare Before You Renew",
                                                      "See How Agencies Switch"]),
                                      d=[D_ALL[4], D_ALL[0], D_ALL[2], D_ALL[1]], p=("compare", "agencies"))],
    "Agency Plan Pricing": [dict(h=swap(H_CORE, ["Agency Plan: $79/Month", "$4/mo Per Extra Account",
                                                 "Yearly: 2 Months Free"]),
                                 d=[D_ALL[2], D_ALL[0], D_ALL[1], D_ALL[4]], p=("pricing", "agency"))],
    "Generic Scheduler (agency-intent visitors only)": [dict(h=swap(H_CORE, ["Back for Your Agency Trial?",
                                                                             "Your Clients, One Dashboard"]),
                                                             d=D_ALL[:4], p=("agencies", "trial"))],
}

errors, ad_rows = [], []
for campaign, groups in ((C_US, GROUPS), (C_UKCA, GROUPS), (C_TEST, GROUPS), (C_RLSA, RLSA)):
    for ag, (url, _) in groups.items():
        final = url or f"{B}/compare/alternatives/"
        for a in ADS[ag]:
            h, d = a["h"], a["d"]
            if len(h) != 15 or len(set(h)) != 15: errors.append(f"{ag}: {len(set(h))} unique headlines")
            if len(d) != 4: errors.append(f"{ag}: {len(d)} descriptions")
            errors += [f"H>30 ({len(x)}): {x}" for x in h if len(x) > 30]
            errors += [f"D>90 ({len(x)}): {x}" for x in d if len(x) > 90]
            errors += [f"Path>15: {x}" for x in a["p"] if len(x) > 15]
            ad_rows.append([campaign, ag, "Responsive search ad", final, *a["p"], *h, *d])

with open(f"{OUT}/responsive-search-ads.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad Group", "Ad type", "Final URL", "Path 1", "Path 2"]
               + [f"Headline {i}" for i in range(1, 16)] + [f"Description {i}" for i in range(1, 5)])
    w.writerows(ad_rows)

# ---------------- assets ----------------
SITELINKS = [
    ("Agency Plan & Pricing", f"{B}/plans-and-pricing/", "20 accounts and 3 users, $79/mo", "Yearly billing: 2 months free"),
    ("RecurPost for Agencies", AGENCY_PAGE, "A separate workspace per client", "Built for client work"),
    ("White-Label Reports", f"{B}/features/measure/brand-logo-white-label-reports/", "Reports with your agency logo", "Scheduled client reports"),
    ("Client Approval Workflow", f"{B}/features/collaborate/approval-workflow/", "Clients approve posts by link", "Internal and external review"),
    ("Roles & Permissions", f"{B}/features/collaborate/roles-and-permissions/", "Control who can do what", "Team and client access"),
    ("Shared Client Calendar", f"{B}/features/collaborate/shared-calendar/", "View-only link for clients", "Clients comment, no login"),
    ("Switch to RecurPost", f"{B}/migrate/", "Keep queues and libraries", "Move without losing approvals"),
    ("Book a Product Demo", "https://social.recurpost.com/book-demo/", "See the agency workflow live", "Ask about your client setup"),
]
CALLOUTS = ["No Credit Card Needed", "14-Day Free Trial", "A Workspace Per Client", "White-Label Reports",
            "Client Approval Links", "No-Password Onboarding", "Automated Client Reports", "Roles & Permissions",
            "2 Months Free on Yearly", "iOS & Android Apps"]
SNIPPET = ("Service catalog", ["Client workspaces", "Approval workflow", "White-label reports",
                               "Shared calendars", "Social inbox", "Evergreen recycling"])
PRICES = [("Agency plan", "79", "per month", "20 accounts, 3 users"),
          ("Agency yearly", "790", "per year", "2 months free"),
          ("Extra social account", "4", "per month", "Add as clients grow"),
          ("Extra teammate", "20", "per month", "Add team seats")]
with open(f"{OUT}/assets.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Asset type", "Text / Header", "Line 1 / Values", "Line 2 / Unit", "Final URL", "Level"])
    for t, u, d1, d2 in SITELINKS:
        if len(t) > 25: errors.append(f"Sitelink>25: {t}")
        errors += [f"SL desc>35 ({len(x)}): {x}" for x in (d1, d2) if len(x) > 35]
        w.writerow(["Sitelink", t, d1, d2, u, "Agency campaigns"])
    for c in CALLOUTS:
        if len(c) > 25: errors.append(f"Callout>25: {c}")
        w.writerow(["Callout", c, "", "", "", "Agency campaigns"])
    errors += [f"Snippet>25: {v}" for v in SNIPPET[1] if len(v) > 25]
    w.writerow(["Structured snippet", SNIPPET[0], "; ".join(SNIPPET[1]), "", "", "Agency campaigns"])
    for name, price, unit, desc in PRICES:
        if len(name) > 25 or len(desc) > 25: errors.append(f"Price text>25: {name} / {desc}")
        w.writerow(["Price", f"{name} | USD {price}", desc, unit, f"{B}/plans-and-pricing/", "Agency campaigns"])

print(f"keywords: {len(kw_rows)} rows ({len(uniq)} unique), ads: {len(ad_rows)}")
print("ERRORS:" if errors else "All length checks passed")
for e in errors: print("  ", e)
