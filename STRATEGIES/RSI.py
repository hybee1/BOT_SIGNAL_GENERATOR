def fut_rsi_buy_strategy(buy_frame):
    # result2 = ""

    if ((buy_frame['rsi_short'].iloc[-2] > buy_frame['rsi_long'].iloc[-2]) and
            (buy_frame['rsi_short'].iloc[-3] < buy_frame['rsi_long'].iloc[-3]) and
            (buy_frame['rsi_short'].iloc[-4] < buy_frame['rsi_long'].iloc[-4])):
        print('BUY RSI TRUE1')
        result2 = True

    elif ((buy_frame['rsi_short'].iloc[-2] > buy_frame['rsi_long'].iloc[-2]) and
          (buy_frame['rsi_short'].iloc[-3] > buy_frame['rsi_long'].iloc[-3]) and
          (buy_frame['rsi_short'].iloc[-4] < buy_frame['rsi_long'].iloc[-4]) and
          (buy_frame['rsi_short'].iloc[-5] < buy_frame['rsi_long'].iloc[-5])):
        print('BUY RSI TRUE2')
        result2 = True

    elif ((buy_frame['rsi_short'].iloc[-2] > buy_frame['rsi_long'].iloc[-2]) and
          (buy_frame['rsi_short'].iloc[-3] > buy_frame['rsi_long'].iloc[-3]) and
          (buy_frame['rsi_short'].iloc[-4] < buy_frame['rsi_long'].iloc[-4])):
        print('BUY RSI TRUE3')
        result2 = True

    elif ((buy_frame['rsi_short'].iloc[-2] > buy_frame['rsi_long'].iloc[-2]) and
          (buy_frame['rsi_short'].iloc[-3] > buy_frame['rsi_long'].iloc[-3]) and
          (buy_frame['rsi_short'].iloc[-4] > buy_frame['rsi_long'].iloc[-4]) and
          (buy_frame['rsi_short'].iloc[-5] < buy_frame['rsi_long'].iloc[-5])):
        print('BUY RSI TRUE4')
        result2 = True

    else:
        result2 = False

    return result2


def rsi_sell_strategy(sell_frame):

    if ((sell_frame['rsi_long'].iloc[-2] > sell_frame['rsi_short'].iloc[-2]) and
            (sell_frame['rsi_long'].iloc[-3] < sell_frame['rsi_short'].iloc[-3]) and
            (sell_frame['rsi_long'].iloc[-4] < sell_frame['rsi_short'].iloc[-4])):
        print('SELL RSI TRUE1')
        result2 = True

    elif ((sell_frame['rsi_long'].iloc[-2] > sell_frame['rsi_short'].iloc[-2]) and
          (sell_frame['rsi_long'].iloc[-3] > sell_frame['rsi_short'].iloc[-3]) and
          (sell_frame['rsi_long'].iloc[-4] < sell_frame['rsi_short'].iloc[-4]) and
          (sell_frame['rsi_long'].iloc[-5] < sell_frame['rsi_short'].iloc[-5])):
        print('SELL RSI TRUE2')
        result2 = True

    elif ((sell_frame['rsi_long'].iloc[-2] > sell_frame['rsi_short'].iloc[-2]) and
          (sell_frame['rsi_long'].iloc[-3] > sell_frame['rsi_short'].iloc[-3]) and
          (sell_frame['rsi_long'].iloc[-4] < sell_frame['rsi_short'].iloc[-4])):
        print('SELL RSI TRUE3')
        result2 = True

    elif ((sell_frame['rsi_long'].iloc[-2] > sell_frame['rsi_short'].iloc[-2]) and
          (sell_frame['rsi_long'].iloc[-3] > sell_frame['rsi_short'].iloc[-3]) and
          (sell_frame['rsi_long'].iloc[-4] > sell_frame['rsi_short'].iloc[-4]) and
          (sell_frame['rsi_long'].iloc[-5] < sell_frame['rsi_short'].iloc[-5])):
        print('SELL RSI TRUE4')
        result2 = True

    else:
        result2 = False

    return result2
