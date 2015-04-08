#include <maya/MIOStream.h>
#include <maya/MSimple.h>
#include <maya/MGlobal.h>


DeclareSimpleCommand(Hello_Dude, PLUGIN_COMPANY, "4.5");

MStatus Hello_Dude::doIt(const MArgList&)
{
	MGlobal::displayInfo("Hi Dude Again!");
	return MS::kSuccess;
}