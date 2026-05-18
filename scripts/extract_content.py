#!/usr/bin/env python3
"""Refactor index.html for Decap CMS.

Reads index.html, assigns stable data-cms keys to every editable element,
extracts the actual text into content.json, and rewrites index.html.

Run once. After this, content.json is the source of truth for all copy.
"""

from bs4 import BeautifulSoup
from pathlib import Path
import json
import sys

ROOT = Path("/home/gkim/personal/pnp")
HTML_PATH = ROOT / "index.html"
JSON_PATH = ROOT / "content.json"

with HTML_PATH.open("r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

content = {}

# Each (section_name, parent_selector) pair captures all .translatable
# elements inside that parent and assigns sequential keys.
SECTIONS = [
    ("nav",          "header nav .nav-links"),
    ("hero",         ".hero"),
    ("about",        "#about"),
    ("services",     "#services"),
    ("modal_sme",    "#modal-sme"),
    ("modal_exec",   "#modal-exec"),
    ("modal_custom", "#modal-custom"),
    ("contact",      "#contact"),
    ("trust",        ".trust-strip"),
    ("footer",       "footer"),
]

# Translatable (.translatable) — gets data-ko + data-en in JSON
for section_name, parent_selector in SECTIONS:
    parent = soup.select_one(parent_selector)
    if not parent:
        print(f"warn: section {section_name} ({parent_selector}) not found")
        continue
    i = 0
    for el in parent.select(".translatable"):
        existing = el.get("data-cms")
        if existing:
            key = existing
        else:
            key = f"{section_name}.t{i}"
            el["data-cms"] = key
            i += 1
        ko = el.get("data-ko", "")
        en = el.get("data-en", "")
        content[key] = {"ko": ko, "en": en}

# Non-translatable — single string value
def add_static(selector, key, getter=lambda el: el.get_text(strip=True)):
    el = soup.select_one(selector)
    if not el:
        print(f"warn: static {key} ({selector}) not found")
        return
    if not el.get("data-cms"):
        el["data-cms"] = key
    content[key] = getter(el)

add_static(".hero-eyebrow", "hero.eyebrow")
add_static(".trust-label", "trust.label")
add_static(".contact-info-box h3", "contact.logo")

# Tagline contains "People & Performance" — preserve the literal text
tagline_el = soup.select_one(".contact-info-box .tagline")
if tagline_el:
    if not tagline_el.get("data-cms"):
        tagline_el["data-cms"] = "contact.tagline"
    content["contact.tagline"] = tagline_el.decode_contents().replace("&amp;", "&").strip()

# Phone + email inside the second/third .contact-info-item
contact_items = soup.select(".contact-info-item")
if len(contact_items) >= 3:
    phone_p = contact_items[1].select_one("p")
    if phone_p:
        if not phone_p.get("data-cms"):
            phone_p["data-cms"] = "contact.phone"
        content["contact.phone"] = phone_p.get_text(strip=True)
    email_p = contact_items[2].select_one("p")
    if email_p:
        if not email_p.get("data-cms"):
            email_p["data-cms"] = "contact.email"
        content["contact.email"] = email_p.get_text(strip=True)

# Logo wordmark in header
logo_el = soup.select_one(".logo")
if logo_el:
    if not logo_el.get("data-cms"):
        logo_el["data-cms"] = "site.logo"
    content["site.logo"] = logo_el.get_text(strip=True)

# Sort content.json keys for stable diffs
content_sorted = dict(sorted(content.items()))

with JSON_PATH.open("w", encoding="utf-8") as f:
    json.dump(content_sorted, f, ensure_ascii=False, indent=2)

with HTML_PATH.open("w", encoding="utf-8") as f:
    f.write(str(soup))

translatable_count = sum(1 for v in content.values() if isinstance(v, dict))
static_count = sum(1 for v in content.values() if isinstance(v, str))

print(f"\nWrote {JSON_PATH}")
print(f"  {translatable_count} translatable entries (ko/en pairs)")
print(f"  {static_count} static entries")
print(f"\nUpdated {HTML_PATH}")
