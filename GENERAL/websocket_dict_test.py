import time
# import asyncio
#
# async def abc():
#
#     trade_signal = {'SIGNAL': False, 'BUY ENTRY': False, 'BUY EXIT': False,
#                     'SELL ENTRY': False, 'SELL EXIT': False}
#
#     await asyncio.sleep(1)
#
#     return trade_signal


from tradingview_ta import TA_Handler, Interval, Exchange

btcusdt = TA_Handler(
    symbol="BTCUSDT",
    screener="Crypto",
    exchange="Binance",
    interval=Interval.INTERVAL_5_MINUTES,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
print(btcusdt.get_analysis().summary)