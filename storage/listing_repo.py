def upsert_listing(conn, row: dict) -> None:
    conn.execute("""
    INSERT INTO listings (
      hash_id, market, source, source_listing_id, listing_url, property_type,
      city, neighborhood, street, rooms, bathrooms, area_sqm,
      price_ils, date_updated, is_active, raw_json
    ) VALUES (
      :hash_id, :market, :source, :source_listing_id, :listing_url, :property_type,
      :city, :neighborhood, :street, :rooms, :bathrooms, :area_sqm,
      :price_ils, :date_updated, :is_active, :raw_json
    )
    ON CONFLICT(hash_id) DO UPDATE SET
      price_ils=excluded.price_ils,
      is_active=excluded.is_active,
      raw_json=excluded.raw_json
    """, row)
