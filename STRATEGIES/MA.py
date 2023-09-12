def ma_buy_strategy(buy_frame):
    # NOTE ADX MUST BE GREATER THAN 25 FOR ALL CASES

    # (R[-5] AND R[-5] < MA_20[-5]) AND (G[-4,-3, -2]) AND (G[-4] < MA_20[-4]) AND
    # ((G[-3] CUT THRU MA_20[-3]) OR (G[-2] CUT THRU MA_20[-2]))
    if ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

         ((buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
         (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
         (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2])) and

         (buy_frame['High'].iloc[-5] and buy_frame['Open'].iloc[-5] < buy_frame['ma_20'].iloc[-5]) and

         ((buy_frame['High'].iloc[-4] and buy_frame['Close'].iloc[-4]) < buy_frame['ma_20'].iloc[-4]) and

         (((buy_frame['High'].iloc[-3] and buy_frame['Close'].iloc[-3]) < buy_frame['ma_20'].iloc[-3]) or
         (((buy_frame['Low'].iloc[-3] and buy_frame['Open'].iloc[-3]) < buy_frame['ma_20'].iloc[-3]) and
         ((buy_frame['High'].iloc[-3] and buy_frame['Close'].iloc[-3]) > buy_frame['ma_20'].iloc[-3]))) and

         (((buy_frame['Low'].iloc[-2] and buy_frame['Open'].iloc[-2]) > buy_frame['ma_20'].iloc[-2]) or
          (((buy_frame['Low'].iloc[-3] and buy_frame['Open'].iloc[-2]) < buy_frame['ma_20'].iloc[-2]) and
          ((buy_frame['High'].iloc[-2] and buy_frame['Close'].iloc[-2]) > buy_frame['ma_20'].iloc[-2])))):

        print('BUY MA_20 TRUE1')
        result2 = True

    # (R[-5] AND R[-5] > MA_20[-5]) AND (G[-4,-3, -2]) AND (G[-4] > MA_20[-4]) AND
    # ((G[-3] > MA_20[-3]) AND (G[-2] > MA_20[-2]))
    elif ((buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

          ((buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and
           (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
           (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2])) and

          ((buy_frame['Low'].iloc[-5] and buy_frame['Close'].iloc[-5]) > buy_frame['ma_20'].iloc[
              -5]) and

          ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-4]) > buy_frame['ma_20'].iloc[-4]) and

          ((buy_frame['Low'].iloc[-3] and buy_frame['Open'].iloc[-3]) > buy_frame['ma_20'].iloc[-3]) and
          ((buy_frame['Low'].iloc[-4] and buy_frame['Open'].iloc[-2]) > buy_frame['ma_20'].iloc[-2])):

        print('BUY MA_20 TRUE2')
        result2 = True

    else:
        result2 = False

    return result2


def ma_sell_strategy(sell_frame):
    # NOTE ADX MUST BE GREATER THAN 25 FOR ALL CASES

    # (G[-5] AND G[-5] > MA_20[-5]) AND (R[-4,-3, -2]) AND (R[-4] > MA_20[-4]) AND
    # ((R[-3] CUT THRU MA_20[-3]) OR (R[-2] CUT THRU MA_20[-2]))
    if ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

         ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
          (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
          (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2])) and

          ((sell_frame['Low'].iloc[-5] and sell_frame['Open'].iloc[-5]) > sell_frame['ma_20'].iloc[-5]) and

          ((sell_frame['Low'].iloc[-4] and sell_frame['Close'].iloc[-4]) > sell_frame['ma_20'].iloc[-4]) and

          (((sell_frame['Low'].iloc[-3] and sell_frame['Close'].iloc[-3]) > sell_frame['ma_20'].iloc[-3]) or
           (((sell_frame['High'].iloc[-3] and sell_frame['Open'].iloc[-3]) > sell_frame['ma_20'].iloc[-3]) and
          (sell_frame['Low'].iloc[-3] and sell_frame['Close'].iloc[-3] < sell_frame['ma_20'].iloc[-3]))) and

          (((sell_frame['Low'].iloc[-2] and sell_frame['Close'].iloc[-2]) < sell_frame['ma_20'].iloc[-2]) or
           (((sell_frame['High'].iloc[-2] and sell_frame['Open'].iloc[-2]) > sell_frame['ma_20'].iloc[-2]) and
            (sell_frame['Low'].iloc[-2] and sell_frame['Close'].iloc[-2] < sell_frame['ma_20'].iloc[-2])))):

        print('SELL MA_20 TRUE1')
        result2 = True

    # (G[-5] AND G[-5] < MA_20[-5]) AND (R[-4,-3, -2]) AND (R[-4] < MA_20[-4]) AND
    # ((R[-3] < MA_20[-3]) AND (R[-2] < MA_20[-2]))
    elif ((sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

          ((sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and
           (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
           (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2])) and

          ((sell_frame['High'].iloc[-5] and sell_frame['Close'].iloc[-5]) < sell_frame['ma_20'].iloc[-5]) and

          ((sell_frame['High'].iloc[-4] and sell_frame['Open'].iloc[-4]) < sell_frame['ma_20'].iloc[-4]) and

          ((sell_frame['High'].iloc[-3] and sell_frame['Open'].iloc[-3]) < sell_frame['ma_20'].iloc[-3]) and
          ((sell_frame['High'].iloc[-3] and sell_frame['Open'].iloc[-2]) < sell_frame['ma_20'].iloc[-2])):

        print('SELL MA_20 TRUE2')
        result2 = True

    else:
        result2 = False

    return result2
