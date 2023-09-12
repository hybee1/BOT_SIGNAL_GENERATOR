
# ****** BUY OUT AND SELL OUT WHEN MARKET IS EXPERIENCING POOR VOLATILITY *************
def price_touch_lower_band(buy_frame):

    if ((buy_frame['lowerband'].iloc[-2] >= buy_frame['Open'].iloc[-2] or
         buy_frame['lowerband'].iloc[-2] >= buy_frame['High'].iloc[-2] or
         buy_frame['lowerband'].iloc[-2] >= buy_frame['Low'].iloc[-2] or
         buy_frame['lowerband'].iloc[-2] >= buy_frame['Close'].iloc[-2])):
        print('PRICE TOUCHED THE LOWER BAND EXTREME volatility')
        return True

    elif ((buy_frame['Open'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['High'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['Low'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['Close'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10)):

        print('buy out diff of 10 EXTREME volatility')
        return True


def extreme_volatility_buy_out(buy_frame):

    if price_touch_lower_band(buy_frame):

        print('BUY OUT SIGNAL FROM WHEN MARKET IS EXPERIENCING POOR VOLATILITY')
        return True


# ****** BUY OUT AND SELL OUT WHEN MARKET IS EXPERIENCING POOR VOLATILITY *************
