from numpy import *
import cccpLibs as lib

# Structure to house dataset name and array of values
class DataSet:
	def __init__(self, name, vals):
		self.name, self.vals = name,vals
	def println(self):
		print "Name: %s\tVals: %s \tMax: %s" % (self.name, len(self.vals), max(self.vals))

# Structure to house correlations for two datasets
class xCor:
	def __init__(self, p, s, shiftRange):
		self.primary, self.secondary = p, s
		self.maxIndex=0
		self.rVals = []
		for i in range(0,shiftRange):
			self.rVals.append('')
	
	def correlate(self,shift):
		x,y = lib.getMatchingArrays(self.primary.vals[shift:],self.secondary.vals)
		r = corrcoef(x,y)[0,1]
		self.rVals[shift] = r
		
		if r == max(self.rVals):
			self.maxIndex=shift
		
	# Append XML file, or just print info for debugging
	def println(self,f=None):
		if f is None:
			print "%s\t vs. %s" % (self.primary.name, self.secondary.name)
			print "Max:%f\tShift:%d" % (max(self.rVals), self.maxIndex)
		else:
			print >> f, "<cross><primary>%s</primary><secondary>%s</secondary><max>%d</max><vals>" % (self.primary.name, self.secondary.name, self.maxIndex)
			for i in range(len(self.rVals)):
				print >> f, "<val><r>%f</r><shift>%d</shift></val>" % (self.rVals[i],i)
			print >> f, "</vals></cross>"
