
cache = {}

# 0(2^n)


def naive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return naive_fib(n-1) + naive_fib(n-2)
# 60 minutes into lecture

# 0(n)


def cache_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in cache:
        cache[n] = cache_fib(n-1) + cache_fib(n-2)

    return cache[n]


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


def get_fibonacci(n):
    fib_list = [0, 1]
    num1 = 0
    num2 = 1
    while len(fib_list) <= n:
        result = 0
        result = num1 + num2
        num1 = num2
        num2 = result
        fib_list.append(result)
    print(fib_list)
    return fib_list[n - 1]


# print(get_fibonacci(40))


for i in range(20):
    print(get_fibonacci(i))

    import time
start_time = time.time()
# Run code
end_time = time.time()
print(f"Runtime: {end_time - start_time} seconds")
