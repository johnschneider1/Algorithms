#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # we need to set our base case like fib base case is important

    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


for i in range(24):
    print(eating_cookies(i))


print(eating_cookies(10))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


# 4 cookies
# 3,1
# 2,2
# 2,1,1
# 1,3
# 1,2,1
# 1,1,2
# 1,1,1,1
# 5 cookies
# 3,2
# 3,1,1
# 2,3
# 2,2,1
# 2,1,2
# 2,1,1,1
# 1,3,1
# 1,2,2
# 1,2,1,1
# 1,1,1,1,1
# 1,1,2,1
# 1,1,3
# 1,1,1,2
# n = result
# 0 = 1
# 1 = 1
# 2 = 2
# 3 = 4
# 4 = 7
# 5 = 13
# 6 = 24
# 7 = 44
# 8 = 81
# 9 = 149
# 10 = 274
