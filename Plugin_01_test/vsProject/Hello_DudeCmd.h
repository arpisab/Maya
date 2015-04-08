#ifndef HELLODUDE_H
#define HELLODUDE_H

#include <maya/MArgList.h>
#include <maya/MObject.h>
#include <maya/MGlobal.h>
#include <maya/MPxCommand.h>

class HelloDude : public MPxCommand {
public:
	HelloDude() {};
	virtual MStatus doIt(const MArgList&);
	static void* creator();
};
#endif