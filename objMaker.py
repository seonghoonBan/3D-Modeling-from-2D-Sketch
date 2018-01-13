from meshMaker import *
import numpy as np
import pymesh
import IPython
from viewPoint import *

FastMode =False

def bodyMaker(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,ID,path):
    global body
    print("Making Side Mesh...")
    side = sideMesh(triangualtion(side1),200)
    pymesh.meshio.save_mesh("%ssidetest.obj"%path, side)
    print("Fixing Side Mesh...")
    #side=fixmesh.fix_mesh(side,detail="normal")
    print("Side Mesh Done")
    ##SIDE out
    #pymesh.meshio.save_mesh("objs/side_%s.obj"%ID, side)
    print("Making Top Mesh...")
    top = topMesh(triangualtion(top1),200)
    pymesh.meshio.save_mesh("%stoptest.obj"%path, top)
    print("Fixing Top Mesh...")
    #top=fixmesh.fix_mesh(top,detail="normal")
    print("Top Mesh Done")
    ##TOP out
    #pymesh.meshio.save_mesh("objs/top_%s.obj"%ID, top)
    print("Making Front Mesh...")
    front = frontMesh(triangualtion(front1),frontD,frontC,frontH,ratioF)
    pymesh.meshio.save_mesh("%sfronttest.obj"%path, front)
    print("Fixing Front Mesh...")
    #front=fixmesh.fix_mesh(front,detail="normal")
    print("Front Mesh Done")
    ##FRONT out
    #pymesh.meshio.save_mesh("objs/front_%s.obj"%ID, front)
    print("Making Back Mesh...")
    back = backMesh(triangualtion(back1),backD,backC,backH,ratioB)
    pymesh.meshio.save_mesh("%sbacktest.obj"%path, back)
    print("Fixing Back Mesh...")
    #back=fixmesh.fix_mesh(back,detail="normal")
    print("Back Mesh Done")
    ##BACK out
    #pymesh.meshio.save_mesh("objs/back_%s.obj"%ID, back)

    print("Intersect between SIDE-TOP")
    sidetop = pymesh.boolean(side, top,operation="intersection",engine="cork")
    print("Fixing SIDE-TOP Mesh..")
    #pymesh.meshio.save_mesh("objs/sidetop2_%s.obj"%ID, sidetop)
    if FastMode is False:
        sidetop=fixmesh.fix_mesh(sidetop,detail="normal")
    #pymesh.meshio.save_mesh("%ssidetop.obj"%path, sidetop)
    pymesh.meshio.save_mesh("objs/sidetop_%s.obj"%ID, sidetop)
    print("Intersect between SIDE-TOP-FRONT")
    sidetopfront = pymesh.boolean(sidetop, front,operation="intersection",engine="cork")
    print("Fixing SIDE-TOP-FRONT Mesh..")
    if FastMode is False:
        sidetopfront=fixmesh.fix_mesh(sidetopfront,detail="normal")
    pymesh.meshio.save_mesh("objs/sidetopfront_%s.obj"%ID, sidetopfront)
    print("Intersect between SIDE-TOP-FRONT-BACK")
    sidetopfrontback = pymesh.boolean(sidetopfront, back,operation="intersection",engine="cork")
    print("Fixing SIDE-TOP-FRONT-BACK Mesh..")
    pymesh.meshio.save_mesh("objs/sidetopfrontback%s.obj"%ID, sidetopfrontback)
    if FastMode is True:
        sidetopfrontback=fixmesh.fix_mesh(sidetopfrontback,detail="low")
    else:
        sidetopfrontback=fixmesh.fix_mesh(sidetopfrontback,detail="enormal")
    body=sidetopfrontback
    print("ALL DONE.. Saving as 'body.obj'")
    pymesh.meshio.save_mesh("objs/body%s.obj"%ID, sidetopfrontback)
    pymesh.meshio.save_mesh("%sbody.obj"%path, sidetopfrontback)





def frontGlass(path):
    print("Making front glass part")
    top = topMeshR(triangualtion(top2),100)
    if FastMode is False:
        top=fixmesh.fix_mesh(top,detail="normal")
    frontGlass = pymesh.boolean(top, body,operation="intersection",engine="cork")
    if FastMode is False:
        frontGlass=fixmesh.fix_mesh(frontGlass,detail="enormal")
    print("it's done.. Saving as 'frontGlass.obj'")
    pymesh.meshio.save_mesh("%sfrontGlass.obj"%path, frontGlass)

def headLight(ratioF,frontD,frontC,frontH,path):
    print("Making head light part")
    front = frontMeshH(triangualtion(front4),frontD,frontC,frontH,ratioF)
    #front=fixmesh.fix_mesh(front,detail="normal")
    headLight = pymesh.boolean(front, body,operation="intersection",engine="cork")
    if FastMode is False:
        headLight=fixmesh.fix_mesh(headLight,detail="enormal")
    print("it's done.. Saving as 'headLight.obj'")
    pymesh.meshio.save_mesh("%sheadLight.obj"%path, headLight)

def sideGlass(path):
    print("Making side glass part")
    side = sideMesh(triangualtion(side2),200)
    if FastMode is False:
        side=fixmesh.fix_mesh(side,detail="normal")
    sideGlass = pymesh.boolean(side, body,operation="intersection",engine="cork")
    pymesh.meshio.save_mesh("objs/sideglassTest.obj", sideGlass)
    if FastMode is False:
        sideGlass=fixmesh.fix_mesh(sideGlass,detail="enormal")
    print("it's done.. Saving as 'sideGlass.obj'")
    pymesh.meshio.save_mesh("%ssideGlass.obj"%path, sideGlass)

def sideDoor(path):
    print("Making side door part")
    side = sideMeshR(triangualtion(side8),200)
    if FastMode is False:
        side=fixmesh.fix_mesh(side,detail="normal")
    sideDoor = pymesh.boolean(side, body,operation="intersection",engine="cork")
    if FastMode is False:
        sideDoor=fixmesh.fix_mesh(sideDoor,detail="enormal")
    print("it's done.. Saving as 'sideDoor.obj'")
    pymesh.meshio.save_mesh("%ssideDoor.obj"%path, sideDoor)

def backLight(ratioB,backD,backC,backH,path):
    print("Making back light part")
    back = backMeshH(triangualtion(back4),backD,backC,backH,ratioB)
    pymesh.meshio.save_mesh("%sbackLightTest.obj"%path, back)
    #back=fixmesh.fix_mesh(back,detail="normal")
    backLight = pymesh.boolean(back, body,operation="intersection",engine="igl")
    if FastMode is False:
        backLight=fixmesh.fix_mesh(backLight,detail="enormal")
    print("it's done.. Saving as 'backLight.obj'")
    pymesh.meshio.save_mesh("%sbackLight.obj"%path, backLight)


def backGlassTop(path):
    print("Making back glass part")
    top = topMeshR(triangualtion(top0),100)
    #pymesh.meshio.save_mesh("objs/backglassTest.obj", top)
    #top=fixmesh.fix_mesh(top,detail="normal")
    backGlass = pymesh.boolean(top, body,operation="intersection",engine="cork")
    if FastMode is False:
        backGlass=fixmesh.fix_mesh(backGlass,detail="enormal")
    print("it's done.. Saving as 'backGlass.obj'")
    pymesh.meshio.save_mesh("%sbackGlass.obj"%path, backGlass)


def backGlass(ratioB,backD,backC,backH,path):
    print("Making back glass part")
    back = backMesh(triangualtion(back2),backD,backC,backH,ratioB)
    if FastMode is False:
        back=fixmesh.fix_mesh(back,detail="normal")
    backGlass = pymesh.boolean(back, body,operation="intersection",engine="cork")
    if FastMode is False:
        backGlass=fixmesh.fix_mesh(backGlass,detail="enormal")
    print("it's done.. Saving as 'backGlass.obj'")
    pymesh.meshio.save_mesh("%sbackGlass.obj"%path, backGlass)

def trunk(ratioB,backD,backC,backH,path):
    print("Making trunk part")
    back = backMeshH(triangualtion(back3),backD,backC,backH,ratioB)
    if FastMode is False:
        back=fixmesh.fix_mesh(back,detail="normal")
    trunk = pymesh.boolean(back, body,operation="intersection",engine="cork")
    if FastMode is False:
        trunk=fixmesh.fix_mesh(trunk,detail="enormal")
    print("it's done.. Saving as 'trunk.obj'")
    pymesh.meshio.save_mesh("%strunk.obj"%path, trunk)

def backBumper(ratioB,backD,backC,backH,path):
    print("Making back bumper part")
    back = backMeshHR(triangualtion(back6),backD,backC,backH,ratioB)
    pymesh.meshio.save_mesh("%sbackBumperTest.obj"%path, back)
    #back=fixmesh.fix_mesh(back,detail="normal")
    backBumper = pymesh.boolean(back, body,operation="intersection",engine="cork")
    if FastMode is False:
        backBumper=fixmesh.fix_mesh(backBumper,detail="enormal")
    print("it's done.. Saving as 'backBumper.obj'")
    pymesh.meshio.save_mesh("%sbackBumper.obj"%path, backBumper)

def grill(ratioF,frontD,frontC,frontH,path):
    print("Making grill part")
    front = frontMeshH(triangualtion(front5),frontD,frontC,frontH,ratioF)
    #front=fixmesh.fix_mesh(front,detail="normal")
    Grill = pymesh.boolean(front, body,operation="intersection",engine="igl")
    if FastMode is False:
        Grill=fixmesh.fix_mesh(Grill,detail="enormal")
    print("it's done.. Saving as 'grill.obj'")
    pymesh.meshio.save_mesh("%sgrill.obj"%path, Grill)

def frontBumper(ratioF,frontD,frontC,frontH,path):
    print("Making front bumper part")
    front = frontMeshHR(triangualtion(front9),frontD,frontC,frontH,ratioF)
    if FastMode is False:
        front=fixmesh.fix_mesh(front,detail="normal")
    frontBumper = pymesh.boolean(front, body,operation="intersection",engine="igl")
    if FastMode is False:
        frontBumper=fixmesh.fix_mesh(frontBumper,detail="enormal")
    print("it's done.. Saving as 'frontBumper.obj'")
    pymesh.meshio.save_mesh("%sfrontBumper.obj"%path, frontBumper)

def dataLoader(path):
    print("Load Body from obj file")
    global body
    body=pymesh.load_mesh("%sbody.obj"%path)

def partMaker(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,ID,path):
    #bodyMaker(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,ID,path)
    dataLoader(path)
    frontGlass(path)
    headLight(ratioF,frontD,frontC,frontH,path)
    frontBumper(ratioF,frontD,frontC,frontH,path)
    backLight(ratioB,backD,backC,backH,path)
    backGlassTop(path)
    trunk(ratioB,backD,backC,backH,path)
    sideGlass(path)
    sideDoor(path)
    backBumper(ratioB,backD,backC,backH,path)
    grill(ratioF,frontD,frontC,frontH,path)
    
    
    #backGlass(ratioB,backD,backC,backH,path)
    
    

#partMaker(2.6,600,3.0,576,"700_900_2.4","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
#partMaker(3.0,600,2.98,576,"700_900_3.4","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
#partMaker(2.3828,600,frontC,2.7150,576,frontC,"ID","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
#bodyMaker(2.3828,800,0.99809257089501911959835729058562,25.78,2.7150,800,0.99689621914928869357692626128948,45.314,"800","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
frontD=-800
backD=-1000
#print(getBackPoint(backD))
partMaker(getFrontPoint(frontD)[2],-frontD,getFrontPoint(frontD)[0],getFrontPoint(frontD)[1],getBackPoint(backD)[2],-backD,getBackPoint(backD)[0],getBackPoint(backD)[1],"%d_%d"%(-frontD,-backD),"/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 




#print(getFrontPoint(frontD))
#print(getBackPoint(backD))
#ratioF,frontD,ratioB,backD,ID)

''' 700, 900, 2.4
bodyMaker(2.8,500,700,"500_700_2.8")
bodyMaker(2.6,500,700,"500_700_2.6")
bodyMaker(2.4,500,700,"500_700_2.4")
bodyMaker(2.2,500,700,"500_700_2.2")
bodyMaker(2,500,700,"500_700_2")

bodyMaker(2.8,600,800,"600_800_2.8")
bodyMaker(2.6,600,800,"600_800_2.6")
bodyMaker(2.4,600,800,"600_800_2.4")
bodyMaker(2.2,600,800,"600_800_2.2")
bodyMaker(2,600,800,"600_800_2")

bodyMaker(2.8,700,900,"700_900_2.8")
bodyMaker(2.6,700,900,"700_900_2.6")
bodyMaker(2.4,700,900,"700_900_2.4")
bodyMaker(2.2,700,900,"700_900_2.2")
bodyMaker(2,700,900,"700_900_2")

def frontGlassMaker(ratioF,frontD):
    top = topMesh(triangualtion(top2),200)
    top=fixmesh.fix_mesh(top,detail="normal")
    front = frontMesh(triangualtion(front2),frontD,ratioF)
    front=fixmesh.fix_mesh(front,detail="normal")
    frontGlass = pymesh.boolean(front, top,operation="intersection",engine="cork")
    frontGlass=fixmesh.fix_mesh(frontGlass,detail="normal")
    print("front glass part is done.. Saving as 'frontGlass.obj'")
    pymesh.meshio.save_mesh("objs/frontGlass.obj", frontGlass)
'''