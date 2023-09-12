import asyncio

from binance import AsyncClient


#  THE BELOW CODE WILL WORK FOR GETTING MULTIPLE HISTORICAL KLINES FOR DIFFERENT COIN-PAIRS AT
# ONCE USING ASYNC BUT THE PROBLEM IS HOW YOU IDENTIFY EACH RESPONSE AS IN IS THIS DATA FOR
# BTCUSDT OR ETHUSDT

# IT IS THE "CLIENT" THAT MAKES IT ASYNC/COROUTINE IN THIS METHOD, IB LOOK WELL
def get_Task(list_Of_Coin_Pairs, client, interval, look_back):
    tasks = []
    for Coin_Pair in list_Of_Coin_Pairs:
        # THE "asyncio.create_task" THROWS IT ONTO THE EVENT STRAIGHT
        tasks.append(asyncio.create_task(client.futures_historical_klines(Coin_Pair, interval,
                                                                          look_back + 'min ago UTC')))

    return tasks


async def get_Responses(list_Of_Coin_Pairs, client, symbol, interval, look_back):
    client = await AsyncClient.create()
    tasks = get_Task(list_Of_Coin_Pairs, client, interval, look_back)
    responses = await asyncio.gather(*tasks)
    # client.get_exchange_info(), client.get_all_tickers()
    for res in responses:
        pass


# **********************************************************************************

