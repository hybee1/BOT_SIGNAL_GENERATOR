import asyncio
import json
import multiprocessing
import time

import websocket
import websockets

from MAIN_BOT_SERVER2 import send_signal

records1 = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False, 'SELL ENTRY': False,
            'SELL EXIT': False, 'FROM_BOT': False}


def get_Signal_From_Bot(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):
    while True:
        n = 1

        records1 = send_signal(no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable)
        # print('N = ', n, '\n')
        n += 1

        # print('RECORD BEFORE UPDATING TO records1[\'FROM_BOT\'] = True = ', records1)
        records1['FROM_BOT'] = True

        records.put(records1)
        # print('RECORD AFTER UPDATING TO records1[\'FROM_BOT\'] = True SING RECORDS = ', records1)

        print('\n RECORD UPDATED\n')


async def abc(records):
    async with websockets.connect("ws://192.168.88.11:8000/bot_server", ping_interval=None, ) as websocket:
        print('CONNECTION OPENED')
        msg_count = 0
        N1 = 1


        p1_first_run = False
        while True:
            # ************** ORIGINAL CODE ********************
            # if p1.is_alive():  # THE CODE IS JUST TO HOLD ON TILL P1 JOINS THE MAIN THREAD
            #     x1 = 1
            #     # print('P1 IS STILL ALIVE')
            # elif not p1.is_alive():  # SINCE P1 NOT ALIVE HERE
            #
            #     print('STARTING PROCESS 1 FOR THE', N1, 'TIME \n')
            #
            #     p1.start()
            #     p1_first_run = True
            #     N1 += 1
            #     print('JUST STARTED P1 A WHILE AGO')
            # *********************************

            if p1_first_run:  # P1 RAN SUCCESSFULLY THE FIRST TIME AND P1 IS A LOOP SO NO NEED STARTING AGAIN
                x1 = 1
            else:  # P1 HAS NOT BEEN STARTED THE FIRST TIME SO START P1
                print('STARTING PROCESS 1 FOR THE', N1, 'TIME \n')

                p1.start()
                p1_first_run = True
                N1 += 1
                print('JUST STARTED P1 A WHILE AGO')

            if not records.empty():
                msg_count += 1
                x = records.get()
                # print('X = ', x)
                # print('X[\'FROM_BOT\'] = ', x['FROM_BOT'])
                x['message_batch'] = msg_count
                if x['FROM_BOT']:
                    await websocket.send(json.dumps({'message': x}))
                    print('******just sent a record to server*********')
                    x['FROM_BOT'] = False
            # time.sleep(1.5)
            await asyncio.sleep(1)


def terminate_all_processes(process1, process2):
    while True:
        user_input = input('type \'STOP\' to quit program \n')
        if user_input.lower() == 'stop':
            process1.kill()
            process1.close()
            process2.kill()
            process1.close()


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating multiprocessing Queue
        records = multiprocessing.Queue()
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

    p1 = multiprocessing.Process(target=get_Signal_From_Bot, args=(records, no_of_candles, coinPair,
                                                                   buy_stop_loss_variable, sell_stop_loss_variable))

    # asyncio.run(send_Signal_To_Websocket_Server(records))

    # creating new processes
    # p2 = multiprocessing.Process(target=abc, args=(records,))
    # # p3 = multiprocessing.Process(target=terminate_all_processes, args=(p1, p2,))


    websocket.enableTrace(True)
    asyncio.run(abc(records))
