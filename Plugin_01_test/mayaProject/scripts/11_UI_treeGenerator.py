# This script creates UI that generates trees on selected vertices

import maya.cmds as mc

if mc.window( "dumWin", exists=True ):
    mc.deleteUI( "dumWin" )
    
RandomGWin = mc.window( "dumWin", t="Random Generator", w=300, h=300 )
mc.columnLayout( adj=True )
mc.separator( h=10 )
mc.text( "Select random vertices" )
mc.separator( h=10 )
mc.button( l="Generate Random Trees", h=50, c="ranGenerator()" )

mc.showWindow(RandomGWin)

def ranGenerator():
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