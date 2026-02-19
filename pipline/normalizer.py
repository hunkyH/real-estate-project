import re
import datetime
import json
from config import PROPERTY_TYPE_MAP
from config import MARKETS
import hashlib


def parse_price_ils(v) -> int | None:
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return int(v)
    s = str(v)
    digits = re.sub(r"[^\d]", "", s)
    return int(digits) if digits else None

def parse_rooms(v) -> float | None:
    if v is None:
        return None
    try:
        return float(str(v).strip())
    except ValueError:
        return None

def parse_date_ddmmyyyy(v) -> str | None:
    if not v:
        return None
    try:
        dt = datetime.strptime(v.strip(), "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return None

def normalize_city(v, market) -> str | None:
    if not v:
        return None
    s = v.strip()
    if s in (MARKETS):
        return market
    else:
        return s
    
def sha1_hash(*parts: str) -> str:
    joined = "|".join((p or "").strip().lower() for p in parts)
    return hashlib.sha1(joined.encode("utf-8")).hexdigest()

def normalize_listing(raw: dict, scrape_date: str, market) -> dict:
    print(raw)
    source = raw.get("source")
    
    out = {
        "hash_id": None,
        "market" : market,
        "source": source,
        "source_listing_id": None,
        "listing_url": raw.get("url"),
        "property_type": None,
        "city": None,
        "neighborhood": None,
        "street": None,
        "rooms": None,
        "bathrooms": None,
        "area_sqm": None,
        "price_ils": None,
        "date_updated": None,
        "is_active": True,
        "scrape_date": scrape_date,
        "raw_json": json.dumps(raw, ensure_ascii=False),
        
    }
    
    if source == "homeless":
        out["property_type"] = PROPERTY_TYPE_MAP.get(raw.get("type"),"unknown")
        out["city"] = normalize_city(raw.get("city"),market)
        out["neighborhood"] = raw.get("neighborhood")
        out["street"] = raw.get("street")
        out["rooms"] = parse_rooms(raw.get("rooms"))
        out["bathrooms"] = parse_rooms(raw.get("bathrooms"))
        out["price_ils"] = parse_price_ils(raw.get("price"))
        out["date_updated"] = parse_date_ddmmyyyy(raw.get("date_updated"))
        
    if source == "onmap":
        out["city"] = normalize_city(raw.get("city"),market)
        out["neighborhood"] = raw.get("neighborhood")
        out["price_ils"] = parse_price_ils(raw.get("price"))
        out["street"] = raw.get("street")
        out["rooms"] = parse_rooms(raw.get("rooms"))
        out["bathrooms"] = parse_rooms(raw.get("bathrooms"))
        
    out["hash_id"] = sha1_hash(
        out["city"] or "",
        out["neighborhood"] or "",
        out["street"] or "",
        str(out["rooms"] or ""),
        str(out["area_sqm"] or ""),
        str(out["price_ils"] or ""),
    ) 
    return out
        
