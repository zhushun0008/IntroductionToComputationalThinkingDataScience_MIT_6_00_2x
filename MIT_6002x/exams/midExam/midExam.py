__author__ = 'zhushun0008'


import pylab
import random

randomList1 = []
randomList2 = []
for i in range(1000):
    randomList1.append(int( random.random() * 2))

for i in range(1000):
    randomList2.append(random.choice((0,1)))

pylab.figure()
pylab.hist(randomList1)
pylab.show()
pylab.hist(randomList2)
pylab.show()