#!/usr/bin/python3
"""Pascal’s triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascal’s triangle"""
    list_T = []
    if(n <= 0):
        return list_T
    for i in range(n):
        list_T.append([])
        """list_T[i].append(1)"""
        for j in range(1, i):
            list_T[i].append(list_T[i - 1][j - 1] + list_T[i - 1][j])
        if(n != 0):
            list_T[i].append(1)
    return list_T
