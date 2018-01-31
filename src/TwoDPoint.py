class TwoDPoint:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

#    def setSortByX(self, sort_by_x):
#        self.sort_by_x = sort_by_x

    def __lt__(self, other):
        if (self.x == other.x):
            return self.y<other.y
        else:
            return self.x<other.x

    def __str__(self):
        return "("+ str(self.x)+"," +str(self.y)+")"

    @staticmethod
    def p(point1, point2, point3):
        zCrossProduct = (point2.x-point1.x)*(point3.y-point1.y)-(point2.y-point1.y)*(point3.x-point1.x)

        if zCrossProduct > 0:
            return 1
        elif zCrossProduct < 0:
            return -1
        else:
            return 0

