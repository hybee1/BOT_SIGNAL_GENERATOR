from STRATEGIES.AROON_COPY import aroon_buy_strategy, aroon_sell_strategy
from STRATEGIES.BB_CONFIRM import bollinger_band_buy_confirm
from STRATEGIES.BB_TRENDING import bollinger_band_buy
from STRATEGIES.DMI import dmi_buy_strategy, dmi_sell_strategy
from STRATEGIES.EMA import ema_buy_strategy, ema_sell_strategy
from STRATEGIES.MA import ma_buy_strategy, ma_sell_strategy
from STRATEGIES.MACD import macd_buy_strategy, macd_sell_strategy
from STRATEGIES.SUPPORT_AND_RESISTANCE_LINE import sup_res_line_buy
from STRATEGIES.TRENDING_CAND_PATN import cand_patn_buy
from STRATEGIES.UNIVERSAL import universal_buy


def trending_buy_entry(buy_frame, sell_frame, no_of_candles):
    # check = [
    #          aroon_buy_strategy(buy_frame), bollinger_band_buy(buy_frame), bollinger_band_buy_confirm(buy_frame),
    #          dmi_buy_strategy(buy_frame), ema_buy_strategy(buy_frame), ma_buy_strategy(buy_frame),
    #          macd_buy_strategy(buy_frame),
    #          ]
    # check = [
    #      bollinger_band_buy(buy_frame), bollinger_band_buy_confirm(buy_frame), macd_buy_strategy(buy_frame),
    # ]
    #
    # print('buy check is: ', str(check))
    #
    # x = check.count(True)
    # print('COUNT IS ', x, '\n')
    # or sup_res_line_buy(no_of_candles) or sup_res_line_buy(buy_frame, sell_frame, no_of_candles)
    if universal_buy(buy_frame) or cand_patn_buy(buy_frame):
        print('')
        # buy_order(symbol1, get_qty(coin1, symbol1))
        return True

    return False
