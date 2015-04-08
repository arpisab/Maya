import maya.cmds as mc

hsbcBuilding = mc.polyCube(h=9,n="HSBC")
mc.move(0,9/2.0,0,hsbcBuilding)
mc.polyExtrudeFacet( hsbcBuilding[0] +".f[1]", kft=False, ltz=2, ls=(.5, .5, 0) )
# kft is keepFacesTogether; ltz is localTranslateZ; ls is local scale;

mc.select(clear =True)