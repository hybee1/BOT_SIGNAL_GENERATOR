# SUPPORT RESISTANCE LINE STRATEGY PART 2

# THE BELOW WILL FIND THE SWING LOWS
def lowest_swing_low(buy_frame, no_of_candles):
    lowest_sup_res_line = []

    i1 = -no_of_candles

    while i1 < 0:
        # print('i = ', i1)
        i2 = i1 + 1
        i3 = i1 + 2
        i4 = i1 + 3
        i5 = i1 + 4

        if i1 < -2:

            if ((buy_frame['Low'].iloc[i1] > buy_frame['Low'].iloc[i2]) and
                    (buy_frame['Low'].iloc[i2] > buy_frame['Low'].iloc[i3]) and
                    (buy_frame['Low'].iloc[i4] > buy_frame['Low'].iloc[i3]) and
                    (buy_frame['Low'].iloc[i5] > buy_frame['Low'].iloc[i4])):

                if buy_frame['Close'].iloc[i3] > buy_frame['Open'].iloc[i3]:
                    lowest_sup_res_line.append(buy_frame['Open'].iloc[i3])

                elif buy_frame['Open'].iloc[i3] > buy_frame['Close'].iloc[i3]:
                    lowest_sup_res_line.append(buy_frame['Close'].iloc[i3])
        else:
            break
        i1 += 1

    # print('lowest point = ', lowest_sup_res_line)
    # print('2')
    return lowest_sup_res_line


# lowest

# THE BELOW WILL FIND THE SWING HIGHS
def highest_swing_high(sell_frame, no_of_candles):
    highest_sup_res_line = []

    i1 = -no_of_candles

    while i1 < 0:
        # print('i = ', i1)
        i2 = i1 + 1
        i3 = i1 + 2
        i4 = i1 + 3
        i5 = i1 + 4

        if i1 < -2:
            if ((sell_frame['High'].iloc[i1] < sell_frame['High'].iloc[i2]) and
                    (sell_frame['High'].iloc[i2] < sell_frame['High'].iloc[i3]) and
                    (sell_frame['High'].iloc[i4] < sell_frame['High'].iloc[i3]) and
                    (sell_frame['High'].iloc[i5] < sell_frame['High'].iloc[i4])):

                if sell_frame['Close'].iloc[i3] > sell_frame['Open'].iloc[i3]:
                    highest_sup_res_line.append(sell_frame['Open'].iloc[i3])

                elif sell_frame['Open'].iloc[i3] > sell_frame['Close'].iloc[i3]:
                    highest_sup_res_line.append(sell_frame['Close'].iloc[i3])
        else:
            break
        i1 += 1
    # print('highest point = ', highest_sup_res_line)
    # print('3')
    return highest_sup_res_line


# highest

# IT WILL ALSO FINALISE OR COMPILE ALL THE SUPPORT AND RESISTANCE IN THIS METHOD
def calculate_sup_and_res_line(buy_frame, sell_frame, no_of_candles):
    all_sup_res_line = []

    all_sup_res_line.extend(lowest_swing_low(buy_frame, no_of_candles))
    all_sup_res_line.extend(highest_swing_high(sell_frame, no_of_candles))

    all_sup_res_line.sort()

    i = 0
    while i < len(all_sup_res_line):

        if all_sup_res_line.count(all_sup_res_line[i]) > 1:
            all_sup_res_line.pop(all_sup_res_line.index(all_sup_res_line[i]))
            i = -1
        i += 1

    if len(all_sup_res_line) > 0:
        pass
        # print('NUMBER OF SUPPORT AND RESISTANCE LINES: ', len(all_sup_res_line))
        # print(all_sup_res_line, '\n')
        # print('4')

    else:
        pass
        # print('No Support and Resistance lines found')

    return all_sup_res_line


# finding buy entry
def sup_res_line_buy(self, no_of_candles, ):
    all_sup_res_line2 = self.calculate_sup_and_res_line(no_of_candles)

    if len(all_sup_res_line2) > 0:

        for loop in all_sup_res_line2:
            # red[-5], green[-4,-3,-2], green[-3] below or cuts thru, green[-2] cuts thru or above
            if ((self.sell_frame['Open'].iloc[-5] > self.sell_frame['Close'].iloc[-5] and
                 self.buy_frame['Close'].iloc[-4] > self.buy_frame['Open'].iloc[-4] and
                 self.buy_frame['Close'].iloc[-3] > self.buy_frame['Open'].iloc[-3] and
                 self.buy_frame['Close'].iloc[-2] > self.buy_frame['Open'].iloc[-2]) and

                 (self.sell_frame['Open'].iloc[-5] and self.sell_frame['High'].iloc[-5] < loop) and

                 (self.buy_frame['Close'].iloc[-4] and self.buy_frame['High'].iloc[-4] < loop) and

                 ((self.buy_frame['Close'].iloc[-3] and self.buy_frame['High'].iloc[-3] < loop) or
                 ((self.buy_frame['Low'].iloc[-3] and self.buy_frame['Open'].iloc[-3] < loop) and
                 (self.buy_frame['Close'].iloc[-3] and self.buy_frame['High'].iloc[-3] > loop))) and

                 ((self.buy_frame['Low'].iloc[-2] and self.buy_frame['Open'].iloc[-2] > loop) or
                 ((self.buy_frame['Low'].iloc[-2] and self.buy_frame['Open'].iloc[-2] < loop) and
                 (self.buy_frame['Close'].iloc[-2] and self.buy_frame['High'].iloc[-2] > loop)))):
                print('Support and Resistance level: ', loop, ' --BUY--')
                return True
    return False


# end finding buy entry

# finding sell entry
def sup_res_line_sell(self, no_of_candles):

    all_sup_res_line3 = self.calculate_sup_and_res_line(no_of_candles)

    if len(all_sup_res_line3) > 0:

        for loop in all_sup_res_line3:
            # green[-5], green[-4,-3,-2], red[-3] above or cuts thru, red[-2] cuts thru or below
            if ((self.buy_frame['Close'].iloc[-5] > self.buy_frame['Open'].iloc[-5] and
                 self.sell_frame['Open'].iloc[-4] > self.sell_frame['Close'].iloc[-4] and
                 self.sell_frame['Open'].iloc[-3] > self.sell_frame['Close'].iloc[-3] and
                 self.sell_frame['Open'].iloc[-2] > self.sell_frame['Close'].iloc[-2]) and

                (self.buy_frame['Low'].iloc[-5] and self.buy_frame['Open'].iloc[-5] > loop) and

                (self.sell_frame['Close'].iloc[-4] and self.sell_frame['Low'].iloc[-4] > loop) and

                ((self.sell_frame['Close'].iloc[-3] and self.sell_frame['Low'].iloc[-3] > loop) or

                ((self.sell_frame['High'].iloc[-3] and self.sell_frame['Open'].iloc[-3] > loop) and
                (self.sell_frame['Close'].iloc[-3] and self.sell_frame['Low'].iloc[-3] < loop))) and

                ((self.sell_frame['High'].iloc[-2] and self.sell_frame['Open'].iloc[-2] < loop) or
                ((self.sell_frame['High'].iloc[-2] and self.sell_frame['Open'].iloc[-2] > loop) and
                (self.sell_frame['Close'].iloc[-2] and self.sell_frame['Low'].iloc[-2] < loop)))):
                print('Support and Resistance level: ', loop, ' --SELL--')
                return True
    return False

# end finding sell entry

# END SUPPORT RESISTANCE LINE STRATEGY
