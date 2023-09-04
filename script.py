import yfinance as yf

class Stock():
    def __init__(self, input_stock_name):
        self.stock_name = yf.Ticker(input_stock_name)
        self.stock_info = self.stock_name.info

    def __repr__(self):
        return '{}'.format(self.stock_info["symbol"])
    
    def ticker_symbol(self):
        return f'{self.stock_info["symbol"]}'
    
    def current_price(self):
        stock_price = self.stock_info['currentPrice']
        return stock_price

class GamePrompt():
    def __init__(self):
        pass

    def message(self, message=''):
        return input(message)
    
#create game prompt
get_prompt = GamePrompt()
input_stock_name = get_prompt.message('''Enter the ticker symbol of the stock to get the last closing price:
''')
                                      

# print('Enter the ticker symbol of the stock to get the current price:')
# input_stock_name = input()

#instancia con el ticker para saber si se puede usar dentro de la
#clase Portafolio

def get_stock_price():
    try:
        stock = Stock(input_stock_name)
        stock_price = stock.current_price()
        return stock_price

    except:
        print(f'Please provide a valid ticker {input_stock_name}, does not exists.')

game_prompt = get_prompt.message(f'''Current price: {get_stock_price()} 
    Do you want to buy {input_stock_name} stocks at: ${get_stock_price()}?
    Y -> Yes
    N -> No & quit game
    A -> Search for Another stock name
''')


# if game_input == 'A':

    

