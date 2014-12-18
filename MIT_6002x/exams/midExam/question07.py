__author__ = 'zhushun0008'

import random
import pylab

def generateBallList():
    ballList = []
    numBalls = 1000
    for i in range(numBalls):
        ballList.append(random.choice((0, 1)))

    return ballList

def LV(ballList):
    '''
        LV METHOD
        Point to a random ball. If it is white, then exit. If it is black, then repeat (e.g. choose another random ball,
        and test). The procedure returns the number of tries until a white ball is found.
    '''
    numBalls = len(ballList)
    randomLocation = random.randint(0, numBalls-1)
    numTries = 1
    while ballList[randomLocation] != 0:
            numTries += 1
            randomLocation = random.randint(0, numBalls-1)

    return numTries


def test():
    ballList = generateBallList()
    histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros

    for i in range(1000):

        result = LV(ballList)

        histogram[ result ] += 1

    pylab.figure()
    pylab.plot([1, 2, 3], histogram[1:4])
    pylab.show()

test()