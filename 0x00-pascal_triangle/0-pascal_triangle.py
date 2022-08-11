#!/usr/bin/python3
"""Pascal’s triangle"""


def binomialCoeff(n, k):
    """ calculate the value of Binomial Coefficient """
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascal’s triangle"""
    l1 = []
    for line in range(0, n):
        l2 = []
        for i in range(0, line + 1):
            l2.append(binomialCoeff(line, i))
        l1.append(l2)
    return l1
