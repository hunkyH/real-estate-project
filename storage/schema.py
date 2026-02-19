def init_db(conn) -> None:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS listings (
      hash_id TEXT PRIMARY KEY,
      market TEXT NOT NULL,
      source TEXT NOT NULL,
      source_listing_id TEXT,
      listing_url TEXT,
      property_type TEXT,
      city TEXT,
      neighborhood TEXT,
      street TEXT,
      rooms REAL,
      bathrooms REAL,
      area_sqm REAL,
      price_ils INTEGER,
      date_updated TEXT,
      is_active INTEGER NOT NULL,
      raw_json TEXT
    )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_listings_market ON listings(market)")

    conn.commit()
