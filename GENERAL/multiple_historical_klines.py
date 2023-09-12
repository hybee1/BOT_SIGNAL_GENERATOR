# SO I WROTE BELOW CODE INSTEAD

import asyncio
import time
from datetime import datetime
import pandas as pd
import talib
from binance import AsyncClient, Client

list_Of_CoinPairs = [('BTCUSDT', ''), ('ETHUSDT', '')]  # LIST OF TUPPLES


async def get_minutes_data(symbol, interval, look_back):
    client = await AsyncClient.create()
    try:
        frame = pd.DataFrame(await client.futures_historical_klines(symbol, interval, look_back + 'min ago UTC'))

        frame = frame.iloc[:, :6]
        frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        frame = frame.set_index('Time')
        frame.index = pd.to_datetime(frame.index, unit='ms')
        frame = frame.astype(float)

        return frame

    except Exception as e:
        print('ERROR GETTING HISTORICAL DATA FOR', symbol.upper())
        print('ERROR =', e)
        return ''


def add_Indicators_To_Frame(frame1):
    try:
        # ADX
        frame1['adx_line'] = talib.ADX(frame1.High, frame1.Low, frame1.Close, timeperiod=14)

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


async def get_Historical_Klines(list_Of_CoinPairs, client, interval, look_back):
    i = 0
    try:
        if len(list_Of_CoinPairs) != 0:
            for coin_pair in list_Of_CoinPairs:
                try:  # SHOULD INCASE THERE IS AN ERROR THE LOOP CONTINUES TO THE NEXT ROUND
                    # CHANGING EACH ITEM(A TUPLE TO A SMALL SO THAT IT CAN BE MODIFIED
                    tuple_was_changed_to_list = list(list_Of_CoinPairs[i])

                    # SET/UPDATE THE SECOND ITEM OF THE TUPLE WHICH IS NOW A SMALL LIST
                    # PLS NOTE IF THE LENGTH OF THE SMALL LIST IS ONE IT WILL CAUSE ERROR
                    if len(tuple_was_changed_to_list) != 1:  # AS IN TWO
                        tuple_was_changed_to_list[1] = await get_minutes_data(coin_pair, interval, look_back)

                        # CHANGE THE SMALL LIST BACK TO A TUPLE
                        change_list_to_tuple = tuple(tuple_was_changed_to_list)

                        # ADD THE TUPLE BACK TO IT ORIGINAL POISTION IN THE LARGER LIST PLS SEE ABOVE
                        list_Of_CoinPairs[i] = change_list_to_tuple
                        i += 1

                    else:
                        raise Exception ('EEROR FOR THIS PAIR', coin_pair)

                except Exception as e:
                    print('ERROR GETTING HISTORICAL DATA FOR', coin_pair.upper())
                    print('ERROR =', e)

    except Exception as e:
        print('1. ERROR =', e)

    return list_Of_CoinPairs


def buy_and_sell_frame_data(list_Of_CoinPairs):
    result = {}
    results = []
    i = 0
    for coin_pair in list_Of_CoinPairs:

        # SHOULD INCASE THERE IS AN ERROR THE LOOP CONTINUES TO THE NEXT ROUND
        try:

            buy_frame2 = pd.DataFrame()
            sell_frame2 = pd.DataFrame()

            # CHANGING EACH ITEM(A TUPLE TO A SMALL SO THAT IT CAN BE MODIFIED
            tuple_was_changed_to_list = list(list_Of_CoinPairs[i])

            # SHOULD INCASE THERE IS AN ERROR THE LOOP CONTINUES TO THE NEXT ROUND
            try:
                indicators_frame = add_Indicators_To_Frame(tuple_was_changed_to_list[1]).copy()

                result['symbol'] = coin_pair
                result['buy_frame'] = indicators_frame.copy()
                result['sell_frame'] = indicators_frame.copy()

                results.append(result)

            except Exception as e:
                print('ERROR ADDING INDICATORS  AND CREATING BUY AND SELL FRAME\n')

        except Exception as e:
            print('11. ERROR', e, '\n')

    return results


from datetime import datetime
def adf():
    client = Client()

    time_res = client.get_server_time()
    print(time_res)
    time_res1 = datetime.fromtimestamp(time_res["serverTime"]/1000)

    print(time_res1)

adf()