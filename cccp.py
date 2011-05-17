import cccpLibs as lib
import cccpIO as io
import cccpStructs as structs

log = io.setupLog()
cfgName,config = io.getConfig()
csvName,data = io.loadCSV(config)

# Operational Info, for debug purposes
print "CSV Name: " + csvName
print "Data Sets: " + str(len(data))
print "Points: " + str(len(data[0].vals))
print "Shifts: " + str(config.getint('Settings','range'))

xmlName = lib.constructMatrix(data,config)
print "Performed Cross Correlations"

io.cleanup(cfgName,csvName,xmlName)
print "Cleaned Up Files"
log.close()
