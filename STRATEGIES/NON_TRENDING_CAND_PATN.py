from GENERAL.GENERAL import (doji_Green, doji_Red, doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green,
                             dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, harami_Green, harami_Red, hanging_Man_Green,
                             hanging_Man_Red, inverted_Hammer_Green, inverted_Hammer_Red, spinning_Top_Green,
                             spinning_Top_Red,
                             marubozu_Green, marubozu_Red, shooting_Star_Green, shooting_Star_Red)


# I ADDED BELOW MID-B MYSELF I THINK DIDN'T TAKE NOTE OF MAY BE THEY WERE BELOW OR ABOVE MID-B
# FROM OBSERVATIONS/EXPERIMENTS/TRIALS THEY DIDN'T REALLY DO WELL, A LOT OF WRONG SIGNALS WERE GENERATE
# THAT IS WHY I AM ADDING BELOW MID-B MYSELF, TO SEE HOW THEY FARE
def cand_patn_buy(buy_frame):
    # [-5]G IS ENGULFING BULLISH WHICH IS GREEN AND [-4]G AND[-3, -2]R AND ADX < 25
    if (
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and engulfing_Green(buy_frame, 5)) and

            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 1 ENGULFING BULLISH WHICH IS GREEN')
        return True

    # [-5]G IS ENGULFING BULLISH WHICH IS GREEN AND [-4, -3]R AND[-2]G AND ADX < 25
    elif (
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and engulfing_Green(buy_frame, 5)) and

            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):
        print('non-trending cand_patn_buy 2 ENGULFING BULLISH WHICH IS GREEN')
        return True

    # [-5]G IS ENGULFING BULLISH WHICH IS GREEN AND [-4]G AND[-3, -2]R AND ADX < 25
    elif (
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and engulfing_Green(buy_frame, 5)) and

            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 3 ENGULFING BULLISH WHICH IS GREEN')
        return True

    # [-5]G AND [-4]R IS ENGULFING BEARISH WHICH IS RED AND [-3, -2]R AND ADX < 25
    if (
            # [-5]G
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

            # [-4]R AND ABOVE MID-B
            ((buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and engulfing_Red(buy_frame, 4)) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 4 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-6]G AND [-5]R IS ENGULFING BEARISH WHICH IS RED AND [-4, -3, -2]G AND ADX < 25
    elif (
            # [-6]G
            (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and

            # [-5]R ENGULFING BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and engulfing_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 5 ENGULFING BEARISH WHICH IS RED')
        return True

    # 3G AND THE LAST G WHICH IS [-2] IS DOJI STAR BULLISH WHICH IS GREEN AND ALL ABOVE MID-B ADX < 25
    elif (

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G IS DOJI STAR BEARISH WHICH IS GREEN
            ((buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and doji_Star_Green(buy_frame, 2)) and

            # [-4] ABOVE MID-B
            (buy_frame['Low'].iloc[-4] > buy_frame['middleband'].iloc[-4]) and

            # [-3] ABOVE MID-B
            (buy_frame['Low'].iloc[-3] > buy_frame['middleband'].iloc[-3]) and

            # [-2] ABOVE MID-B
            (buy_frame['Low'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 6 DOJI STAR BEARISH WHICH IS GREEN')

        return True

    # 3R WHERE 2ND R IS DOJI STAR BEARISH WHICH IS RED AND 3G ALL BTW LOWER-B AND MID-B ADX < 25
    # [-7]R AND [-6]R IS DOJI STAR BEARISH WHICH IS RED AND [-5]R AND [-4, -3, -2]G AND
    # ALL BTW LOWER-B AND MID-B ADX < 25
    elif (

            # [-7]R
            (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

            # [-6]R IS DOJI STAR BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and doji_Star_Red(buy_frame, 6)) and

            # [-5]R
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-7]R BTW LOWER-B AND MID-B
            (buy_frame['lowereband'].iloc[-7] < buy_frame['Low'].iloc[-7] < buy_frame['High'].iloc[-7]
             < buy_frame['middleband'].iloc[-7]) and

            # [-6]R BTW LOWER-B AND MID-B
            (buy_frame['lowereband'].iloc[-6] < buy_frame['Low'].iloc[-6] < buy_frame['High'].iloc[-6]
             < buy_frame['middleband'].iloc[-6]) and

            # [-5]R BTW LOWER-B Abuy_frameND MID-B
            (buy_frame['lowereband'].iloc[-5] < buy_frame['Low'].iloc[-5] < buy_frame['High'].iloc[-5]
             < buy_frame['middleband'].iloc[-5]) and

            # [-4]G BTW LOWER-B AND MID-B
            (buy_frame['lowereband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['High'].iloc[-4]
             < buy_frame['middleband'].iloc[-4]) and

            # [-3]G BTW LOWER-B AND MID-B
            (buy_frame['lowereband'].iloc[-3] < buy_frame['Low'].iloc[-3] < buy_frame['High'].iloc[-3]
             < buy_frame['middleband'].iloc[-3]) and

            # [-2]G BTW LOWER-B AND MID-B
            (buy_frame['lowereband'].iloc[-2] < buy_frame['Low'].iloc[-2] < buy_frame['High'].iloc[-2]
             < buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 7 DOJI STAR BULLISH WHICH IS RED')
        return True

    # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED AND [-4]R AND [-3, -2]G AND ADX < 25
    elif (
            # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and gravestone_doji_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 8 GRAVESTONE DOJI BEARISH WHICH IS RED')
        return True

    # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-4, -3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]G IS SHOOTING STAR BEARISH WHICH IS GRREN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and shooting_Star_Green(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 9 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-4]R IS SPINNING TOP BLACK WHICH IS RED AND [-3]G, [-2]R AND ADX < 25
    elif (
            # [-4]R IS SPINNING TOP BLACK WHICH IS RED
            ((buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and spinning_Top_Red(buy_frame, 4)) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 10 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]R IS SPINNING TOP BLACK WHICH IS RED AND [-4, -3, -2]G AND ADX < 25
    elif (
            # [-5]R IS SPINNING TOP BLACK WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and spinning_Top_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 11 SPINNING TOP BLACK WHICH IS RED')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4]R AND [-3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS HAMMER WHICH IS RED
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and hammer_Red(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 12 HAMMER WHICH IS RED')
        return True

    # [-5]R IS INVERTED HAMMER WHICH IS RED AND [-4]G AND [-3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]R IS INVERTED HAMMER WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and inverted_Hammer_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 13 INVERTED HAMMER WHICH IS RED')
        return True

    # [-5]R IS HANGING MAN WHICH IS RED AND [-4]G AND [-3, -2]R AND ADX < 25
    elif (
            # [-5]R IS HANGING MAN WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hanging_Man_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 14 HANGING MAN WHICH IS RED')
        return True

    # [-5]R IS HANGING MAN WHICH IS RED AND [-4]G AND [-3, -2]R AND ADX < 25
    elif (
            # [-5]R IS HANGING MAN WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hanging_Man_Red(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 15 HANGING MAN WHICH IS RED')
        return True

    # [-5]R IS HANGING MAN WHICH IS RED AND [-4]R AND [-3]G AND [-2]R ADX < 25
    elif (
            # [-5]R IS HANGING MAN WHICH IS RED
            ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and hanging_Man_Red(buy_frame, 5)) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 16 HANGING MAN WHICH IS RED')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]G AND [-3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and hanging_Man_Green(buy_frame, 5)) and

            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            # [-3]R
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            # [-2]G
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_buy 17 HANGING MAN WHICH IS GREEN')
        return True

    # # [-6]G IS DRAGONFLY WHICH IS GREEN AND [-5]G AND [-4]R AND [-3]G IS DRAGONFLY WHICH IS GREEN [-2]G AND ADX < 25
    # elif (
    #         # [-6]G IS DRAGONFLY WHICH IS GREEN
    #         ((buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and hanging_Man_Green(buy_frame, 6)) and
    #
    #         # [-5]G
    #         (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G IS DRAGONFLY WHICH IS GREEN
    #         ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and hanging_Man_Green(buy_frame, 3)) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 18 DRAGONFLY WHICH IS GREEN * ')
    #     return True

    # # [-7]R IS BEARISH ENGULFING WHICH IS RED [-6]G [-5]R AND [-4]G [-3]G DOJI ONLY WHICH IS GREEN [-2]G AND ADX < 25
    # elif (
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
    #         # [-3]G
    #         ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and doji_Green(buy_frame, 3)) and
    #
    #         # [-2]G
    #         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 19 BEARISH ENGULFING WHICH IS RED AND DOJI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G AND [-4]R [-3]R DOJI ONLY WHICH IS RED [-2]R AND ADX < 25
    # elif (
    #         # [-5]G
    #         (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and doji_Red(buy_frame, 3)) and
    #
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 20 DOJI WHICH IS RED * ')
    #     return True
    #
    # # [-5, -4]R AND [-3]G BULLISH ENGILFING WHICH IS GREEN [-2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G
    #         ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and engulfing_Green(buy_frame, 3)) and
    #
    #         # [-2]G
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 21 BULLISH ENGILFING WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH ENGILFING WHICH IS GREEN [-4,-3]R [-2]G AND ADX < 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and engulfing_Green(buy_frame, 5)) and
    #
    #         # [-4]R
    #         (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
    #
    #         # [-3]R
    #         (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
    #
    #         # [-2]G
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 22 BULLISH ENGILFING WHICH IS GREEN * ')
    #     return True
    #
    # # [-6]R BEARISH HARAMI WHICH IS RED [-5, -4, -3, -2]R AND ADX < 25
    # elif (
    #         # [-6]R
    #         ((buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and harami_Red(buy_frame, 6)) and
    #
    #         # [-5]R
    #         (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 23 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH HARAMI WHICH IS GREEN [-4, -3]R [-2]G AND ADX < 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and harami_Green(buy_frame, 5)) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 24 BULLISH HARAMI WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R BEARISH HARAMI WHICH IS RED [-4]R [-3, -2]G AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and harami_Red(buy_frame, 5)) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 25 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH MARUBOZU WHICH IS RED AND [-5]R HIGH LESS THAN MID-B [-4, -3]G [-2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and marubozu_Red(buy_frame, 5)) and
    #
    #         # [-5]R HIGH LESS THAN MID-B
    #         buy_frame['High'].iloc[-5] < buy_frame['middleband'].iloc[-5] and
    #
    #         # [-4]G
    #         (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 26 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH MARUBOZU WHICH IS RED AND [-4]G [-3,-2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and marubozu_Red(buy_frame, 5)) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 27 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH MARUBOZU WHICH IS RED [-4]G [-3]R [-2]G AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and marubozu_Red(buy_frame, 5)) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 28 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-7, -6]G [-5]R BEARISH MARUBOZU WHICH IS RED [-4, -3, -2]R AND ADX < 25
    # elif (
    #         # [-7]G
    #         (buy_frame['Close'].iloc[-7] > buy_frame['Open'].iloc[-7]) and
    #
    #         # [-6]R
    #         (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and
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
    #         # [-2]R
    #         (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
    #
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 30 BEARISH MARUBOZU WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4, -3]R [-2]G AND ADX < 25
    # elif (
    #         # [-5]G
    #         ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and marubozu_Green(buy_frame, 5)) and
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
    #         (buy_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 31 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True


# I ADDED BELOW MID-B MYSELF I THINK DIDN'T TAKE NOTE OF MAY BE THEY WERE BELOW OR ABOVE MID-B
# FROM OBSERVATIONS/EXPERIMENTS/TRIALS THEY DIDN'T REALLY DO WELL, A LOT OF WRONG SIGNALS WERE GENERATE
# THAT IS WHY I AM ADDING BELOW MID-B MYSELF, TO SEE HOW THEY FARE
def cand_patn_sell(sell_frame):
    # [-5]G AND [-4]R IS ENGULFING BEARISH WHICH IS RED AND [-3]G AND [-2]R AND ADX < 25
    if (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            # [-4]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and engulfing_Red(sell_frame, 4) and
             (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4])) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 1 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-6]G AND [-5]R IS ENGULFING BEARISH WHICH IS RED AND [-4]G AND [-3, -2]R AND ADX < 25
    elif (
            # [-6]G
            (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

            # [-5]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and engulfing_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 2 ENGULFING BEARISH WHICH IS RED')
        return True

    # [-4]G IS DOJI STAR BEARISH WHICH IS GREEN AND [-3, -2]R AND ALL BTW LOWER-B AND MID-B ADX < 25
    elif (
            # [-4]G IS DOJI STAR BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and doji_Star_Green(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-4] BTW LOWER-B AND MID-B
            (sell_frame['lowereband'].iloc[-4] < sell_frame['Low'].iloc[-4] < sell_frame['High'].iloc[-4]
             < sell_frame['middleband'].iloc[-4]) and

            # [-3] BTW LOWER-B AND MID-B
            (sell_frame['lowereband'].iloc[-3] < sell_frame['Low'].iloc[-3] < sell_frame['High'].iloc[-3]
             < sell_frame['middleband'].iloc[-3]) and

            # [-2] BTW LOWER-B AND MID-B
            (sell_frame['lowereband'].iloc[-2] < sell_frame['Low'].iloc[-2] < sell_frame['High'].iloc[-2]
             < sell_frame['middleband'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 3 DOJI STAR BEARISH WHICH IS GREEN')
        return True

    # [-4]R IS DRAGONFLY DOJI BULLISH WHICH IS RED AND [-3, -2]R AND ADX < 25
    elif (
            # [-4]R AND ABOVE MID-B
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and dragonfly_Doji_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 4 DRAGONFLY DOJI BULLISH WHICH IS RED')
        return True

    # [-5]G IS DRAGONFLY DOJI BULLISH WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX < 25
    elif (
            # [-5]G IS DRAGONFLY DOJI BULLISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and dragonfly_Doji_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 5 DRAGONFLY DOJI BULLISH WHICH IS GREEN')
        return True

    # [-4]R IS GRAVESTONE DOJI BEARISH WHICH IS RED AND [-3, -2]R AND ADX < 25
    elif (
            # [-4]R IS GRAVESTONE DOJI BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and gravestone_doji_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 6 GRAVESTONE DOJI BEARISH WHICH IS RED')
        return True

    # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED AND [-4, -3]G AND [-2]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN
    # AND ADX < 25
    elif (
            # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and gravestone_doji_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and gravestone_doji_Green(sell_frame, 2)) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 7 GRAVESTONE DOJI BEARISH WHICH IS RED AND '
              'GRAVESTONE DOJI BEARISH WHICH IS GREEN')
        return True

    # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED AND [-4,-3, -2]G AND ADX < 25
    elif (
            # [-5]R IS GRAVESTONE DOJI BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and gravestone_doji_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 8 GRAVESTONE DOJI BEARISH WHICH IS RED')
        return True

    # [-5]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN AND [-4,-3, -2]R AND ADX < 25
    elif (
            # [-5]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and gravestone_doji_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 9 GRAVESTONE DOJI BEARISH WHICH IS GREEN')
        return True

    # [-5]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN AND [-4,-3, -2]G AND ADX < 25
    elif (
            # [-5]G IS GRAVESTONE DOJI BEARISH WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and gravestone_doji_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 10 GRAVESTONE DOJI BEARISH WHICH IS GREEN')
        return True

    # [-5]R IS SHOOTING STAR BEARISH WHICH IS RED AND [-4, -3, -2]G AND ADX < 25
    elif (
            # [-5]R IS SHOOTING STAR BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and shooting_Star_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 11 SHOOTING STAR BEARISH WHICH IS RED')
        return True

    # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-4]R AND [-3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS SHOOTING STAR BEARISH WHICH IS GRREN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and shooting_Star_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 12 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-5]R IS SHOOTING STAR BEARISH WHICH IS RED [-4, -3]R AND ADX < 25
    elif (
            # [-4]R IS SHOOTING STAR BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and shooting_Star_Red(sell_frame, 4)) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 13 SHOOTING STAR BEARISH WHICH IS RED')
        return True

    # [-5]G IS SHOOTING STAR BEARISH WHICH IS GREEN AND [-4]G AND [-3, -2]R AND ADX < 25
    elif (
            # [-5]G IS SHOOTING STAR BEARISH WHICH IS GRREN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and shooting_Star_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 14 SHOOTING STAR BEARISH WHICH IS GREEN')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN AND [-4]G, AND [-3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and spinning_Top_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 15 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN AND [-4]R AND [-3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and spinning_Top_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 16 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]R IS GRAVESTONE DOJI WHICH IS RED AND [-4]R AND [-3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS GRAVESTONE DOJI WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and gravestone_doji_Red(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 17 GRAVESTONE DOJI WHICH IS RED')
        return True

    # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN AND [-4, -3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS SPINNING TOP WHITE WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and spinning_Top_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 18 SPINNING TOP WHITE WHICH IS GREEN')
        return True

    # [-5]R IS HAMMER WHICH IS RED AND [-4, -3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]R IS HAMMER WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and hammer_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 19 HAMMER WHICH IS RED')
        return True

    # [-5]G IS HAMMER WHICH IS GREEN AND [-4]G AND [-3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]R IS HAMMER WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hammer_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 20 HAMMER WHICH IS GREEN')
        return True

    # [-5]R IS INVERTED HAMMER WHICH IS RED AND [-4, -3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]R IS INVERTED HAMMER WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and inverted_Hammer_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 21 INVERTED HAMMER WHICH IS RED')
        return True

    # [-5]G IS INVERTED HAMMER WHICH IS GREEN AND [-4, -3, -2]R AND ADX < 25
    elif (
            # [-5]G IS INVERTED HAMMER WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and inverted_Hammer_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 22 INVERTED HAMMER WHICH IS GREEN')
        return True

    # [-5]G IS INVERTED HAMMER WHICH IS GREEN AND [-4]G AND [-3]R AND [-2]G AND ADX < 25
    elif (
            # [-5]G IS INVERTED HAMMER WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and inverted_Hammer_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 23 INVERTED HAMMER WHICH IS GREEN')
        return True

    # [-5]R IS INVERTED HAMMER WHICH IS RED AND AND [-4]R AND [-3]G AND[-2]R AND ADX < 25
    elif (
            # [-5]R IS INVERTED HAMMER WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and inverted_Hammer_Red(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 24 INVERTED HAMMER WHICH IS RED')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX < 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hanging_Man_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 25 HANGING MAN WHICH IS GREEN')
        return True

    # [-5]R IS HANGING MAN WHICH IS RED AND [-4, -3, -2]G AND ADX < 25
    elif (
            # [-5]R IS HANGING MAN WHICH IS RED
            ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and hanging_Man_Red(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 26 HANGING MAN WHICH IS RED')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]R AND [-3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hanging_Man_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 27 HANGING MAN WHICH IS GREEN')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4]R AND [-3, -2]G AND ADX < 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hanging_Man_Green(sell_frame, 5)) and

            # [-4]R
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]G
            (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 28 HANGING MAN WHICH IS GREEN')
        return True

    # [-5]G IS HANGING MAN WHICH IS GREEN AND [-4, -3]G AND [-2]R AND ADX < 25
    elif (
            # [-5]G IS HANGING MAN WHICH IS GREEN
            ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and hanging_Man_Green(sell_frame, 5)) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 29 HANGING MAN WHICH IS GREEN')
        return True

    # 2G AND 2R WHERE 1ST R IS ENGULFING BEARISH WHICH IS RED
    # [-5, -4]G AND [-3]R IS ENGULFING BEARISH WHICH IS RED AND [-2]R AND ADX < 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R AND ENGULFING BEARISH WHICH IS RED
            ((sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and engulfing_Red(sell_frame, 3)) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('non-trending cand_patn_sell 30 ENGULFING BEARISH WHICH IS RED')
        return True

    # # [-5]G IS DOJI WHICH IS RED AND [-4]R AND [-3]G AND [-2]G AND ADX < 25
    # elif (
    #         # [-5]G IS DRAGONFLY WHICH IS GREEN
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and doji_Green(sell_frame, 5)) and
    #
    #         # [-4]R
    #         (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
    #
    #         # [-3]G IS DRAGONFLY WHICH IS GREEN
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]G
    #         (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_buy 31 DOJI WHICH IS RED * ')
    #     return True
    #
    # # [-6]R IS HAMMER WHICH IS RED AND [-5]R AND [-4]R AND [-3]G WHICH IS BULLISH GREEN [-2]R AND ADX < 25
    # elif (
    #         # [-6]R IS HAMMER WHICH IS RED
    #         ((sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and hammer_Red(sell_frame, 6)) and
    #
    #         # [-5R
    #         (sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and
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
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 32 HAMMER WHICH IS RED AND BULLISH GREEN * ')
    #     return True
    #
    # # [-5]R BEARISH ENGULFING WHICH IS RED [-4, -3]G AND [-2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and engulfing_Red(sell_frame, 5)) and
    #
    #         # [-4]G
    #         (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 33 BULLISH ENGULFING WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH HARAMI WHICH IS RED [-4]G, [-3]R AND [-2]G AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and harami_Red(sell_frame, 5)) and
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
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 34 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]R BEARISH HARAMI WHICH IS RED [-4, -3]G AND [-2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and harami_Red(sell_frame, 5)) and
    #
    #         # [-4]G
    #         (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 35 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-7, -6]R [-5]G [-4]R BEARISH HARAMI WHICH IS RED [-4]G [-3]G, [-2]R AND ADX < 25
    # elif (
    #         # [-7]R
    #         (sell_frame['Open'].iloc[-7] > sell_frame['Close'].iloc[-7]) and
    #
    #         # [-6]R
    #         (sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and
    #
    #         # [-5]G
    #         (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
    #
    #         # [-4]R
    #         ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and harami_Red(sell_frame, 9)) and
    #
    #         # [-3]G
    #         (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 36 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-6]R BEARISH HARAMI WHICH IS RED[-5, -4, -3, -2]G AND ADX < 25
    # elif (
    #         # [-6]R
    #         ((sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and harami_Red(sell_frame, 6)) and
    #
    #         # [-5]G
    #         (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
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
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 37 BEARISH HARAMI WHICH IS RED * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4]R [-3]G [-2]R AND ADX < 25
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
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 38 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH MARUBOZU WHICH IS GREEN [-4]G [-3, -2]R AND ADX < 25
    # elif (
    #         # [-5]G
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and marubozu_Green(sell_frame, 5)) and
    #
    #         sell_frame['Low'].iloc[-5] > sell_frame['middleband'].iloc[-5] and
    #
    #         # [-4]G
    #         (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
    #
    #         sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4] and
    #
    #         # [-3]R
    #         (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
    #
    #         sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3] and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2] and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 39 BULLISH MARUBOZU WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]G BULLISH ENGULFING WHICH IS GREEN [-4]R [-3]G [-2]R AND ADX < 25
    # elif (
    #         # [-5]G
    #         ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and engulfing_Green(sell_frame, 5)) and
    #
    #         sell_frame['HIGH'].iloc[-5] < sell_frame['middleband'].iloc[-5] and
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
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 40 BULLISH ENGULFING WHICH IS GREEN * ')
    #     return True
    #
    # # [-5]R [-4]R BULLISH ENGULFING WHICH IS RED [-3, -2]R AND ADX < 25
    # elif (
    #         # [-5]R
    #         (sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and
    #
    #         # [-4]R
    #         ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and engulfing_Green(sell_frame, 4)) and
    #
    #         sell_frame['low'].iloc[-4] > sell_frame['middleband'].iloc[-4] and
    #
    #         # [-3]R
    #         (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
    #
    #         # [-2]R
    #         (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
    #
    #         (sell_frame['adx_line'].iloc[-2] < 25)):
    #
    #     print('non-trending cand_patn_sell 41 BULLISH ENGULFING WHICH IS RED * ')
    #     return True
