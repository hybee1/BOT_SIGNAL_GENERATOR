# ********* BOLLINGER BAND WHEN MARKET IS TRENDING****************
def bollinger_band_buy(buy_frame):
    if (
            (buy_frame['middleband'].iloc[-4] < buy_frame['middleband'].iloc[-3] <
             buy_frame['middleband'].iloc[-2]) and

            ((buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] < 25) and
             buy_frame['adx_line'].iloc[-2] >= 25)):
        print('bollinger band buy 1')
        return True

    elif ((buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
           buy_frame['middleband'].iloc[-2]) and

          (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4] and
           buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3] and
           buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['adx_line'].iloc[-2] > 25) and

          (buy_frame['Volume'].iloc[-5] > 5000 or buy_frame['Volume'].iloc[-4] > 5000 or
           buy_frame['Volume'].iloc[-3] > 5000 or buy_frame['Volume'].iloc[-2] > 5000)):

        print('bollinger band buy 2')
        return True

    elif ((buy_frame['adx_line'].iloc[-4] > buy_frame['adx_line'].iloc[-3] >
           buy_frame['adx_line'].iloc[-2] > 25) and

          (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
           buy_frame['middleband'].iloc[-2]) and

          (buy_frame['lowerband'].iloc[-2] >= buy_frame['Open'].iloc[-2] or
           buy_frame['lowerband'].iloc[-2] >= buy_frame['High'].iloc[-2] or
           buy_frame['lowerband'].iloc[-2] >= buy_frame['Low'].iloc[-2] or
           buy_frame['lowerband'].iloc[-2] >= buy_frame['Close'].iloc[-2])):

        print('bollinger band buy 3')
        return True

    elif ((25 > buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] <
           buy_frame['adx_line'].iloc[-2] > 25) and

          (buy_frame['adx_line'].iloc[-2] < 35) and

          (buy_frame['middleband'].iloc[-4] < buy_frame['middleband'].iloc[-3] <
           buy_frame['middleband'].iloc[-2])):

        print('bollinger band buy 4')
        return True

    elif ((25 >= buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] <
           buy_frame['adx_line'].iloc[-2]) and

          (buy_frame['adx_line'].iloc[-2] < 35) and

          (buy_frame['middleband'].iloc[-4] < buy_frame['middleband'].iloc[-3] <
           buy_frame['middleband'].iloc[-2])):

        print('bollinger band buy 5')
        return True

    elif ((buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
           buy_frame['middleband'].iloc[-2]) and

          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5] and

           buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4] and
           buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3] and
           buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['lowerband'].iloc[-5] >= buy_frame['Open'].iloc[-5] or
           buy_frame['lowerband'].iloc[-5] >= buy_frame['High'].iloc[-5] or
           buy_frame['lowerband'].iloc[-5] >= buy_frame['Low'].iloc[-5] or
           buy_frame['lowerband'].iloc[-5] >= buy_frame['Close'].iloc[-5])):

        print('bollinger band buy 6')
        return True

    elif ((buy_frame['middleband'].iloc[-4] < buy_frame['middleband'].iloc[-3] <
           buy_frame['middleband'].iloc[-2]) and

          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5] and

           buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4] and
           buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3] and
           buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['Open'].iloc[-5] > buy_frame['middleband'].iloc[-5] or
           buy_frame['High'].iloc[-5] > buy_frame['middleband'].iloc[-5]) and

          (buy_frame['Low'].iloc[-5] < buy_frame['middleband'].iloc[-5] or
           buy_frame['Close'].iloc[-5] < buy_frame['middleband'].iloc[-5])):

        print('bollinger band buy 7 cut thru mid-band')
        return True

    # [-5]R AND [-4,-3,-2]G AND (LOWERBAND < [-5]R < MIDDLEBAND) AND (LOWERBAND < [-4]G < MIDDLEBAND)
    # AND ([-3]G IS BELOW OR CUTS THRU MIDDLEBAND ABOVE) AND ([-2]G IS CUTS THRU OR ABOVE MIDDLEBAND)

    elif ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

          (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
          (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
          (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['lowerband'].iloc[-5] < buy_frame['Low'].iloc[-5] < buy_frame['High'].iloc[-5] <
           buy_frame['middleband'].iloc[-5]) and

          (buy_frame['lowerband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['High'].iloc[-4] <
           buy_frame['middleband'].iloc[-4]) and

          ((buy_frame['lowerband'].iloc[-3] < buy_frame['Low'].iloc[-3] < buy_frame['High'].iloc[-3] <
            buy_frame['middleband'].iloc[-3]) or

           ((buy_frame['lowerband'].iloc[-3] < buy_frame['Low'].iloc[-3] <
             buy_frame['middleband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Open'].iloc[-3] <
             buy_frame['middleband'].iloc[-3]) and
            (buy_frame['middleband'].iloc[-3] < buy_frame['Close'].iloc[-3] <
             buy_frame['upperband'].iloc[-3]) and
            (buy_frame['middleband'].iloc[-3] < buy_frame['High'].iloc[-3] <
             buy_frame['upperband'].iloc[-3]))) and

          (((buy_frame['lowerband'].iloc[-2] < buy_frame['Low'].iloc[-2] <
             buy_frame['middleband'].iloc[-2]) and
            (buy_frame['lowerband'].iloc[-2] < buy_frame['Open'].iloc[-2] <
             buy_frame['middleband'].iloc[-2]) and
            (buy_frame['middleband'].iloc[-2] < buy_frame['Close'].iloc[-2] <
             buy_frame['upperband'].iloc[-2]) and
            (buy_frame['middleband'].iloc[-2] < buy_frame['High'].iloc[-2] <
             buy_frame['upperband'].iloc[-2])) or

           (buy_frame['middleband'].iloc[-2] < buy_frame['Low'].iloc[-2])) and

          (buy_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band buy 8 like ma')
        return True

    # REVERSE BUY IB LOOK WELL
    # [-5]G AND [-4,-3,-2]R AND (LOWERBAND < [-5]G < MIDDLEBAND) AND (LOWERBAND < [-4]R < MIDDLEBAND)
    # AND (LOWERBAND < [-3]R < MIDDLEBAND) AND (MIDDLEBAND > [-2]R AND [-2]R CUTS THRU BELOW LOWERBAND)

    elif ((buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

          (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
          (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
          (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

          (buy_frame['lowerband'].iloc[-5] < buy_frame['Low'].iloc[-5] < buy_frame['High'].iloc[-5] <
           buy_frame['middleband'].iloc[-5]) and

          (buy_frame['lowerband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['High'].iloc[-4] <
           buy_frame['middleband'].iloc[-4]) and

          (buy_frame['lowerband'].iloc[-3] < buy_frame['Low'].iloc[-3] < buy_frame['High'].iloc[-3] <
           buy_frame['middleband'].iloc[-3]) and

          (buy_frame['middleband'].iloc[-2] > buy_frame['High'].iloc[-2] > buy_frame['lowerband'].iloc[-2] >
           buy_frame['Close'].iloc[-2]) and

          (buy_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band trending reverse buy ')
        return True

    # [-3]R AND [-2]G AND ([-3]R CUT THRU LOWERBAND BUT < MIDDLEBAND) AND ([-2]G CUT THRU LOWERBAND BUT < MIDDLEBAND)
    # ADX < 35

    elif ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

          (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['middleband'].iloc[-3] > buy_frame['High'].iloc[-3] > buy_frame['Low'].iloc[-3] <
           buy_frame['lowerband'].iloc[-3]) and

          (buy_frame['middleband'].iloc[-2] > buy_frame['High'].iloc[-2] > buy_frame['Low'].iloc[-2] <
           buy_frame['lowerband'].iloc[-2]) and

          (buy_frame['adx_line'].iloc[-2] < 35)):

        print('bollinger band buy R and G cut thru ')
        return True

    # [-6]G [-5, -4, -3]R [-2]G AND ALL ARE BTW MID-B AND LOWER-B AND ADX > 25
    elif (
            (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
            # [-6]G
            (buy_frame['middleband'].iloc[-6] > buy_frame['High'].iloc[-6] > buy_frame['Low'].iloc[-6] >
             buy_frame['lowerband'].iloc[-6]) and
            # [-5]R
            (buy_frame['middleband'].iloc[-5] > buy_frame['High'].iloc[-5] > buy_frame['Low'].iloc[-5] >
             buy_frame['lowerband'].iloc[-5]) and
            # [-4]R
            (buy_frame['middleband'].iloc[-4] > buy_frame['High'].iloc[-4] > buy_frame['Low'].iloc[-4] >
             buy_frame['lowerband'].iloc[-4]) and
            # [-3]R
            (buy_frame['middleband'].iloc[-3] > buy_frame['High'].iloc[-3] > buy_frame['Low'].iloc[-3] >
             buy_frame['lowerband'].iloc[-3]) and
            # [-2]G
            (buy_frame['middleband'].iloc[-2] > buy_frame['High'].iloc[-2] > buy_frame['Low'].iloc[-2] >
             buy_frame['lowerband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band buy G3RG')
        return True

    # [-5]R AND [-4, -3]G AND [-2]R AND [-5]R [-4]G ARE BETWEEN UPPERBAND AND MIDDLEBAND, AND [-3]G [-2]R CUT
    # THRU UPPERBAND AND ADX > 25
    elif (
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Open'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-5]R
            ((buy_frame['High'].iloc[-5] and buy_frame['Open'].iloc[-5]) < buy_frame['upperband'].iloc[-5]) and
            ((buy_frame['High'].iloc[-5] and buy_frame['Open'].iloc[-5]) > buy_frame['middleband'].iloc[-5]) and
            ((buy_frame['Low'].iloc[-5] and buy_frame['Close'].iloc[-5]) > buy_frame['middleband'].iloc[-5]) and

            # [-4]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and

            # [-3]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and

            # [-2]R
            ((buy_frame['High'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['upperband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Close'].iloc[-4]) > buy_frame['middleband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('bollinger band buy RG AND GR cut thru upper B ')
        return True

    # [-4, -3, -2]G AND [-4]G CUT THRU LOWERBAND BUT [-4]H < MID-B AND ADX > 25
    elif (
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-4]G
            ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['middleband'].iloc[-4]) and
            ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) < buy_frame['lowerband'].iloc[-4]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):
        print('trending buy [-4]g cut thru lower b')
        return True


def bollinger_band_sell(sell_frame):
    if (
            (sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] >
             sell_frame['middleband'].iloc[-2]) and

            ((sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] < 25) and
             sell_frame['adx_line'].iloc[-2] >= 25)):
        print('bollinger band sell 1')
        return True

    elif (
            (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
             sell_frame['middleband'].iloc[-2]) and

            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
             sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
             sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25) and

            (sell_frame['Volume'].iloc[-5] > 5000 or sell_frame['Volume'].iloc[-4] > 5000 or
             sell_frame['Volume'].iloc[-3] > 5000 or sell_frame['Volume'].iloc[-2] > 5000)):

        print('bollinger band sell 2')
        return True

    elif ((sell_frame['adx_line'].iloc[-4] > sell_frame['adx_line'].iloc[-3] >
           sell_frame['adx_line'].iloc[-2] > 25) and

          (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
           sell_frame['middleband'].iloc[-2]) and

          (sell_frame['upperband'].iloc[-2] <= sell_frame['Open'].iloc[-2] or
           sell_frame['upperband'].iloc[-2] <= sell_frame['High'].iloc[-2] or
           sell_frame['upperband'].iloc[-2] <= sell_frame['Low'].iloc[-2] or
           sell_frame['upperband'].iloc[-2] <= sell_frame['Close'].iloc[-2])):

        print('bollinger band sell 3')
        return True

    elif ((25 > sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] <
           sell_frame['adx_line'].iloc[-2] > 25) and

          (sell_frame['adx_line'].iloc[-2] < 35) and

          (sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] >
           sell_frame['middleband'].iloc[-2])):

        print('bollinger band sell 4')
        return True

    elif ((25 >= sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] <
           sell_frame['adx_line'].iloc[-2]) and

          (sell_frame['adx_line'].iloc[-2] < 35) and

          (sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] >
           sell_frame['middleband'].iloc[-2])):

        print('bollinger band sell 5')
        return True

    elif ((sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
           sell_frame['middleband'].iloc[-2]) and

          (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5] and

           sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
           sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
           sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (sell_frame['Open'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['High'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['Low'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['Close'].iloc[-5] >= sell_frame['upperband'].iloc[-5])):

        print('bollinger band sell 6')
        return True

    elif ((sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] >
           sell_frame['middleband'].iloc[-2]) and

          (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5] and

           sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
           sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
           sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (sell_frame['Open'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['High'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['Low'].iloc[-5] >= sell_frame['upperband'].iloc[-5] or
           sell_frame['Close'].iloc[-5] >= sell_frame['upperband'].iloc[-5])):

        print('bollinger band sell 6')
        return True

    elif ((sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] >
           sell_frame['middleband'].iloc[-2]) and

          (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5] and

           sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4] and
           sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3] and
           sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (sell_frame['Open'].iloc[-5] < sell_frame['middleband'].iloc[-5] or
           sell_frame['Low'].iloc[-5] < sell_frame['middleband'].iloc[-5]) and

          (sell_frame['High'].iloc[-5] > sell_frame['middleband'].iloc[-5] or
           sell_frame['Close'].iloc[-5] > sell_frame['middleband'].iloc[-5])):

        print('bollinger band sell 7 cut thru mid-band')
        return True

    # [-5]G AND [-4,-3,-2]R AND (MIDDLEBAND < [-5]G < UPPERBAND) AND (MIDDLEBAND < [-4]G < UPPERBAND)
    # AND ([-3]R IS ABOVE OR CUTS THRU MIDDLEBAND BELOW) AND ([-2]R IS CUTS THRU MIDDLEBAND BELOW OR BELOW MIDDLEBAND)

    elif ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

          (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
          (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
          (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (sell_frame['middleband'].iloc[-5] < sell_frame['Low'].iloc[-5] < sell_frame['High'].iloc[-5] <
           sell_frame['upperband'].iloc[-5]) and

          (sell_frame['middleband'].iloc[-4] < sell_frame['Low'].iloc[-4] < sell_frame['High'].iloc[-4] <
           sell_frame['upperband'].iloc[-4]) and

          ((sell_frame['middleband'].iloc[-3] < sell_frame['Low'].iloc[-3] < sell_frame['High'].iloc[-3] <
            sell_frame['upperband'].iloc[-3]) or

           ((sell_frame['middleband'].iloc[-3] < sell_frame['High'].iloc[-3] <
             sell_frame['upperband'].iloc[-3]) and
            (sell_frame['middleband'].iloc[-3] < sell_frame['Open'].iloc[-3] <
             sell_frame['upperband'].iloc[-3]) and
            (sell_frame['middleband'].iloc[-3] > sell_frame['Close'].iloc[-3] >
             sell_frame['lowerband'].iloc[-3]) and
            (sell_frame['middleband'].iloc[-3] > sell_frame['Low'].iloc[-3] >
             sell_frame['lowerband'].iloc[-3]))) and

          (((sell_frame['middleband'].iloc[-2] < sell_frame['High'].iloc[-2] <
             sell_frame['upperband'].iloc[-2]) and
            (sell_frame['middleband'].iloc[-2] < sell_frame['Open'].iloc[-2] <
             sell_frame['upperband'].iloc[-2]) and
            (sell_frame['middleband'].iloc[-2] > sell_frame['Close'].iloc[-2] >
             sell_frame['lowerband'].iloc[-2]) and
            (sell_frame['middleband'].iloc[-2] > sell_frame['Low'].iloc[-2] >
             sell_frame['lowerband'].iloc[-2])) or

           (sell_frame['middleband'].iloc[-2] > sell_frame['High'].iloc[-2])) and

          (sell_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band sell 8 like ma')
        return True

    # REVERSE SELL IB LOOK WELL
    # [-5]R AND [-4,-3,-2]G AND (MIDDLEBAND < [-5]G < UPPERBAND) AND (MIDDLEBAND < [-4]R < UPPERBAND)
    # AND (MIDDLEBAND < [-3]R < UPPERBAND) AND (MIDDLEBAND < [-2]R AND [-2]R CUTS THRU ABOVE UPPERBAND)

    elif ((sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and

          (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
          (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
          (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and

          (sell_frame['middleband'].iloc[-5] < sell_frame['Low'].iloc[-5] < sell_frame['High'].iloc[-5] <
           sell_frame['upperband'].iloc[-5]) and

          (sell_frame['middleband'].iloc[-4] < sell_frame['Low'].iloc[-4] < sell_frame['High'].iloc[-4] <
           sell_frame['upperband'].iloc[-4]) and

          (sell_frame['middleband'].iloc[-3] < sell_frame['Low'].iloc[-3] < sell_frame['High'].iloc[-3] <
           sell_frame['upperband'].iloc[-3]) and

          (sell_frame['middleband'].iloc[-2] < sell_frame['Low'].iloc[-2] < sell_frame['upperband'].iloc[-2] <
           sell_frame['Close'].iloc[-2]) and

          (sell_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band trending reverse sell ')
        return True

    # [-3]G AND [-2]R AND ([-3]G CUT THRU UPPERBAND AND > MIDDLEBAND) AND ([-2]RG CUT THRU UPPERBAND AND > MIDDLEBAND)
    # ADX < 35
    elif ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

          (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (sell_frame['High'].iloc[-3] > sell_frame['upperband'].iloc[-3] > sell_frame['Low'].iloc[-3] >
           sell_frame['middleband'].iloc[-3]) and

          (sell_frame['High'].iloc[-2] > sell_frame['upperband'].iloc[-2] > sell_frame['Low'].iloc[-2] >
           sell_frame['middleband'].iloc[-2]) and

          (sell_frame['adx_line'].iloc[-2] < 35)):

        print('bollinger band sell G and R cut thru ')
        return True

    # [-6]R [-5, -4, -3]G [-2]R AND ALL ARE BTW MID-B AND UPPER-B AND ADX > 25
    elif (
            (sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
            # [-6]R
            (sell_frame['upperband'].iloc[-6] > sell_frame['High'].iloc[-6] > sell_frame['Low'].iloc[-6] >
             sell_frame['middleband'].iloc[-6]) and
            # [-5]G
            (sell_frame['upperband'].iloc[-5] > sell_frame['High'].iloc[-5] > sell_frame['Low'].iloc[-5] >
             sell_frame['middleband'].iloc[-5]) and
            # [-4]G
            (sell_frame['upperband'].iloc[-4] > sell_frame['High'].iloc[-4] > sell_frame['Low'].iloc[-4] >
             sell_frame['middleband'].iloc[-4]) and
            # [-3]R
            (sell_frame['upperband'].iloc[-3] > sell_frame['High'].iloc[-3] > sell_frame['Low'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]) and
            # [-2]R
            (sell_frame['upperband'].iloc[-2] > sell_frame['High'].iloc[-2] > sell_frame['Low'].iloc[-2] >
             sell_frame['middleband'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('bollinger band sell R3GR')
        return True
