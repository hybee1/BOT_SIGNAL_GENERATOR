''' LIST OF METHODS
1. sell_out_from_bb(buy_frame):
2. sell_out_dmi(buy_frame):
3. ma_sell_out(buy_frame, sell_frame, sell_stop_loss_variable):
4. volume_sell_out(buy_frame):
'''

from GENERAL.GENERAL import (doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green, dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, hanging_Man_Green, hanging_Man_Red,
                             inverted_Hammer_Green, inverted_Hammer_Red, spinning_Top_Green, spinning_Top_Red,
                             shooting_Star_Green, shooting_Star_Red, manual_Hammer, manual_Inverted_Hammer)


# SIGNAL FROM BOLLINGER BAND
def sell_out_from_bb(sell_frame):
    if ((sell_frame['upperband'][-2] <= sell_frame['Open'][-2] or
         sell_frame['upperband'][-2] <= sell_frame['High'][-2] or
         sell_frame['upperband'][-2] <= sell_frame['Low'][-2] or
         sell_frame['upperband'][-2] <= sell_frame['Close'][-2]) and

            (25 < sell_frame['adx_line'][-3] > sell_frame['adx_line'][-2] < 25)):

        print('SIGNAL FROM MARKET TRENDING, WE IN A BUY TRADE AND PRICE TOUCHES '
              'THE UPPER BAND')
        return True

    elif ((-sell_frame['Open'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['High'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['Low'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10 or
           -sell_frame['Close'].iloc[-2] + sell_frame['upperband'].iloc[-2] <= 10) and

          (25 < sell_frame['adx_line'][-4] > sell_frame['adx_line'][-3] >
           sell_frame['adx_line'][-2] < 25)):

        print('SIGNAL FROM MARKET TRENDING, WE IN A BUY TRADE AND PRICE DIFF '
              'THE UPPER BAND')
        return True


# END SIGNAL FROM BOLLINGER BAND

# SELL OUT SIGNAL FROM DMI WHEN DMI CROSS ABOVE PLUS_DI WHERE PLUS_DI > MINUS_DI
def sell_out_dmi(sell_frame):
    if ((sell_frame['plus_DI'].iloc[-2] > sell_frame['minus_DI'].iloc[-2] and
         sell_frame['plus_DI'].iloc[-3] > sell_frame['minus_DI'].iloc[-3] and
         sell_frame['plus_DI'].iloc[-4] > sell_frame['minus_DI'].iloc[-4]) and

            (sell_frame['plus_DI'].iloc[-4] > sell_frame['dmi_line'].iloc[-4] and
             sell_frame['plus_DI'].iloc[-3] > sell_frame['dmi_line'].iloc[-3] and
             sell_frame['plus_DI'].iloc[-2] < sell_frame['dmi_line'].iloc[-2]) and

            (sell_frame['dmi_line'].iloc[-2] > sell_frame['minus_DI'].iloc[-2] and
             sell_frame['dmi_line'].iloc[-3] > sell_frame['minus_DI'].iloc[-3] and
             sell_frame['dmi_line'].iloc[-4] > sell_frame['minus_DI'].iloc[-4]) and

            (sell_frame['plus_DI'].iloc[-2] > 39) and

            (sell_frame['plus_DI'].iloc[-2] - sell_frame['minus_DI'].iloc[-2] > 22)):
        print('SELL OUT FROM DMI SELL 1')
        return True

    # SELL OUT SIGNAL FROM DMI WHEN DMI CROSS BELOW MINUS_DI WHERE PLUS_DI > MINUS_DI
    elif ((sell_frame['plus_DI'].iloc[-2] > sell_frame['minus_DI'].iloc[-2] and
           sell_frame['plus_DI'].iloc[-3] > sell_frame['plus_DI'].iloc[-3] and
           sell_frame['plus_DI'].iloc[-4] > sell_frame['plus_DI'].iloc[-4]) and

          (sell_frame['plus_DI'].iloc[-4] > sell_frame['dmi_line'].iloc[-4] and
           sell_frame['plus_DI'].iloc[-3] > sell_frame['dmi_line'].iloc[-3] and
           sell_frame['plus_DI'].iloc[-2] > sell_frame['dmi_line'].iloc[-2]) and

          (sell_frame['dmi_line'].iloc[-2] > sell_frame['minus_DI'].iloc[-2] and
           sell_frame['dmi_line'].iloc[-3] > sell_frame['minus_DI'].iloc[-3] and
           sell_frame['dmi_line'].iloc[-4] < sell_frame['minus_DI'].iloc[-4])):

        print('SELL OUT FROM DMI SELL 2')
        return True


# END SELL OUT SIGNAL FROM DMI WHEN DMI CROSS ABOVE PLUS_DI WHERE PLUS_DI > MINUS_DI

# MOVING AVERAGE SELL OUT
def ma_sell_out(buy_frame, sell_frame, buy_stop_loss_variable):
    # WE ARE IN BUY POSITION SO ARE TRYING TO LOOK FOR BUY OUT CONDITIONS
    # [-2] IS R AND [-2] OPEN IS > [-2] MA_20 AND [-2] CLOSE IS < [-2] MA_20
    # NEW BELOW
    # [-3, -2] IS R AND [-3]R > MA_20 AND [-3] AND [-2] OPEN IS > [-2] MA_20 AND [-2] CLOSE IS < [-2] MA_20
    #
    if ((sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            (sell_frame['Close'].iloc[-3] > sell_frame['ma_20'].iloc[-3]) and

            (sell_frame['Open'].iloc[-2] > sell_frame['ma_20'].iloc[-2]) and
            (sell_frame['Close'].iloc[-2] < sell_frame['ma_20'].iloc[-2])):

        print('SELL OUT SIGNAL FROM MA SELL OUT DOUBLE R CUT THRU')
        return True

    # CONDITION [-3] IS G AND [-2] IS R AND ( ([-3]CLOSE - HALF OF STOP LOSS) > [-2] CLOSE)
    elif ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

          (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

          (buy_frame['Close'].iloc[-3] - int(buy_stop_loss_variable / 2) > sell_frame['Close'].iloc[-2])):

        print('SELL OUT SIGNAL FROM MA SELL OUT 2')
        return True

    # CONDITION [-3] IS R AND [-2] IS R
    elif ((sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

          (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and

          (sell_frame['Close'].iloc[-3] - int(buy_stop_loss_variable / 2) > buy_frame['Close'].iloc[
              -2])):

        print('SELL OUT SIGNAL FROM MA SELL OUT 3')
        return True


# END MOVING AVERAGE SELL OUT

# VOLUME SELL OUT
def volume_sell_out(sell_frame):
    if (sell_frame['Volume'].iloc[-2] > 7500 and
            sell_frame['Close'].iloc[-1] < sell_frame['Close'].iloc[-2]):
        print('WE ARE IN A LONG POSITION AND THERE IS A SURGE IN VOLUME IN THE OPPOSITE '
              'DIRECTION A TEMP CONFIRMATION, BUT WE ARE GETTING OUT ANYWAYS')

        return True


def trend_cand_patn_sell_out(sell_frame):
    # PRICE HAS BEEN GOING UP AND [-3]G IS SHOOTING STAR [-2]G IS GRAVESTONE AT ADX > 25
    if (
            # PRICE HAS BEEN GOING UP
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # [-3]G IS SHOOTING STAR
            ((sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and shooting_Star_Green(sell_frame, 3)) and

            # [-2]G IS GRAVESTONE
            ((sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and gravestone_doji_Green(sell_frame, 2)) and

            (sell_frame['adx_line'].iloc[-2] > 25)):
        print('TRENDING CAND_PATN SELL_OUT 1 ')

        return True


# END VOLUME SELL OUT


def trending_sell_exit(buy_frame, sell_frame, buy_stop_loss_variable):
    if sell_out_from_bb(sell_frame):
        return True

    elif sell_out_dmi(sell_frame):
        return True

    elif ma_sell_out(buy_frame, sell_frame, buy_stop_loss_variable):
        return True

    elif volume_sell_out(sell_frame):
        return True

    elif trend_cand_patn_sell_out(sell_frame):
        return True
