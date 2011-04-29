from ClocktailsCLOpts import CLOpts
from StructuredGenerator import *
import os

import sys

"""
	Clockfails

	Examples:
	Prince Edward's flaming splean
	The ruptured bladder of King Terrence
	The Prince Regent's mistifying utterance

	specify structure in files?
	e.g.
	The <name>'s <intransitive verb>* <adjective> <noun>    
	The <adjective> <noun> of <name>
	<name>'s <adjective> <noun>
	
	so we need a structure name, verb, adject and noun file. 

	4:
	random selection of generator
	5:
	generation of clocktail name. 

	6:
	read mixers and spirits
	7:
	generation of clocktail ingredients	
"""


import FileHandling
import random
import uuid
import struct

def warmupRNG():
	sum = 0.0
	for i in range(0,10000):
		sum += random.random()
	return sum

if __name__=="__main__":
	aseed = struct.unpack("<I", os.urandom(4))
	random.seed(int(aseed[0]))
	
	sum = warmupRNG()

	opts = CLOpts(sys.argv[1:])

	multipleProb = 0.2
	stringSetNames = ["noun", "verb", "adj", "title", "name", "namestruct"]
	stringSets = dict(zip(stringSetNames, map(lambda x: FileHandling.getLinesFromFile(opts[x]), stringSetNames)))	
	generators = map(lambda line: StructuredGenerator(line, stringSets, multipleProb), stringSets["namestruct"])	
	
	print random.choice(generators).generateString()

	stringSetNames = ["drinkstruct", "spirit", "mixer"] 	
	stringSets = dict(zip(stringSetNames, map(lambda x: FileHandling.getLinesFromFile(opts[x]), stringSetNames)))
	generators = map(lambda line: StructuredGenerator(line, stringSets, multipleProb), stringSets["drinkstruct"])

	print random.choice(generators).generateString()
