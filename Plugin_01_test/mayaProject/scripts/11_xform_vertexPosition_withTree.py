import maya.cmds as cmds

myVerList = cmds.ls( selection=True, fl=True )

for ver in myVerList:
    verPos = cmds.xform( ver, q=True, ws=True, t=True )
    print verPos
    myT = tree()
    cmds.move( verPos[0], verPos[1], verPos[2], myT )
    
def tree():
    treeTrunk = mc.polyCylinder( r=0, h=6, sx=8, n="Tree_Trunk" )
    mc.move( 0,6/2.4,0, treeTrunk )
    
    treeBody = mc.polySphere( r=3, sx=8, sy=8, n="Tree_Body" )
    mc.move( 0,8,0, treeBody ) 
    
    mc.scale( 1,2,1, treeBody )
    mc.select( treeTrunk, treeBody )
    myTree = cmds.polyUnite( ch=False )
    cmds.rename( "Tree#" )

# ----------------------------------------------------->