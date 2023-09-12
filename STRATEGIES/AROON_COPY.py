
def aroon_buy_strategy(buy_frame):
    # result2 = ""

    if ((buy_frame['aroonup'].iloc[-2] > 92 and buy_frame['aroondown'].iloc[-2] <= 8) and

            ((buy_frame['aroonup'].iloc[-3] < 92 and buy_frame['aroondown'].iloc[-3] <= 8) or
             (buy_frame['aroonup'].iloc[-3] > 92 and buy_frame['aroondown'].iloc[-3] >= 8) or
             (buy_frame['aroonup'].iloc[-3] < 92 and buy_frame['aroondown'].iloc[-3] >= 8)) and

            ((buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] <= 8) or
             (buy_frame['aroonup'].iloc[-4] > 92 and buy_frame['aroondown'].iloc[-4] >= 8) or
             (buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] >= 8))):
        print('BUY AROON UP TRUE1')
        result2 = True

    elif ((buy_frame['aroonup'].iloc[-2] > 92 and buy_frame['aroondown'].iloc[-2] <= 8) and
          (buy_frame['aroonup'].iloc[-3] > 92 and buy_frame['aroondown'].iloc[-3] <= 8) and

          ((buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] <= 8) or
           (buy_frame['aroonup'].iloc[-4] > 92 and buy_frame['aroondown'].iloc[-4] >= 8) or
           (buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] >= 8)) and

          ((buy_frame['aroonup'].iloc[-5] < 92 and buy_frame['aroondown'].iloc[-5] <= 8) or
           (buy_frame['aroonup'].iloc[-5] > 92 and buy_frame['aroondown'].iloc[-5] >= 8) or
           (buy_frame['aroonup'].iloc[-5] < 92 and buy_frame['aroondown'].iloc[-5] >= 8))):
        print('BUY AROON UP TRUE2')
        result2 = True

    elif ((buy_frame['aroonup'].iloc[-2] > 92 and buy_frame['aroondown'].iloc[-2] <= 8) and
          (buy_frame['aroonup'].iloc[-3] > 92 and buy_frame['aroondown'].iloc[-3] <= 8) and

          ((buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] <= 8) or
           (buy_frame['aroonup'].iloc[-4] > 92 and buy_frame['aroondown'].iloc[-4] >= 8) or
           (buy_frame['aroonup'].iloc[-4] < 92 and buy_frame['aroondown'].iloc[-4] >= 8))):
        print('BUY AROON UP TRUE3')
        result2 = True

    # elif buy_frame['aroonup'].iloc[-2] > 92 and buy_frame['aroondown'].iloc[-2] != 0:
    #     print('BUY AROON UP TRUE4')
    #     result2 = True

    else:
        result2 = False

    return result2


def aroon_sell_strategy(sell_frame):

        # result2 = ""

        if ((sell_frame['aroondown'].iloc[-2] > 92 and sell_frame['aroonup'].iloc[-2] <= 8) and

                ((sell_frame['aroondown'].iloc[-3] < 92 and sell_frame['aroonup'].iloc[-3] <= 8) or
                 (sell_frame['aroondown'].iloc[-3] > 92 and sell_frame['aroonup'].iloc[-3] >= 8) or
                 (sell_frame['aroondown'].iloc[-3] < 92 and sell_frame['aroonup'].iloc[-3] >= 8)) and

                ((sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] <= 8) or
                 (sell_frame['aroondown'].iloc[-4] > 92 and sell_frame['aroonup'].iloc[-4] >= 8) or
                 (sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] >= 8))):

            print('SELL AROON DOWN TRUE1')
            result2 = True

        elif ((sell_frame['aroondown'].iloc[-2] > 92 and sell_frame['aroonup'].iloc[-2] <= 8) and
              (sell_frame['aroondown'].iloc[-3] > 92 and sell_frame['aroonup'].iloc[-3] <= 8) and

              ((sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] <= 8) or
               (sell_frame['aroondown'].iloc[-4] > 92 and sell_frame['aroonup'].iloc[-4] >= 8) or
               (sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] >= 8)) and

              ((sell_frame['aroondown'].iloc[-5] < 92 and sell_frame['aroonup'].iloc[-5] <= 8) or
               (sell_frame['aroondown'].iloc[-5] > 92 and sell_frame['aroonup'].iloc[-5] >= 8) or
               (sell_frame['aroondown'].iloc[-5] < 92 and sell_frame['aroonup'].iloc[-5] >= 8))):
            # and sell_frame['aroonup'].iloc[-3] >= 8
            print('SELL AROON DOWN TRUE2')
            result2 = True

        elif ((sell_frame['aroondown'].iloc[-2] > 92 and sell_frame['aroonup'].iloc[-2] <= 8) and
              (sell_frame['aroondown'].iloc[-3] > 92 and sell_frame['aroonup'].iloc[-3] <= 8) and

              ((sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] <= 8) or
               (sell_frame['aroondown'].iloc[-4] > 92 and sell_frame['aroonup'].iloc[-4] >= 8) or
               (sell_frame['aroondown'].iloc[-4] < 92 and sell_frame['aroonup'].iloc[-4] >= 8))):
            print('SELL AROON DOWN TRUE3')
            result2 = True

        # elif sell_frame['aroondown'].iloc[-2] > 92 and sell_frame['aroonup'].iloc[-2] >= 8:
        #     print('SELL AROON DOWN TRUE4')
        #     result2 = True

        else:
            result2 = False

        return result2
