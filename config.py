

BASE_URLS = {
    "yad2": {"tel_aviv": "https://www.yad2.co.il/realestate/forsale/tel-aviv-area?area=1&city=5000", "ramat_gan": "https://www.yad2.co.il/realestate/forsale/tel-aviv-area?area=3&city=8600", "givataym": "https://www.yad2.co.il/realestate/forsale/tel-aviv-area?area=3&city=6300"},
    "madlan": {"tel_aviv": "https://www.madlan.co.il/for-sale/%D7%AA%D7%9C-%D7%90%D7%91%D7%99%D7%91-%D7%99%D7%A4%D7%95-%D7%99%D7%A9%D7%A8%D7%90%D7%9C", "ramat_gan": "https://www.madlan.co.il/for-sale/%D7%A8%D7%9E%D7%AA-%D7%92%D7%9F-%D7%99%D7%A9%D7%A8%D7%90%D7%9C", "givataym": "https://www.madlan.co.il/for-sale/%D7%92%D7%91%D7%A2%D7%AA%D7%99%D7%99%D7%9D-%D7%99%D7%A9%D7%A8%D7%90%D7%9C"},
    "onmap": {"tel_aviv": "https://www.onmap.co.il/en/search/homes/buy/tel-aviv-yafo/place_Bk8pkxcIG", "ramat_gan": "https://www.onmap.co.il/en/search/homes/buy/ramat-gan/place_BJ7j1g9UG/c_32.070890,34.826430/t_32.114900,34.892050/z_12", "givataym": "https://www.onmap.co.il/en/search/homes/buy/givatayim/place_Skw6kx58M/c_32.070180,34.809190/t_32.084920,34.831160/z_13"},
    "homeless": {"tel_aviv": "https://www.homeless.co.il/sale/city=%D7%AA%D7%9C%20%D7%90%D7%91%D7%99%D7%91", "ramat_gan": "https://www.homeless.co.il/sale/city=%d7%a8%d7%9e%d7%aa%20%d7%92%d7%9f", "givataym": "https://www.homeless.co.il/sale/city=%d7%92%d7%91%d7%a2%d7%aa%d7%99%d7%99%d7%9d"}
    }

MARKETS = {
    "givatayim": {"he": "גבעתיים", "en": "Givatayim"},
    "tel_aviv": {"he": "תל אביב", "en": "Tel Aviv"},
    "ramat_gan": {"he": "רמת גן", "en": "Ramat Gan"},
}

PROPERTY_TYPE_MAP = {
    "דירה": "apartment",
    "דירת גן": "garden_apartment",
    "פנטהאוז": "penthouse",
    "דופלקס": "duplex",
}