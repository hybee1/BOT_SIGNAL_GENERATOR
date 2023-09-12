from GENERAL.GENERAL import (doji_Star, dragonfly_Doji, gravestone_doji, hammer, hanging_Man,
                             inverted_Hammer, spinning_Top, shooting_Star,
                             manual_Hammer, manual_Inverted_Hammer)


def cand_patn_buy(buy_frame):
    # [-4]G AND [-3, -2]R AND [-4]G is (manual-hammer or hammer or doji_star or dragonfly_doji or
    # hanging_Man or spinning_Top) AND [-4]G IS BETWEEN UPPERBAND AND MIDDLEBAND, AND ADX > 25
    if (
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (manual_Hammer(buy_frame) or hammer(buy_frame, 4) or doji_Star(buy_frame, 4) or dragonfly_Doji(buy_frame, 4) or
             hanging_Man(buy_frame, 4) or spinning_Top(buy_frame, 4)) and

            # [-4]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['middlerband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['middlerband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 1')
        return True

    # [-4]G AND [-3, -2]R AND [-4]G is (manual-inverted-hammer or inverted_Hammer or
    # gravestone_doji or shooting_Star OR spinning_Top OR doji_Star) AND [-4]G IS
    # BETWEEN MIDDLEBAND AND LOWERBAND, AND ADX > 25
    elif (
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (manual_Inverted_Hammer(buy_frame) or inverted_Hammer(buy_frame, 4) or gravestone_doji(buy_frame, 4) or shooting_Star(buy_frame, 4) or
             doji_Star(buy_frame, 4) or spinning_Top(buy_frame, 4)) and

            # [-4]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['middlerband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 2')
        return True

    # [-4]R AND [-3, -2]G AND [-4]R is (manual-inverted-hammer or inverted_Hammer or gravestone_doji
    # or shooting_Star OR spinning_Top OR doji_Star) AND [-4]R IS BETWEEN UPPERRBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (manual_Inverted_Hammer(buy_frame) or inverted_Hammer(buy_frame, 4) or gravestone_doji(buy_frame, 4) or shooting_Star(buy_frame, 4) or
             doji_Star(buy_frame, 4) or spinning_Top(buy_frame, 4)) and

            # [-4]R
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) < buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 3')
        return True

    # [-4]R AND [-3, -2]G AND [-4]R is (manual-inverted-hammer or inverted hammer or doji_star or
    # gravestone_doji or shooting_Star or spinning_Top) AND [-4]R IS BETWEEN LOWERBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (manual_Inverted_Hammer(buy_frame) or inverted_Hammer(buy_frame, 4) or gravestone_doji(buy_frame, 4) or
             shooting_Star(buy_frame, 4) or doji_Star(buy_frame, 4) or spinning_Top(buy_frame, 4)) and

            # [-4]R
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) < buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 4')
        return True

    # [-4, -3, -2]G AND [-4]G is (manual-inverted-hammer or inverted_Hammer or gravestone_doji or
    # shooting_Star OR spinning_Top OR doji_Star) AND [-4]G IS BETWEEN UPPERBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (manual_Inverted_Hammer(buy_frame) or inverted_Hammer(buy_frame, 4) or gravestone_doji(buy_frame, 4) or shooting_Star(buy_frame, 4) or
             doji_Star(buy_frame, 4) or spinning_Top(buy_frame, 4)) and

            # [-4]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 5')
        return True

    # [-4]R AND [-3, -2]G AND [-4]R is (doji_star ) AND [-4]R IS BETWEEN LOWERBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (doji_Star(buy_frame, 4) ) and

            # [-4]R
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) < buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['lowerband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 6')
        return True


def cand_patn_sell(sell_frame):
    # [-4, -3, -2]G AND [-4]G is (manual-inverted-hammer or inverted_Hammer or gravestone_doji or
    # shooting_Star OR spinning_Top OR doji_Star) AND [-4]G IS BETWEEN LOWERBAND AND MIDDLEBAND, AND ADX > 25
    if (
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (manual_Inverted_Hammer(sell_frame) or inverted_Hammer(sell_frame, 4) or gravestone_doji(sell_frame, 4) or shooting_Star(sell_frame, 4) or
             doji_Star(sell_frame, 4) or spinning_Top(sell_frame, 4)) and

            # [-4]G
            ((sell_frame['High'].iloc[-4] and sell_frame['Close'].iloc[-4]) < sell_frame['middleband'].iloc[-4]) and
            ((sell_frame['High'].iloc[-4] and sell_frame['Close'].iloc[-4]) > sell_frame['lowerband'].iloc[-4]) and
            ((sell_frame['Low'].iloc[-4] and sell_frame['Open'].iloc[-4]) > sell_frame['lowerband'].iloc[-4]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_sell 1')
        return True

    # [-4]R AND [-3, -2]G AND [-4]R is (manual-hammer or hammer or doji_star or dragonfly_doji or
    # hanging_Man or spinning_Top) AND [-4]R IS BETWEEN UPPERRBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (manual_Hammer(sell_frame) or hammer(sell_frame, 4) or doji_Star(sell_frame, 4) or dragonfly_Doji(sell_frame, 4) or
             hanging_Man(sell_frame, 4) or spinning_Top(sell_frame, 4)) and

            # [-4]R
            ((sell_frame['High'].iloc[-4] and sell_frame['Open'].iloc[-4]) < sell_frame['upperband'].iloc[-4]) and
            ((sell_frame['High'].iloc[-4] and sell_frame['Open'].iloc[-4]) > sell_frame['middleband'].iloc[-4]) and
            ((sell_frame['Low'].iloc[-4] and sell_frame['Close'].iloc[-4]) > sell_frame['middleband'].iloc[-4]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_sell 2')
        return True

    # [-4]G AND [-3, -2]R AND [-4]G is (manual-inverted-hammer or inverted_Hammer or gravestone_doji or s
    # hooting_Star OR spinning_Top OR doji_Star) AND [-4]G IS BETWEEN UPPERRBAND AND MIDDLEBAND, AND ADX > 25
    elif (
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (manual_Inverted_Hammer(sell_frame) or inverted_Hammer(sell_frame, 4) or gravestone_doji(sell_frame, 4) or shooting_Star(sell_frame, 4) or
             doji_Star(sell_frame, 4) or spinning_Top(sell_frame, 4)) and

            # [-4]G
            ((sell_frame['High'].iloc[-4] and sell_frame['Close'].iloc[-4]) < sell_frame['upperband'].iloc[-4]) and
            ((sell_frame['High'].iloc[-4] and sell_frame['Close'].iloc[-4]) > sell_frame['middleband'].iloc[-4]) and
            ((sell_frame['Low'].iloc[-4] and sell_frame['Open'].iloc[-4]) > sell_frame['middleband'].iloc[-4]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_sell 3')
        return True
