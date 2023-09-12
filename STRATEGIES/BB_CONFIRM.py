# ****** buy and sell confirm ******************

def bollinger_band_buy_confirm(buy_frame):
    if ((buy_frame['adx_line'].iloc[-4] > buy_frame['adx_line'].iloc[-3] >
         buy_frame['adx_line'].iloc[-2] > 25) and

            (buy_frame['lowerband'].iloc[-6] >= buy_frame['Open'].iloc[-6] or
             buy_frame['lowerband'].iloc[-6] >= buy_frame['High'].iloc[-6] or
             buy_frame['lowerband'].iloc[-6] >= buy_frame['Low'].iloc[-6] or
             buy_frame['lowerband'].iloc[-6] >= buy_frame['Close'].iloc[-6] or

             buy_frame['lowerband'].iloc[-5] >= buy_frame['Open'].iloc[-5] or
             buy_frame['lowerband'].iloc[-5] >= buy_frame['High'].iloc[-5] or
             buy_frame['lowerband'].iloc[-5] >= buy_frame['Low'].iloc[-5] or
             buy_frame['lowerband'].iloc[-5] >= buy_frame['Close'].iloc[-5]) and

            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5] and

             buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4] and
             buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3] and
             buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2])):
        print('bollinger band buy 6 confirm')
        return True

    elif ((25 < buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] <
           buy_frame['adx_line'].iloc[-2] < 45) and

          (buy_frame['Open'].iloc[-6] >= buy_frame['upperband'].iloc[-6] or
           buy_frame['High'].iloc[-6] >= buy_frame['upperband'].iloc[-6] or
           buy_frame['Low'].iloc[-6] >= buy_frame['upperband'].iloc[-6] or
           buy_frame['Close'].iloc[-6] >= buy_frame['upperband'].iloc[-6] or

           buy_frame['Open'].iloc[-5] >= buy_frame['upperband'].iloc[-5] or
           buy_frame['High'].iloc[-5] >= buy_frame['upperband'].iloc[-5] or
           buy_frame['Low'].iloc[-5] >= buy_frame['upperband'].iloc[-5] or
           buy_frame['Close'].iloc[-5] >= buy_frame['upperband'].iloc[-5]) and

          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5] and

           buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4] and
           buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3] and
           buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2])):
        print('bollinger band buy 7 confirm')
        return True


def bollinger_band_sell_confirm(sell_frame):
    if ((sell_frame['adx_line'].iloc[-4] > sell_frame['adx_line'].iloc[-3] >
         sell_frame['adx_line'].iloc[-2] > 25) and

            (sell_frame['Open'].iloc[-6] >= sell_frame['upperband'].iloc[-6] or
             sell_frame['High'].iloc[-6] >= sell_frame['upperband'].iloc[-6] or
             sell_frame['Low'].iloc[-6] >= sell_frame['upperband'].iloc[-6] or
             sell_frame['Close'].iloc[-6] >= sell_frame['upperband'].iloc[-6] or

             sell_frame['Open'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
             sell_frame['High'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
             sell_frame['Low'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
             sell_frame['Close'].iloc[-5] >= sell_frame['upperband'].iloc[-5]) and

            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5] and

             sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
             sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
             sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2])):
        print('bollinger band sell 6 confirm')
        return True

    elif ((25 < sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] <
           sell_frame['adx_line'].iloc[-2] < 45) and

          (sell_frame['lowerband'].iloc[-6] >= sell_frame['Open'].iloc[-6] or
           sell_frame['lowerband'].iloc[-6] >= sell_frame['High'].iloc[-6] or
           sell_frame['lowerband'].iloc[-6] >= sell_frame['Low'].iloc[-6] or
           sell_frame['lowerband'].iloc[-6] >= sell_frame['Close'].iloc[-6] or

           sell_frame['lowerband'].iloc[-5] >= sell_frame['Open'].iloc[-5] or
           sell_frame['lowerband'].iloc[-5] >= sell_frame['High'].iloc[-5] or
           sell_frame['lowerband'].iloc[-5] >= sell_frame['Low'].iloc[-5] or
           sell_frame['lowerband'].iloc[-5] >= sell_frame['Close'].iloc[-5]) and

          (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5] and

           sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
           sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
           sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2])):
        print('bollinger band sell 7 confirm')
        return True

# ****** buy and sell confirm **********
