from STRATEGIES.BB_NON_TRENDING import bollinger_band_buy2
from STRATEGIES.NON_TRENDING_CAND_PATN import cand_patn_buy
from STRATEGIES.UNIVERSAL import universal_buy


def non_trending_bb_buy_entry(buy_frame):
    if universal_buy(buy_frame):
        return True
    elif cand_patn_buy(buy_frame):
        return True
    elif bollinger_band_buy2(buy_frame):
        return True


