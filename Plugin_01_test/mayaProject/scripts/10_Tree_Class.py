# Tree class

import maya.cmds as cmds

# sx stands for subdivisions
treeTrunk = cmds.polyCylinder( r=0, h=6, sx=8, n="Tree_Trunk" )
cmds.move( 0,6/2.0,0, treeTrunk )

treeBody = cmds.polySphere( r=3, sx=8, sy=8, n="Tree_Body" )
cmds.move( 0,8,0, treeBody ) 
cmds.scale( 1,2,1, treeBody )
cmds.select( treeTrunk, treeBody )
# this function merges the two geometry and the command ch erases the hystory
cmds.polyUnite( ch=False )
Uni_Tree = cmds.rename( "TREE" )
cmds.scale( 0.7,0.7,0.7, Uni_Tree )