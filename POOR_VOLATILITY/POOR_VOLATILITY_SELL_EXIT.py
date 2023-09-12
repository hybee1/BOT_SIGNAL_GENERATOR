# ****** BUY OUT AND SELL OUT WHEN MARKET IS EXPERIENCING POOR VOLATILITY *************

def price_touch_upper_band(sell_frame):
    if ((sell_frame['upperband'].iloc[-2] <= sell_frame['Open'].iloc[-2] or
         sell_frame['upperband'].iloc[-2] <= sell_frame['High'].iloc[-2] or
         sell_frame['upperband'].iloc[-2] <= sell_frame['Low'].iloc[-2] or
         sell_frame['upperband'].iloc[-2] <= sell_frame['Close'].iloc[-2])):

        print('PRICE TOUCHED THE UPPER BAND poor volatility')
        return True

    elif ((-sell_frame['Open'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['High'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['Low'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['Close'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10)):

        print('sell out diff of 10 poor volatility')
        return True


def poor_volatility_sell_out(sell_frame):
    if price_touch_upper_band(sell_frame):
        print('SELL OUT SIGNAL FROM WHEN MARKET IS EXPERIENCING POOR VOLATILITY')
        return True

# ****** BUY OUT AND SELL OUT WHEN MARKET IS EXPERIENCING POOR VOLATILITY *************
