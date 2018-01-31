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

    def __str__(self):
        string = "["
        i=0
        while (i < len(self.points)-1):
            string += str(self.points[i])+","
            i+=1

        return string + str(self.points[-1]) +"]"





