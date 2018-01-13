from meshMaker import *
import numpy as np
import pymesh
import IPython


def bodyMaker(ratioF,frontD,ratioB,backD,ID,path):
    global body
    print("Making Side Mesh...")
    side = sideMesh(triangualtion(side1),200)
    print("Fixing Side Mesh...")
    side=fixmesh.fix_mesh(side,detail="ehigh")
    print("Side Mesh Done")
    ##SIDE out
    pymesh.meshio.save_mesh("objs/side_%s.obj"%ID, side)
    print("Making Top Mesh...")
    top = topMesh(triangualtion(top1),200)
    print("Fixing Top Mesh...")
    top=fixmesh.fix_mesh(top,detail="ehigh")
    print("Top Mesh Done")
    ##TOP out
    pymesh.meshio.save_mesh("objs/top_%s.obj"%ID, top)
    print("Making Front Mesh...")
    front = frontMesh(triangualtion(front1),frontD,ratioF)
    print("Fixing Front Mesh...")
    front=fixmesh.fix_mesh(front,detail="ehigh")
    print("Front Mesh Done")
    ##FRONT out
    pymesh.meshio.save_mesh("objs/front_%s.obj"%ID, front)
    print("Making Back Mesh...")
    back = backMesh(triangualtion(back1),backD,ratioB)
    print("Fixing Back Mesh...")
    back=fixmesh.fix_mesh(back,detail="ehigh")
    print("Back Mesh Done")
    ##BACK out
    pymesh.meshio.save_mesh("objs/back_%s.obj"%ID, back)

    print("Intersect between SIDE-TOP")
    sidetop = pymesh.boolean(side, top,operation="intersection",engine="igl")
    print("Fixing SIDE-TOP Mesh..")
    sidetop=fixmesh.fix_mesh(sidetop,detail="ehigh")
    pymesh.meshio.save_mesh("%ssidetop.obj"%path, sidetop)
    #pymesh.meshio.save_mesh("objs/sidetop_%s.obj"%ID, sidetop)
    print("Intersect between SIDE-TOP-FRONT")
    sidetopfront = pymesh.boolean(sidetop, front,operation="intersection",engine="igl")
    print("Fixing SIDE-TOP-FRONT Mesh..")
    sidetopfront=fixmesh.fix_mesh(sidetopfront,detail="ehigh")
    pymesh.meshio.save_mesh("objs/sidetopfront_%s.obj"%ID, sidetopfront)
    print("Intersect between SIDE-TOP-FRONT-BACK")
    sidetopfrontback = pymesh.boolean(sidetopfront, back,operation="intersection",engine="igl")
    print("Fixing SIDE-TOP-FRONT-BACK Mesh..")
    sidetopfrontback=fixmesh.fix_mesh(sidetopfrontback,detail="ehigh")
    body=sidetopfrontback
    print("ALL DONE.. Saving as 'body.obj'")
    pymesh.meshio.save_mesh("objs/body%s.obj"%ID, sidetopfrontback)
    pymesh.meshio.save_mesh("%sbody.obj"%path, sidetopfrontback)
    #IPython.embed()





def frontGlass(path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    top = topMesh(triangualtion(top2),200)
    top=fixmesh.fix_mesh(top,detail="ehigh")
    frontGlass = pymesh.boolean(top, body,operation="intersection",engine="igl")
    frontGlass=fixmesh.fix_mesh(frontGlass,detail="ehigh")
    print("front glass part is done.. Saving as 'frontGlass.obj'")
    pymesh.meshio.save_mesh("%sfrontGlass.obj"%path, frontGlass)

def headLight(ratioF,frontD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    front = frontMesh(triangualtion(front4),frontD,ratioF)
    front=fixmesh.fix_mesh(front,detail="ehigh")
    headLight = pymesh.boolean(front, body,operation="intersection",engine="igl")
    headLight=fixmesh.fix_mesh(headLight,detail="ehigh")
    print("front glass part is done.. Saving as 'headLight.obj'")
    pymesh.meshio.save_mesh("%sheadLight.obj"%path, headLight)

def sideGlass(path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    side = sideMesh(triangualtion(side2),200)
    side=fixmesh.fix_mesh(side,detail="ehigh")
    sideGlass = pymesh.boolean(side, body,operation="intersection",engine="igl")
    sideGlass=fixmesh.fix_mesh(sideGlass,detail="ehigh")
    print("front glass part is done.. Saving as 'sideGlass.obj'")
    pymesh.meshio.save_mesh("%ssideGlass.obj"%path, sideGlass)

def sideDoor(path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    side = sideMesh(triangualtion(side8),200)
    side=fixmesh.fix_mesh(side,detail="ehigh")
    sideDoor = pymesh.boolean(side, body,operation="intersection",engine="igl")
    sideDoor=fixmesh.fix_mesh(sideDoor,detail="ehigh")
    print("front glass part is done.. Saving as 'sideDoor.obj'")
    pymesh.meshio.save_mesh("%ssideDoor.obj"%path, sideDoor)

def backLight(ratioB,backD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    back = backMesh(triangualtion(back4),backD,ratioB)
    back=fixmesh.fix_mesh(back,detail="ehigh")
    backLight = pymesh.boolean(back, body,operation="intersection",engine="igl")
    backLight=fixmesh.fix_mesh(backLight,detail="ehigh")
    print("front glass part is done.. Saving as 'backLight.obj'")
    pymesh.meshio.save_mesh("%sbackLight.obj"%path, backLight)

def backGlass(ratioB,backD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    back = backMesh(triangualtion(back2),backD,ratioB)
    back=fixmesh.fix_mesh(back,detail="ehigh")
    backGlass = pymesh.boolean(back, body,operation="intersection",engine="igl")
    backGlass=fixmesh.fix_mesh(backGlass,detail="ehigh")
    print("front glass part is done.. Saving as 'backGlass.obj'")
    pymesh.meshio.save_mesh("%sbackGlass.obj"%path, backGlass)

def trunk(ratioB,backD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    back = backMesh(triangualtion(back3),backD,ratioB)
    back=fixmesh.fix_mesh(back,detail="ehigh")
    trunk = pymesh.boolean(back, body,operation="intersection",engine="igl")
    trunk=fixmesh.fix_mesh(trunk,detail="ehigh")
    print("front glass part is done.. Saving as 'trunk.obj'")
    pymesh.meshio.save_mesh("%strunk.obj"%path, trunk)

def backBumper(ratioB,backD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    back = backMesh(triangualtion(back6),backD,ratioB)
    back=fixmesh.fix_mesh(back,detail="ehigh")
    backBumper = pymesh.boolean(back, body,operation="intersection",engine="igl")
    backBumper=fixmesh.fix_mesh(backBumper,detail="ehigh")
    print("front glass part is done.. Saving as 'backBumper.obj'")
    pymesh.meshio.save_mesh("%sbackBumper.obj"%path, backBumper)

def grill(ratioF,frontD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    front = frontMesh(triangualtion(front5),frontD,ratioF)
    front=fixmesh.fix_mesh(front,detail="ehigh")
    Grill = pymesh.boolean(front, body,operation="intersection",engine="igl")
    Grill=fixmesh.fix_mesh(Grill,detail="ehigh")
    print("front glass part is done.. Saving as 'grill.obj'")
    #pymesh.meshio.save_mesh("objs/grill.obj", front)
    pymesh.meshio.save_mesh("%sgrill.obj"%path, Grill)

def frontBumper(ratioF,frontD,path):
    #body = pymesh.load_mesh("objs/body_700_900_2.4.obj")
    front = frontMesh(triangualtion(front9),frontD,ratioF)
    front=fixmesh.fix_mesh(front,detail="ehigh")
    frontBumper = pymesh.boolean(front, body,operation="intersection",engine="igl")
    frontBumper=fixmesh.fix_mesh(frontBumper,detail="ehigh")
    print("front glass part is done.. Saving as 'frontBumper.obj'")
    pymesh.meshio.save_mesh("%sfrontBumper.obj"%path, frontBumper)

def dataLoader(path):
    global body
    body=pymesh.load_mesh("%sbody.obj"%path)

def partMaker(ratioF,frontD,ratioB,backD,ID,path):
    bodyMaker(ratioF,frontD,ratioB,backD,ID,path)
    #dataLoader(path)
    frontGlass(path)
    headLight(ratioF,frontD,path)
    frontBumper(ratioF,frontD,path)
    backLight(ratioB,backD,path)
    backGlass(ratioB,backD,path)
    trunk(ratioB,backD,path)
    sideGlass(path)
    sideDoor(path)
    backBumper(ratioB,backD,path)
    grill(ratioF,frontD,path)
    

#partMaker(2.6,600,3.0,576,"700_900_2.4","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
partMaker(3.05,600,2.98,576,"700_900_3.4","/Users/seonghoonban/Dropbox/BS01-AutomatedCarDesign/Prgram/CarModelFromPython/Assets/") 
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
    frontGlass = pymesh.boolean(front, top,operation="intersection",engine="igl")
    frontGlass=fixmesh.fix_mesh(frontGlass,detail="normal")
    print("front glass part is done.. Saving as 'frontGlass.obj'")
    pymesh.meshio.save_mesh("objs/frontGlass.obj", frontGlass)
'''