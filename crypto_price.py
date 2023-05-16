import requests

# function uses a token that is provided by user input and returns a token symbol that is being used in second function
def get_token_price(token):

    # catch the exception when someone enters the token name that doesn't exist
    try:
        response = requests.get(f"https://coins.llama.fi/prices/current/coingecko:{token}?searchWidth=1h").json()
        
        process_data = response['coins']
        final_data = process_data[f'coingecko:{token}']

        for key, value in final_data.items():
            print(key.title(), ':', value)
            if key == 'symbol' : return value

    except KeyError as detail:
        print('Cryptocurrency / token not found: ', detail)

# token symbol from previous function is being used as parameter 
def get_live_price(symbol):

    response = requests.get(f"https://api.bybit.com/spot/v3/public/quote/ticker/price?symbol={symbol}USDT").json()
    processed_data = response['result']

    for key, value in processed_data.items():
        if key == 'price' : print('Live price from the Bybit exchange:', value)

def get_user_input():
    
    #let the user choose what token they want to see and also lower whatever they write
    return input("\nEnter name of the crypto token: ").lower()


def main():
    get_live_price(get_token_price(get_user_input()))

if __name__ == "__main__":
    main()




