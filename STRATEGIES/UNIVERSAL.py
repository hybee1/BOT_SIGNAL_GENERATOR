from GENERAL.GENERAL3 import (
    engulfing_Green, engulfing_Red, belt_Hold_Green, belt_Hold_Red,
    abandon_Baby_Green, abandon_Baby_Red,
    three_White_Soldiers_Green, three_Black_Crows_Red, identical_Three_Crows_Red,
    morning_Star_Green, evening_Star_Red, concealing_Baby_Swallow_Red,
    three_Line_Strike_Green, three_Line_Strike_Red,
    morning_Doji_Star_Green, evening_Doji_Star_Red,
    rising_Falling_Three_Methods_Green, rising_Falling_Three_Methods_Red,
    separating_Lines_Green, separating_Lines_Red,
    three_Outside_Up_Down_Green, three_Outside_Up_Down_Red,

    at_Least_3_Low, at_Least_3_High)


def universal_buy(buy_frame):

    # NON-TRENDING FRACTALS USING BB: FRACTAL IS A CANDLE HAVING HIGHEST HIGH OR LOWEST LOW THAN PREVIOUS CANDLE
    # AND NEXT CANDLE, [-4] LOW > [-3] LOW < [-2] LOW AND ALL CANDLES ARE BELOW MID-B
    # AND [-2] ADX < 25
    if (
            # [-3] HAS LOWEST LOW THAN [-4] AND [-2]
            (buy_frame['Low'].iloc[-4] > buy_frame['Low'].iloc[-3] < buy_frame['Low'].iloc[-2]) and

            (
             # [-3] is R and high>open
            (
            (
             (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
             (buy_frame['Low'].iloc[-3] < buy_frame['Close'].iloc[-3])
             ) or

             # [-3] is G and high>close
             (
             (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
             (buy_frame['Low'].iloc[-3] < buy_frame['Open'].iloc[-3])
             ) )
               and

             # [-2] is R and high>open
            (
            (
             (buy_frame['Open'].iloc[-2] > buy_frame['Close'].iloc[-2]) and
             (buy_frame['Low'].iloc[-2] < buy_frame['Close'].iloc[-2])
              ) or

              # [-2] is G and high>close
              (
               (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and
                 (buy_frame['Low'].iloc[-2] < buy_frame['Open'].iloc[-2])
               )

            ) )and

            (buy_frame['High'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and
            (buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['High'].iloc[-2] < buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] < 25)):

        print('UNIVERSAL non-trending fractal using bb buy 1')
        return True

    # TRENDING FRACTALS USING BB: FRACTAL IS A CANDLE HAVING HIGHEST HIGH OR LOWEST LOW THAN PREVIOUS CANDLE
    # AND NEXT CANDLE, [-4] LOW > [-3] LOW < [-2] LOW AND ALL CANDLES ARE BELOW MID-B
    # AND [-3] VOLUME GREATER THAN -[4] AND [-2] AND [-2] ADX > 25
    elif (
            # [-3] HAS HIGHEST HIGH THAN [-5] AND [-4]
            (buy_frame['Low'].iloc[-4] > buy_frame['Low'].iloc[-3] < buy_frame['Low'].iloc[-2]) and

            (buy_frame['Close'].iloc[-3] > buy_frame['Open'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-3] is G and Low < open
            (buy_frame['Low'].iloc[-3] < buy_frame['Open'].iloc[-3]) and

            # [-2] is G and Low < open
            (buy_frame['Low'].iloc[-2] < buy_frame['Open'].iloc[-2]) and

            (buy_frame['Low'].iloc[-3] > buy_frame['lowerband'].iloc[-3]) and

            (buy_frame['Volume'].iloc[-4] < buy_frame['Volume'].iloc[-3] > buy_frame['Volume'].iloc[-2]) and

            (buy_frame['High'].iloc[-4] < buy_frame['middleband'].iloc[-4]) and
            (buy_frame['High'].iloc[-3] < buy_frame['middleband'].iloc[-3]) and
            (buy_frame['High'].iloc[-2] < buy_frame['middleband'].iloc[-2]) and

            (buy_frame['adx_line'].iloc[-2] > 25)):

        print('UNIVERSAL trending fractal using bb buy 1')
        return True

    # EMA_50: WHEN PRICE IS ABOVE IT THAT IS LAST 5 CANDLES DID NOT TOUCH EMA_50
    # AND [-2] LOW TOUCHED EMA_50, THEN PRICE WILL GO UP
    elif (
            (buy_frame['ema_50'].iloc[-7] < buy_frame['Low'].iloc[-7]) and

            (buy_frame['ema_50'].iloc[-6] < buy_frame['Low'].iloc[-6]) and

            (buy_frame['ema_50'].iloc[-5] < buy_frame['Low'].iloc[-5]) and

            (buy_frame['ema_50'].iloc[-4] < buy_frame['Low'].iloc[-4]) and

            (buy_frame['ema_50'].iloc[-3] < buy_frame['Low'].iloc[-3]) and

            (buy_frame['ema_50'].iloc[-2] < buy_frame['Low'].iloc[-2]) and

            (buy_frame['Low'].iloc[-2] - buy_frame['ema_50'].iloc[-2] <= 10)):

        print('EMA_50 BUY ENTRY 1')
        return True

    # [-5]G [-4, -3]R [-2]G AND ALL BELOW MID B
    elif (
            (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and
            (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and
            (buy_frame['Close'].iloc[-2] > buy_frame['Open'].iloc[-2]) and

            # [-5]G
            (buy_frame['middleband'].iloc[-5] > buy_frame['High'].iloc[-5]) and
            # [-4]R
            (buy_frame['middleband'].iloc[-4] > buy_frame['High'].iloc[-4]) and
            # [-3]R
            (buy_frame['middleband'].iloc[-3] > buy_frame['High'].iloc[-3]) and
            # [-2]G
            (buy_frame['middleband'].iloc[-2] > buy_frame['High'].iloc[-2]) and

            not (buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3] >
                 buy_frame['middleband'].iloc[-2])
    ):
        print('UNIVERSAL BUY 1')
        return True

    # [-4, -3, -2] MIDDLE-B IS GOING UP AND DIFF BTW [-4, -3, -2] UPPER-B AND LOWER-B IS INCREASING AND
    # [-4, -3, -2]VOLUME ARE ALL LESS THAN 1K AND [-5] ADX > [-4] ADX < [-3] ADX < [-2] ADX
    elif (
            # [-4, -3, -2] MIDDLE-B IS GOING UP
            (buy_frame['middleband'].iloc[-4] < buy_frame['middleband'].iloc[-3] < buy_frame['middleband'].iloc[-2]) and

            # DIFF BTW [-4, -3, -2] UPPER-B AND LOWER-B IS INCREASING
            ((buy_frame['upperband'].iloc[-4] - buy_frame['lowerband'].iloc[-4]) >
             (buy_frame['upperband'].iloc[-3] - buy_frame['lowerband'].iloc[-3]) >
             (buy_frame['upperband'].iloc[-2] - buy_frame['lowerband'].iloc[-2])) and

            # [-4, -3, -2]VOLUME ARE ALL LESS THAN 1K
            ((buy_frame['Volume'].iloc[-4] <= 1000) and
             (buy_frame['middleband'].iloc[-3] <= 1000) and
             (buy_frame['middleband'].iloc[-2] <= 1000)) and

            # [-5] ADX > [-4] ADX < [-3] ADX < [-2] ADX: MEANING AT TE POINT WHERE ADX STARTS GOING UP

            # [-4]G
            ((buy_frame['adx_line'].iloc[-5] > buy_frame['adx_line'].iloc[-4] < buy_frame['adx_line'].iloc[-3] <
              buy_frame['adx_line'].iloc[-2]))
    ):
        print('BUY WHEN LARGE BB WIDTH')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS Three_white_soldiers (NOTE [-4,-3] ARE PART OF THE
    # Three_white_soldiers  OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER Three_white_soldiers and a MACD
    elif (
            (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7] ) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6] ) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5] ) and

            three_White_Soldiers_Green(buy_frame, 2) and (
                    buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
            (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('3 WHITE SOLDIERS BULLISH WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP BEFORE')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS morning_Star_Green (NOTE [-4,-3] ARE PART OF THE
    # morning_Star_Green OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER morning_Star_Green and a MACD
    elif (
          (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

          # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
          (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

          # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
          (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

          # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
          (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

          morning_Star_Green(buy_frame, 2) and (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
          (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('morning_Star_Green BULLISH WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP BEFORE')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS three_Line_Strike_Green (NOTE [-4,-3] ARE PART OF THE
    # three_Line_Strike_Green OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER three_Line_Strike_Green and a MACD
    elif (
           (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

           three_Line_Strike_Green(buy_frame, 2) and (
                    buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
           (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('three_Line_Strike_Green BULLISH WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP BEFORE')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS morning_Doji_Star_Green (NOTE [-4,-3] ARE PART OF THE
    # morning_Doji_Star_Green OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER morning_Doji_Star_Green and a MACD
    elif (
           (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

           morning_Doji_Star_Green(buy_frame, 2) and (
                    buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2]) and
           (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('morning_Doji_Star_Green BULLISH WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP BEFORE')
        return True

    # THIS IS A TREND CONTINUATION, PRICE WAS GOING UP ALREADY
    elif (
            rising_Falling_Three_Methods_Green(buy_frame, 2) and
            (buy_frame['macdsignal'].iloc[-2] > buy_frame['macd'].iloc[-2]) and
            (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])

    ):
        print('rising_Falling_Three_Methods_Red BULLISH, CONTINUATION PRICE WAS GOING UP ALREADY ')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS three_Outside_Up_Down_Green (NOTE [-4,-3] ARE PART
    # OF THE three_Outside_Up_Down_Green and a MACD, OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER
    # three_Outside_Up_Down_Green
    elif (
           (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

           three_Outside_Up_Down_Green(buy_frame, 2) and
           (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('three_Outside_Up_Down_Green BULLISH, PRICE WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP ')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-6,-5,-4] AND [-2]G IS engulfing_Green (NOTE [-3,-2] ARE PART
    # OF THE engulfing_Green and a MACD, OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER engulfing_Green
    elif (
           (buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5] > buy_frame['middleband'].iloc[-4]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

            # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
            (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

            engulfing_Green(buy_frame, 2) and
           (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('engulfing_Green BULLISH, PRICE WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION UP')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-5-4-3] AND [-2]G IS belt_Hold_Green and a MACD
    # YOU CAN ADD ANOTHER GREEN CANDLE AFTER belt_Hold_Green
    elif (
          (buy_frame['middleband'].iloc[-5] > buy_frame['middleband'].iloc[-4] > buy_frame['middleband'].iloc[-3]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-4] > buy_frame['Close'].iloc[-4]) and

           # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
           (buy_frame['Open'].iloc[-3] > buy_frame['Close'].iloc[-3]) and

            belt_Hold_Green(buy_frame, 2) and
          (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('belt_Hold_Green BULLISH, PRICE WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP')
        return True

    # abandon_Baby_Red
    # PRICE HAS BEEN GOING DOWN THAT [-7,-6-5] AND [-2]G IS abandon_Baby_Green (NOTE [-4,-3] ARE PART
    # abandon_Baby_Green and a MACD, OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER
    # abandon_Baby_Green
    elif (
          (buy_frame['middleband'].iloc[-7] > buy_frame['middleband'].iloc[-6] > buy_frame['middleband'].iloc[-5]) and

             # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
             (buy_frame['Open'].iloc[-7] > buy_frame['Close'].iloc[-7]) and

             # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
             (buy_frame['Open'].iloc[-6] > buy_frame['Close'].iloc[-6]) and

             # PRICE HAS BEEN GOING DOWN THAT[-7, -6-5]
             (buy_frame['Open'].iloc[-5] > buy_frame['Close'].iloc[-5]) and

            abandon_Baby_Green(buy_frame, 2) and
            (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('abandon_Baby_Green BULLISH, PRICE WAS GOING DOWN BEFORE ABOUT TO CHANGE DIRECTION GOING UP')
        return True

    # PRICE HAS BEEN GOING UP THAT [-6,-5, -4,] AND [-2]G IS separating_Lines_Green (NOTE [-3,-2] ARE PART
    # separating_Lines_Green and a MACD, OPTIONAL YOU CAN ADD ANOTHER GREEN CANDLE AFTER
    # separating_Lines_Green
    elif (
            (buy_frame['middleband'].iloc[-6] < buy_frame['middleband'].iloc[-5] < buy_frame['middleband'].iloc[-4]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (buy_frame['Close'].iloc[-6] > buy_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (buy_frame['Close'].iloc[-5] > buy_frame['Open'].iloc[-5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (buy_frame['Close'].iloc[-4] > buy_frame['Open'].iloc[-4]) and

            separating_Lines_Green(buy_frame, 2) and
            (buy_frame['macd'].iloc[-2] > buy_frame['macdsignal'].iloc[-2])
    ):
        print('separating_Lines_Green BULLISH, PRICE WAS GOING UP BEFORE, SO UP-TREND CONTINUATION')
        return True


def universal_sell(sell_frame):

    # NON-TRENDING FRACTALS USING BB: FRACTAL IS A CANDLE HAVING HIGHEST HIGH OR LOWEST LOW THAN PREVIOUS CANDLE
    # AND NEXT CANDLE, [-4] HIGH < [-3] HIGH > [-2] HIGH AND ALL CANDLES ARE ABOVE MID-B
    # AND [-2] ADX < 25
    if (
            # [-3] HAS HIGHEST HIGH THAN [-5] AND [-4]
            (sell_frame['High'].iloc[-4] < sell_frame['High'].iloc[-3] > sell_frame['High'].iloc[-2]) and

            (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and
            (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and
            (sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and

            (
               # [-3] is R and high>open
               (
                (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and
                (sell_frame['High'].iloc[-3] > sell_frame['Open'].iloc[-3])
                ) or

               # [-3] is G and high>close
                (
                 (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
                 (sell_frame['High'].iloc[-3] > sell_frame['Close'].iloc[-3])
                 )
                 and

                 # [-2] is R and high>open
               (
                       (
                  (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and
                  (sell_frame['High'].iloc[-2] > sell_frame['Open'].iloc[-2])
                  ) or

                 # [-2] is G and high>close
                 (
                  (
                  (sell_frame['Close'].iloc[-2] > sell_frame['Open'].iloc[-2]) and
                  (sell_frame['High'].iloc[-2] > sell_frame['Close'].iloc[-2])
                  )

            ) )
            ) and

            (sell_frame['adx_line'].iloc[-2] < 25)):

        print('UNIVERSAL non-trending fractal using bb sell 1')
        return True

    # TRENDING FRACTALS USING BB: FRACTAL IS A CANDLE HAVING HIGHEST HIGH OR LOWEST LOW THAN PREVIOUS CANDLE
    # AND NEXT CANDLE, [-4] HIGH < [-3] HIGH > [-2] HIGH AND ALL CANDLES ARE ABOVE MID-B
    # AND # [-3] high>open AND# [-2] high>open AND [-3] HIGH > UPPER-B
    # AND [-3] VOLUME GREATER THAN -[4] AND [-2] AND [-2] ADX > 25
    elif (
            # [-3] HAS HIGHEST HIGH THAN [-5] AND [-4]
            (sell_frame['High'].iloc[-4] < sell_frame['High'].iloc[-3] > sell_frame['High'].iloc[-2]) and

            (sell_frame['High'].iloc[-3] > sell_frame['upperband'].iloc[-3]) and

            (sell_frame['Open'].iloc[-3] > sell_frame['Close'].iloc[-3]) and

            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-3] is R and high>open
            (sell_frame['High'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            # [-2] is R and high>open
            (sell_frame['High'].iloc[-2] > sell_frame['Open'].iloc[-2]) and


            (sell_frame['Volume'].iloc[-4] < sell_frame['Volume'].iloc[-3] > sell_frame['Volume'].iloc[-2]) and

            (sell_frame['Low'].iloc[-4] > sell_frame['middleband'].iloc[-4]) and
            (sell_frame['Low'].iloc[-3] > sell_frame['middleband'].iloc[-3]) and
            (sell_frame['Low'].iloc[-2] > sell_frame['middleband'].iloc[-2]) and

            (sell_frame['adx_line'].iloc[-2] > 25)):

        print('UNIVERSAL trending fractal using bb sell 1')
        return True

    # EMA_50: WHEN PRICE IS BELOW IT THAT IS LAST 5 CANDLES DID NOT TOUCH EMA_50
    # AND [-2] HIGH TOUCHED EMA_50, THEN PRICE WILL GO DOWN
    elif (
            (sell_frame['ema_50'].iloc[-7] > sell_frame['High'].iloc[-7]) and

            (sell_frame['ema_50'].iloc[-6] > sell_frame['High'].iloc[-6]) and

            (sell_frame['ema_50'].iloc[-5] > sell_frame['High'].iloc[-5]) and

            (sell_frame['ema_50'].iloc[-4] > sell_frame['High'].iloc[-4]) and

            (sell_frame['ema_50'].iloc[-3] > sell_frame['High'].iloc[-3]) and

            (sell_frame['ema_50'].iloc[-2] > sell_frame['High'].iloc[-2]) and

            (sell_frame['ema_50'].iloc[-2] - sell_frame['High'].iloc[-2] <= 10)):

        print('EMA_50 SELL ENTRY 1')
        return True

    # [-5]R [-4, -3]G [-2]R AND ALL ABOVE MID B
    elif (
            (sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and
            (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and
            (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and
            (sell_frame['Open'].iloc[-2] > sell_frame['Close'].iloc[-2]) and

            # [-5]R
            (sell_frame['middleband'].iloc[-5] < sell_frame['Low'].iloc[-5]) and
            # [-4]G
            (sell_frame['middleband'].iloc[-4] < sell_frame['Low'].iloc[-4]) and
            # [-3]G
            (sell_frame['middleband'].iloc[-3] < sell_frame['Low'].iloc[-3]) and
            # [-2]R
            (sell_frame['middleband'].iloc[-2] < sell_frame['Low'].iloc[-2]) and

            not (sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[-3] <
                 sell_frame['middleband'].iloc[-2])
    ):
        print('UNIVERSAL SELL 1')
        return True

    # [-4, -3, -2] MIDDLE-B IS GOING DOWN AND DIFF BTW [-4, -3, -2] UPPER-B AND LOWER-B IS INCREASING AND
    # [-4, -3, -2]VOLUME ARE ALL LESS THAN 1K AND [-5] ADX > [-4] ADX < [-3] ADX < [-2] ADX
    elif (
            # [-4, -3, -2] MIDDLE-B IS GOING DOWN
            (sell_frame['middleband'].iloc[-4] > sell_frame['middleband'].iloc[-3] > sell_frame['middleband'].iloc[
                -2]) and

            # DIFF BTW [-4, -3, -2] UPPER-B AND LOWER-B IS INCREASING
            ((sell_frame['upperband'].iloc[-4] - sell_frame['lowerband'].iloc[-4]) >
             (sell_frame['upperband'].iloc[-3] - sell_frame['lowerband'].iloc[-3]) >
             (sell_frame['upperband'].iloc[-2] - sell_frame['lowerband'].iloc[-2])) and

            # [-4, -3, -2]VOLUME ARE ALL LESS THAN 1K
            ((sell_frame['Volume'].iloc[-4] <= 1000) and
             (sell_frame['middleband'].iloc[-3] <= 1000) and
             (sell_frame['middleband'].iloc[-2] <= 1000)) and

            # [-5] ADX > [-4] ADX < [-3] ADX < [-2] ADX: MEANING AT TE POINT WHERE ADX STARTS GOING UP
            ((sell_frame['adx_line'].iloc[-5] > sell_frame['adx_line'].iloc[-4] < sell_frame['adx_line'].iloc[-3] <
              sell_frame['adx_line'].iloc[-2]))
    ):
        print('BUY WHEN LARGE BB WIDTH')
        return True

    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS three_Black_Crows_Red (NOTE [-4,-3] ARE PART OF THE
    # three_Black_Crows_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER three_Black_Crows_Red and a MACD
    elif (
          (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[-5]) and

            # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
            (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

            # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
            (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

            # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
            (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            three_Black_Crows_Red(sell_frame, 2) and (
                    sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('3 three_Black_Crows_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS identical_Three_Crows_Red (NOTE [-4,-3] ARE PART OF THE
    # identical_Three_Crows_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER identical_Three_Crows_Red and a MACD
    elif (
            (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[
                -5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            identical_Three_Crows_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('3 identical_Three_Crows_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS evening_Star_Red (NOTE [-4,-3] ARE PART OF THE
    # evening_Star_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER evening_Star_Red and a MACD
    elif (
            (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[
                -5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            evening_Star_Red(sell_frame, 2) and (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('3 evening_Star_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # PRICE HAS BEEN GOING DOWN THAT [-8,-7,-6] AND [-2]R IS concealing_Baby_Swallow_Red (NOTE [-5-4,-3,-2] ARE PART
    # OF THE concealing_Baby_Swallow_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER
    # concealing_Baby_Swallow_Red and a MACD
    elif (
            (sell_frame['middleband'].iloc[-8] > sell_frame['middleband'].iloc[-7] > sell_frame['middleband'].iloc[
                -6]) and

             # PRICE HAS BEEN GOING DOWN THAT [-8,-7,-6]
             (sell_frame['Open'].iloc[-8] > sell_frame['Close'].iloc[-8]) and

             # PRICE HAS BEEN GOING DOWN THAT[ [-8,-7,-6]
             (sell_frame['Open'].iloc[-7] > sell_frame['Close'].iloc[-7]) and

             # PRICE HAS BEEN GOING DOWN THAT [-8,-7,-6]
             (sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and

            concealing_Baby_Swallow_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('3 concealing_Baby_Swallow_Red BEARISH, PRICE WAS GOING DOWN BEFORE, SO DOWN-TREND CONTINUATION ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-8,-7,-6] AND [-2]R IS three_Line_Strike_Red [-5-4,-3,-2] ARE PART
    # OF THE three_Line_Strike_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER
    # three_Line_Strike_Red and a MACD
    elif (
            (sell_frame['middleband'].iloc[-8] < sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[
                -6]) and

             # PRICE HAS BEEN GOING DOWN THAT [-8,-7,-6]
             (sell_frame['Close'].iloc[-8] > sell_frame['Open'].iloc[-8]) and

             # PRICE HAS BEEN GOING DOWN THAT[ [-8,-7,-6]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING DOWN THAT [-8,-7,-6]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

            three_Line_Strike_Red(sell_frame, 2) and (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('three_Line_Strike_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS evening_Doji_Star_Red (NOTE [-4,-3] ARE PART
    # OF THE evening_Doji_Star_Red OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER
    # evening_Doji_Star_Red and a MACD
    elif (
            (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[
                -5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            evening_Doji_Star_Red(sell_frame, 2) and (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('evening_Doji_Star_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # THIS IS A TREND CONTINUATION, PRICE WAS GOING DOWN ALREADY
    elif (
            rising_Falling_Three_Methods_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2]) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])

    ):
        print('rising_Falling_Three_Methods_Red BEARISH, CONTINUATION PRICE WAS GOING DOWN ALREADY ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS three_Outside_Up_Down_Red (NOTE [-4,-3] ARE PART
    # OF THE three_Outside_Up_Down_Red and a MACD, OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER
    # three_Outside_Up_Down_Red
    elif (
            (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[
                -5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            three_Outside_Up_Down_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('three_Outside_Up_Down_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN ')
        return True

    # PRICE HAS BEEN GOING UP THAT [-6-5-4] AND [-2]R IS engulfing_Red (NOTE [-3,-2] ARE PART
    # OF THE engulfing_Red and a MACD, OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER engulfing_Red
    elif (
           (sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[-5] < sell_frame['middleband'].iloc[
                -4]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

            engulfing_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('engulfing_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN')
        return True

    # PRICE HAS BEEN GOING UP THAT [-5-4-3] AND [-2]R IS belt_Hold_Red and a MACD
    # YOU CAN ADD ANOTHER RED CANDLE AFTER belt_Hold_Red
    elif (
           (sell_frame['middleband'].iloc[-5] < sell_frame['middleband'].iloc[-4] < sell_frame['middleband'].iloc[
                -3]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-4] > sell_frame['Open'].iloc[-4]) and

             # PRICE HAS BEEN GOING UP THAT [-6-5-4]
             (sell_frame['Close'].iloc[-3] > sell_frame['Open'].iloc[-3]) and

            belt_Hold_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('belt_Hold_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN')
        return True

    # abandon_Baby_Red
    # PRICE HAS BEEN GOING UP THAT [-7,-6-5] AND [-2]R IS abandon_Baby_Red (NOTE [-4,-3] ARE PART
    # abandon_Baby_Red and a MACD, OPTIONAL YOU CAN ADD ANOTHER RED CANDLE AFTER
    # abandon_Baby_Red
    elif (
           (sell_frame['middleband'].iloc[-7] < sell_frame['middleband'].iloc[-6] < sell_frame['middleband'].iloc[
                -5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-7] > sell_frame['Open'].iloc[-7]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-6] > sell_frame['Open'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Close'].iloc[-5] > sell_frame['Open'].iloc[-5]) and

            abandon_Baby_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('abandon_Baby_Red BEARISH, PRICE WAS GOING UP BEFORE ABOUT TO CHANGE DIRECTION GOING DOWN')
        return True

    # PRICE HAS BEEN GOING UP THAT [-6, -5, -4] AND [-2]R IS separating_Lines_Red (NOTE [-3,-2] ARE PART
    # separating_Lines_Red and a MACD, OPTIONALYOU CAN ADD ANOTHER RED CANDLE AFTER
    # separating_Lines_Red
    elif (
            (sell_frame['middleband'].iloc[-6] > sell_frame['middleband'].iloc[-5] > sell_frame['middleband'].iloc[
                -4]) and

             # PRICE HAS BEEN GOING UP THAT [-6, -5, -4]
             (sell_frame['Open'].iloc[-6] > sell_frame['Close'].iloc[-6]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Open'].iloc[-5] > sell_frame['Close'].iloc[-5]) and

             # PRICE HAS BEEN GOING UP THAT[-7, -6-5]
             (sell_frame['Open'].iloc[-4] > sell_frame['Close'].iloc[-4]) and

            separating_Lines_Red(sell_frame, 2) and
            (sell_frame['macdsignal'].iloc[-2] > sell_frame['macd'].iloc[-2])
    ):
        print('separating_Lines_Red BEARISH, PRICE WAS GOING DOWN, SO DOWN-TREND CONTINUATION')
        return True
