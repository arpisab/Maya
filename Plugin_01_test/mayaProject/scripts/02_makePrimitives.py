import maya.cmds as mc

myHight = 2  
myCube = mc.polyCube(w= 2, h=myHight, d=2, n="Cube") 
mc.move(0,myHight/2.0,0,myCube, r=True)    
mc.rotate(0,0,0,myCube, r=True)

myCone = mc.polyCone(n="Pyramid")
mc.move(-5,myHight/2.0,0,myCone, r=True)    
mc.rotate(0,0,0,myCone, r=True)

myCylinder = mc.polyCylinder(n="Cylinder")
mc.move(-10,myHight/2.0,0,myCylinder, r=True)    
mc.rotate(0,0,0,myCylinder, r=True)