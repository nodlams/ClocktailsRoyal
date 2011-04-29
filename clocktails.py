from ClocktailsCLOpts import CLOpts
from StructuredGenerator import *
import os

import sys

"""
	Clockfails
"""


import FileHandling
import random
import uuid
import struct
import glob

def warmupRNG():
	sum = 0.0
	for i in range(0,10000):
		sum += random.random()
	return sum

def generateFromStruct(structname, stringSets, multiprob):
	generators = map(lambda line: StructuredGenerator(line, stringSets, multiprob), stringSets[structname])	
	
	return random.choice(generators).generateString()
	
def getStringSets(filenames, ext):
	stringSetNames = FileHandling.getFileNamesWithExt("txt", filenames)
	stringSets = dict(zip(map(lambda (name,_): name, stringSetNames), map(lambda (name,ext): FileHandling.getLinesFromFile(name + ext), stringSetNames)))
	return stringSets

if __name__=="__main__":
	aseed = struct.unpack("<I", os.urandom(4))
	random.seed(int(aseed[0]))
	
	sum = warmupRNG()

	opts = CLOpts(sys.argv[1:])

	multipleProb = float(opts[opts.multiProbOpt])
	dStructName = os.path.splitext(opts[opts.drinkStructOpt])[0]
	nStructName = os.path.splitext(opts[opts.nameStructOpt])[0]
	ext = "txt"

	filesInDir = glob.glob("*." + ext)
	stringSets = getStringSets(filesInDir, ext)	

	print generateFromStruct(nStructName, stringSets, multipleProb)
	print generateFromStruct(dStructName, stringSets, multipleProb)
