def dmi_buy_strategy(buy_frame):
    if ((buy_frame['plus_DI'].iloc[-2] > buy_frame['minus_DI'].iloc[-2] and
         buy_frame['plus_DI'].iloc[-3] > buy_frame['minus_DI'].iloc[-3]) and

            (buy_frame['minus_DI'].iloc[-4] > buy_frame['dmi_line'].iloc[-4] and
             buy_frame['minus_DI'].iloc[-3] > buy_frame['dmi_line'].iloc[-3] and
             buy_frame['minus_DI'].iloc[-2] < buy_frame['dmi_line'].iloc[-2]) and

            (buy_frame['minus_DI'].iloc[-2] < 18) and

            (buy_frame['plus_DI'].iloc[-2] - buy_frame['minus_DI'].iloc[-2] > 19)):

        print('BUY DMI TRUE1')
        result2 = True

    else:
        result2 = False

    return result2


def dmi_sell_strategy(sell_frame):
    if ((sell_frame['minus_DI'].iloc[-2] > sell_frame['plus_DI'].iloc[-2] and
         sell_frame['minus_DI'].iloc[-3] > sell_frame['plus_DI'].iloc[-3]) and

            (sell_frame['plus_DI'].iloc[-4] > sell_frame['dmi_line'].iloc[-4] and
             sell_frame['plus_DI'].iloc[-3] > sell_frame['dmi_line'].iloc[-3] and
             sell_frame['plus_DI'].iloc[-2] < sell_frame['dmi_line'].iloc[-2]) and

            (sell_frame['plus_DI'].iloc[-2] < 18) and

            (sell_frame['minus_DI'].iloc[-2] - sell_frame['plus_DI'].iloc[-2] > 19)):

        print('SELL DMI TRUE1')
        result2 = True

    else:
        result2 = False

    return result2
