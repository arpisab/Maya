import maya.cmds as mc

# the code below has to be add only when connecting this script with the create window script!
def hsbc() :
    
    # also we need to indent the code below with tab in order to locate in the def hsbc function
    hsbcBuilding = mc.polyCube(h=9,n="HSBC")
    mc.move(0,9/2.0,0,hsbcBuilding)
    mc.polyExtrudeFacet( hsbcBuilding[0] +".f[1]", kft=False, ltz=2, ls=(.5, .5, 0) )
    # kft is keepFacesTogether; ltz is localTranslateZ; ls is local scale;
    
    mc.select(clear =True)