from flask import Flask
from yahoofinance import Stocks

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!!!!!'

@app.route('/yahoofinance/api/quotes/<string:symbol>', methods=['GET'])
def get_quotes(symbol):
    quotes = Stocks()
    quotes.set_last_trade()
    quotes.set_change_in_percent()
    quotes.set_last_trade_date()
    quotes.set_last_trade_time()
    return quotes.get_financial_data(symbol)


if __name__ == '__main__':
    app.run(debug=True)