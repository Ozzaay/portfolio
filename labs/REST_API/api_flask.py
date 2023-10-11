#     /weather?city=Stockholm
#     Returnerar aktuell väderinformation för en angiven stad (notera att detta kan kräva integration med ett externt väder-API).
#     /daily-joke
#     Returnerar ett slumpmässigt skämt.
#     /count-words
#     Tar emot en textsträng och returnerar antal ord i texten.
#     /is-palindrome?word=anna
#     Tar emot ett ord eller en fras och kontrollerar om det är ett palindrom (läses likadant framifrån som bakifrån).
#     /countries
#     Returnerar en lista av länder och eventuellt någon tillhörande information, t.ex. huvudstad.
#     /daily-horoscope?sign=leo
#     Returnerar dagens horoskop för ett angivet stjärntecken (detta kan baseras på fördefinierade horoskop eller hämtas från en extern källa).
from flask import Flask, jsonify
import random
from datetime import date
import requests

names = ("Tom", "Erik","John","Niclas","Ossian","Oskar","Viktor","Victor","Max")

class Currency_converter:
    rates = {} 
    def __init__(self, url):
        data = requests.get(url).json()
 
        self.rates = data["rates"] 
 
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency]
 
        amount = round(amount * self.rates[to_currency], 2)
        return initial_amount,from_currency,amount,to_currency     
url = str.__add__('http://data.fixer.io/api/latest?access_key=',"b022a6a761629be8b407f7f1b89e9f99")
c = Currency_converter(url)
from_country = "USD"
to_country = "SEK"
amount = 100


app = Flask(__name__)


@app.route("/random_number", methods=["GET"])
def random_number():
    return jsonify(random.randint(1,100))

@app.route("/random_name")
def random_name():
    return jsonify(random.choice(names))

@app.route("/current_date")
def current_date():
    return jsonify(date.today())

@app.route("/convert-currency")
def convert_currency():
    return jsonify(c.convert(from_country,to_country,amount))

if __name__ == '__main__':
    
    app.run(debug=True)