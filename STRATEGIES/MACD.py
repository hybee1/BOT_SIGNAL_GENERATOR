
def macd_buy_strategy(buy_frame):

    if ((buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
            (buy_frame['macd'].iloc[-3] < buy_frame['macdsignal'].iloc[-3]) and
            (buy_frame['macd'].iloc[-4] < buy_frame['macdsignal'].iloc[-4])):
        print('BUY MACD TRUE1')
        result2 = True

    elif ((buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
          (buy_frame['macd'].iloc[-3] > buy_frame['macdsignal'].iloc[-3]) and
          (buy_frame['macd'].iloc[-4] < buy_frame['macdsignal'].iloc[-4]) and
          (buy_frame['macd'].iloc[-5] < buy_frame['macdsignal'].iloc[-5])):
        print('BUY MACD TRUE2')
        result2 = True

    elif ((buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
          (buy_frame['macd'].iloc[-3] > buy_frame['macdsignal'].iloc[-3]) and
          (buy_frame['macd'].iloc[-4] < buy_frame['macdsignal'].iloc[-4])):
        print('BUY MACD TRUE3')
        result2 = True

    else:
        result2 = False

    return result2


def macd_sell_strategy(sell_frame):

    # result2 = ""

    if ((sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and
            (sell_frame['macdsignal'].iloc[-3] < sell_frame['macd'].iloc[-3]) and
            (sell_frame['macdsignal'].iloc[-4] < sell_frame['macd'].iloc[-4])):
        print('SELL MACD TRUE1')
        result2 = True

    elif ((sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and
          (sell_frame['macdsignal'].iloc[-3] > sell_frame['macd'].iloc[-3]) and
          (sell_frame['macdsignal'].iloc[-4] < sell_frame['macd'].iloc[-4]) and
          (sell_frame['macdsignal'].iloc[-5] < sell_frame['macd'].iloc[-5])):
        print('SELL MACD TRUE2')
        result2 = True

    elif ((sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and
          (sell_frame['macdsignal'].iloc[-3] > sell_frame['macd'].iloc[-3]) and
          (sell_frame['macdsignal'].iloc[-4] < sell_frame['macd'].iloc[-4])):
        print('SELL MACD TRUE3')
        result2 = True

    else:
        result2 = False

    return result2
