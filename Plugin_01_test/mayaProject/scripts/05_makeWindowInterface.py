import maya.cmds as mc

# 02 - rutine code that we need to write
if mc.window("dumWin", exists = True):
    mc.deleteUI("dumWin")

# 01 - create the code below first
myWindow = mc.window("dumWin", t="Building Generator ver 0.1r", w=320, h=250, sizeable=False)
mc.columnLayout(adj = True)


# 03- load image
imagepath = mc.internalVar(upd = True) + "icons/windowLogo.jpg"
mc.image(w=300, h=100, image = imagepath)
mc.separator( height=10, style='double' ) 
mc.button( h=50, l = "Create HSBC Building", c = "hsbc()")



# 01 - create the code below first
mc.showWindow(myWindow)


# 04 - below we put the create extrusion function
def hsbc() :
    
    hsbcBuilding = mc.polyCube(h=9,n="HSBC")
    mc.move(0,9/2.0,0,hsbcBuilding)
    mc.polyExtrudeFacet( hsbcBuilding[0] +".f[1]", kft=False, ltz=2, ls=(.5, .5, 0) )
    
    mc.select(clear =True)
