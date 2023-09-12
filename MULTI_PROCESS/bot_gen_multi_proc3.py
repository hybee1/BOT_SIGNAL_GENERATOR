import asyncio
import json
import multiprocessing
import time

import websocket
import websockets

from MAIN_BOT_SERVER3 import send_signal

records1 = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False, 'SELL ENTRY': False,
            'SELL EXIT': False, 'FROM_BOT': False}


async def get_Signal_From_Bot(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):
    n = 1

    records1 = await send_signal(no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable)
    # print('N = ', n, '\n')
    n += 1

    # print('RECORD BEFORE UPDATING TO records1[\'FROM_BOT\'] = True = ', records1)
    records1['FROM_BOT'] = True

    records.put(records1)
    # print('RECORD AFTER UPDATING TO records1[\'FROM_BOT\'] = True SING RECORDS = ', records1)

    print('\n RECORD UPDATED\n')


async def get_Signal_From_Bot_Loop(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):
    while True:
        await get_Signal_From_Bot(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable)
        await asyncio.sleep(0.5)


def get_Signal_From_Bot_Loop_1(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):
    asyncio.run(
        get_Signal_From_Bot_Loop(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable))


async def abc(records):
    first_connection = True
    while True:
        try:
            async with websockets.connect("ws://127.0.0.1:8000/bot_server", ping_interval=None, ) as websocket:
                # await asyncio.sleep(1.5)
                print('CONNECTION OPENED')
                msg_count = 0
                N1 = 1

                # p3.start()
                # **********************************
                while True:

                    if p1.is_alive():
                        x1 = 1
                        # print('P1 IS STILL ALIVE')
                    elif not p1.is_alive():  # SINCE P1 NOT ALIVE HERE

                        print('STARTING PROCESS 1 FOR THE', N1, 'TIME \n')

                        p1.start()
                        N1 += 1
                        print('JUST STARTED P1 A WHILE AGO')
                    # *********************************

                    if not records.empty():
                        msg_count += 1
                        x = records.get()
                        # print('X = ', x)
                        # print('X[\'FROM_BOT\'] = ', x['FROM_BOT'])
                        x['message_batch'] = msg_count
                        j=0
                        if x['FROM_BOT']:
                            # print('J ', j)
                            # j+=1
                            # print('X2 = ', x)
                            await websocket.send(json.dumps({'message': x}))

                            print('******just sent a record to server*********')
                            x['FROM_BOT'] = False

                    # time.sleep(0.5)
                    await asyncio.sleep(0.8)
                    first_connection = False

        except Exception as e:
            if first_connection:
                print('\nCAN\'T CONNECT TO WEBSOCKET SERVER...... '
                      '\nTHIS MIGHT BE AN INTERNET ISSUE FROM YOUR END'
                      '\nOR '
                      '\nYOU CONTACT admin@software.com')
                break
            else:
                print('\nOH SORRY, DISCONNECTED FROM WEBSOCKET')
                print('RECONNECTING TO WEBSOCKET \n')
                continue


def terminate_all_processes():
    user_input = input('type \'STOP\' to quit program \n')
    stop_all_processes.put(user_input)


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating multiprocessing Queue
        records = multiprocessing.Queue()
        stop_all_processes = multiprocessing.Queue()
        # records1 = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False, 'SELL ENTRY': False,
        #             'SELL EXIT': False, 'FROM_BOT': False}
    # records.put(records1)

    buy_stop_loss_variable = 130  # 0.9975 you multiply this by the price the asset was bought to get
    #                                  # the stop loss value
    sell_stop_loss_variable = 130  # 1.0025 you multiply this by the price the asset was sold to get

    coinPair = 'BTCUSDT'
    coin = 'USDT'

    no_of_candles = 72  # 6 hours
    no_of_recent_candles = 12  # 1 hour

    p1 = multiprocessing.Process(target=get_Signal_From_Bot_Loop_1, args=(records, no_of_candles, coinPair,
                                                                   buy_stop_loss_variable, sell_stop_loss_variable))

    # asyncio.run(send_Signal_To_Websocket_Server(records))

    # creating new processes
    # p2 = multiprocessing.Process(target=abc, args=(records,))
    # p3 = multiprocessing.Process(target=terminate_all_processes)

    # p3.start()
    websocket.enableTrace(True)
    asyncio.run(abc(records))
