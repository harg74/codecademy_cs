import yfinance as yf

import pandas as pd

sp500 = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data_table = pd.read_html(sp500)
tickers_list = (data_table[0]['Symbol']).tolist()


class Stock():
    def __init__(self):
        self.stock_name = ''
        self.stock_info = ''

    def __repr__(self):
        return '{}'.format(self.stock_info["symbol"])

    def ticker_symbol(self, input_stock_name):
        self.stock_name = yf.Ticker(input_stock_name)
        self.stock_info = self.stock_name.info
        return f'{self.stock_info["symbol"]}'
    
    def current_price(self, input_stock_name):
        self.stock_name = yf.Ticker(input_stock_name)
        self.stock_info = self.stock_name.info
        self.stock_price = self.stock_info['currentPrice']
        return self.stock_price

class GamePrompt():
    def __init__(self):
        pass

    def message(self, message=''):
        return input(message)

class Portfolio():
    def __init__(self):
        self.stocks_dict = {}
        self.total_qty = 0
        self.buy_price = 0

    def buy_stock(self, stock_name, qty_bought, buy_price):
        self.buy_price = buy_price
        transaction = {'quantity': qty_bought, 'buy_price': buy_price}
        if stock_name not in self.stocks_dict:
            self.stocks_dict[stock_name] = [transaction]
        else:
            self.stocks_dict[stock_name].append(transaction)

    def show_last_buy(self,input_stock_name):
        last_buy = self.stocks_dict[input_stock_name]
        last_buy = last_buy[-1]
        values_list = last_buy.values()

        # Initialize variables to store the values
        value1 = None
        value2 = None

        # Iterate over the values and assign them to variables
        for i, value in enumerate(values_list):
            if i == 0:
                value1 = value
            elif i == 1:
                value2 = value
        
        print(f' You bought {value1} {input_stock_name} share(s) at {value2} USD!')
        print()

    def show_portfolio(self):
        print(self.stocks_dict)
        for k, v in self.stocks_dict.items():
            print(k,v)

def get_input_stock_name(prompt):
    if welcome_prompt_input == 'Y':
        input_stock_name = prompt.message('''Enter the ticker symbol of the stock to get the last closing price:
        ''')
        return input_stock_name
    
def get_stock_price(stock_obj, input_stock_name):
    if input_stock_name in tickers_list:
        stock_price = stock_obj.current_price(input_stock_name)
        return stock_price
    else:

        print(f'Please provide a valid ticker "{input_stock_name}", does not exists!')
        return game_logic()

def keep_playing(prompt):
    keep_playing_input = prompt.message('''Do you want to keep buying shares?
    Y -> Yes
    N -> No & Quit game''')
    return keep_playing_input
            
#create portfolio object
portfolio_obj = Portfolio()
#create stock object
stock_obj = Stock()
#create game prompt object 
prompt = GamePrompt()

#Welcome Prompt
welcome_prompt_input = prompt.message('''Welcome to the Stock Simulator
Do you want to start buying company shares?
Y -> Yes
N -> No & quit game''')


def game_logic():
    stock_name = get_input_stock_name(prompt)

    while True:

        current_price = get_stock_price(stock_obj, stock_name)

        game_prompt = prompt.message(f'''Current price: {current_price} 
            Do you want to buy {stock_name} stocks at: ${current_price}?
            Y -> Yes
            N -> No & Quit game
            A -> Search for Another stock name
        ''')

        if game_prompt == 'Y':
            input_qty_bought = prompt.message(f'How many {stock_name} stocks you want to buy?')
            print()
            portfolio_obj.buy_stock(stock_name, int(input_qty_bought), current_price)

            portfolio_obj.show_last_buy(stock_name)
            print()
            portfolio_obj.show_portfolio()
            print()

            keep_playing_decision = keep_playing(prompt)

            if keep_playing_decision == 'Y':
                stock_name = get_input_stock_name(prompt)
            elif keep_playing_decision == 'N':
                exit()
            else:
                print("Select a valid option. Type Y to keep playing or N to quit the game")
                keep_playing()
        elif game_prompt == 'N':   
            exit()
        elif game_prompt == 'A':
            stock_name = get_input_stock_name(prompt)

if welcome_prompt_input == 'Y':
    game_logic()
else:
    exit()




