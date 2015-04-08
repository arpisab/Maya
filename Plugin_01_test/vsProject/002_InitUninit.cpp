#include <maya/MIOStream.h>
//#include <maya/MSimple.h>
//#include <maya/MGlobal.h>

#include "Hello_DudeCmd.h"
#include <maya/MFnPlugin.h>

void* HelloDude::creator() { return new HelloDude; }

MStatus HelloDude::doIt(const MArgList& argList) {
	MGlobal::displayInfo("Hello Dude!");
	return MS::kSuccess;
}

MStatus initializePlugin(MObject obj) {
	MFnPlugin plugin(obj, "Chad Vernon", "1.0", "Any");
	MStatus status = plugin.registerCommand("helloDude", HelloDude::creator);
	CHECK_MSTATUS_AND_RETURN_IT(status);
	return status;
}

MStatus uninitializePlugin(MObject obj) {
	MFnPlugin plugin(obj);
	MStatus status = plugin.deregisterCommand("helloDude");
	CHECK_MSTATUS_AND_RETURN_IT(status);
	return status;
}