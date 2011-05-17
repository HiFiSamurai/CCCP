import csv,sys,ConfigParser,os,gzip
import lxml.etree as ET
import cccpStructs as structs
from datetime import datetime

# Fetches config file for cccp. Quits if arguments are invalid.
def getConfig():
	if len(sys.argv) < 2 or ".cfg" not in sys.argv[1]:
		print "Usage: cccp.py configFile.cfg"
		sys.exit()
	cfgName = sys.argv[1]
	config = ConfigParser.RawConfigParser()
	config.readfp(open(cfgName))

	return cfgName,config

def setupLog():
	logName=sys.path[0] +"/cccp.log"
	logFile=open(logName,'a')
	sys.stdout=logFile
	sys.stderr=logFile
	print "\nCCCP: " + str(datetime.now())
	return logFile

# Import CSV and convert to arrays
def loadCSV(config):
	filename = config.get('Settings','csvName')
	reader = csv.reader(open(filename, "rb"))
	
	headers = reader.next()
	units = reader.next()
	data = []
	for i in range(1,len(headers)):
		data.append(structs.DataSet(headers[i],[]))
	
	for row in reader:
		for j in range(0,len(data)):
			data[j].vals.append(row[j+1])	# Assumes timestamps in first row
	return filename,data

# Deletes input files after completion, zips and moves XML file
def cleanup(cfgFile, csvFile, xmlFile):
	xml = open(xmlFile, 'rb')
	gz = gzip.open(xmlFile.replace(".xml",".gz"), 'wb')
	gz.writelines(xml)
	gz.close()
	xml.close()

	newXML = xmlFile.replace("Storage","Complete")
	os.system ("mv %s %s" % (xmlFile, newXML))

	os.remove(cfgFile)
	os.remove(csvFile)
