from TwoDPoint import TwoDPoint
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
            self.points+=[point]

    def computeConvexHull(self):
        self.points = sorted(self.points, reverse=True)
        p1 = self.points[0]
        i = 0;
        while self.points[i].x==p1.x:
            i+=1
        self.points[0:i] = reversed(self.points[0:i])
        convexHull = [p1,self.points[1],self.points[2]]
        i = 3 # the first three points can be in the convex hull
        convexNum = 2
        while (i < len(self.points)):
            while (TwoDPoint.p(self.points[convexNum-1],self.points[convexNum],self.points[i])<=0):
                convexNum-=1;
                #convexHull.pop() # unnecessary
            convexHull[convexNum] = self.points[i];
            i+=1;
        return convexHull

    def __str__(self):
        string = "["
        i=0
        while (i < len(self.points)-1):
            string += str(self.points[i])+","
            i+=1

        return string + str(self.points[-1]) +"]"





