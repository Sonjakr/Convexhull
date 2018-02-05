from TwoDPoint import TwoDPoint
from GrahamScan import GrahamScan
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



point = TwoDPoint(2,3)
gs = GrahamScan("/Users/sonja/PycharmProjects/ConvexHull/src/testData")

points = gs.points;
orig_x = [point.x for point in gs.points]
orig_y = [point.y for point in gs.points]
#plt.scatter(orig_x,orig_y)
list = gs.computeConvexHull()
i=1
pivot = gs.points[0]
#while (i < len(gs.points)):
#    plt.plot([pivot.x,gs.points[i].x],[pivot.y,gs.points[i].y],"k-",lw=0.5)
#    i+=1

#plt.show()
nums = len(gs.points)-1
print nums
fig,ax = plt.subplots(figsize=(7.5,7.5))
#ax = plt.axes(xlim = (-7,7),ylim=(-7,7))
line, = ax.plot([],[])
def init():
    #ine.set_data([],[])
    return

def animate(i):
    global points
    ax.cla()
    ax.plot([pivot.x, points[i+1].x], [pivot.y, points[i+1].y], "k-", lw=0.5)
    #plt.show()
    #print "lol"
    #line.set_data([pivot.x, points[i].x],[pivot.y, points[i].y])
    return

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=nums,interval=30,blit=True)

#x_list = [point.x for point in list]
#y_list = [point.y for point in list]
#plt.scatter(x_list,y_list)
#plt.show()