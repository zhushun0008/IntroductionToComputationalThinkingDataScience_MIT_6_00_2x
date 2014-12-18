__author__ = 'zhushun0008'

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals
pylab.figure()
##pylab.plot(xVals, tVals)
## pylab.hist(tVals)
##pylab.plot(sorted(xVals), yVals)

##pylab.plot(xVals, sorted(yVals))    # Question 3-6
pylab.plot(sorted(xVals), sorted(yVals))    # Question 3-7
pylab.show()