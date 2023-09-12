import asyncio
import time
from datetime import datetime
import pandas as pd
import talib

first_time_run = True


def get_minutes_data(client, symbol, interval, look_back):
    frame = pd.DataFrame(client.futures_historical_klines(symbol, interval, look_back + 'min ago UTC'))

    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)

    return frame


def add_Indicators_To_Frame(frame1):
    try:
        # ADX
        frame1['adx_line'] = talib.ADX(frame1.High, frame1.Low, frame1.Close, timeperiod=5)

        # BOLLINGER BAND
        upperband, middleband, lowerband = talib.BBANDS(frame1.Close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        frame1['lowerband'] = lowerband
        frame1['middleband'] = middleband
        frame1['upperband'] = upperband

        # EMA
        frame1['ema_50'] = talib.EMA(frame1.Close, timeperiod=50)
        frame1['ema_short'] = talib.EMA(frame1.Close, timeperiod=12)
        frame1['ema_long'] = talib.EMA(frame1.Close, timeperiod=25)

        # DMI, MINUS_DI, PLUS_DI
        frame1['plus_DI'] = talib.PLUS_DI(frame1.High, frame1.Low, frame1.Close, timeperiod=14)
        frame1['minus_DI'] = talib.MINUS_DI(frame1.High, frame1.Low, frame1.Close, timeperiod=14)
        frame1['dmi_line'] = talib.ADX(frame1.High, frame1.Low, frame1.Close, timeperiod=14)

        # MA
        frame1['ma_20'] = talib.MA(frame1.Close, timeperiod=20, matype=0)

        # RSI
        rsi_short = talib.RSI(frame1.Close, timeperiod=10)
        rsi_long = talib.RSI(frame1.Close, timeperiod=50)
        frame1['rsi_short'] = rsi_short
        frame1['rsi_long'] = rsi_long

        # AROON_UP AROON_DOWN
        aroondown, aroonup = talib.AROON(frame1.High, frame1.Low, timeperiod=13)
        frame1['aroonup'] = aroonup
        frame1['aroondown'] = aroondown

        # MACD
        macd, macdsignal, macdhist = talib.MACD(frame1.Close, fastperiod=12, slowperiod=25, signalperiod=9)

        frame1['macd'] = macd
        frame1['macdsignal'] = macdsignal

        # 3WHITESOLDIERS
        integer_3_white_soldiers = talib.CDL3WHITESOLDIERS(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['3_white_soldiers'] = integer_3_white_soldiers

        # 3BLACKCROWS
        integer_3_black_crows = talib.CDL3BLACKCROWS(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['3_black_crows'] = integer_3_black_crows

        # IDENTICAL3CROWS
        integer_identical_3_crows = talib.CDLIDENTICAL3CROWS(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['identical_3_crows'] = integer_identical_3_crows

        # MORNINGSTAR
        integer_morning_star = talib.CDLMORNINGSTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['morning_star'] = integer_morning_star

        # CDLMORNINGDOJISTAR - morning_doji_star
        integer_morning_doji_star = talib.CDLMORNINGDOJISTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['morning_doji_star'] = integer_morning_doji_star

        # EVENINGSTAR
        integer_evening_star = talib.CDLEVENINGSTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['evening_star'] = integer_evening_star

        # CDLEVENINGDOJISTAR - evening_doji_star
        integer_evening_doji_star = talib.CDLEVENINGDOJISTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['evening_doji_star'] = integer_evening_doji_star

        # CONCEALBABYSWALLOW
        integer_concealing_baby_swallow = talib.CDLCONCEALBABYSWALL(frame1.Open, frame1.High, frame1.Low,
                                                                    frame1.Close)
        frame1['concealing_baby_swallow'] = integer_concealing_baby_swallow

        # 3LINESTRIKE
        integer_three_line_strike = talib.CDL3LINESTRIKE(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['three_line_strike'] = integer_three_line_strike

        # CDLRISEFALL3METHODS - Rising Three Methods == Reliable - Continuation
        integer_rising_falling_three_methods = talib.CDLRISEFALL3METHODS(frame1.Open, frame1.High, frame1.Low,
                                                                         frame1.Close)
        frame1['rising_falling_three_methods'] = integer_rising_falling_three_methods

        # CDL3OUTSIDE - Three Outside Up/Down
        integer_three_outside_up_down = talib.CDL3OUTSIDE(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['three_outside_up_down'] = integer_three_outside_up_down

        # CDLBELTHOLD - Belt-hold
        integer_belt_hold = talib.CDLBELTHOLD(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['belt_hold'] = integer_belt_hold

        # CDLABANDONEDBABY - Abandoned Baby
        integer_abandon_baby = talib.CDLABANDONEDBABY(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['abandon_baby'] = integer_abandon_baby

        # CDLSEPARATINGLINES - Separating Lines
        integer_separating_lines = talib.CDLABANDONEDBABY(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['separating_lines'] = integer_separating_lines

        # Doji
        integer_doji = talib.CDLDOJI(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['doji'] = integer_doji

        # Doji Star
        integer_doji_star = talib.CDLDOJISTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['doji_star'] = integer_doji_star

        # Dragonfly Doji
        integer_dragonfly_doji = talib.CDLDRAGONFLYDOJI(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['dragonfly_doji'] = integer_dragonfly_doji

        # Engulfing
        integer_engulfing = talib.CDLENGULFING(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['engulfing'] = integer_engulfing

        # gravestone_doji
        integer_gravestone_doji = talib.CDLGRAVESTONEDOJI(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['gravestone_doji'] = integer_gravestone_doji

        # Hammer
        integer_hammer = talib.CDLHAMMER(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['hammer'] = integer_hammer

        # Hanging Man
        integer_hanging_man = talib.CDLHANGINGMAN(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['hanging_man'] = integer_hanging_man

        # Harami
        integer_harami = talib.CDLHARAMI(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['harami'] = integer_harami

        # Inverted Hammer
        integer_inverted_hammer = talib.CDLINVERTEDHAMMER(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['inverted_hammer'] = integer_inverted_hammer

        # CDLMARUBOZU - Marubozu
        integer_marubozu = talib.CDLMARUBOZU(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['marubozu'] = integer_marubozu

        # Spinning Top
        integer_spinning_top = talib.CDLSPINNINGTOP(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['spinning_top'] = integer_spinning_top

        # Shooting Star
        integer_shooting_star = talib.CDLSHOOTINGSTAR(frame1.Open, frame1.High, frame1.Low, frame1.Close)
        frame1['shooting_star'] = integer_shooting_star

        frame44 = frame1.copy()

        return frame44

    except Exception as e:
        print('ERROR COMPUTING ALL INDICATORS')
        print('ERROR = ', e, '\n')


# Doji BULLISH = G
def doji_Green(frame, position):
    int_position = int(position) * -1
    if frame['doji'].iloc[int_position] == 100:
        print('Doji bearish which is green at position ', int_position, ' = ', frame['doji'].iloc[int_position])
        return True


# Doji BULLISH = R
def doji_Red(frame, position):
    int_position = int(position) * -1
    if frame['doji'].iloc[int_position] == -100:
        print('Doji bullish which is red at position ', int_position, ' = ', frame['doji'].iloc[int_position])
        return True


# Doji Star BEARISH = G
def doji_Star_Green(frame, position):
    int_position = int(position) * -1
    if frame['doji_star'].iloc[int_position] == 100:
        print('Doji Star bearish which is green at position ', int_position, ' = ', frame['doji_star'].iloc[int_position])
        return True


# Doji Star BULLISH = R
def doji_Star_Red(frame, position):
    int_position = int(position) * -1
    if frame['doji_star'].iloc[int_position] == -100:
        print('Doji Star bullish which is red at position ', int_position, ' = ', frame['doji_star'].iloc[int_position])
        return True


# Dragonfly Doji Bullish = G
def dragonfly_Doji_Green(frame, position):
    int_position = int(position) * -1
    if frame['dragonfly_doji'].iloc[int_position] == 100:
        print('Dragonfly Doji bullish which is green at position ', int_position, ' = ',
              frame['dragonfly_doji'].iloc[int_position])
        return True


# Dragonfly Doji Bullish = R
def dragonfly_Doji_Red(frame, position):
    int_position = int(position) * -1
    if frame['dragonfly_doji'].iloc[int_position] == -100:
        print('Dragonfly Doji bullish which is red at position ', int_position, ' = ',
              frame['dragonfly_doji'].iloc[int_position])
        return True


# Engulfing Bullish = G
def engulfing_Green(frame, position):
    int_position = int(position) * -1
    if frame['engulfing'].iloc[int_position] == 100:
        print('Engulfing bullish which is green at position ', int_position, ' = ', frame['engulfing'].iloc[int_position])
        return True


# Engulfing Bearish = R
def engulfing_Red(frame, position):
    int_position = int(position) * -1
    if frame['engulfing'].iloc[int_position] == -100:
        print('Engulfing bearish which is red at position ', int_position, ' = ', frame['engulfing'].iloc[int_position])
        return True


# gravestone_doji Bearish which = G
def gravestone_doji_Green(frame, position):
    int_position = int(position) * -1
    if frame['gravestone_doji'].iloc[int_position] == 100:
        print('gravestone_doji which is green at position ', int_position, ' = ',
              frame['gravestone_doji'].iloc[int_position])
        return True


# gravestone_doji Bearish which = R
def gravestone_doji_Red(frame, position):
    int_position = int(position) * -1
    if frame['gravestone_doji'].iloc[int_position] == -100:
        print('gravestone_doji which is red at position ', int_position, ' = ', frame['gravestone_doji'].iloc[int_position])
        return True


# Hammer Bullish = G
def hammer_Green(frame, position):
    int_position = int(position) * -1
    if frame['hammer'].iloc[int_position] == 100:
        print('Hammer which is green at position ', int_position, ' = ', frame['hammer'].iloc[int_position])
        return True


# Hammer Bullish = R
def hammer_Red(frame, position):
    int_position = int(position) * -1
    if frame['hammer'].iloc[int_position] == -100:
        print('Hammer which is red at position ', int_position, ' = ', frame['hammer'].iloc[int_position])
        return True


# Harami Bullish = G
def harami_Green(frame, position):
    int_position = int(position) * -1
    if frame['harami'].iloc[int_position] == 100:
        print('harami which is green at position ', int_position, ' = ', frame['harami'].iloc[int_position])
        return True


# Harami Bearish = R
def harami_Red(frame, position):
    int_position = int(position) * -1
    if frame['harami'].iloc[int_position] == -100:
        print('harami which is red at position ', int_position, ' = ', frame['harami'].iloc[int_position])
        return True


# Hanging Man Bearish = G
def hanging_Man_Green(frame, position):
    int_position = int(position) * -1
    if frame['hanging_man'].iloc[int_position] == 100:
        print('Hanging Man which is green at position ', int_position, ' = ', frame['hanging_man'].iloc[int_position])
        return True


# Hanging Man Bearish = R
def hanging_Man_Red(frame, position):
    int_position = int(position) * -1
    if frame['hanging_man'].iloc[int_position] == -100:
        print('Hanging Man which is red at position ', int_position, ' = ', frame['hanging_man'].iloc[int_position])
        return True


# Inverted Hammer Bullish = G
def inverted_Hammer_Green(frame, position):
    int_position = int(position) * -1
    if frame['inverted_hammer'].iloc[int_position] == 100:
        print('Inverted Hammer which is green at position ', int_position, ' = ',
              frame['inverted_hammer'].iloc[int_position])
        return True


# Inverted Hammer Bullish = R
def inverted_Hammer_Red(frame, position):
    int_position = int(position) * -1
    if frame['inverted_hammer'].iloc[int_position] == -100:
        print('Inverted Hammer which is red at position ', int_position, ' = ', frame['inverted_hammer'].iloc[int_position])
        return True


# Marubozu white = G
def marubozu_Green(frame, position):
    int_position = int(position) * -1
    if frame['marubozu'].iloc[int_position] == 100:
        print('marubozu which is green at position ', int_position, ' = ', frame['marubozu'].iloc[int_position])
        return True


# Marubozu black = R
def marubozu_Red(frame, position):
    int_position = int(position) * -1
    if frame['marubozu'].iloc[int_position] == -100:
        print('marubozu which is red at position ', int_position, ' = ', frame['marubozu'].iloc[int_position])
        return True


# Spinning Top white = G
def spinning_Top_Green(frame, position):
    int_position = int(position) * -1
    if frame['spinning_top'].iloc[int_position] == 100:
        print('Spinning Top which is green at position ', int_position, ' = ', frame['spinning_top'].iloc[int_position])
        return True


# Spinning Top black = R
def spinning_Top_Red(frame, position):
    int_position = int(position) * -1
    if frame['spinning_top'].iloc[int_position] == -100:
        print('Spinning Top which is red at position ', int_position, ' = ', frame['spinning_top'].iloc[int_position])
        return True


# Shooting Star bearish = G
def shooting_Star_Green(frame, position):
    int_position = int(position) * -1
    if frame['shooting_star'].iloc[int_position] == 100:
        print('Shooting Star which is green at position ', int_position, ' = ', frame['shooting_star'].iloc[int_position])
        return True


# Shooting Star bearish = R
def shooting_Star_Red(frame, position):
    int_position = int(position) * -1
    if frame['shooting_star'].iloc[int_position] == -100:
        print('Shooting Star which is red at position ', int_position, ' = ', frame['shooting_star'].iloc[int_position])
        return True


# 3WHITESOLDIERS  = G
def three_White_Soldiers_Green(frame, position):
    int_position = int(position) * -1
    if frame['3_white_soldiers'].iloc[int_position] == 100:
        print('3_white_soldiers bullish which is green at position ', int_position, ' = ',
              frame['3_white_soldiers'].iloc[int_position])
        return True


# MORNINGSTAR  = G
def morning_Star_Green(frame, position):
    int_position = int(position) * -1
    if frame['morning_star'].iloc[int_position] == 100:
        print('morning_star bullish which is green at position ', int_position, ' = ',
              frame['morning_star'].iloc[int_position])
        return True


# CDLMORNINGDOJISTAR
def morning_Doji_Star_Green(frame, position):
    int_position = int(position) * -1
    if frame['morning_doji_star'].iloc[int_position] == 100:
        print('morning_doji_star bullish which is green at position ', int_position, ' = ',
              frame['morning_doji_star'].iloc[int_position])
        return True


# EVENINGSTAR = R
def evening_Star_Red(frame, position):
    int_position = int(position) * -1
    if frame['evening_star'].iloc[int_position] == -100:
        print('evening_star bearish which is red at position ', int_position, ' = ',
              frame['evening_star'].iloc[int_position])
        return True


# CDLEVENINGDOJISTAR
def evening_Doji_Star_Red(frame, position):
    int_position = int(position) * -1
    if frame['evening_doji_star'].iloc[int_position] == -100:
        print('evening_doji_star bearish which is red at position ', int_position, ' = ',
              frame['evening_doji_star'].iloc[int_position])
        return True


# 3BLACKCROWS = R
def three_Black_Crows_Red(frame, position):
    int_position = int(position) * -1
    if frame['3_black_crows'].iloc[int_position] == -100:
        print('3_black_crows bearish which is red at position ', int_position, ' = ',
              frame['3_black_crows'].iloc[int_position])
        return True


# 3LINESTRIKE = G
def three_Line_Strike_Green(frame, position):
    int_position = int(position) * -1
    if frame['three_line_strike'].iloc[int_position] == 100:
        print('three_line_strike bullish which is green at position ', int_position, ' = ',
              frame['three_line_strike'].iloc[int_position])
        return True


# three_outside_up_down = G
def three_Outside_Up_Down_Green(frame, position):
    int_position = int(position) * -1
    if frame['three_outside_up_down'].iloc[int_position] == 100:
        print('three_outside_up_down bullish which is green at position ', int_position, ' = ',
              frame['three_outside_up_down'].iloc[int_position])
        return True


# three_outside_up_down = R
def three_Outside_Up_Down_Red(frame, position):
    int_position = int(position) * -1
    if frame['three_outside_up_down'].iloc[int_position] == -100:
        print('three_outside_up_down bearish which is red at position ', int_position, ' = ',
              frame['three_outside_up_down'].iloc[int_position])
        return True


# belt_hold = G
def belt_Hold_Green(frame, position):
    int_position = int(position) * -1
    if frame['belt_hold'].iloc[int_position] == 100:
        print('belt_hold bullish which is green at position ', int_position, ' = ', frame['belt_hold'].iloc[int_position])
        return True


# # belt_hold = R
def belt_Hold_Red(frame, position):
    int_position = int(position) * -1
    if frame['belt_hold'].iloc[int_position] == -100:
        print('belt_hold bearish which is red at position ', int_position, ' = ',
              frame['belt_hold'].iloc[int_position])
        return True


# abandon_baby
# abandon_baby = G
def abandon_Baby_Green(frame, position):
    int_position = int(position) * -1
    if frame['abandon_baby'].iloc[int_position] == 100:
        print('abandon_baby bullish which is green at position ', int_position, ' = ',
              frame['abandon_baby'].iloc[int_position])
        return True


# # abandon_baby = R
def abandon_Baby_Red(frame, position):
    int_position = int(position) * -1
    if frame['abandon_baby'].iloc[int_position] == -100:
        print('abandon_baby bearish which is red at position ', int_position, ' = ',
              frame['abandon_baby'].iloc[int_position])
        return True


# 3LINESTRIKE = R
def three_Line_Strike_Red(frame, position):
    int_position = int(position) * -1
    if frame['three_line_strike'].iloc[int_position] == -100:
        print('three_line_strike bearish which is red at position ', int_position, ' = ',
              frame['three_line_strike'].iloc[int_position])
        return True


# rising_three_methods = G == Reliable - Continuation
def rising_Falling_Three_Methods_Green(frame, position):
    int_position = int(position) * -1
    if frame['rising_falling_three_methods'].iloc[int_position] == 100:
        print('rising_falling_three_methods bearish which is green at position ', int_position, ' = ',
              frame['rising_falling_three_methods'].iloc[int_position])
        return True


# falling_three_methods = R == Reliable - Continuation
def rising_Falling_Three_Methods_Red(frame, position):
    int_position = int(position) * -1
    if frame['rising_falling_three_methods'].iloc[int_position] == -100:
        print('rising_falling_three_methods bearish which is red at position ', int_position, ' = ',
              frame['rising_falling_three_methods'].iloc[int_position])
        return True


# separating_lines = G
def separating_Lines_Green(frame, position):
    int_position = int(position) * -1
    if frame['separating_lines'].iloc[int_position] == 100:
        print('separating_lines bearish which is green at position ', int_position, ' = ',
              frame['separating_lines'].iloc[int_position])
        return True


# separating_lines = R
def separating_Lines_Red(frame, position):
    int_position = int(position) * -1
    if frame['separating_lines'].iloc[int_position] == -100:
        print('separating_lines bearish which is red at position ', int_position, ' = ',
              frame['separating_lines'].iloc[int_position])
        return True


# IDENTICAL3CROWS = R
def identical_Three_Crows_Red(frame, position):
    int_position = int(position) * -1
    if frame['identical_3_crows'].iloc[int_position] == -100:
        print('identical_3_crows bearish which is red at position ', int_position, ' = ',
              frame['identical_3_crows'].iloc[int_position])
        return True


# CONCEALBABYSWALL - Concealing Baby Swallow
def concealing_Baby_Swallow_Red(frame, position):
    int_position = int(position) * -1
    if frame['concealing_baby_swallow'].iloc[int_position] == -100:
        print('concealing_baby_swallow bearish which is red at position ', int_position, ' = ',
              frame['concealing_baby_swallow'].iloc[int_position])
        return True


# THE BELOW CHECKS AND COUNT THE NUMBER OF TIMES LOW CUTS BELOW LOWER-B IN 10 SAMPLES.
# IF COUNT IS >= 3 RETURN TRUE ELSE RETURN FALSE
def at_Least_3_Low(frame):
    count = 0
    for i in range(-11, -1):
        if frame['Low'].iloc[i] <= frame['lowerband'].iloc[i]:
            count+=1

    if count >= 3:
        return True

    return False


# THE BELOW CHECKS AND COUNT THE NUMBER OF TIMES HIGH CUTS ABOVE UPPER-B IN 10 SAMPLES.
# IF COUNT IS >= 3 RETURN TRUE ELSE RETURN FALSE
def at_Least_3_High(frame):
    count = 0
    for i in range(-11, -1):
        if frame['High'].iloc[i] <= frame['upperband'].iloc[i]:
            count += 1

    if count >= 3:
        return True

    return False

# MANUAL HAMMER AT -4
def manual_Hammer(buy_frame):
    # HAMMER GREEN
    if (
            (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
            # HAMMER TIP
            ((buy_frame['High'].iloc[-4] == buy_frame['Close'].iloc[-4]) or
             (buy_frame['High'].iloc[-4] - buy_frame['Close'].iloc[-4] < 7)) and

            # HAMMER HEAD for green or red pls look well
            (buy_frame['Close'].iloc[-4] - buy_frame['Open'].iloc[-4] <= 20) and

            # SIGNIFYING HANDLE
            (buy_frame['Open'].iloc[-4] > buy_frame['Low'].iloc[-4]) and

            # DISTANCE BTW HAMMER AND HANDLE
            (buy_frame['Open'].iloc[-4] - buy_frame['Low'].iloc[-4] > 12)):

        print('MANUAL GREEN HAMMER')
        return True

    # HAMMER RED
    elif (
            # HAMMER TIP
            ((buy_frame['High'].iloc[-4] == buy_frame['Open'].iloc[-4]) or
             (buy_frame['High'].iloc[-4] - buy_frame['Open'].iloc[-4] < 7)) and

            # HAMMER HEAD
            (buy_frame['Open'].iloc[-4] - buy_frame['Close'].iloc[-4] <= 20) and

            # SIGNIFYING HANDLE
            (buy_frame['Close'].iloc[-4] > buy_frame['Low'].iloc[-4]) and

            # DISTANCE BTW HAMMER AND HANDLE
            (buy_frame['Close'].iloc[-4] - buy_frame['Low'].iloc[-4] > 12)):

        print('MANUAL RED HAMMER')
        return True


# MANUAL INVERTED HAMMER AT -4
def manual_Inverted_Hammer(sell_frame):
    # INVERTED HAMMER GREEN
    if (
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # DISTANCE BTW HAMMER AND HANDLE
            (sell_frame['High'].iloc[-4] - sell_frame['Close'].iloc[-4] > 12) and

            # SIGNIFYING HANDLE
            (sell_frame['High'].iloc[-4] - sell_frame['Close'].iloc[-4]) and

            # INVERTED HAMMER TIP; THAT IS BOTTOM
            ((sell_frame['Open'].iloc[-4] == sell_frame['Low'].iloc[-4]) or
             (sell_frame['Open'].iloc[-4] - sell_frame['Low'].iloc[-4] < 7)) and

            # HAMMER HEAD
            (sell_frame['Close'].iloc[-4] - sell_frame['Open'].iloc[-4] <= 20)):

        print('MANUAL GREEN INVERTED HAMMER')
        return True

    # INVERTED HAMMER RED
    elif (
            (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            # DISTANCE BTW HAMMER AND HANDLE
            (sell_frame['High'].iloc[-4] - sell_frame['Open'].iloc[-4] > 12) and

            # SIGNIFYING HANDLE
            (sell_frame['High'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            # INVERTED HAMMER TIP; THAT IS BOTTOM
            ((sell_frame['Close'].iloc[-4] == sell_frame['Low'].iloc[-4]) or
             (sell_frame['Close'].iloc[-4] - sell_frame['Low'].iloc[-4] < 7)) and

            # HAMMER HEAD
            (sell_frame['Open'].iloc[-4] - sell_frame['Close'].iloc[-4] <= 20)):

        print('MANUAL RED INVERTED HAMMER')
        return True


# def raw_data_for_buy_signal(frame1):
#     buy_frame = frame1.copy()
#
#     return buy_frame

#
#
# def raw_data_for_sell_signal(frame1):
#
#     sell_frame = frame1.copy()
#
#     return sell_frame


def buy_and_sell_frame_data(client, symbol, interval, look_back):
    frame = pd.DataFrame()
    indicators_frame = pd.DataFrame()
    buy_frame2 = pd.DataFrame()
    sell_frame2 = pd.DataFrame()

    while True:

        try:
            frame = get_minutes_data(client, symbol, interval, look_back)
            break
        except Exception as e:
            print('ERROR GETTING MINUTE DATA FROM SOURCE DUE TO INTERNET ISSUE PLEASE '
                  '\nRESOLVE INTERNET ISSUE.... RETRYING IN 3 SECONDS.... \n')
            time.sleep(3)
            continue

    try:
        indicators_frame = add_Indicators_To_Frame(frame).copy()
        # buy_frame2 = add_Indicators_To_Frame(frame).copy()
        # sell_frame2 = add_Indicators_To_Frame(frame).copy()
        buy_frame2 = indicators_frame.copy()
        sell_frame2 = indicators_frame.copy()

    except Exception as e:
        print('ERROR ADDING INDICATORS  AND CREATING BUY AND SELL FRAME\n')

    return buy_frame2, sell_frame2


# def run_At_Interval_of_5Mins():
async def run_At_Interval_of_5Mins():
    now = datetime.now()
    hour1 = now.hour
    minutes1 = now.minute
    seconds1 = now.second

    local_current_time = now.strftime("%H:%M:%S")
    print("Current Time =", local_current_time)  # Current Time = 07:41:19

    # THIS PROGRAM CONVERTS SECONDS TO MINUTES
    # def convert_Seconds_To_Minutes(sec):
    async def convert_Seconds_To_Minutes(sec):
        sec_value = sec % (24 * 3600)
        hour_value = sec_value // 3600
        sec_value %= 3600
        min1 = sec_value // 60
        sec_value %= 60
        # print("Converted sec value in hour:", hour_value)
        # print("Converted sec value in minutes:", min1)
        return hour_value, min1, sec_value

    # **************************************************
    global first_time_run
    if int(minutes1) % 5 == 0:

        if first_time_run:
            # THIS RUNS IMMEDIATELY
            first_time_run = False
            print('yes')
        else:
            # WE WANT THE PROGRAM TO RUN EVERY 5mins 10sec
            c = 300 + 10 - seconds1  # FACTOR IN THE SECONDS SINCE WE PICK DATE TIME
            h11, m11, s11 = await convert_Seconds_To_Minutes(c)
            print('the program will wait for ', m11, 'minutes', s11, ' seconds for the next loop to run')
            # time.sleep(300 + 10 - seconds1)
            await asyncio.sleep(300 + 10 - seconds1)

    else:
        if int(minutes1) < 5:
            wait_time_in_minutes = 5 - int(minutes1)
            wait_time_in_seconds = wait_time_in_minutes * 60
            ''' print('the program will wait for ', wait_time_in_minutes, 'minutes', ' or ',
            #       wait_time_in_seconds, ' seconds') '''
            wait_time_in_seconds = wait_time_in_seconds - seconds1

            ''' WE MUST FACTOR IN THE SECONDS WE PICKED TIME, RUN THE PROGRAM AND TAKE NOTE OF
                YOUR SYSTEM TIME YOU WILL SEE WHAT I AM SAYING '''

            h1, m1, s1 = await convert_Seconds_To_Minutes(wait_time_in_seconds)

            if first_time_run:
                first_time_run = False
                print('the program will wait for ', m1, 'minutes', s1, ' seconds before running')
                # time.sleep(wait_time_in_seconds)
                await asyncio.sleep(wait_time_in_seconds)
                print('less than 5, waited')
            else:
                # WE WANT THE PROGRAM TO RUN EVERY 5mins 10sec
                print('the program will wait for ', m1, 'minutes', s1 + 10, ' seconds before running')
                # time.sleep(wait_time_in_seconds + 10)  # THE SECONDS SINCE WE PICK DATE TIME has already been
                await asyncio.sleep(wait_time_in_seconds + 10)
                # above

        else:
            rq = int(minutes1) // 5
            wait_time_in_minutes = (rq + 1) * 5 - int(minutes1)
            wait_time_in_seconds = wait_time_in_minutes * 60
            # print('the program will wait for ', wait_time_in_minutes, 'minutes', ' or ',
            #       wait_time_in_seconds, ' seconds')
            wait_time_in_seconds = wait_time_in_seconds - seconds1  # WE MUST FACTOR IN THE SECONDS WE PICKED
            #                                                        # TIME, RUN THE PROGRAM AND TAKE NOTE OF
            #                                                        # YOUR SYSTEM TIME YOU WILL SEE WHAT I AM
            #                                                        # SAYING
            h1, m1, s1 = await convert_Seconds_To_Minutes(wait_time_in_seconds)

            if first_time_run:
                first_time_run = False
                print('the bot program will wait for ', m1, 'minutes', s1, ' seconds before running')
                # time.sleep(wait_time_in_seconds)
                await asyncio.sleep(wait_time_in_seconds)
                print('waited')
            else:
                print('the bot program will wait for ', m1, 'minutes', s1 + 10, ' seconds before running')
                # time.sleep(wait_time_in_seconds + 10)
                await asyncio.sleep(wait_time_in_seconds + 10)
    return ''


# ********** adX line ****************************
def is_market_trending(buy_frame):
    # *********** TRYING THIS NEW CODE TO SEE HOW IT FARES
    try:
        # ************* CHECKING FOR TRENDING *****************
        if buy_frame['adx_line'][-3] < 25 < buy_frame['adx_line'][-2]:  # MEANING 24 THEN 26
            print('\nMARKET IS TRENDING')
            return True

        elif buy_frame['adx_line'][-3] > 25 and buy_frame['adx_line'][-2] > 25:  # MEANING 26 THEN 27
            print('\nMARKET IS TRENDING')
            return True
        # *************************************************************

        # ************* CHECKING FOR NON TRENDING *****************
        elif buy_frame['adx_line'][-3] > 25 > buy_frame['adx_line'][-2]:  # MEANING 26 THEN 24
            print('\nMARKET IS NON-TRENDING')
            return False

        elif buy_frame['adx_line'][-3] < 25 and buy_frame['adx_line'][-2] < 25:  # MEANING 23 THEN 24
            print('\nMARKET IS NON-TRENDING')
            return False
        # *************************************************************

    except Exception as e:
        print('ERROR CHECK IF MARKET IS TRENDING')
        print('ERROR = ', e)
    # *************** ORIGINAL CODE ********************
    # i = -2
    # try:
    #     while i > -10:
    #         if buy_frame['adx_line'][i] < 25:
    #             i -= 1
    #             continue
    #         else:
    #             print('\nMARKET IS TRENDING')
    #             return True
    #     print('\nMARKET IS NON TRENDING... SWITCHING STRATEGY TO BOLLINGER BAND\n')
    #     return False
    # except Exception as e:
    #     print('ERROR CHECK IF MARKET IS TRENDING')
    #     print('ERROR = ', e)
    # *********************************************************


# ********** adX line ****************************

# ******** is the market experiencing a goog volatility *********
def is_market_volatility_poor(buy_frame, coin_pair):
    i = -2
    try:
        while i > -7:
            if buy_frame['upperband'].iloc[i] - buy_frame['lowerband'].iloc[i] <= 69:
                i -= 1
                continue
            else:
                '''
                # print(coin_pair, 'MARKET IS CURRENTLY EXPERIENCING VERY LOW VOLATILITY.. IT\'S BEST'
                #                  ' WE AVOID TRADING FOR NOW\n')
                # return True
                '''
                return False
        print(coin_pair, 'MARKET IS CURRENTLY EXPERIENCING VERY LOW VOLATILITY.. IT\'S BEST'
                         ' WE AVOID TRADING FOR NOW\n')
        return True
    except Exception as e:
        print('ERROR CHECK IF MARKETVOLATILITY IS POOR')
        print('ERROR = ', e)


# ******** is the market experiencing a goog volatility *********

# ********* is the market experiencing extreme volatility ***********
def is_market_volatility_extreme(buy_frame, coin_pair):
    i = -2
    extreme_volatility_count = 0
    try:
        while i > -10:
            if float(buy_frame['Volume'].iloc[i]) > float(5500):
                extreme_volatility_count += 1
                # continue
            i -= 1

        if extreme_volatility_count >= 3:
            print(coin_pair, 'MARKET IS CURRENTLY EXPERIENCING EXTREME VOLATILITY.. IT\'S BEST'
                             ' WE AVOID TRADING FOR NOW\n')
            return True

        else:

            return False

    except Exception as e:
        print('ERROR CHECKING IF MARKET VOLATILITY IS EXTREME')
        print('ERROR = ', e)

# ********* is the market experiencing extreme volatility ***********
