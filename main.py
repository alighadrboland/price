from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def fetch_prices():
    url = "https://brsapi.ir/Api/User.php?key=FreeTZPrEbgTZzbW2SSGXOlzjlulRFcz"
    response = requests.get(url)
    data = response.json()

    usdt_price = data.get("usdt")
    gold_price = data.get("geram18")

    result = {
        "usdt": usdt_price,
        "geram18": gold_price
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
