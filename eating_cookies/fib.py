
# cache = {}

# 0(2^n)


# def naive_fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return naive_fib(n-1) + naive_fib(n-2)
# 60 minutes into lecture

# 0(n)


# def cache_fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     if n not in cache:
#         cache[n] = cache_fib(n-1) + cache_fib(n-2)

#     return cache[n]


# for i in range(40):
#     print(cache_fib(i))


# def bottom_up_fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     prevprev = 0
#     prev = 1

#     for _ in range(n-1)
#     cur = prevprev + prev

#     prevprev = prev
#     prev = cur

#     return cur


# def get_fibonacci(n):
#     fib_list = [0, 1]
#     num1 = 0
#     num2 = 1
#     while len(fib_list) <= n:
#         result = 0
#         result = num1 + num2
#         num1 = num2
#         num2 = result
#         fib_list.append(result)
#     print(fib_list)
#     return fib_list[n - 1]


# print(get_fibonacci(40))


# for i in range(20):
#     print(get_fibonacci(i))

#     import time
# start_time = time.time()
# # Run code
# end_time = time.time()
# print(f"Runtime: {end_time - start_time} seconds")


prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

total = 0
for food in prices:
    print(prices[food] * stock[food])
    total = total + prices[food] * stock[food]
print(total)


# shopping_list = ["banana", "orange", "apple"]

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }

# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }


# def compute_bill(food):
#     total = 0
#     for item in food:
#         total = total + prices[item]
#     return total


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def computes_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


print(f"it will cost you", computes_bill(shopping_list))


lloyd = {
    "name": "Lloyd",
    "homework": [],
    "quizzes": [],
    "tests": []
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]
for student in students:
    print(student["name"])
    print(f"they have scored:", student["homework"])
    print(student["quizzes"])
    print(student["tests"])

    """
def is_anagram(s0, s1):
	s0 = normalize(s0)
	s1 = normalize(s1)
​
	return s0 == s1
"""
​
# def normalize(s):
# 	return ''.join(sorted(list(s.lower())))  # alphabetical version
# ​
# def find_anagrams(words):
# 	anagrams = {}
# ​
# 	for w in words:
# 		signature = normalize(w)
# ​
# 		if signature not in anagrams:
# 			anagrams[signature] = []
# ​
# 		anagrams[signature].append(w)   # ["dog", "god"]
# ​
# 	longest = []
# ​
# 	for a in anagrams:
# 		if len(anagrams[a]) > len(longest):
# 			longest = anagrams[a]
# ​
# 	print(longest)
# ​
# words = []
# ​
# with open('words.txt') as fp:
# 	for line in fp:
# 		words.append(line.strip())
# ​
# find_anagrams(words)
