"""
These are exercises for list
"""


def exercise1(a, threshold):
    print([item for item in a if item < threshold])


def exercise2(a):
    a.sort()
    print(a)
    print(list(filter(lambda x: x % 2 == 0, a)))
    print(list(filter(lambda x: x % 2 != 0, a)))


def exercise3(a, b):
    return list(set(a).intersection(set(b)))


def exercise4(a, n):
    if n >= 3:
        print(a)
    else:
        a.sort()
        print([*a[:n], *a[-n:]])


def exercise5_loop(n):
    result = list()
    for ele in n:
        if ele not in result:
            result.append(ele)
    return result


def exercise5_set(n):
    return list(set(n))
