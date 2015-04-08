import maya.cmds as mc

if mc.window(myWindow, exists = True) :
    mc.deleteUI(myWindow)

myWindow = mc.window("testWin", t="Arguments_RK", w=300, h=300)

mc.columnLayout(adj = True)

mc.showWindow(myWindow)