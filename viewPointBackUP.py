import warnings
warnings.filterwarnings('ignore', 'The iteration is not making good progress')

import numpy as np
from scipy.optimize import fsolve
import scipy.optimize as opt
from csvParse import *

import IPython




def frontEq(z):
    global fd
    frontD=fd
    c=z[0]
    y=z[1]
    f=np.zeros(2)
    f[0]=(-73*106*c)/((-208-frontD)*120)-(((1-c**2)**0.5)*(-283-frontD)+c*(-63-y))/(c*(-283-frontD)-((1-c**2)**0.5)*(-63-y))
    f[1]=(93*106*c)/((-208-frontD)*120)-(((1-c**2)**0.5)*(45-frontD)+c*(90-y))/(c*(45-frontD)-((1-c**2)**0.5)*(90-y))
    return f
def backEq(z):
    global bd
    backD=bd
    c=z[0]
    y=z[1]
    f=np.zeros(2)
    f[0]=(-67*96*c)/((-236-backD)*100)-(((1-c**2)**0.5)*(-284-backD)+c*(-55-y))/(c*(-284-backD)-((1-c**2)**0.5)*(-55-y))
    f[1]=(83*96*c)/((-236-backD)*100)-(((1-c**2)**0.5)*(-86-backD)+c*(89-y))/(c*(-86-backD)-((1-c**2)**0.5)*(89-y))
    return f

def getFrontPoint(frontD):
    global fd
    fd=frontD
    z=opt.fsolve(frontEq,[0.99999,0.0])
    fk=z[0]*106/((-208-frontD)*120)*(-frontD)*2
    return z[0],z[1],fk


def getBackPoint(backD):
    global bd
    bd=backD
    z=opt.fsolve(backEq,[0.99999,0.0])
    bk=z[0]*96/((-236-backD)*100)*(-backD)*2
    return z[0],z[1],bk

#IPython.embed()
#print(getFrontPoint(-800))
#print(getBackPoint(-800))