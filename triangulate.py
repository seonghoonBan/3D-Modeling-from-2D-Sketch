import numpy as np
import IPython
from csvParse import *

import matplotlib.pyplot as plt
from triangle import triangulate, plot as tplot


def triangualtion(data):
    seg=[]
    holes = []
    for i in range(len(data)):
        if i != len(data)-1:
            seg.append([i,i+1])
        else :
            seg.append([len(data)-1,0])
    holes.append([0.0,120.0])
    inputMesh = {'vertices': None, 'holes': None, 'segments': None,}
    inputMesh['vertices']=data
    inputMesh['segments'] = np.array(seg)
    inputMesh['holes'] = np.array(holes,dtype='double')
    outputMesh = triangulate(inputMesh, 'pq20D')
    return outputMesh

#plt.figure(figsize=(14,14))
#ax = plt.subplot(111, aspect='equal')
#tplot.plot(ax, **cncfq20dt)
#plt.show()
#IPython.embed()
