import cccpStructs as structs
from multiprocessing import Process
from os import environ

# Does correlation of lists. Shifts values and re-correlates across entire list length.
def crossCor(primary,secondary,shiftRange):
	r = structs.xCor(primary,secondary,shiftRange)

	for i in range(shiftRange):
		r.correlate(i)

	return r

# Get arrays of matching points locations. Rows with blank entries are ignored.
def getMatchingArrays(x,y):
	xOut,yOut = [],[]
	for xCurrent,yCurrent in zip(x,y):
		if isNumber(xCurrent) and isNumber(yCurrent):
			xOut.append(xCurrent)
			yOut.append(yCurrent)
	return xOut,yOut

def isNumber(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

# Construct Matrix containing Cross-Correlation structures for all dataset pairs
def constructMatrix(data,config):
	n = len(data)
	shifts = config.getint('Settings','range') + 1		# Gives full range from 0 to x, instead of 0 to x-1
	filename = config.get('Settings','csvName')
	filename = filename.replace("Config", "Storage").replace(".csv",".xml")

	f = file(filename,'w')
	print >> f, "<cccp>"
	print >> f, cfgParams(config)
	print >> f, "<grid>"
	f.close()

	threads=[]
	for i in range(n):
		for j in range(n):
			p = Process(target=multiCorelate, args=(data,i,j,shifts,filename))
			p.start()
			threads.append(p)
	for t in threads:
		t.join()

	f = file(filename,'a')
	print >> f, "</grid></cccp>"			# Add closing XML tag
	f.close()
	return filename

# Performs cross correlation of two data sets across shift range. Represents single thread within program
def multiCorelate(data,i,j,shiftRange,filename):
	f = file(filename,'a')
	c = crossCor(data[i],data[j],shiftRange)
	c.println(f)				# Append to XML files
	f.close()

# Takes each parameter from cfg file and writes as an xml tag
def cfgParams(config):
	xml = "<params>"
	for section in config.sections():
		for option in config.options(section):
			xml += xmlTag(option,config.get(section, option))
	xml += "</params>"
	return xml

def xmlTag(name,value):
	return "<" + str(name) + ">" + str(value) + "</" + str(name) + ">"
