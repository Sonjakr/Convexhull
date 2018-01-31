from TwoDPoint import TwoDPoint
from GrahamScan import GrahamScan

point = TwoDPoint(2,3)
gs = GrahamScan("/Users/sonja/PycharmProjects/ConvexHull/src/testData")

print gs

list = gs.computeConvexHull()
print gs
print list
print "eowrhp"
for item in list:
    print item
