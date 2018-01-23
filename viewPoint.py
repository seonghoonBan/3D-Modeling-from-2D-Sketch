import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

import numpy as np
from scipy.optimize import fsolve
import scipy.optimize as opt
from csvParse import *
import math

import IPython
from sympy import nsolve

#FboxRIGHT FboxUP FboxDOWN BboxRIGHT BboxUP BboxDOWN sideFP1 sideFP2 sideBP1 sideBP2 topFP topBP
#120        93       -73    100      83     -67    [45,90] [-283,-63] [-86,89] [-284,-55]  [-208,106] [-236,96]

#FboxRIGHT=120
#FboxUP =93
#FboxDOWN =-73
#BboxRIGHT =100
#BboxUP =83
#BboxDOWN =-67
#ideFP1 =[37.10614470104024, 120.18473390645732]
#sideFP2 =[-283,-63]
#sideBP1 =[-86,89]
#sideBP2 =[-284,-55]
#topFP =[-208,106]
#topBP=[-236,96]

print(FboxRIGHT)
print(FboxUP)
print(FboxDOWN)
print(BboxRIGHT)
print(BboxUP)
print(BboxDOWN)
print(sideFP1)
print(sideFP2)
print(sideBP1) #-x
print(sideBP2) #-x
print(topFP)
print(topBP) #-x

def frontEq(z):
    global fd
    frontD=fd
    c=z[0]
    y=z[1]
    f=np.zeros(2)
    #print((c*(sideFP1[0]-frontD)-((1-c**2)**0.5)*(sideFP1[1]-y)))
    f[0]=(FboxDOWN*topFP[1]*math.cos(c))/((topFP[0]-frontD)*FboxRIGHT)-(((1-math.cos(c)**2)**0.5)*(sideFP2[0]-frontD)+math.cos(c)*(sideFP2[1]-y))/(math.cos(c)*(sideFP2[0]-frontD)-((1-math.cos(c)**2)**0.5)*(sideFP2[1]-y))
    f[1]=(FboxUP*topFP[1]*math.cos(c))/((topFP[0]-frontD)*FboxRIGHT)-(((1-math.cos(c)**2)**0.5)*(sideFP1[0]-frontD)+math.cos(c)*(sideFP1[1]-y))/(math.cos(c)*(sideFP1[0]-frontD)-((1-math.cos(c)**2)**0.5)*(sideFP1[1]-y))
    return f

def backEq(z):
    global bd
    backD=bd
    c=z[0]
    y=z[1]
    f=np.zeros(2)
    f[0]=(BboxDOWN*topBP[1]*math.cos(c))/((-topBP[0]-backD)*BboxRIGHT)-(((1-math.cos(c)**2)**0.5)*(-sideBP2[0]-backD)+math.cos(c)*(sideBP2[1]-y))/(math.cos(c)*(-sideBP2[0]-backD)-((1-math.cos(c)**2)**0.5)*(sideBP2[1]-y))
    f[1]=(BboxUP*topBP[1]*math.cos(c))/((-topBP[0]-backD)*BboxRIGHT)-(((1-math.cos(c)**2)**0.5)*(-sideBP1[0]-backD)+math.cos(c)*(sideBP1[1]-y))/(math.cos(c)*(-sideBP1[0]-backD)-((1-math.cos(c)**2)**0.5)*(sideBP1[1]-y))
    return f

def getFrontPoint(frontD):
    global fd
    fd=frontD
    z=opt.fsolve(frontEq,[0.0,0.0])
    fk=math.cos(z[0])*topFP[1]/((topFP[0]-frontD)*FboxRIGHT)*(-frontD)*2
    return math.cos(z[0]),z[1],fk


def getBackPoint(backD):
    global bd
    bd=backD
    z=opt.fsolve(backEq,[0.0,0.0])
    bk=math.cos(z[0])*topBP[1]/((-topBP[0]-backD)*BboxRIGHT)*(-backD)*2
    return math.cos(z[0]),z[1],bk

#fd=800
#print(frontEq([0.9999,0.0]))
frontD=-800
#print(nsolve(frontEq, [0.0, 0]))
print(getFrontPoint(-800))
#print("------------------------------------------------------------------------------")
print(getBackPoint(-1000))
#IPython.embed()
#print(getFrontPoint(-800))
#print(getBackPoint(-800))