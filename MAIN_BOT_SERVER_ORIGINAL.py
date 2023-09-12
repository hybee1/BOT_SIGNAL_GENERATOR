from SOUND.ENTRY_SOUND import entry_sound
from SOUND.EXIT_SOUND import exit_sound
from binance import Client
from binance import AsyncClient
from time import ctime
import ntplib
import win32api
import pytz
from datetime import datetime
import time

from GENERAL.GENERAL import (run_At_Interval_of_5Mins, buy_and_sell_frame_data,
                             is_market_volatility_poor, is_market_trending, is_market_volatility_extreme)

from EXTREME_VOLATILITY.EXTREME_VOLATILITY_BUY_EXIT import extreme_volatility_buy_out
from EXTREME_VOLATILITY.EXTREME_VOLATILITY_SELL_EXIT import extreme_volatility_sell_out

from POOR_VOLATILITY.POOR_VOLATILITY_BUY_EXIT import poor_volatility_buy_out
from POOR_VOLATILITY.POOR_VOLATILITY_SELL_EXIT import poor_volatility_sell_out

from TRENDING.TRENDING_BUY_ENTRY import trending_buy_entry
from TRENDING.TRENDING_SELL_ENTRY import trending_sell_entry

from TRENDING.TRENDING_BUY_EXIT import trending_buy_exit
from TRENDING.TRENDING_SELL_EXIT import trending_sell_exit

from NON_TRENDING.NON_TRENDING_BUY_ENTRY import non_trending_bb_buy_entry
from NON_TRENDING.NON_TRENDING_SELL_ENTRY import non_trending_bb_sell_entry

from NON_TRENDING.NON_TRENDING_BUY_EXIT import non_trending_bb_buy_exit
from NON_TRENDING.NON_TRENDING_SELL_EXIT import non_trending_bb_sell_exit

# # Establishing OR CREATING AN INSTANCE OF connection using my api key and api secret
# key20 = 'b3jIi33kBinHb2Abynll7UqnlujIjIUDpsCiBOrnw3O3S1pYkGsRFgpYUp56SUl7'
# key30 = 'UDcTVacJzDY4stSiXx9cN4oxIxKg32mnuSBHj4O7850NLjF6n2y6IlacJIvnD0Ah'

buy_stop_loss_variable = 130  # 0.9975 you multiply this by the price the asset was bought to get
#                                  # the stop loss value
sell_stop_loss_variable = 130  # 1.0025 you multiply this by the price the asset was sold to get

coinPair = 'BTCUSDT'
coin = 'USDT'

no_of_candles = 72  # 6 hours
no_of_recent_candles = 12  # 1 hour


# THE BELOW SET THE SYSTEM DATE AND TIME USING INTERNET TIME
def set_System_DateTime_Using_Internet_DateTime():
    while True:
        try:
            # your_country_date_time = ''

            # format_data = "%d/%m/%y %H:%M:%S.%f"
            format_data1 = "%a %b %d %H:%M:%S %Y"
            ntpClient = ntplib.NTPClient()
            resp = ntpClient.request('pool.ntp.org')
            date_time = ctime(resp.tx_time)

            # print('INTERNET TIME IS BEFORE ', date_time)
            # print('INTERNET TIME IS BEFORE TYPE OF ', type(date_time))

            # this is the example output INTERNET TIME IS  Wed Oct 26 16:22:47 2022 NOTE THE OUTPUT IS IN STRING
            # SO FOR DATETIME MANIPULATIONS CONVERT TO DATETIME OBJECT FIRST USING 'strptime'

            date_time1 = datetime.strptime(date_time, format_data1)

            # print('INTERNET TIME IS AFTER ', date_time1)

            # this is the example output INTERNET TIME IS AFTER  2022 - 10 - 27 09: 56:30 ' NOTE THE OUTPUT IS A
            # DATETIME OBJECT SO FOR DATETIME MANIPULATIONS SO YOU DON'T NEED TO CONVERT TO DATETIME OBJECT
            # AS IT IS A DATETIME OBJECT ALREADY

            print('')
            # *******************************************************************
            # utc_date_time = date_time1.replace(tzinfo=timezone.utc)
            # utc_date_time = date_time1.tzinfo
            # *******************************************************************

            # CODE EXPLANATION: 'date_time1' IS A DATETIME OBJECT AND HAS NO TIMEZONE INFO SO WE FIRST CONVERT IT
            # TO OR ADD TIMEZONE INFORMATION UTC(DATE TIME) IN THIS CASE AS RECOMMENDED BY ONLINE SOURCES FOR
            # HANDLING DATE TIME FOR DIFF REGIONS
            utc_date_time = date_time1.astimezone(pytz.utc)

            # print('INTERNET TIME IS UTC ', utc_date_time)

            # print('INTERNET TIME IS UTC ', utc_date_time.tzinfo)

            # ********************************************88
            # WE ARE USING THE UTC TIME BECAUSE YOUR SYSTEM TIME ZONE OR REGION WILL ALSO HAVE EFFECT IN
            # SETTING THE CORRECT TIME AS PER YOUR REGION BASE ON THE UTC TIME
            year = utc_date_time.year
            month = utc_date_time.month
            dayofweek = utc_date_time.isoweekday()
            day = utc_date_time.day
            hour = utc_date_time.hour
            minute = utc_date_time.minute
            second = utc_date_time.second
            millisecond = utc_date_time.microsecond // 1000

            # print('year: ', year, '', 'month: ', month, '', 'dayofweek: ', dayofweek, '', 'day: ', day)
            # print('hour: ', hour, '', 'minute: ', minute, '', 'second: ', second, '', 'millisecond: ',
            #       millisecond)

            win32api.SetSystemTime(year, month, dayofweek, day, hour, minute, second, millisecond)

            print('SYSTEM DATE AND TIME UPDATED..\n')
            return 'Success'

        except Exception as e:
            print('ERROR UPDATING SYSTEM DATE AND TIME \nMAKE SURE YOU HAVE \n'
                  '1. ADMINISTRATIVE PRIVILEGES\n'
                  '2. INTERNET CONNECTIVITY.. \n' + str(e))
            # return 'Error'
            print('\nRETRYING IN 3 SECONDS...\n')
            time.sleep(3)  # SLEEP FOR 3 SECONDS BEFORE RETRYING CONNECTION
            continue


# ***************************************************************************************

async def send_signal(no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):

    set_system_Date_And_Time = set_System_DateTime_Using_Internet_DateTime()

    trade_signal = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False,
                    'SELL ENTRY': False, 'SELL EXIT': False, 'FROM_BOT': False}

    if set_system_Date_And_Time == 'Success':

        client = Client()
        ax = await run_At_Interval_of_5Mins()

        # while True:
        trade_signal = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False,
                        'SELL ENTRY': False, 'SELL EXIT': False}

        print("\nSTARTING LOOP")
        buy_frame, sell_frame = buy_and_sell_frame_data(client, coinPair, '5m', '2000')

        if is_market_volatility_extreme(buy_frame, coinPair):
            print('inside extreme volatility')

            ''' # THIS WILL BUY OR SELL US OUT FROM A TRADE IN CASE WE ARE IN '''
            if extreme_volatility_buy_out(buy_frame):
                print('BUY OUT FROM EXTREME VOLATILITY\n')
                trade_signal['BUY EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

            elif extreme_volatility_sell_out(sell_frame):
                print('SELL OUT FROM EXTREME VOLATILITY\n')
                trade_signal['SELL EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

        elif is_market_volatility_poor(buy_frame, coinPair):
            print('inside poor volatility')

            ''' # THIS WILL BUY OR SELL US OUT FROM A TRADE IN CASE WE ARE IN '''
            if poor_volatility_buy_out(buy_frame):
                print('BUY OUT FROM POOR VOLATILITY\n')
                trade_signal['BUY EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

            elif poor_volatility_sell_out(sell_frame):
                print('SELL OUT FROM POOR VOLATILITY\n')
                trade_signal['SELL EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

        elif is_market_trending(buy_frame):
            print('inside trending')

            if trending_buy_entry(buy_frame, sell_frame, no_of_candles):
                # print("\n2")
                print('BUY ENTRY FROM TRENDING\n')
                trade_signal['BUY ENTRY'] = True
                trade_signal['SIGNAL'] = True
                entry_sound()  # PLAY SOUND
                # return trade_signal

            elif trending_sell_entry(buy_frame, sell_frame, no_of_candles):
                # print("\n2")
                print('SELL ENTRY FROM TRENDING\n')
                trade_signal['SELL ENTRY'] = True
                trade_signal['SIGNAL'] = True
                entry_sound()  # PLAY SOUND
                # return trade_signal

            if trending_buy_exit(buy_frame, sell_frame, sell_stop_loss_variable):
                print('BUY EXIT FROM TRENDING\n')
                trade_signal['BUY EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

            elif trending_sell_exit(buy_frame, sell_frame, buy_stop_loss_variable):
                print('SELL EXIT FROM TRENDING\n')
                trade_signal['SELL EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

        else:  # MARKET IS RANGING OR NON TRENDING
            print('inside non-trending')

            if non_trending_bb_buy_entry(buy_frame):
                print('BUY ENTRY FROM NON TRENDING\n')
                trade_signal['BUY ENTRY'] = True
                trade_signal['SIGNAL'] = True
                entry_sound()  # PLAY SOUND
                # return trade_signal

            elif non_trending_bb_sell_entry(sell_frame):
                print('SELL ENTRY FROM NON TRENDING\n')
                trade_signal['SELL ENTRY'] = True
                trade_signal['SIGNAL'] = True
                entry_sound()  # PLAY SOUND
                # return trade_signal

            if non_trending_bb_buy_exit(buy_frame):
                print('BUY EXIT FROM NON TRENDING\n')
                trade_signal['BUY EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

            elif non_trending_bb_sell_exit(sell_frame):
                print('SELL EXIT FROM NON TRENDING\n')
                trade_signal['SELL EXIT'] = True
                trade_signal['SIGNAL'] = True
                exit_sound()  # PLAY SOUND
                # return trade_signal

        return trade_signal

        # return trade_signal  #  PART OF ORIGINAL CODE BEFORE

        # print("\nGOING TO SLEEP FOR 301 SECONDS, APPROX 5-MINUTES")

        # run_At_Interval_of_5Mins()
        # time.sleep(301)

    else:  # unable to set system date and time
        # return ''
        # exit()
        print("\nUNABLE TO SET TIME")
        return trade_signal
