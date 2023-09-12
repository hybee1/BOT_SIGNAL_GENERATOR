import asyncio
import json
import multiprocessing
import time

import websocket
import websockets

from MAIN_BOT_SERVER import send_signal

records1 = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False, 'SELL ENTRY': False,
            'SELL EXIT': False, 'FROM_BOT': False}


def get_Signal_From_Bot(records, no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable):
    n = 1

    records1 = send_signal(no_of_candles, coinPair, buy_stop_loss_variable, sell_stop_loss_variable)
    # print('N = ', n, '\n')
    n += 1

    # print('RECORD BEFORE UPDATING TO records1[\'FROM_BOT\'] = True = ', records1)
    records1['FROM_BOT'] = True

    records.put(records1)
    # print('RECORD AFTER UPDATING TO records1[\'FROM_BOT\'] = True SING RECORDS = ', records1)

    print('\n RECORD UPDATED\n')


# def on_message(message, records):
#     # ws.send(message)
#     print('message ', message)
#     # message1 = json.loads(message)
#     # print(message1["SIGNAL"])
#
#
# def on_error(ws, error):
#     print('error = ', error)
#
#
# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")
#
#
# def on_open(ws):
#     # ws.send(json.dumps({'message':'Hi Server, I want to connect to you?'}))
#     print('ws in open = ', ws)
#     print("CONNECTION OPEN")
#     while True:
#         x = records.get()
#         if x['FROM_BOT']:
#             ws.send(records.get())
#             print('******just sent a record to server*********')
#
#
# # websocket.enableTrace(True)
#
#
# def abc():
#     ws = websocket.WebSocketApp("ws://192.168.88.11:8000/bot_server",
#                                 on_open=on_open,
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close,
#                                 on_data=records.get())
#     #on_data=records.get()

#     ws.run_forever()
from websockets.sync.client import connect


def abc(records):
    with connect("ws://192.168.88.11:8000/bot_server") as websocket:
        print('CONNECTION OPENED')
        msg_count = 0
        while True:
            if not records.empty():
                msg_count += 1
                x = records.get()
                # print('X = ', x)
                # print('X[\'FROM_BOT\'] = ', x['FROM_BOT'])
                x['message_batch'] = msg_count
                if x['FROM_BOT']:
                    websocket.send(json.dumps({'message': x}))
                    print('******just sent a record to server*********')
                    x['FROM_BOT'] = False
            time.sleep(1.5)


def terminate_all_processes(process1, process2):
    while True:
        user_input = input('type \'STOP\' to quit program \n')
        if user_input.lower() == 'stop':
            process1.kill()
            process1.close()
            process2.kill()
            process1.close()


# SEND SIGNAL TO WEBSOCKET SERVER SO THAT SERVER CAN SEND TO CONNECTED WEBSOCKET CLIENTS
# async def send_Signal_To_Websocket_Server(records):
#     first_connection = True
#     print('1. RECORDS = ', records.get(records1))
#     while True:
#         try:
#
#
#         except Exception as e:
#             if first_connection:
#                 print('\nCAN\'T CONNECT TO WEBSOCKET SERVER...... '
#                       '\nTHIS MIGHT BE AN INTERNET ISSUE FROM YOUR END'
#                       '\nOR '
#                       '\nYOU CONTACT admin@software.com')
#                 break
#             else:
#                 print('OH SORRY, DISCONNECTED FROM WEBSOCKET')
#                 print('RECONNECTING TO WEBSOCKET \n')
#                 continue


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating multiprocessing Queue
        records = multiprocessing.Queue()
        # records1 = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False, 'SELL ENTRY': False,
        #             'SELL EXIT': False, 'FROM_BOT': False}
    records.put(records1)

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
    p2 = multiprocessing.Process(target=abc, args=(records,))
    # p3 = multiprocessing.Process(target=terminate_all_processes, args=(p1, p2,))

    # p1.start()
    p2.start()
    # p3.start()

    # MAKE YOU START P1 HERE
    # while True:
    #     if p1.is_alive():
    #         print('PROCESS 1 IS ALIVE.....  STARTING PROCESS 2')
    #         break

    # MAKE YOU START P2 HERE
    while True:
        if p2.is_alive():
            print('PROCESS 2 IS ALIVE.....  ')
            break

    # p1.join()
    # p2.join()

    '''
    IBRO NOTE P2 WILL NEVER COME TO END SINCE IN P2 FUNCTION ITSELF IT'S AN ENDLESS 
    LOOP PLS STUDY TO KNOW WHY
    '''

    print('\n AFTER PROCESS 2 WAS STARTED.....  ')
    while p2.is_alive():
        # p1.join()  # THIS WILL ALLOW P1 TO JOIN MAIN THREAD BY WAITING FOR P1 TO FINISH EXECUTING

        # while True:
        if p1.is_alive():  # THE CODE IS JUST TO HOLD ON TILL P1 JOINS THE MAIN THREAD
            x1 = 1

        elif not p1.is_alive():  # SINCE P1 NOT ALIVE HERE
            print('P1 NOT ALIVE')
            N1 = 2  # SINCE WE HAVE STARTED IT BEFORE
            p1.run()
            print('STARTING PROCESS 1 AGAIN FOR THE ', N1, ' TIME')
            N1 += 1
            print('P1 IS ALIVE')


    # p3.join()
    # p3.close()
    # print('***************THANK YOU GOODBYE*************')
    # exit()
    while True:
        if not p2.is_alive():
            user_input = input('type \'STOP\' to quit program \n')
            if user_input.lower() == 'stop':
                p1.kill()
                p2.kill()
                exit()
