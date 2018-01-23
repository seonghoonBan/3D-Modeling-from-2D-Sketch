from triangulate import *
import numpy as np
import pymesh
import IPython
import math

import fixmesh


def topMesh(data,thickness):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],100-thickness,data['vertices'][i][1]])
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],100,data['vertices'][i][1]])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][1],data['triangles'][i][2]])
        faces.append([data['triangles'][i][0]+len(data['vertices']),data['triangles'][i][2]+len(data['vertices']),data['triangles'][i][1]+len(data['vertices'])])
    
    for i in range(1500):
        if i !=1499:
            faces.append([i,i+1,len(data['vertices'])+i])
            faces.append([i+1,len(data['vertices'])+i+1,len(data['vertices'])+i])
        else:
            faces.append([1499,0,len(data['vertices'])+1499])
            faces.append([0,len(data['vertices']),len(data['vertices'])+1499])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def sideMesh(data,thickness):
    vertices=[]
    faces=[]
    print(len(data['vertices']))
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],data['vertices'][i][1],-thickness/2])
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],data['vertices'][i][1],thickness/2])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
        faces.append([data['triangles'][i][0]+len(data['vertices']),data['triangles'][i][1]+len(data['vertices']),data['triangles'][i][2]+len(data['vertices'])])
    
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices'])+i,i+1])
            faces.append([i+1,len(data['vertices'])+i,len(data['vertices'])+i+1])
        else:
            faces.append([1499,len(data['vertices'])+1499,0])
            faces.append([0,len(data['vertices'])+1499,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def frontMesh(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        
        
        y=data['vertices'][i][1]*ratio
        z=data['vertices'][i][0]*ratio
        c=cos
        s=-math.sqrt(1-c*c)
        x=distance*2/cos
        vertices.append([c*x-s*y-distance,s*x+c*y+height,z])
        #vertices.append([thickness,data['vertices'][i][1]*ratio,data['vertices'][i][0]*ratio])
    vertices.append([-distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices']),i+1])
        else:
            faces.append([1499,len(data['vertices']),0])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)

def frontMeshH(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        
        
        y=data['vertices'][i][1]*ratio*0.5
        z=data['vertices'][i][0]*ratio*0.5
        c=cos
        s=-math.sqrt(1-c*c)
        x=distance/cos
        vertices.append([c*x-s*y-distance,s*x+c*y+height,z])
        #vertices.append([thickness,data['vertices'][i][1]*ratio,data['vertices'][i][0]*ratio])
    vertices.append([-distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices']),i+1])
        else:
            faces.append([1499,len(data['vertices']),0])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def backMesh(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        y=data['vertices'][i][1]*ratio
        z=-data['vertices'][i][0]*ratio
        c=cos
        s=math.sqrt(1-c*c)
        x=-distance*2/cos
        vertices.append([c*x-s*y+distance,s*x+c*y+height,z])
        #(data['vertices'][i][1]-42)*ratio,-data['vertices'][i][0]*ratio])
    vertices.append([distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices']),i+1])
        else:
            faces.append([1499,len(data['vertices']),0])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)

def backMeshH(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        y=data['vertices'][i][1]*ratio*0.5
        z=-data['vertices'][i][0]*ratio*0.5
        c=cos
        s=math.sqrt(1-c*c)
        x=-distance/cos
        vertices.append([c*x-s*y+distance,s*x+c*y+height,z])
        #(data['vertices'][i][1]-42)*ratio,-data['vertices'][i][0]*ratio])
    vertices.append([distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices']),i+1])
        else:
            faces.append([1499,len(data['vertices']),0])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)







##------------------



def topMeshR(data,thickness):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],100-thickness,data['vertices'][i][1]])
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],100,data['vertices'][i][1]])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][1],data['triangles'][i][2]])
        faces.append([data['triangles'][i][0]+len(data['vertices']),data['triangles'][i][2]+len(data['vertices']),data['triangles'][i][1]+len(data['vertices'])])
    
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices'])+i,i+1])
            faces.append([i+1,len(data['vertices'])+i,len(data['vertices'])+i+1])
        else:
            faces.append([1499,len(data['vertices'])+1499,0])
            faces.append([0,len(data['vertices'])+1499,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def sideMeshR(data,thickness):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],data['vertices'][i][1],-thickness/2])
    for i in range(len(data['vertices'])):
        vertices.append([data['vertices'][i][0],data['vertices'][i][1],thickness/2])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
        faces.append([data['triangles'][i][0]+len(data['vertices']),data['triangles'][i][1]+len(data['vertices']),data['triangles'][i][2]+len(data['vertices'])])
    
    for i in range(1500):
        if i !=1499:
            faces.append([i,len(data['vertices'])+i,i+1])
            faces.append([i+1,len(data['vertices'])+i,len(data['vertices'])+i+1])
        else:
            faces.append([1499,len(data['vertices'])+1499,0])
            faces.append([0,len(data['vertices'])+1499,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def frontMeshR(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        
        
        y=data['vertices'][i][1]*ratio
        z=data['vertices'][i][0]*ratio
        c=cos
        s=-math.sqrt(1-c*c)
        x=distance*2/cos
        vertices.append([c*x-s*y-distance,s*x+c*y+height,z])
        #vertices.append([thickness,data['vertices'][i][1]*ratio,data['vertices'][i][0]*ratio])
    vertices.append([-distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][1],data['triangles'][i][2]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,i+1,len(data['vertices'])])
        else:
            faces.append([1499,0,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)

def frontMeshHR(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        
        
        y=data['vertices'][i][1]*ratio*0.5
        z=data['vertices'][i][0]*ratio*0.5
        c=cos
        s=-math.sqrt(1-c*c)
        x=distance/cos
        vertices.append([c*x-s*y-distance,s*x+c*y+height,z])
        #vertices.append([thickness,data['vertices'][i][1]*ratio,data['vertices'][i][0]*ratio])
    vertices.append([-distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][2],data['triangles'][i][1]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,i+1,len(data['vertices'])])
        else:
            faces.append([1499,0,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


def backMeshR(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        y=data['vertices'][i][1]*ratio
        z=-data['vertices'][i][0]*ratio
        c=cos
        s=math.sqrt(1-c*c)
        x=-distance*2/cos
        vertices.append([c*x-s*y+distance,s*x+c*y+height,z])
        #(data['vertices'][i][1]-42)*ratio,-data['vertices'][i][0]*ratio])
    vertices.append([distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][1],data['triangles'][i][2]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,i+1,len(data['vertices'])])
        else:
            faces.append([1499,0,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)

def backMeshHR(data,distance,cos,height,ratio):
    vertices=[]
    faces=[]
    for i in range(len(data['vertices'])):
        y=data['vertices'][i][1]*ratio*0.5
        z=-data['vertices'][i][0]*ratio*0.5
        c=cos
        s=math.sqrt(1-c*c)
        x=-distance/cos
        vertices.append([c*x-s*y+distance,s*x+c*y+height,z])
        #(data['vertices'][i][1]-42)*ratio,-data['vertices'][i][0]*ratio])
    vertices.append([distance,height,0])
    vertices=np.array(vertices)

    for i in range(len(data['triangles'])):
        faces.append([data['triangles'][i][0],data['triangles'][i][1],data['triangles'][i][2]])
    for i in range(1500):
        if i !=1499:
            faces.append([i,i+1,len(data['vertices'])])
        else:
            faces.append([1499,0,len(data['vertices'])])
    faces=np.array(faces)
    return pymesh.form_mesh(vertices, faces)


