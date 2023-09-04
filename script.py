import yfinance as yf

class Stock():
    def __init__(self, input_stock_name):
        self.stock_name = yf.Ticker(input_stock_name)
        self.stock_info = self.stock_name.info

    def __repr__(self):
        return f'{self.stock_info["symbol"]}'
    
    def ticker_symbol(self):
        return f'{self.stock_info["symbol"]}'
    
    def current_price(self):
        stock_price = self.stock_info['currentPrice']
        return stock_price