import requests
import json

# آدرس API
url = "https://brsapi.ir/Api/User.php?key=FreeTZPrEbgTZzbW2SSGXOlzjlulRFcz"

# ارسال درخواست
response = requests.get(url)
data = response.json()

# استخراج قیمت تتر و طلای ۱۸ عیار
usdt_price = data.get("usdt")
gold_price = data.get("geram18")

# ساخت دیکشنری خروجی
result = {
    "usdt": usdt_price,
    "geram18": gold_price
}

# ذخیره در فایل JSON
with open("prices.json", "w", encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("فایل prices.json ساخته شد.")
