''' LIST OF METHODS
1. buy_out_from_bb(buy_frame):
2. boy_out_dmi(buy_frame):
3. ma_buy_out(buy_frame, sell_frame, sell_stop_loss_variable):
4. volume_buy_out(buy_frame):
'''
from GENERAL.GENERAL import (doji_Star_Green, doji_Star_Red, dragonfly_Doji_Green, dragonfly_Doji_Red,
                             engulfing_Green, engulfing_Red, gravestone_doji_Green, gravestone_doji_Red,
                             hammer_Green, hammer_Red, hanging_Man_Green, hanging_Man_Red,
                             inverted_Hammer_Green, inverted_Hammer_Red, spinning_Top_Green, spinning_Top_Red,
                             shooting_Star_Green, shooting_Star_Red, manual_Hammer, manual_Inverted_Hammer)


# SIGNAL BUY OUT FROM BOLLINGER BAND
def buy_out_from_bb(buy_frame):
    if ((buy_frame['lowerband'][-2] >= buy_frame['Open'][-2] or
         buy_frame['lowerband'][-2] >= buy_frame['High'][-2] or
         buy_frame['lowerband'][-2] >= buy_frame['Low'][-2] or
         buy_frame['lowerband'][-2] >= buy_frame['Close'][-2]) and

            (25 < buy_frame['adx_line'][-3] > buy_frame['adx_line'][-2] < 25)):

        print('SIGNAL FROM MARKET TRENDING, WE IN A SELL TRADE AND PRICE TOUCHES '
              'THE LOWER BAND')
        # fut_buy_to_exit_trade(symbol1, quantity, sell_entry_price1)
        return True

    elif ((buy_frame['Open'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['High'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['Low'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10 or
           buy_frame['Close'].iloc[-2] - buy_frame['lowerband'].iloc[-2] <= 10) and

          (25 < buy_frame['adx_line'][-4] > buy_frame['adx_line'][-3] >
           buy_frame['adx_line'][-2] < 25)):

        print('SIGNAL FROM MARKET TRENDING, WE IN A SELL TRADE AND PRICE DIFF '
              'THE LOWER BAND')
        # fut_buy_to_exit_trade(symbol1, quantity, sell_entry_price1)
        return True


# END SIGNAL BUY OUT FROM BOLLINGER BAND

# BUY OUT SIGNAL FROM DMI WHEN DMI CROSS ABOVE MINUS_DI WHERE MINUS_DI > PLUS_DI
def boy_out_dmi(buy_frame):
    if ((buy_frame['minus_DI'].iloc[-2] > buy_frame['plus_DI'].iloc[-2] and
         buy_frame['minus_DI'].iloc[-3] > buy_frame['plus_DI'].iloc[-3] and
         buy_frame['minus_DI'].iloc[-4] > buy_frame['plus_DI'].iloc[-4]) and

            (buy_frame['minus_DI'].iloc[-4] > buy_frame['dmi_line'].iloc[-4] and
             buy_frame['minus_DI'].iloc[-3] > buy_frame['dmi_line'].iloc[-3] and
             buy_frame['minus_DI'].iloc[-2] < buy_frame['dmi_line'].iloc[-2]) and

            (buy_frame['dmi_line'].iloc[-2] > buy_frame['plus_DI'].iloc[-2] and
             buy_frame['dmi_line'].iloc[-3] > buy_frame['plus_DI'].iloc[-3] and
             buy_frame['dmi_line'].iloc[-4] > buy_frame['plus_DI'].iloc[-4]) and

            (buy_frame['minus_DI'].iloc[-2] > 39) and

            (buy_frame['minus_DI'].iloc[-2] - buy_frame['plus_DI'].iloc[-2] > 22)):

        print('BUY OUT FROM DMI BUY 1')
        # fut_buy_to_exit_trade(symbol1, quantity, sell_entry_price1)
        return True

    # BUY OUT SIGNAL FROM DMI WHEN DMI CROSS BELOW PLUS_DI WHERE MINUS_DI > PLUS_DI
    elif ((buy_frame['minus_DI'].iloc[-2] > buy_frame['plus_DI'].iloc[-2] and
           buy_frame['minus_DI'].iloc[-3] > buy_frame['plus_DI'].iloc[-3] and
           buy_frame['minus_DI'].iloc[-4] > buy_frame['plus_DI'].iloc[-4]) and

          (buy_frame['minus_DI'].iloc[-4] > buy_frame['dmi_line'].iloc[-4] and
           buy_frame['minus_DI'].iloc[-3] > buy_frame['dmi_line'].iloc[-3] and
           buy_frame['minus_DI'].iloc[-2] > buy_frame['dmi_line'].iloc[-2]) and

          (buy_frame['dmi_line'].iloc[-2] > buy_frame['plus_DI'].iloc[-2] and
           buy_frame['dmi_line'].iloc[-3] > buy_frame['plus_DI'].iloc[-3] and
           buy_frame['dmi_line'].iloc[-4] < buy_frame['plus_DI'].iloc[-4])):

        print('BUY OUT FROM DMI BUY 2')
        # fut_buy_to_exit_trade(symbol1, quantity, sell_entry_price1)
        return True


# END BUY OUT SIGNAL FROM DMI WHEN DMI CROSS ABOVE MINUS_DI WHERE MINUS_DI > PLUS_DI

# MOVING AVERAGE BUY OUT
def ma_buy_out(buy_frame, sell_frame, sell_stop_loss_variable):
    # WE ARE IN SELL POSITION SO ARE TRYING TO LOOK FOR BUY OUT CONDITIONS
    # [-2] IS G AND [-2] OPEN IS < [-2] MA_20 AND [-2] CLOSE IS > [-2] MA_20 === ORIGINAL
    # NEW BELOW
    # [-3, -2] IS G AND [-3]G < MA_20 AND [-3] AND [-2] OPEN IS < [-2] MA_20 AND [-2] CLOSE IS > [-2] MA_20
    #
    if ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            (buy_frame['Close'].iloc[-3] < buy_frame['ma_20'].iloc[-3]) and

            (buy_frame['Open'].iloc[-2] < buy_frame['ma_20'].iloc[-2]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['ma_20'].iloc[-2])):

        print('BUY OUT SIGNAL FROM MA BUY OUT DOUBLE G CUT THRU')
        return True

    # CONDITION [-3] IS R AND [-2] IS G
    elif ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

          (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['Close'].iloc[-3] + int(sell_stop_loss_variable / 2) < buy_frame['Close'].iloc[
              -2])):

        print('BUY OUT SIGNAL FROM MA BUY OUT 2')
        return True

    # CONDITION [-3] IS G AND [-2] IS G
    elif ((buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and

          (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['Close'].iloc[-3] + int(sell_stop_loss_variable / 2) < buy_frame['Close'].iloc[
              -2])):

        print('BUY OUT SIGNAL FROM MA BUY OUT 3')
        return True


# END MOVING AVERAGE BUY OUT

# VOLUME BUY OUT
def volume_buy_out(buy_frame):
    if (buy_frame['Volume'].iloc[-2] > 7500 and buy_frame['Close'].iloc[-1] >
            buy_frame['Close'].iloc[-2]):
        print('WE ARE IN A SHORT POSITION AND THERE IS A SURGE IN VOLUME IN THE OPPOSITE '
              'DIRECTION A TEMP CONFIRMATION, BUT WE ARE GETTING OUT ANYWAYS')

        return True


def trend_cand_patn_buy_out(buy_frame):
    # [-5]R [-4]G [-3]G [-2]G IS GRAVESTONE AT ADX > 25
    if (
            # [-5]R
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and
            # [-4]G
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            # [-3]G
            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            # [-2]G
            ((buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and gravestone_doji_Green(buy_frame, 4)) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('TRENDING CAND_PATN BUY_OUT 1 ')

        return True

    # PRICE HAS BEEN GOING DOWN AND [-3]R IS SPINNING TOP [-2]G AT ADX > 25
    elif (
          # [-5]R
          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

          # [-4]R
          (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

          # [-3]R IS SPINNING TOP
          ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and spinning_Top_Red(buy_frame, 3)) and

          # [-2]G
          (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

          (buy_frame['adx_line'].iloc[-2] > 25)):

        print('TRENDING CAND_PATN BUY_OUT 2 ')

        return True

    # PRICE HAS BEEN GOING DOWN AND [-3]R IS INVERTED HAMMER [-2]R IS SPINNING TOP AT ADX > 25
    elif (
          # [-5]R
          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

          # [-4]R
          (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

          # [-3]R IS INVERTED HAMMER
          ((buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and inverted_Hammer_Red(buy_frame, 3)) and

          # [-2]R
          ((buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and spinning_Top_Red(buy_frame, 3)) and

          (buy_frame['adx_line'].iloc[-2] > 25)):

        print('TRENDING CAND_PATN BUY_OUT 2 ')

        return True

# END VOLUME BUY OUT


def trending_buy_exit(buy_frame, sell_frame, sell_stop_loss_variable):
    if buy_out_from_bb(buy_frame):
        return True

    elif boy_out_dmi(buy_frame):
        return True

    elif ma_buy_out(buy_frame, buy_frame, sell_stop_loss_variable):
        return True

    elif volume_buy_out(buy_frame):
        return True

    elif trend_cand_patn_buy_out(buy_frame):
        return True
