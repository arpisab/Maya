import maya.cmds as mc

if mc.window(myWindow, exists = True) :
    mc.deleteUI(myWindow)

myWindow = mc.window("testWin", t="Arguments_RK", w=300, h=300)

mc.columnLayout(adj = True)

mc.text("Give the details of W, H and D")
# l stands for label; c stands for command;
mc.button(l = "Create a Cube", c = "makeCube(5,2,5,1)") 

mc.showWindow(myWindow)

def makeCube(wid, hei, dep, mov):
    cube = mc.polyCube(w=wid, h=hei, d=dep, n="BOX")
    mc.move(0,mov,0,cube)
