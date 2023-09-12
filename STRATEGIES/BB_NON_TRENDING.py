# ********** bollinger band when market is not trending **********

def bollinger_band_buy2(buy_frame):
    # [-3]R AND [-2]G AND [-3] CUTS THRU LOWER BAND BUT LOWER THAN MIDDLE B AND
    # [-2] CUTS THRU LOWER BAND GOING UP AND BUT LOWER THAN MIDDLE B
    if (
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['Open'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and

            (buy_frame['Open'].iloc[-3] > buy_frame['lowerband'].iloc[-3]) and
            (buy_frame['High'].iloc[-3] > buy_frame['lowerband'].iloc[-3]) and
            (buy_frame['Close'].iloc[-3] < buy_frame['lowerband'].iloc[-3]) and
            (buy_frame['Low'].iloc[-3] < buy_frame['lowerband'].iloc[-3]) and

            (buy_frame['High'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and

            (buy_frame['High'].iloc[-2] > buy_frame['lowerband'].iloc[-2]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['lowerband'].iloc[-2]) and
            (buy_frame['Open'].iloc[-2] < buy_frame['lowerband'].iloc[-2]) and
            (buy_frame['Low'].iloc[-2] < buy_frame['lowerband'].iloc[-2]) ):

        print('bollinger band 12 buy, 2 and 3 cut thru going up ')
        return True

    # elif ((buy_frame['lowerband'].iloc[-2] >= buy_frame['Open'].iloc[-2] or
    #        buy_frame['lowerband'].iloc[-2] >= buy_frame['High'].iloc[-2] or
    #        buy_frame['lowerband'].iloc[-2] >= buy_frame['Low'].iloc[-2] or
    #        buy_frame['lowerband'].iloc[-2] >= buy_frame['Close'].iloc[-2]) and
    #
    #       (buy_frame['adx_line'].iloc[-2] < 22) and
    #
    #       not (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
    #            buy_frame['middleband'].iloc[-2])):
    #
    #     print('bollinger band2 buy cut below')
    #     return True



    # [-6]G AND [-5,-4,-3]R AND (MIDDLEBAND < [-6,-5]G < UPPERBAND) AND (MIDDLEBAND < [-5]G < UPPERBAND)
    # AND ([-4]R IS ABOVE OR CUTS THRU MIDDLEBAND) AND ([-3]R IS CUTS THRU OR BELOW MIDDLEBAND)

    elif ((buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and

          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
          (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
          (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

          (buy_frame['middleband'].iloc[-6] < buy_frame['High'].iloc[-6] < buy_frame['upperband'].iloc[-6]) and
          (buy_frame['middleband'].iloc[-6] < buy_frame['Open'].iloc[-6] < buy_frame['upperband'].iloc[-6]) and
          (buy_frame['middleband'].iloc[-6] < buy_frame['Close'].iloc[-6] < buy_frame['upperband'].iloc[-6]) and
          (buy_frame['middleband'].iloc[-6] < buy_frame['Low'].iloc[-6] < buy_frame['upperband'].iloc[-6]) and

          (buy_frame['middleband'].iloc[-5] < buy_frame['High'].iloc[-5] < buy_frame['upperband'].iloc[-5]) and
          (buy_frame['middleband'].iloc[-5] < buy_frame['Open'].iloc[-5] < buy_frame['upperband'].iloc[-5]) and
          (buy_frame['middleband'].iloc[-5] < buy_frame['Close'].iloc[-5] < buy_frame['upperband'].iloc[-5]) and
          (buy_frame['middleband'].iloc[-5] < buy_frame['Low'].iloc[-5] < buy_frame['upperband'].iloc[-5]) and

          (((buy_frame['middleband'].iloc[-4] < buy_frame['High'].iloc[-4] < buy_frame['upperband'].iloc[-4]) and
            (buy_frame['middleband'].iloc[-4] < buy_frame['Open'].iloc[-3] < buy_frame['upperband'].iloc[-4]) and
            (buy_frame['middleband'].iloc[-4] < buy_frame['Close'].iloc[-4] < buy_frame['upperband'].iloc[-4]) and
            (buy_frame['middleband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['upperband'].iloc[-4])) or

           ((buy_frame['middleband'].iloc[-4] < buy_frame['High'].iloc[-4] < buy_frame['upperband'].iloc[-4]) and
            (buy_frame['middleband'].iloc[-4] < buy_frame['Open'].iloc[-4] < buy_frame['upperband'].iloc[-4]) and
            (buy_frame['lowerband'].iloc[-4] < buy_frame['Close'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and
            (buy_frame['lowerband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['middleband'].iloc[-4]))) and

          (((buy_frame['middleband'].iloc[-3] < buy_frame['High'].iloc[-3] < buy_frame['upperband'].iloc[-3]) and
            (buy_frame['middleband'].iloc[-3] < buy_frame['Open'].iloc[-3] <
             buy_frame['upperband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Close'].iloc[-3] <
             buy_frame['middleband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Low'].iloc[-3] <
             buy_frame['middleband'].iloc[-3])) or

           ((buy_frame['lowerband'].iloc[-3] < buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Open'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Close'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['lowerband'].iloc[-3] < buy_frame['Low'].iloc[-3] < buy_frame['middleband'].iloc[-3]))) and

          (buy_frame['adx_line'].iloc[-2] < 25)):

        print('bollinger band2 non-trending buy 8 like ma')
        return True

    # [-6]R AND IS BTW MID-B AND UPPER-B AND [-5,-4]G AND IS BTW MID-B AND UPPER-B AND ([-3]G IS BTW MID-B AND UPPER-B OR CUT
    # THRU UPPER-B) AND ([-2]G CUT THRU UPPER-B OR ABOVE UPPER-B) AND ADX IS < 25
    elif (
            (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-6]R IS BTW MID-B AND UPPER-B we are using 'low and high' as the parameter here think hybee
            (buy_frame['middleband'].iloc[-6] < buy_frame['Low'].iloc[-6] < buy_frame['High'].iloc[-6] <
             buy_frame['upperband'].iloc[-6]) and

            # [-5]G IS BTW MID-B AND UPPER-B we are using 'low and high' as the parameter here think hybee
            (buy_frame['middleband'].iloc[-5] < buy_frame['Low'].iloc[-5] < buy_frame['High'].iloc[-5] <
             buy_frame['upperband'].iloc[-5]) and

            # [-4]G IS BTW MID-B AND UPPER-B we are using 'low' as the parameter here think hybee
            (buy_frame['middleband'].iloc[-4] < buy_frame['Low'].iloc[-4] < buy_frame['High'].iloc[-4] <
             buy_frame['upperband'].iloc[-4]) and

            # [-3]G IS BTW MID-B AND UPPER-B we are using 'low' as the parameter here think hybee
            ((buy_frame['middleband'].iloc[-3] < buy_frame['Low'].iloc[-3] < buy_frame['High'].iloc[-3] <
             buy_frame['upperband'].iloc[-3]) or

            # and [-3]G cut thru upper-B
            ((buy_frame['Close'].iloc[-3] > buy_frame['upperband'].iloc[-3]) and
            (buy_frame['High'].iloc[-3] > buy_frame['upperband'].iloc[-3]) and
            (buy_frame['Open'].iloc[-3] < buy_frame['upperband'].iloc[-3]) and
            (buy_frame['Low'].iloc[-3] < buy_frame['upperband'].iloc[-3]))) and

            # and [-2]G cut thru upper-B
            (((buy_frame['Close'].iloc[-2] > buy_frame['upperband'].iloc[-2]) and
            (buy_frame['High'].iloc[-2] > buy_frame['upperband'].iloc[-2]) and
            (buy_frame['Open'].iloc[-2] < buy_frame['upperband'].iloc[-2]) and
            (buy_frame['Low'].iloc[-2] < buy_frame['upperband'].iloc[-2])) or

            # [-2]G IS ABOVE UPPER-B we are using 'low' as the parameter here think hybee
            (buy_frame['Low'].iloc[-2] > buy_frame['upperband'].iloc[-2])) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('bollinger band 13 buy ')
        return True

    # [-4]R AND [-3, -2]G AND [-4]R AND [-3] G BETWEEN LOWERBAND AND MIDDLEBAND, AND
    # [-2]G CUTS THRU MIDDLE BAND GOING UP
    elif (
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-4] IS R
            (buy_frame['Open'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and
            (buy_frame['High'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and
            (buy_frame['Close'].iloc[-4] > buy_frame['lowerband'].iloc[-4]) and
            (buy_frame['Low'].iloc[-4] > buy_frame['lowerband'].iloc[-4]) and
            # [-3] IS G
            (buy_frame['Close'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['lowerband'].iloc[-3]) and
            (buy_frame['Low'].iloc[-3] > buy_frame['lowerband'].iloc[-3]) and

             # [-2] IS GREEN
             (buy_frame['High'].iloc[-2] < buy_frame['upperband'].iloc[-2]) and
             (buy_frame['Close'].iloc[-2] < buy_frame['upperband'].iloc[-2]) and

            (buy_frame['High'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['middleband'].iloc[-2]) and

             (buy_frame['Open'].iloc[-2] < buy_frame['middleband'].iloc[-2]) and
             (buy_frame['Low'].iloc[-2] < buy_frame['middleband'].iloc[-2]) and

            (buy_frame['Open'].iloc[-2] > buy_frame['lowerband'].iloc[-2]) and
            (buy_frame['Low'].iloc[-2] > buy_frame['lowerband'].iloc[-2])):
        print('bollinger band 3c buy, 4 and 3 and 2 cut thru going up ')
        return True

def bollinger_band_sell2(sell_frame):
    # [-3]G AND [-2]R AND [-3] CUTS THRU UPPER BAND BUT ABOVE THAN MIDDLE B  AND
    # [-2] CUTS THRU UPPER BAND BUT ABOVE THAN MIDDLE B GOING DOWN

    if (
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['High'].iloc[-3] > sell_frame['upperband'].iloc[-3]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['upperband'].iloc[-3]) and
            (sell_frame['Open'].iloc[-3] < sell_frame['upperband'].iloc[-3]) and
            (sell_frame['Low'].iloc[-3] < sell_frame['upperband'].iloc[-3]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and
            (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and

            (sell_frame['High'].iloc[-2] > sell_frame['upperband'].iloc[-2]) and
            (sell_frame['Close'].iloc[-2] > sell_frame['upperband'].iloc[-2]) and
            (sell_frame['Open'].iloc[-2] < sell_frame['upperband'].iloc[-2]) and
            (sell_frame['Low'].iloc[-2] < sell_frame['upperband'].iloc[-2]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and
            (sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2]) ):

        print('bollinger band 12 sell, , 2 and 3 cut thru going down')
        return True

    # elif ((sell_frame['upperband'].iloc[-2] <= sell_frame['Open'].iloc[-2] or
    #        sell_frame['upperband'].iloc[-2] <= sell_frame['High'].iloc[-2] or
    #        sell_frame['upperband'].iloc[-2] <= sell_frame['Low'].iloc[-2] or
    #        sell_frame['upperband'].iloc[-2] <= sell_frame['Close'].iloc[-2]) and
    #
    #       (sell_frame['adx_line'].iloc[-2] < 22) and
    #
    #       not (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
    #            sell_frame['middleband'].iloc[-2])):
    #
    #     print('bollinger band2 sell cut above')
    #     return True

    # [-6]R AND [-5,-4,-3]G AND (LOWERBAND < [-6]R < MIDDLEBAND) AND (LOWERBAND < [-5]G < MIDDLEBAND)
    # AND ([-4]G IS BELOW OR CUTS THRU MIDDLEBAND) AND ([-3]G IS CUTS OR ABOVE THRU MIDDLEBAND)

    elif ((sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and

          (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
          (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
          (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

          (sell_frame['lowerband'].iloc[-6] < sell_frame['High'].iloc[-6] <
           sell_frame['middleband'].iloc[-6]) and
          (sell_frame['lowerband'].iloc[-6] < sell_frame['Open'].iloc[-6] <
           sell_frame['middleband'].iloc[-6]) and
          (sell_frame['lowerband'].iloc[-6] < sell_frame['Close'].iloc[-6] <
           sell_frame['middleband'].iloc[-6]) and
          (sell_frame['lowerband'].iloc[-6] < sell_frame['Low'].iloc[-6] <
           sell_frame['middleband'].iloc[-6]) and

          (sell_frame['lowerband'].iloc[-5] < sell_frame['Low'].iloc[-5] <
           sell_frame['middleband'].iloc[-5]) and
          (sell_frame['lowerband'].iloc[-5] < sell_frame['Open'].iloc[-5] <
           sell_frame['middleband'].iloc[-5]) and
          (sell_frame['lowerband'].iloc[-5] < sell_frame['Close'].iloc[-5] <
           sell_frame['middleband'].iloc[-5]) and
          (sell_frame['lowerband'].iloc[-5] < sell_frame['High'].iloc[-5] <
           sell_frame['middleband'].iloc[-5]) and

          (((sell_frame['lowerband'].iloc[-4] < sell_frame['Low'].iloc[-4] <
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['Open'].iloc[-4] <
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['Close'].iloc[-4] <
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['High'].iloc[-4] <
             sell_frame['middleband'].iloc[-4])) or

           ((sell_frame['lowerband'].iloc[-4] < sell_frame['Low'].iloc[-4] <
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['Open'].iloc[-4] <
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['Close'].iloc[-4] >
             sell_frame['middleband'].iloc[-4]) and
            (sell_frame['lowerband'].iloc[-4] < sell_frame['High'].iloc[-4] >
             sell_frame['middleband'].iloc[-4]))) and

          (((sell_frame['lowerband'].iloc[-3] < sell_frame['Low'].iloc[-3] <
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['Open'].iloc[-3] <
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['Close'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['High'].iloc[-3] >
             sell_frame['middleband'].iloc[-3])) or

           ((sell_frame['lowerband'].iloc[-3] < sell_frame['Low'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['Open'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['Close'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]) and
            (sell_frame['lowerband'].iloc[-3] < sell_frame['High'].iloc[-3] >
             sell_frame['middleband'].iloc[-3]))) and

          (sell_frame['adx_line'].iloc[-2] < 25)):

        print('bollinger band2 non-trending sell 8 like ma')
        return True

        # [-6]G AND IS BTW MID-B AND LOWER-B AND [-5,-4]R AND IS BTW MID-B AND LOWER-B AND ([-3]R IS BTW MID-B AND
        # LOWER-B OR CUT THRU LOWER-B) AND ([-2]R CUT THRU LOWER-B OR BELOW LOWER-B) AND ADX IS < 25
    elif (
            (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

            (sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-6]G IS BTW MID-B AND LOWER-B we are using 'high and low' as the parameter here think hybee
            (sell_frame['middleband'].iloc[-6] > sell_frame['High'].iloc[-6] > sell_frame['Low'].iloc[-6] >
             sell_frame['lowerband'].iloc[-6]) and

            # [-5]R IS BTW MID-B AND LOWER-B we are using 'high and low' as the parameter here think hybee
            (sell_frame['middleband'].iloc[-5] > sell_frame['High'].iloc[-5] > sell_frame['Low'].iloc[-5] >
             sell_frame['lowerband'].iloc[-5]) and

            # [-4]R IS BTW MID-B AND UPPER-B we are using 'high and low' as the parameter here think hybee
            (sell_frame['middleband'].iloc[-4] > sell_frame['High'].iloc[-4] > sell_frame['Low'].iloc[-4] >
             sell_frame['lowerband'].iloc[-4]) and

            # [-3]R IS BTW MID-B AND UPPER-B we are using 'high and low' as the parameter here think hybee
            (((sell_frame['middleband'].iloc[-3] > sell_frame['High'].iloc[-3] > sell_frame['Low'].iloc[-3] >
               sell_frame['lowerband'].iloc[-3])) or

             # and [-3]R cut thru lower-B
             ((sell_frame['High'].iloc[-3] > sell_frame['lowerband'].iloc[-3]) and
              (sell_frame['Open'].iloc[-3] > sell_frame['lowerband'].iloc[-3]) and
              (sell_frame['Close'].iloc[-3] < sell_frame['lowerband'].iloc[-3]) and
              (sell_frame['Low'].iloc[-3] < sell_frame['lowerband'].iloc[-3]))) and

            # and [-2]R cut thru lower-B
            (((sell_frame['High'].iloc[-2] > sell_frame['lowerband'].iloc[-2]) and
              (sell_frame['Open'].iloc[-2] > sell_frame['lowerband'].iloc[-2]) and
              (sell_frame['Close'].iloc[-2] < sell_frame['lowerband'].iloc[-2]) and
              (sell_frame['Low'].iloc[-2] < sell_frame['lowerband'].iloc[-2])) or

             # [-2]R IS BELOW LOWER-B we are using 'high' as the parameter here think hybee
             (sell_frame['High'].iloc[-2] > sell_frame['upperband'].iloc[-2])) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('bollinger band 13 sell ')
        return True

    # [-4]G AND [-3, -2]R AND [-4]G AND [-3]R BETWEEN UPPERBAND AND MIDDLEBAND, AND
    # [-2]G CUTS THRU MIDDLE BAND GOING DOWN
    elif (
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
            # [-4] IS G
            (sell_frame['High'].iloc[-4] < sell_frame['upperband'].iloc[-4]) and
            (sell_frame['Close'].iloc[-4] < sell_frame['upperband'].iloc[-4]) and
            (sell_frame['Open'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and
            (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and

            # [-3] IS R
            (sell_frame['Open'].iloc[-3] < sell_frame['upperband'].iloc[-3]) and
            (sell_frame['High'].iloc[-3] < sell_frame['upperband'].iloc[-3]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and
            (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and

            # [-2] IS R
            (sell_frame['High'].iloc[-2] < sell_frame['upperband'].iloc[-2]) and
            (sell_frame['Open'].iloc[-2] < sell_frame['upperband'].iloc[-2]) and

            (sell_frame['High'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and

            (sell_frame['Close'].iloc[-2] < sell_frame['middleband'].iloc[-2]) and
            (sell_frame['Low'].iloc[-2] < sell_frame['middleband'].iloc[-2]) and

            (sell_frame['Close'].iloc[-2] > sell_frame['lowerband'].iloc[-2]) and
            (sell_frame['Low'].iloc[-2] > sell_frame['lowerband'].iloc[-2])):
        print('bollinger band 3c sell, 4 and 3 and 2 cut thru going down ')
        return True