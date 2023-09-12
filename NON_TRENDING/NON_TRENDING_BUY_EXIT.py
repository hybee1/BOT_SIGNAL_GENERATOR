''' LIST OF METHODS
1. buy_out_from_bb2(buy_frame):
2. volume_buy_out(buy_frame):
3. cand_patn_buy_out(buy_frame):
'''

from GENERAL.GENERAL import (doji_Green, doji_Red, doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green, dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, harami_Green, harami_Red, hanging_Man_Green,
                             hanging_Man_Red, inverted_Hammer_Green, inverted_Hammer_Red, marubozu_Green,
                             marubozu_Red, spinning_Top_Green, spinning_Top_Red, shooting_Star_Green,
                             shooting_Star_Red)


def buy_out_from_bb2(buy_frame):
    if ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['High'].iloc[-5] >= buy_frame['upperband'].iloc[-5] or
             buy_frame['Low'].iloc[-5] >= buy_frame['upperband'].iloc[-5]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):
        print('WE ARE IN A SHORT POSITION AND PRICE IS TOUCHING OR ABOVE UPPERBAND, A RED AND '
              'THREE GREEN IN UPWARD DIRECTION.. ANYWAYS WE ARE GETTING OUT')

        return True
    elif (
          #   (buy_frame['Open'].iloc[-2] < buy_frame['lowerband'].iloc[-2] or
          #  buy_frame['High'].iloc[-2] < buy_frame['lowerband'].iloc[-2] or
          #  buy_frame['Low'].iloc[-2] < buy_frame['lowerband'].iloc[-2] or
          #  buy_frame['Close'].iloc[-2] < buy_frame['lowerband'].iloc[-2]) and
          # not (buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] < buy_frame['adx_line'].iloc[-2])):

        # NEW CODE
         buy_frame['Low'].iloc[-2] < buy_frame['lowerband'].iloc[-2] and
         not (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
              buy_frame['middleband'].iloc[-2])):

        print('buy out non-trending candle price touch lower B or below lower B')
        return True

    elif (
           #  (buy_frame['Open'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           # buy_frame['High'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           # buy_frame['Low'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           # buy_frame['Close'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10) and
           # not (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
           #       buy_frame['middleband'].iloc[-2])):

        # NEW CODE
         buy_frame['Low'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 and

          (buy_frame['adx_line'].iloc[-2] < 22) and

          not (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
               buy_frame['middleband'].iloc[-2])):

        print('bollinger band2 buy-out diff of 10')
        return True


# VOLUME BUY OUT
def volume_buy_out(buy_frame):
    if (buy_frame['Volume'].iloc[-2] > 7500 and buy_frame['Close'].iloc[-1] >
            buy_frame['Close'].iloc[-2]):
        print('WE ARE IN A SHORT POSITION AND THERE IS A SURGE IN VOLUME IN THE OPPOSITE '
              'DIRECTION A TEMP CONFIRMATION, BUT WE ARE GETTING OUT ANYWAYS')

        return True

    return False


def non_trend_cand_patn_buy_out(buy_frame):
    # PRICE HAS BEEN GOING DOWN [3]R IS HAMMER AND [-2]R IS HAMMER AT ADX < 25
    if (
            # PRICE HAS BEEN GOING DOWN THAT IS [-5, -4]
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

          ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and hammer_Red(buy_frame, 3)) and

          # [-2]R
          ((buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and hammer_Red(buy_frame, 3)) and

          (buy_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN BUY_OUT 1 ')
        return True

    # [-5]G [-4]R, [-3]G BEARISH HARAMI WHICH IS GREEN AND [-2]R AND ADX < 25
    elif (
        # [-5]G
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

            # [-4]R
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            # [-3]G
            ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and harami_Green(buy_frame, 3)) and

            # [-2]R
            (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN BUY_OUT 2 ')
        return True

    return False

# END VOLUME BUY OUT


def non_trending_bb_buy_exit(buy_frame):
    if buy_out_from_bb2(buy_frame):
        return True

    elif volume_buy_out(buy_frame):
        return True

    elif non_trend_cand_patn_buy_out(buy_frame):
        return True