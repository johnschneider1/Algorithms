#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit = []  # set an empty list to add the prices too
    print(profit)
    # loop through the inputed stock prices to find the lowest value
    for i in range(len(prices)):
        # second loop to find the next highest value i + 1
        for j in range(i+1, len(prices)):
            # assign the value of the buy from the first loop
            buy = prices[i]
            # assign the value of the sell from the second loop
            sell = prices[j]
            # determine the edge in the trade by calculating the sell price vs the buy price
            edge = sell - buy
            # append the empty list so we have a stored value of all our trades
            profit.append(edge)
            # take the highest edge from the profit and return that result
            print(profit)
            result = max(profit)
    return result


test_list = [19, 175, 55, 78, 84, 99, 125]
print("largest edge: ", find_max_profit(test_list))

if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

    # automate the task of day trading for you while you're going to Lambda,  the bot should focus on buying and selling amazon stock

    # write a function find_max_profit, that receives as input a llist of stock prices, the function should return the max profit that can be made from a single buy and sell.
    # I must buy first before selling, no shorting is allowed(party pooping)

    # keep track of the current_min_price_so_far and the max_profit_so_far?
    # everybody always buys teh bottom and sells the top
    # module agparse is the "recommended command-line parsing module in the python standard library"
    # determine when to buy
    # determine when to sell
    # determine the profit s-b
    # take the input(prices) and loop to find
    # feels like selection sort, finding a lowest value and finding a higher value
