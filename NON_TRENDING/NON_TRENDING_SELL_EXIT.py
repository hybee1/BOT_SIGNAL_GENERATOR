''' LIST OF METHODS
1. sell_out_from_bb(sell_frame):
2. volume_sell_out(sell_frame):
3. cand_patn_sell_out(sell_frame):
'''
from GENERAL.GENERAL import (doji_Green, doji_Red, doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green, dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, harami_Green, harami_Red, hanging_Man_Green,
                             hanging_Man_Red, inverted_Hammer_Green, inverted_Hammer_Red, marubozu_Green,
                             marubozu_Red, spinning_Top_Green, spinning_Top_Red, shooting_Star_Green,
                             shooting_Star_Red)


# SIGNAL FROM BOLLINGER BAND
def sell_out_from_bb2(sell_frame):
    if ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['High'].iloc[-5] <= sell_frame['lowerband'].iloc[-5] or
             sell_frame['Low'].iloc[-5] <= sell_frame['lowerband'].iloc[-5]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):
        print('WE ARE IN A LONG POSITION AND PRICE IS TOUCHING OR BELOW LOWERBAND, A GREEN AND '
              'THREE RED IN DOWN-WARD DIRECTION.. ANYWAYS WE ARE GETTING OUT')

        return True
    elif (
      # (sell_frame['Open'].iloc[-2] > sell_frame['upperband'].iloc[-2] or
      # sell_frame['High'].iloc[-2] > sell_frame['upperband'].iloc[-2] or
      # sell_frame['Low'].iloc[-2] > sell_frame['upperband'].iloc[-2] or
      # sell_frame['Close'].iloc[-2] > sell_frame['upperband'].iloc[-2]) and
      # not (sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] < sell_frame['adx_line'].iloc[-2])):

        # NEW CODE
         sell_frame['High'].iloc[-2] > sell_frame['upperband'].iloc[-2] and
         not (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
              sell_frame['middleband'].iloc[-2])):

        print('sell out non-trending candle price touch upper B or above upper B')
        return True

    elif (
           #  (-sell_frame['Open'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           # -sell_frame['High'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           # -sell_frame['Low'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           # -sell_frame['Close'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10) and
           # not (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
           #                sell_frame['middleband'].iloc[-2])):

        # NEW CODE
        -sell_frame['High'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 and

          (sell_frame['adx_line'].iloc[-2] < 22) and

          not (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
               sell_frame['middleband'].iloc[-2])):

        print('bollinger band2 sell-out diff of 10 above')
        return True


# VOLUME SELL OUT
def volume_sell_out(sell_frame):
    if (sell_frame['Volume'].iloc[-2] > 7500 and sell_frame['Close'].iloc[-1] <
            sell_frame['Close'].iloc[-2]):
        print('WE ARE IN A LONG POSITION AND THERE IS A SURGE IN VOLUME IN THE OPPOSITE '
              'DIRECTION A TEMP CONFIRMATION, BUT WE ARE GETTING OUT ANYWAYS')

        return True


def non_trend_cand_patn_sell_out(sell_frame):
    # [3]G GRAVESTONE DOJI THAT IS G AND [-2]R AT ADX < 25
    if (
            ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and gravestone_doji_Green(sell_frame, 3)) and

            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN SELL_OUT 1 ')
        return True

    # PRICE HAS BEEN RISING [-5, -4]G AND [-3]R IS GRAVESTONE DOJI AND [-2]R AT ADX < 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]R
            ((sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and gravestone_doji_Red(sell_frame, 3)) and
            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN SELL_OUT 2')
        return True

    # PRICE HAS BEEN RISING [-5, -4]G AND [-3]G IS DRAGONFLY DOJI AND [-2]R AT ADX < 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and dragonfly_Doji_Green(sell_frame, 3)) and
            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN SELL_OUT 3')
        return True

    # PRICE HAS BEEN RISING [-5, -4]G AND [-3]R IS HARAMI WHICH IS RED AND [-2]R AT ADX < 25
    elif (
            # [-5]G
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
            # [-4]G
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G
            ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and harami_Red(sell_frame, 3)) and
            # [-2]R
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('NON_TRENDING CAND_PATN SELL_OUT 4')
        return True


# END VOLUME SELL OUT


def non_trending_bb_sell_exit(sell_frame):
    if sell_out_from_bb2(sell_frame):
        return True

    elif volume_sell_out(sell_frame):
        return True

    elif non_trend_cand_patn_sell_out(sell_frame):
        return True
