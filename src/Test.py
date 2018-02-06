from TwoDPoint import TwoDPoint
from GrahamScan import GrahamScan
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def init():
    line.set_data([],[])
    point.set_data([],[])
    return line,point

#def animate_order(i):
#    global points
#    j = 0
#    lines_x = []
#    lines_y = []
#    while j < i+1:
#        lines_y += [pivot.y,points[j+1].y]
#        lines_x += [pivot.x,points[j+1].x]
#        j+=1
#    line.set_data(lines_x, lines_y)
#    return line,
def animate_graham_scan(i):
    global intermediate_steps,pivot
    lines_x = []
    lines_y = []
    if (i!=0):
        j = 0
        current = intermediate_steps[i - 1]
        while j < len(current)-1:
            lines_y += [current[j].y,current[j+1].y]
            lines_x += [current[j].x,current[j+1].x]
            j+=1
        if i == len(intermediate_steps):
            lines_y += [current[j].y, current[0].y]
            lines_x += [current[j].x, current[0].x]
    line.set_data(lines_x, lines_y)
    point.set_data([pivot.x], [pivot.y])
    return line,point

point = TwoDPoint(2,3)
gs = GrahamScan("/Users/sonja/PycharmProjects/ConvexHull/src/testData")

gs.findPivot()
gs.sortPoints()
intermediate_steps = gs.performGrahamScan()
#for intermediate_step in intermediate_steps:
#    for point in intermediate_step:
#        print point,
#    print
points = gs.points;
orig_x = [point.x for point in gs.points]
orig_y = [point.y for point in gs.points]

pivot = gs.points[0]
nums = len(gs.points)-1
fig,ax = plt.subplots(figsize=(7.5,7.5))
ax = plt.axes(xlim = (-10,10),ylim=(-10,10))
line, = ax.plot([],[],"k-")
point, = ax.plot([],[],"ro")

plt.scatter(orig_x,orig_y,color="k")

#anim = animation.FuncAnimation(fig,animate_order,init_func=init,frames=nums,interval=160,blit=True,repeat = False)
anim2 = animation.FuncAnimation(fig,animate_graham_scan,init_func=init,frames=len(intermediate_steps)+1,interval=1000,blit=True,repeat = True)


plt.show()