# for the scene we need a plane and a selected vertex to move the cube to

import maya.cmds as mc

mySelection = mc.ls( selection=True )
print mySelection

mySelPosition = mc.xform( mySelection, q=True, ws=True, t=True )
print mySelPosition
# 01 let's build acube object
build = tree()
# 02 now let's move the cube to the selcted vertex position absulute position
mc.move( mySelPosition[0], mySelPosition[1], mySelPosition[2], build )

def tree():
    treeTrunk = mc.polyCylinder( r=0, h=6, sx=8, n="Tree_Trunk" )
    mc.move( 0,6/2.4,0, treeTrunk )
    
    treeBody = mc.polySphere( r=3, sx=8, sy=8, n="Tree_Body" )
    mc.move( 0,8,0, treeBody ) 
    
    mc.scale( 1,2,1, treeBody )
    mc.select( treeTrunk, treeBody )
    mc.group( n="Tree Group" )

# -------------------------------------------------------------->