from MAIN_BOT_SERVER import send_signal
import asyncio
import websockets
import time
import json
# from asgiref.sync import async_to_sync

coinPair = 'BTCUSDT'
coin = 'USDT'

no_of_candles = 72  # 6 hours
no_of_recent_candles = 12  # 1 hours
buy_stop_loss_variable = 170  # 0.9975 you multiply this by the price the asset was bought to get
#                                  # the stop loss value
sell_stop_loss_variable = 170  # 1.0025 you multiply this by the price the asset was sold to get


async def websocket_client2():
    first_connection = True
    while True:
        try:
            async with websockets.connect('ws://192.168.88.11:8000/bot_server',
                                          ping_interval=None, ) as client_socket:
                print('\nCONNECTION ESTABLISHED\n')
                first_connection = False
                msg_count = 0
                while True:
                    first_connection = False
                    msg_count = msg_count + 1
                    #     await asyncio.sleep(3)
                    #     await client_socket.send(json.dumps({'message':'Hi Server, I want to connect to you?'}))
                    print('\n       MESSAGE BATCH ', msg_count)
                    print('A1')
                    signal_from_bot = await send_signal(no_of_candles, coinPair, buy_stop_loss_variable,
                                                        sell_stop_loss_variable)

                    if isinstance(signal_from_bot, dict):
                        print('A2')
                        await asyncio.sleep(1)
                        signal_from_bot['message_batch'] = msg_count

                        await client_socket.send(json.dumps({'message': signal_from_bot}))

                        print("A3")
                    else:
                        print("ERROR SENDING TO WEBSOCKET SERVER.....\n")

                    await asyncio.sleep(1.5)

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

    # print(await client_socket.recv())
    # await asyncio.Future()


asyncio.run(websocket_client2())

# import websocket
# from websocket import create_connection
#
# def on_message(ws, message):
#     # print('1')
#     print(message)
#     # message1 = json.loads(message)
#     # print(message1["SIGNAL"])
#
#
# def on_error(ws, error):
#     print(error)
#
#
# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")
#
#
# def on_open(ws):
#     # ws.send(json.dumps({'message':'Hi Server, I want to connect to you?'}))
#     print("Opened connection")
#     while True:
#         signal_from_bot = send_signal(no_of_candles, coinPair, buy_stop_loss_variable,
#                                       sell_stop_loss_variable)
#         ws.send(json.dumps({'message': signal_from_bot}))
#
#
# # websocket.enableTrace(True)
# ws = websocket.WebSocketApp("ws://localhost:8000/bot_server",
#                             on_open=on_open,
#                             on_message=on_message,
#                             on_error=on_error,
#                             on_close=on_close)
# # ws.run_forever()


# while True:
#     ws = create_connection("ws://localhost:8000/bot_server")
#     signal_from_bot = send_signal(no_of_candles, coinPair, buy_stop_loss_variable,
#                                   sell_stop_loss_variable)
#     ws.send(json.dumps({'message': signal_from_bot}))

# ws.run_forever()
