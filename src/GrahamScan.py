from TwoDPoint import TwoDPoint
import math
import copy
import matplotlib.animation as animation

class GrahamScan:
    filename = ""
    points = []

    def __init__(self, filename):
        self.filename = filename
        self.read(filename)

    def read(self,filename):
        file = open(filename,"r")
        rawPoints = file.read().split(" ")
        for point in rawPoints:
            point = point.split(",")
            point = TwoDPoint(float(point[0]),float(point[1]))
            point.sort_by_x = False;
            self.points+=[point]

    def sortPoints(self):
        # assume pivot is at index 0
        i = 1
        pivot = self.points[0]
        angels = []
        while (i < len(self.points)):
            delta_y = pivot.y - self.points[i].y
            delta_x = self.points[i].x-pivot.x
            if delta_y == 0:
                angels+=[math.pi/2]
            elif delta_y<0:
                angels+=[math.atan(delta_x/delta_y)] #vertical line through pivot as reference line for angle
            elif delta_y>0:
                angels += [math.atan(delta_x/delta_y)+  math.pi]
            i+=1
        print angels
        sortedAngels = sorted(zip(angels,self.points[1:]))
        self.points  = [pivot] + [x for _,x in sortedAngels]

    def findPivot(self):
        i = 0
        max = self.points[i]
        # index = i
        while (i < len(self.points)):
            if self.points[i].x > max.x:
                max = self.points[i]
            # indix = i
            elif self.points[i].x == max.x and self.points[i].y < max.y:
                max = self.points[i]
                # index = i
            i += 1
        self.points.remove(max);
        self.points = [max] + self.points

    def performGrahamScan(self):
        intermediate_steps = []
        convexHull = [self.points[0], self.points[1], self.points[2]]
        intermediate_steps = [copy.deepcopy(convexHull)]
        i = 3  # the first three points can be in the convex hull
        convexNum = 2
        while (i < len(self.points)):
            while (TwoDPoint.p(convexHull[-2], convexHull[-1], self.points[i]) <= 0):
                #for animaton can otherwise be commented out
                convexHull.append(self.points[i])
                intermediate_steps+=[copy.deepcopy(convexHull)]
                convexHull.pop()
                # ____________________________________________
                convexNum -= 1;
                convexHull.pop()  # unnecessary
                #intermediate_steps+=[copy.deepcopy(convexHull)]
            convexHull.append(self.points[i]);
            intermediate_steps+=[copy.deepcopy(convexHull)]
            i += 1;
        return intermediate_steps

    def computeConvexHull(self):
        self.findPivot()
        self.sortPoints()
        convexHull = self.performGrahamScan()[-1]
        return convexHull

    def __str__(self):
        string = "["
        i=0
        while (i < len(self.points)-1):
            string += str(self.points[i])+","
            i+=1

        return string + str(self.points[-1]) +"]"





