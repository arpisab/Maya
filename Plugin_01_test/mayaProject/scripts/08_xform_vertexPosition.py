# for the scene we need a plane and a selected vertex to move the cube to

import maya.cmds as mc

mySelection = mc.ls( selection=True )
print mySelection

mySelPosition = mc.xform( mySelection, q=True, ws=True, t=True )
print mySelPosition
# 01 let's build acube object
build = mc.polyCube()
# 02 now let's move the cube to the selcted vertex position absulute position
mc.move( mySelPosition[0], mySelPosition[1], mySelPosition[2], build )


# -------------------------------------------------------------->