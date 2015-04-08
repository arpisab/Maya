import maya.cmds as mc

if mc.window( rWindow, exists=True ) :
    mc.deleteUI( rWindow )

rWindow = mc.window( "radiusWindow", t="inputs_RK", w=300, h=300 )
mc.columnLayout( adj=True )
mc.text( "Choose the Radius", bgc=(0.5,0,0) )


# type f to set the field
myRadius = mc.intSliderGrp( l="Radius", min=0, max=10, f=True )

# l stands for label; c stands for command;
mc.button( l="Create a Sphere", c="mySphere()" ) 

mc.showWindow(rWindow)

# def stands for definition
def mySphere():
    # q stands for quering. q queries the folloing v value
    myFinalRadius = mc.intSliderGrp( myRadius, q=True, v=True )
    # the actual # symbol after Ball lets create balls staring from numer 1
    ball = mc.polySphere( r = myFinalRadius, n="Ball#" )