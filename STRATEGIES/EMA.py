def ema_buy_strategy(buy_frame):
    # result2 = ""

    if ((buy_frame['ema_short'].iloc[-2] > buy_frame['ema_long'].iloc[-2]) and
            (buy_frame['ema_short'].iloc[-3] < buy_frame['ema_long'].iloc[-3]) and
            (buy_frame['ema_short'].iloc[-4] < buy_frame['ema_long'].iloc[-4])):
        print('BUY EMA TRUE1')
        result2 = True

    # the below checks if [-2 AND -3] macd > [-2 AND -3] macdsignal while others are not and
    # [-2 AND -3] ema_short > [-2 AND -3] ema_long while others are not

    elif ((buy_frame['ema_short'].iloc[-2] > buy_frame['ema_long'].iloc[-2]) and
          (buy_frame['ema_short'].iloc[-3] > buy_frame['ema_long'].iloc[-3]) and
          (buy_frame['ema_short'].iloc[-4] > buy_frame['ema_long'].iloc[-4]) and
          (buy_frame['ema_short'].iloc[-5] < buy_frame['ema_long'].iloc[-5])):
        print('BUY EMA TRUE2')
        result2 = True

    # the below checks if [-2 AND -3] macd > [-2 AND -3] macdsignal while others are not and
    # [-2] ema_short > [-2] ema_long while others are not

    elif ((buy_frame['ema_short'].iloc[-2] > buy_frame['ema_long'].iloc[-2]) and
          (buy_frame['ema_short'].iloc[-3] > buy_frame['ema_long'].iloc[-3]) and
          (buy_frame['ema_short'].iloc[-4] < buy_frame['ema_long'].iloc[-4])):
        print('BUY EMA TRUE3')
        result2 = True

    # elif buy_frame['ema_short'].iloc[-2] > buy_frame['ema_long'].iloc[-2]:
    #     print('BUY ema_short TRUE4')
    #     result2 = True

    else:
        result2 = False

    return result2


def ema_sell_strategy(sell_frame):

    if ((sell_frame['ema_long'].iloc[-2] > sell_frame['ema_short'].iloc[-2]) and
            (sell_frame['ema_long'].iloc[-3] < sell_frame['ema_short'].iloc[-3]) and
            (sell_frame['ema_long'].iloc[-4] < sell_frame['ema_short'].iloc[-4])):
        print('SELL EMA TRUE1')
        result2 = True

    elif ((sell_frame['ema_long'].iloc[-2] > sell_frame['ema_short'].iloc[-2]) and
          (sell_frame['ema_long'].iloc[-3] > sell_frame['ema_short'].iloc[-3]) and
          (sell_frame['ema_long'].iloc[-4] > sell_frame['ema_short'].iloc[-4]) and
          (sell_frame['ema_long'].iloc[-5] < sell_frame['ema_short'].iloc[-5])):
        print('SELL EMA TRUE2')
        result2 = True

    elif ((sell_frame['ema_long'].iloc[-2] > sell_frame['ema_short'].iloc[-2]) and
          (sell_frame['ema_long'].iloc[-3] > sell_frame['ema_short'].iloc[-3]) and
          (sell_frame['ema_long'].iloc[-4] < sell_frame['ema_short'].iloc[-4])):
        print('SELL EMA TRUE3')
        result2 = True

    # elif sell_frame['ema_long'].iloc[-2] > sell_frame['ema_short'].iloc[-2]:
    #     print('SELL ema_long TRUE4')
    #     result2 = True

    else:
        result2 = False

    return result2
