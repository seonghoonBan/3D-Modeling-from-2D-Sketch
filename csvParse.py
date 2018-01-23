import csv
import IPython

import numpy as np

#path='bmw 5-series 2013/'
#path='bmw 5-series 2007/'
#path='acura_2007_bahn/'
path='acura2007_2/'
#path='acura2010/'
#path='acura2012/'
#path='bmw2010/'

##---------FRONT data parse
with open('%s1_1.txt'%path,'r') as tsvin:
    global FboxRIGHT
    global FboxUP
    global FboxDOWN
    FboxLEFT=0
    FboxRIGHT=0
    FboxUP=0
    FboxDOWN=0
    tsvin = csv.reader(tsvin, delimiter=' ')
    front1temp=[]
    for row in tsvin:
        front1temp.append([float(row[0]),float(row[1])])
        if float(row[0])>FboxRIGHT:
            FboxRIGHT=float(row[0])
        if float(row[0])<FboxLEFT:
            FboxLEFT=float(row[0])
        if float(row[1])>FboxUP:
            FboxUP=float(row[1])
        if float(row[1])<FboxDOWN:
            FboxDOWN=float(row[1])
    FboxRIGHT=(abs(FboxRIGHT)+abs(FboxLEFT))*0.5
front1=np.array(front1temp)

with open('%s1_2.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    front2temp=[]
    for row in tsvin:
        front2temp.append([float(row[0]),float(row[1])])
front2=np.array(front2temp)

with open('%s1_3.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    front3temp=[]
    for row in tsvin:
        front3temp.append([float(row[0]),float(row[1])])
front3=np.array(front3temp)

with open('%s1_4.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    front4temp=[]
    for row in tsvin:
        front4temp.append([float(row[0]),float(row[1])])
front4=np.array(front4temp)

with open('%s1_5.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    front5temp=[]
    for row in tsvin:
        front5temp.append([float(row[0]),float(row[1])])
front5=np.array(front5temp)

with open('%s1_9.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    front9temp=[]
    for row in tsvin:
        front9temp.append([float(row[0]),float(row[1])])
front9=np.array(front9temp)




##---------SIDE data parse
with open('%s2_1.txt'%path,'r') as tsvin:
    global sideFP1
    global sideFP2
    global sideBP1
    global sideBP2
    sideUP=0
    sideLEFT=0
    sideRIGHT=0
    sideFP1=[60,0]
    sideFP2=[0,0]
    sideBP1=[0,0]
    sideBP2=[0,0]
    tsvin = csv.reader(tsvin, delimiter=' ')
    side1temp=[]
    for row in tsvin:
        side1temp.append([float(row[0]),float(row[1])])
        if float(row[1])>sideUP:
            sideUP=float(row[1])
        if float(row[0])<sideLEFT:
            sideLEFT=float(row[0])
        if float(row[0])>sideRIGHT:
            sideRIGHT=float(row[0])
    for row in side1temp:
        if float(row[0])<sideLEFT+10:
            if float(row[1])<sideFP2[1]:
                sideFP2=[float(row[0]),float(row[1])]
        if float(row[0])>sideRIGHT-10:
            if float(row[1])<sideBP2[1]:
                sideBP2=[float(row[0]),float(row[1])]
        if float(row[1])>sideUP-1:
            if float(row[0])<sideFP1[0]:
                sideFP1=[float(row[0]),float(row[1])]
        if float(row[1])>sideUP-1:
            if float(row[0])>sideBP1[0]:
                sideBP1=[float(row[0]),float(row[1])]
side1=np.array(side1temp)

with open('%s2_2.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side2temp=[]
    for row in tsvin:
        side2temp.append([float(row[0]),float(row[1])])
side2=np.array(side2temp)

with open('%s2_3.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side3temp=[]
    for row in tsvin:
        side3temp.append([float(row[0]),float(row[1])])
side3=np.array(side3temp)

with open('%s2_4.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side4temp=[]
    for row in tsvin:
        side4temp.append([float(row[0]),float(row[1])])
side4=np.array(side4temp)

with open('%s2_5.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side5temp=[]
    for row in tsvin:
        side5temp.append([float(row[0]),float(row[1])])
side5=np.array(side5temp)

with open('%s2_6.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side6temp=[]
    for row in tsvin:
        side6temp.append([float(row[0]),float(row[1])])
side6=np.array(side6temp)

with open('%s2_7.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side7temp=[]
    for row in tsvin:
        side7temp.append([float(row[0]),float(row[1])])
side7=np.array(side7temp)

with open('%s2_8.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    side8temp=[]
    for row in tsvin:
        side8temp.append([float(row[0]),float(row[1])])
side8=np.array(side8temp)





##---------BACK data parse
with open('%s3_1.txt'%path,'r') as tsvin:
    global BboxRIGHT
    global BboxUP
    global BboxDOWN
    BboxLEFT=0
    BboxRIGHT =0
    BboxUP =0
    BboxDOWN =0
    tsvin = csv.reader(tsvin, delimiter=' ')
    back1temp=[]
    for row in tsvin:
        back1temp.append([float(row[0]),float(row[1])])
        if float(row[0])>BboxRIGHT:
            BboxRIGHT=float(row[0])
        if float(row[0])<BboxLEFT:
            BboxLEFT=float(row[0])
        if float(row[1])>BboxUP:
            BboxUP=float(row[1])
        if float(row[1])<BboxDOWN:
            BboxDOWN=float(row[1])
    BboxRIGHT=(abs(BboxRIGHT)+abs(BboxLEFT))*0.5
back1=np.array(back1temp)

with open('%s3_2.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    back2temp=[]
    for row in tsvin:
        back2temp.append([float(row[0]),float(row[1])])
back2=np.array(back2temp)

with open('%s3_3.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    back3temp=[]
    for row in tsvin:
        back3temp.append([float(row[0]),float(row[1])])
back3=np.array(back3temp)

with open('%s3_4.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    back4temp=[]
    for row in tsvin:
        back4temp.append([float(row[0]),float(row[1])])
back4=np.array(back4temp)

with open('%s3_6.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    back6temp=[]
    for row in tsvin:
        back6temp.append([float(row[0]),float(row[1])])
back6=np.array(back6temp)





##---------TOP data parse
# 1->0 2->5 3->4 5->9 6->3 8->6 9->7 0-8
with open('%s4_8.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top0temp=[]
    for row in tsvin:
        top0temp.append([float(row[0]),float(row[1])])
top0=np.array(top0temp)


with open('%s4_0.txt'%path,'r') as tsvin:
    global topFP
    global topBP
    topUP=0
    topFP=[0,0]
    topBP=[0,0]

    tsvin = csv.reader(tsvin, delimiter=' ')
    top1temp=[]
    for row in tsvin:
        top1temp.append([float(row[0]),float(row[1])])
        if float(row[1])>topUP:
            topUP=float(row[1])
    for row in top1temp:
        if float(row[1])>topUP-5:
            if float(row[0])<topFP[0]:
                topFP=[float(row[0]),float(row[1])]
        if float(row[1])>topUP-5:
            if float(row[0])>topBP[0]:
                topBP=[float(row[0]),float(row[1])]   
top1=np.array(top1temp)

with open('%s4_5.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top2temp=[]
    for row in tsvin:
        top2temp.append([float(row[0]),float(row[1])])
top2=np.array(top2temp)

with open('%s4_4.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top3temp=[]
    for row in tsvin:
        top3temp.append([float(row[0]),float(row[1])])
top3=np.array(top3temp)

with open('%s4_4.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top4temp=[]
    for row in tsvin:
        top4temp.append([float(row[0]),float(row[1])])
top4=np.array(top4temp)

with open('%s4_9.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top5temp=[]
    for row in tsvin:
        top5temp.append([float(row[0]),float(row[1])])
top5=np.array(top5temp)

with open('%s4_3.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top6temp=[]
    for row in tsvin:
        top6temp.append([float(row[0]),float(row[1])])
top6=np.array(top6temp)

with open('%s4_7.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top7temp=[]
    for row in tsvin:
        top7temp.append([float(row[0]),float(row[1])])
top7=np.array(top7temp)

with open('%s4_6.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top8temp=[]
    for row in tsvin:
        top8temp.append([float(row[0]),float(row[1])])
top8=np.array(top8temp)

with open('%s4_7.txt'%path,'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter=' ')
    top9temp=[]
    for row in tsvin:
        top9temp.append([float(row[0]),float(row[1])])
top9=np.array(top9temp)