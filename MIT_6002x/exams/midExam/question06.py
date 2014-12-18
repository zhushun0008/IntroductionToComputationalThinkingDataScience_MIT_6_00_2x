__author__ = 'zhushun0008'

import math

def probTest(limit):
    NumChoices = 6
    n = 1
    ProbOfFirstOne = (1 - 1.0 / 6)**(n-1) * (1.0 / 6)
    while ProbOfFirstOne > limit:
        n += 1
        ProbOfFirstOne = (1 - 1.0 / 6)**(n-1) * (1.0 / 6)

    return n