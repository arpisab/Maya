import maya.cmds as mc

myHight = 2    
myCube = mc.polyCube(w= 2, h=myHight, d=2, n="Block") 
mc.move(0,myHight/2.0,0,myCube, r=True)    
mc.rotate(0,0,0,myCube, r=True)