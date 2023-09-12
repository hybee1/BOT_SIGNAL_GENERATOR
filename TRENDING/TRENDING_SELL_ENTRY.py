from STRATEGIES.AROON_COPY import aroon_sell_strategy, aroon_buy_strategy
from STRATEGIES.BB_CONFIRM import bollinger_band_sell_confirm
from STRATEGIES.BB_TRENDING import bollinger_band_sell
from STRATEGIES.DMI import dmi_sell_strategy, dmi_buy_strategy
from STRATEGIES.EMA import ema_sell_strategy, ema_buy_strategy
from STRATEGIES.MA import ma_sell_strategy, ma_buy_strategy
from STRATEGIES.MACD import macd_sell_strategy, macd_buy_strategy
from STRATEGIES.SUPPORT_AND_RESISTANCE_LINE import sup_res_line_sell
from STRATEGIES.TRENDING_CAND_PATN import cand_patn_sell
from STRATEGIES.UNIVERSAL import universal_sell


def trending_sell_entry(buy_frame, sell_frame, no_of_candles):
    # check = [
    #           aroon_sell_strategy(sell_frame), bollinger_band_sell(sell_frame), bollinger_band_sell_confirm(sell_frame),
    #           dmi_sell_strategy(sell_frame), ema_sell_strategy(sell_frame), ma_sell_strategy(sell_frame),
    #           macd_sell_strategy(sell_frame),
    #         ]
    # check = [
    #     bollinger_band_sell(sell_frame), bollinger_band_sell_confirm(sell_frame), macd_sell_strategy(sell_frame),
    # ]
    #
    # print('sell check is: ', str(check))
    #
    # x = check.count(True)
    # print('COUNT IS ', x, '\n')
    # or sup_res_line_sell(no_of_candles) or sup_res_line_sell(buy_frame, sell_frame, no_of_candles)
    if universal_sell(sell_frame) or cand_patn_sell(sell_frame):

        print('')
        # sell_order(symbol1, get_qty(coin1, symbol1))
        return True

    return False
