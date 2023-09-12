from STRATEGIES.BB_NON_TRENDING import bollinger_band_sell2
from STRATEGIES.NON_TRENDING_CAND_PATN import cand_patn_sell
from STRATEGIES.UNIVERSAL import universal_sell


def non_trending_bb_sell_entry(sell_frame):
    if universal_sell(sell_frame):
        return True
    elif cand_patn_sell(sell_frame):
        return True
    elif bollinger_band_sell2(sell_frame):
        return True
