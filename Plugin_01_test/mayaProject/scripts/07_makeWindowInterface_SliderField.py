import maya.cmds as mc

if mc.window( ram, exists=True ):
    mc.deleteUI( ram )

# mnb minimize button, mxb maximaze button
ram = mc.window( "RenamerWin", t="Renamer ver 0.9r", w=300, h=300, sizeable=False, mnb=False, mxb=False )
mc.columnLayout( adj=True )


# upd stands for user preference type
imagePath = mc.internalVar( upd=True ) + "icons/windowLogo.jpg"
mc.image( w=300, h=100, image = imagePath )
mc.separator( h=10 )
mc.text( "Welcome to the Renamer Tool" )
mc.separator( h=10 )

cubW = mc.intSliderGrp( l="Wight ", min=0, max=10, field=True )
cubH = mc.intSliderGrp( l="Hight ", min=0, max=10, field=True )
cubD = mc.intSliderGrp( l="Depth ", min=0, max=10, field=True )

mc.button( l="Create a Cube", c="myCube()" )
mc.separator( h=10 )

# textFieldGrp function creates the text field 
cubeName = mc.textFieldGrp( l="Renamer", editable=True )
mc.button( l="Rename the Cube", c="myCubeRenamer()" )
mc.showWindow( ram ) 


def myCube():
    myCubeWidth = mc.intSliderGrp( cubW, q=True, v=True )
    myCubeHigth = mc.intSliderGrp( cubH, q=True, v=True )
    myCubeDepth = mc.intSliderGrp( cubD, q=True, v=True )
    # ch stands for construction history
    finalCube = mc.polyCube( w=myCubeWidth, h=myCubeHigth, d=myCubeDepth, n="myCube#", ch=False )
    mc.move( 0,myCubeHigth/2.0,0, finalCube, relative=True ) 
    
def myCubeRenamer():
    finalName = mc.textFieldGrp( cubeName, q=True, text=True )
    mc.rename( finalName )