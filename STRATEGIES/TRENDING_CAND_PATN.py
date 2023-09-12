from GENERAL.GENERAL import (doji_Green, doji_Red, doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green,
                             dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, harami_Green, harami_Red, hanging_Man_Green,
                             hanging_Man_Red, inverted_Hammer_Green, inverted_Hammer_Red, marubozu_Green,
                             marubozu_Red, spinning_Top_Green, spinning_Top_Red, shooting_Star_Green,
                             shooting_Star_Red)


def cand_patn_buy(buy_frame):
    # [-4] CAN BE G OR R ,[-3,-2]G AND [-3]G CUT THRU EMA_SHORT OR [-2]G CUT THRU EMA_SHORT
    # AND [-4] HIGH < EMA_SHORT AND ([-3]MACD < [-3]MACDSIGNAL AND [-2]MACD > [-2]MACDSIGNAL)
    # AND 25 < [-2]ADX < 34
    if (
            # [-4] CAN BE G OR R AND HIGH < EMA_SHORT
            (buy_frame['High'].iloc[-4] < buy_frame['ema_short'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-3] CUT THRU EMA_SHORT
            (((buy_frame['High'].iloc[-3] > buy_frame['ema_short'].iloc[-3] or
               buy_frame['Close'].iloc[-3] > buy_frame['ema_short'].iloc[-3]) and
              buy_frame['Open'].iloc[-3] < buy_frame['ema_short'].iloc[-3]) or  # pls read comment above

             # [-2] CUT THRU EMA_SHORT
             ((buy_frame['High'].iloc[-2] > buy_frame['ema_short'].iloc[-2] or
               buy_frame['Close'].iloc[-2] > buy_frame['ema_short'].iloc[-2]) and
              buy_frame['Open'].iloc[-2] < buy_frame['ema_short'].iloc[-2])) and

            (buy_frame['macd'].iloc[-3] < buy_frame['macdsignal'].iloc[-3] and
             buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and

            (25 < buy_frame['adx_line'].iloc[-2] < 34)):

        print('EMA_12 BUY ENTRY 1')
        return True

    # [-4] CAN BE G OR R ,[-3,-2]G AND [-3]G CUT THRU EMA_SHORT OR [-2]G CUT THRU EMA_SHORT
    # HIGH < EMA_SHORT AND ([-4]MACD < [-4]MACDSIGNAL
    # AND [-3]MACD > [-3]MACDSIGNAL AND [-2]MACD > [-2]MACDSIGNAL) AND 25 < [-2]ADX < 34
    elif (
            # [-4] CAN BE G OR R AND HIGH < EMA_SHORT
            (buy_frame['High'].iloc[-4] < buy_frame['ema_short'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-3] CUT THRU EMA_SHORT
            (((buy_frame['High'].iloc[-3] > buy_frame['ema_short'].iloc[-3] or
               buy_frame['Close'].iloc[-3] > buy_frame['ema_short'].iloc[-3]) and
              buy_frame['Open'].iloc[-3] < buy_frame['ema_short'].iloc[-3]) or  # pls read comment above

             # [-2] CUT THRU EMA_SHORT
             ((buy_frame['High'].iloc[-2] > buy_frame['ema_short'].iloc[-2] or
               buy_frame['Close'].iloc[-2] > buy_frame['ema_short'].iloc[-2]) and
              buy_frame['Open'].iloc[-2] < buy_frame['ema_short'].iloc[-2])) and

            (buy_frame['macd'].iloc[-4] < buy_frame['macdsignal'].iloc[-4] and
             buy_frame['macd'].iloc[-3] > buy_frame['macdsignal'].iloc[-3] and
             buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and

            (25 < buy_frame['adx_line'].iloc[-2] < 34)):

        print('EMA_12 BUY ENTRY 2')
        return True

    # [-5] G AND [-4]G IS ENGULFING BULLISH WHICH IS GREEN AND [-3]G AND [-2]R AND ADX > 25
    if (
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

            ((buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and engulfing_Green(buy_frame, 4)) and

            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending cand_patn_buy 1 ENGULFING BULLISH WHICH IS GREEN ')
        return True

    # 2G ENGULFING BEARISH WHICH IS RED 2G AND OPTIONAL R
    # [-6, -5]G AND [-4]R IS ENGULFING BEARISH WHICH IS RED AND [-3, -2]G AND ADX > 25
    elif (
            # [-6]G
            (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and

            # [-5]G
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

            # [-4]R ENGULFING BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and engulfing_Red(buy_frame, 4)) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 2 ENGULFING BEARISH WHICH IS RED')
        return True

    # 2R WHERE 2ND R IS DOJI STAR BULLISH WHICH IS RED AND 3G ALL IS BELOW MID-B ADX > 25
    # [-6]R AND [-5]R IS DOJI STAR BULLISH WHICH IS RED AND [-4, -3, -2]G AND
    # ALL IS BELOW MID-B ADX > 25
    elif (
            # [-6]R
            (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

            # [-5]R IS DOJI STAR BULLISH WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and doji_Star_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-6]R BTW LOWER-B AND MID-B
            (buy_frame['High'].iloc[-6] < buy_frame['middleband'].iloc[-6]) and

            # [-5]R BTW LOWER-B Abuy_frameND MID-B
            (buy_frame['High'].iloc[-5] < buy_frame['middleband'].iloc[-5]) and

            # [-4]G BTW LOWER-B AND MID-B
            (buy_frame['High'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and

            # [-3]G BTW LOWER-B AND MID-B
            (buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and

            # [-2]G BTW LOWER-B AND MID-B
            (buy_frame['High'].iloc[-2] < buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 3 DOJI STAR BULLISH WHICH IS RED')
        return True

    # [-4]G IS DRAGONFLY DOJI BULLISH WHICH IS GREEN AND [-3]G AND [-2]R AND ADX > 25
    elif (
            # [-4]G IS DRAGONFLY DOJI BULLISH WHICH IS GREEN
            ((buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and dragonfly_Doji_Green(buy_frame, 4)) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 4 DRAGONFLY DOJI BULLISH WHICH IS GREEN')
        return True

    # [-5]R IS SHOOTING STAR BEARISH WHICH IS RED [-4, -3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]R IS SHOOTING STAR BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and shooting_Star_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 5 SHOOTING STAR BEARISH WHICH IS RED')
        return True

    # [-5]R IS SPINNING TOP BLACK WHICH IS RED AND [-4, -3, -2]G AND ADX > 25
    elif (
            # [-5]R IS SPINNING TOP BLACK WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and spinning_Top_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-4]G
            (buy_frame['High'].iloc[-4] > buy_frame['middleband'].iloc[-4]) and

            # [-3]G
            (buy_frame['High'].iloc[-3] > buy_frame['middleband'].iloc[-3]) and

            # [-2]G
            (buy_frame['High'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 6 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]R IS SPINNING TOP BLACK WHICH IS RED AND [-4, -3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]R IS SPINNING TOP BLACK WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and spinning_Top_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 7 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]R IS SPINNING TOP BLACK WHICH IS RED AND [-4]R AND [-3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]R IS SPINNING TOP BLACK WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and spinning_Top_Red(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 8 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN  AND [-4, -3, -2]G AND ADX > 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and spinning_Top_Green(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 9 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4, -3, -2]R AND ADX > 25
    elif (
            # [-5]R IS HAMMER WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hammer_Red(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 10 HAMMER WHICH IS RED')
        return True

    # [-5]G IS HAMMER WHICH IS GREEN AND [-4, -3, -2]G AND ADX > 25
    elif (
            # [-5]G IS HAMMER WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and hammer_Green(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 11 HAMMER WHICH IS GRREN')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4]R AND [-3, -2]G AND ADX > 25
    elif (
            # [-5]R IS HAMMER WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hammer_Red(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 12 HAMMER WHICH IS RED')
        return True

    # [-5]G IS INVERTED HAMMER WHICH IS GREEN AND [-4]R AND [-3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]G IS INVERTED HAMMER WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and inverted_Hammer_Green(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 13 INVERTED HAMMER WHICH IS GREEN')
        return True

    # [-5]G IS INVERTED HAMMER WHICH IS GREEN AND [-4]G AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]G IS INVERTED HAMMER WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and inverted_Hammer_Green(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 14 INVERTED HAMMER WHICH IS GREEN')
        return True

    # [-4]R IS INVERTED HAMMER WHICH IS RED AND [-3, -2]R AND ADX > 25
    elif (
            # [-4]R IS INVERTED HAMMER WHICH IS RED
            ((buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and inverted_Hammer_Red(buy_frame, 4)) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 15 INVERTED HAMMER WHICH IS RED')
        return True

    # [-5]R IS HANGING MAN WHICH IS RED AND [-4, -3, -2]G AND ADX > 25
    elif (
            # [-5]R IS HANGING MAN WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hanging_Man_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 16 HANGING MAN WHICH IS RED')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]G AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and hanging_Man_Green(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 17 HANGING MAN WHICH IS GREEN')
        return True

    # 2G AND 2R WHERE 1ST R IS ENGULFING BEARISH WHICH IS RED
    # [-5, -4]G AND [-3]R IS ENGULFING BEARISH WHICH IS RED AND [-2]R AND ADX > 25
    elif (
            # [-5]G
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R AND ENGULFING BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and engulfing_Red(buy_frame, 3)) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_buy 18 ENGULFING BEARISH WHICH IS RED')
        return True

    # # [-5]G IS HAMMER WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX > 25
    # elif (
    #         # [-5]G IS DRAGONFLY WHICH IS GREEN
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and hammer_Green(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 19 HAMMER WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R AND [-4]G [-3]G DOJI ONLY WHICH IS GREEN [-2]G AND ADX > 25
    # elif (
    #         # [-5]R
    #         (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and doji_Green(buy_frame, 3)) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 20 DOJI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5, -4]G AND [-3]G DRAGONFLY WHICH IS GREEN [-2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and
    #
    #         # [-4]R
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and dragonfly_Doji_Green(buy_frame, 3)) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 21 DRAGONFLY WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH ENGULFING WHICH IS GREEN [-4]G AND [-3]R [-2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and engulfing_Green(buy_frame, 5)) and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 22 BULLISH ENGILFING WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R DOJI ONLY WHICH IS RED [-4]G DOJI ONLY WHICH IS RED AND [-3, -2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and doji_Red(buy_frame, 5)) and
    #
    #         # [-4]G
    #         ((buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and doji_Green(buy_frame, 4)) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 23 DOJI ONLY WHICH IS RED AND DOJI ONLY WHICH IS GREEN * ')
    #     return True
    #
    # # [-9]R BEARISH HARAMI WHICH IS RED [-8, -7]R [-6]G [-5]R [-4]G [-3, -2]R AND ADX > 25
    # elif (
    #         # [-9]R
    #         ((buy_frame['Open'].iloc[-9] > buy_frame['Close'].iloc[-9]) and harami_Red(buy_frame, 9)) and
    #
    #         # [-8]R
    #         (buy_frame['Open'].iloc[-8] > buy_frame['Close'].iloc[-8]) and
    #
    #         # [-7]R
    #         (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and
    #
    #         # [-6]G
    #         (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and
    #
    #         # [-5]R
    #         (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 24 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH HARAMI WHICH IS GREEN[-4, -3, -2]R AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and harami_Green(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 25 BULLISH HARAMI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R BEARISH HARAMI WHICH IS RED [-4, -3, -2]G AND ADX > 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Close'].iloc[-5]) and harami_Red(buy_frame, 5)) and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 26 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH HARAMI WHICH IS GREEN[-4]R [-3]G [-2]R AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and harami_Green(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 27 BULLISH HARAMI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH HARAMI WHICH IS GREEN[-4, -3]R [-2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and harami_Green(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 28 BULLISH HARAMI WHICH IS GREEN * ')
    #     return True
    #
    # # [-7, -6]R [-5]R BEARISH MARUBOZU WHICH IS RED [-4, -3]R [-2]G AND ADX > 25
    # elif (
    #         # [-7]R
    #         (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and
    #
    #         # [-6]R
    #         (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and
    #
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and marubozu_Red(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 29 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH MARUBOZU WHICH IS RED [-4]R [-3, -2]G AND ADX > 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and marubozu_Red(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 30 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4]G [-3]R [-2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and marubozu_Green(buy_frame, 5)) and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]R
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_buy 31 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True


def cand_patn_sell(sell_frame):
    # [-4] CAN BE G OR R, [-3,-2]R AND [-3]R CUT THRU EMA_SHORT OR [-2]R CUT THRU EMA_SHORT
    # AND [-4] LOW > EMA_SHORT AND ([-3]MACDSIGNAL < [-3]MACD
    # AND [-2]MACDSIGNAL > [-2]MACD) AND 25 < [-2]ADX < 34
    if (
            # [-4] CAN BE G OR R AND HIGH < EMA_SHORT
            (sell_frame['Low'].iloc[-4] > sell_frame['ema_short'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-3] CUT THRU EMA_SHORT
            (((sell_frame['Open'].iloc[-3] > sell_frame['ema_short'].iloc[-3] > sell_frame['Close'].iloc[-3]) or
              sell_frame['Low'].iloc[-3] < sell_frame['ema_short'].iloc[-3]) or  # pls read comment above

             # [-2] CUT THRU EMA_SHORT
             ((sell_frame['Open'].iloc[-2] > sell_frame['ema_short'].iloc[-2] > sell_frame['Close'].iloc[-2]) or
              sell_frame['Low'].iloc[-2] < sell_frame['ema_short'].iloc[-2])) and

            (sell_frame['macdsignal'].iloc[-3] < sell_frame['macd'].iloc[-3] and
             sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and

            (25 < sell_frame['adx_line'].iloc[-2] < 34)):

        print('TRENDING EMA_12 SELL ENTRY 1')
        return True

    # [-4] CAN BE G OR R, [-3,-2]R AND [-3]R CUT THRU EMA_SHORT OR [-2]R CUT THRU EMA_SHORT
    # AND [-4] LOW > EMA_SHOR AND ([-4]MACDSIGNAL < [-4]MACD
    # AND [-3]MACDSIGNAL > [-3]MACD AND [-2]MACDSIGNAL > [-2]MACD)
    # AND [-2]MACDSIGNAL > [-2]MACD) AND 25 < [-2]ADX < 34
    elif (
            # [-4] CAN BE G OR R AND HIGH < EMA_SHORT
            (sell_frame['Low'].iloc[-4] > sell_frame['ema_short'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]G
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-3] CUT THRU EMA_SHORT
            (((sell_frame['Open'].iloc[-3] > sell_frame['ema_short'].iloc[-3] > sell_frame['Close'].iloc[-3]) or
              sell_frame['Low'].iloc[-3] < sell_frame['ema_short'].iloc[-3]) or  # pls read comment above

             # [-2] CUT THRU EMA_SHORT
             ((sell_frame['Open'].iloc[-2] > sell_frame['ema_short'].iloc[-2] > sell_frame['Close'].iloc[-2]) or
              sell_frame['Low'].iloc[-2] < sell_frame['ema_short'].iloc[-2])) and

            (sell_frame['macdsignal'].iloc[-4] < sell_frame['macd'].iloc[-4] and
             sell_frame['macdsignal'].iloc[-3] > sell_frame['macd'].iloc[-3] and
             sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and

            (25 < sell_frame['adx_line'].iloc[-2] < 34)):

        print('TRENDING EMA_12 SELL ENTRY 2')
        return True

    # [-5]G IS ENGULFING BULLISH WHICH IS GREEN AND [-4, -3, -2]R AND ADX > 25
    elif (
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and engulfing_Green(sell_frame, 5)) and

            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 1 ENGULFING BULLISH WHICH IS GREEN ')
        return True

    # [-5]G IS ENGULFING BULLISH WHICH IS GREEN AND [-4]G AND[-3, -2]R AND ADX > 25
    elif (
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and engulfing_Green(sell_frame, 5)) and

            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 2 ENGULFING BULLISH WHICH IS GREEN')
        return True

    # [-5]R IS ENGULFING BEARISH WHICH IS RED AND [-4, -3, -2]G AND ALL ABOVE MIDDLEBAND AND ADX > 25
    elif (
            # [-5]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and engulfing_Red(sell_frame, 5) and
             (sell_frame['Low'].iloc[-5] > sell_frame['middleband'].iloc[-5])) and

            # [-4]G AND ABOVE MID-B
            ((sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
             (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4])) and

            # [-3]G AND ABOVE MID-B
            ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
             (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3])) and

            # [-2]G AND ABOVE MID-B
            ((sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
             (sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2])) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 3 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-5]G AND [-4]R IS ENGULFING BEARISH WHICH IS RED AND [-3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            (sell_frame['Low'].iloc[-5] > sell_frame['middleband'].iloc[-5]) and

            # [-4]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and engulfing_Red(sell_frame, 4)) and

            (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 4 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-5]G AND [-4]R IS ENGULFING BEARISH WHICH IS RED AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            # [-4]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and engulfing_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 6 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-5]G IS DOJI STAR BEARISH WHICH IS GREEN AND [-4,-3, -2]R AND ADX > 25
    elif (

            # [-5]G AND ABOVE MID-B
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and doji_Star_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['uppereband'].iloc[-5] > sell_frame['Low'].iloc[-5] > sell_frame['middleband'].iloc[-5]) and
            (sell_frame['uppereband'].iloc[-4] > sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and
            (sell_frame['uppereband'].iloc[-3] > sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and
            (sell_frame['uppereband'].iloc[-2] > sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 7 DOJI STAR BEARISH WHICH IS GREEN')
        return True

    # [-5]R IS DRAGONFLY DOJI BULLISH WHICH IS RED AND [-4]G AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and dragonfly_Doji_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 8 DRAGONFLY DOJI BULLISH WHICH IS RED')
        return True

    # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED AND [-4,-3, -2]G AND ADX > 25
    elif (
            # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and gravestone_doji_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 9 GRAVESTONE DOJI BEARISH WHICH IS RED')
        return True

    # [-5]G AND [-4]R IS SHOOTING STAR BEARISH WHICH IS RED AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            # [-4]R IS SHOOTING STAR BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and shooting_Star_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 10 SHOOTING STAR BEARISH WHICH IS RED')
        return True

    # [-5]G AND [-4]R IS SHOOTING STAR BEARISH WHICH IS RED AND [-3]R AND [-2]G AND ADX > 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            # [-4]R IS SHOOTING STAR BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and shooting_Star_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 11 SHOOTING STAR BEARISH WHICH IS RED')
        return True

    # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-4]G AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and shooting_Star_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 12 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-4, -3, -2]R AND ADX > 25
    elif (
            # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and shooting_Star_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 13 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-4]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-3, -2]G AND ADX > 25
    elif (
            # [-4]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and shooting_Star_Green(sell_frame, 4)) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 14 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-4]R IS SPINNING TOP BLACK WHICH IS RED AND [-3, -2]R AND ADX > 25
    elif (
            # [-4]R IS SPINNING TOP BLACK WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and spinning_Top_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 15 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX > 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and spinning_Top_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 16 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN AND [-4, -3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and spinning_Top_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 17 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]G IS HAMMER WHICH IS GREEN AND [-4, -3, -2]R AND ADX > 25
    elif (
            # [-5]G IS HAMMER WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hammer_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 18 HAMMER WHICH IS GREEN')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4]G IS HAMMER WHICH IS GREEN AND [-3, -2]R AND ADX > 25
    elif (
            # [-5]R IS HAMMER WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and hammer_Red(sell_frame, 5)) and

            # [-4]G IS HAMMER WHICH IS GREEN
            ((sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and hammer_Green(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 19 HAMMER WHICH IS RED AND GREEN')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4]R AND [-3]G AND [-2]R AND ADX > 25
    elif (
            # [-5]R IS HAMMER WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and hammer_Red(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 20 HAMMER WHICH IS RED')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX > 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hanging_Man_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 21 HANGING MAN WHICH IS GREEN')
        return True

    # [-4]R IS HANGING MAN WHICH IS RED AND [-3, -2]R ADX > 25
    elif (
            # [-4]R IS HANGING MAN WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and hanging_Man_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('trending cand_patn_sell 22 HANGING MAN WHICH IS RED')
        return True

    # # [-5]R BEARISH HARAMI WHICH IS RED [-4]R, [-3]G AND [-2]R AND ADX > 25
    # elif (
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and harami_Red(sell_frame, 5)) and
    #
    #         # [-4]R
    #         (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_sell 23 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH HARAMI WHICH IS GREEN[-4]G [-3]R [-2]G AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and harami_Green(sell_frame, 5)) and
    #
    #         # [-4]G
    #         (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
    #
    #         # [-3]R
    #         (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_sell 24 BULLISH HARAMI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R BEARISH MARUBOZU WHICH IS RED [-4, -3, -2]G AND ADX > 25
    # elif (
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and marubozu_Red(sell_frame, 5)) and
    #
    #         # [-4]G
    #         (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_selL 25 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-7]G [-6]R [-5]R BEARISH MARUBOZU WHICH IS RED [-4, -3]R [-2]G AND ADX > 25
    # elif (
    #         # [-7]G
    #         (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and
    #
    #         # [-6]R
    #         (sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and
    #
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and marubozu_Red(sell_frame, 5)) and
    #
    #         # [-4]R
    #         (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_sell 26 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4, -3, -2]R AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and marubozu_Green(sell_frame, 5)) and
    #
    #         # [-4]R
    #         (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_sell 27 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4]R [-3]G [-2]R AND ADX > 25
    # elif (
    #         # [-5]G
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and marubozu_Green(sell_frame, 5)) and
    #
    #         # [-4]R
    #         (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] > 25)):
    #
    #     print('trending cand_patn_sell 28 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True
    #
