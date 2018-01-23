from meshMaker import *
import numpy as np
import pymesh
import IPython
from viewPoint import *

FastMode =True

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
        sidetopfrontback=fixmesh.fix_mesh(sidetopfrontback,detail="normal")
    body=sidetopfrontback
    print("ALL DONE.. Saving as 'body.obj'")
    pymesh.meshio.save_mesh("%sbody.obj"%path, sidetopfrontback)





def frontGlass(path):
    print("Making front glass part")
    top = topMesh(triangualtion(top2),100)
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
    side = sideMesh(triangualtion(side8),200)
    if FastMode is False:
        side=fixmesh.fix_mesh(side,detail="normal")
    sideDoor = pymesh.boolean(side, body,operation="intersection",engine="cork")
    if FastMode is False:
        sideDoor=fixmesh.fix_mesh(sideDoor,detail="enormal")
    print("it's done.. Saving as 'sideDoor.obj'")
    pymesh.meshio.save_mesh("%ssideDoor.obj"%path, sideDoor)
    pymesh.meshio.save_mesh("sideDoortest.obj", sideDoor)

def backLight(ratioB,backD,backC,backH,path):
    print("Making back light part")
    back = backMeshH(triangualtion(back4),backD,backC,backH,ratioB)
    pymesh.meshio.save_mesh("%sbackLightTest.obj"%path, back)
    back=fixmesh.fix_mesh(back,detail="normal")
    backLight = pymesh.boolean(back, body,operation="intersection",engine="cork")
    if FastMode is False:
        backLight=fixmesh.fix_mesh(backLight,detail="enormal")
    print("it's done.. Saving as 'backLight.obj'")
    pymesh.meshio.save_mesh("%sbackLight.obj"%path, backLight)


def backGlassTop(path):
    print("Making back glass part")
    top = topMesh(triangualtion(top0),100)
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
        pass
        #back=fixmesh.fix_mesh(back,detail="normal")
    trunk = pymesh.boolean(back, body,operation="intersection",engine="cork")
    if FastMode is False:
        trunk=fixmesh.fix_mesh(trunk,detail="enormal")
    print("it's done.. Saving as 'trunk.obj'")
    pymesh.meshio.save_mesh("%strunk.obj"%path, trunk)

def backBumper(ratioB,backD,backC,backH,path):
    print("Making back bumper part")
    back = backMeshH(triangualtion(back6),backD,backC,backH,ratioB)
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
    front=fixmesh.fix_mesh(front,detail="normal")
    Grill = pymesh.boolean(front, body,operation="intersection",engine="cork")
    if FastMode is False:
        Grill=fixmesh.fix_mesh(Grill,detail="enormal")
    print("it's done.. Saving as 'grill.obj'")
    pymesh.meshio.save_mesh("%sgrill.obj"%path, Grill)

def frontBumper(ratioF,frontD,frontC,frontH,path):
    print("Making front bumper part")
    front = frontMeshH(triangualtion(front9),frontD,frontC,frontH,ratioF)
    if FastMode is False:
        pass
        #front=fixmesh.fix_mesh(front,detail="normal")
    frontBumper = pymesh.boolean(front, body,operation="intersection",engine="cork")
    if FastMode is False:
        frontBumper=fixmesh.fix_mesh(frontBumper,detail="enormal")
    print("it's done.. Saving as 'frontBumper.obj'")
    pymesh.meshio.save_mesh("%sfrontBumper.obj"%path, frontBumper)

def dataLoader(path):
    print("Load Body from obj file")
    global body
    body=pymesh.load_mesh("%sbody.obj"%path)

def partMakerAll(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,ID,path):
    bodyMaker(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,ID,path)
    
    frontGlass(path)
    headLight(ratioF,frontD,frontC,frontH,path)
    frontBumper(ratioF,frontD,frontC,frontH,path)
    backLight(ratioB,backD,backC,backH,path)
    backGlassTop(path)
    trunk(ratioB,backD,backC,backH,path)
    sideGlass(path)
    #sideDoor(path)
    backBumper(ratioB,backD,backC,backH,path)
    grill(ratioF,frontD,frontC,frontH,path)
    #backGlass(ratioB,backD,backC,backH,path)
    partMaker(frontD,backD,"sideDoor","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/",True)


def partMaker(frontD,backD,part,path,Mode):
    global FastMode
    FastMode=Mode

    ratioF=getFrontPoint(-frontD)[2]
    frontC=getFrontPoint(-frontD)[0]
    frontH=getFrontPoint(-frontD)[1]
    ratioB=getBackPoint(-backD)[2]
    backC=getBackPoint(-backD)[0]
    backH=getBackPoint(-backD)[1]

    if part is "body":
        bodyMaker(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,"%d_%d"%(frontD,backD),path)
    elif part is "frontGlass":
        dataLoader(path)
        rontGlass(path)
    elif part is "headLight":
        dataLoader(path)
        headLight(ratioF,frontD,frontC,frontH,path)
    elif part is "frontBumper":
        dataLoader(path)
        frontBumper(ratioF,frontD,frontC,frontH,path)
    elif part is "backLight":
        dataLoader(path)
        backLight(ratioB,backD,backC,backH,path)
    elif part is "backGlass":
        dataLoader(path)
        backGlassTop(path)
    elif part is "trunk":
        dataLoader(path)
        trunk(ratioB,backD,backC,backH,path)
    elif part is "sideGlass":
        dataLoader(path)
        sideGlass(path)
    elif part is "sideDoor":
        dataLoader(path)
        sideDoor(path)
    elif part is "backBumper":
        dataLoader(path)
        backBumper(ratioB,backD,backC,backH,path)
    elif part is "grill":
        dataLoader(path)
        grill(ratioF,frontD,frontC,frontH,path)
    elif part is "All":
        partMakerAll(ratioF,frontD,frontC,frontH,ratioB,backD,backC,backH,"%d_%d"%(frontD,backD),path)

frontD=800
backD=1000

partMaker(frontD,backD,"All","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/",True)

#print(getBackPoint(backD))
#partMakerAll(getFrontPoint(frontD)[2],-frontD,getFrontPoint(frontD)[0],getFrontPoint(frontD)[1],getBackPoint(backD)[2],-backD,getBackPoint(backD)[0],getBackPoint(backD)[1],"%d_%d"%(-frontD,-backD),"/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
#headLight2(getFrontPoint(frontD)[2],-frontD,getFrontPoint(frontD)[0],getFrontPoint(frontD)[1])

