import glob
import os

def discardCrap(line):
	return line.replace("\n", "").strip()

def getLinesFromFile(filename):
	f = open(filename)
	lines = []
	for line in f:
		if line[0] == "#":
			continue
		lines.append(discardCrap(line))

	return lines

def getFileNamesWithExt(ext, filelist):
	return map(lambda x: os.path.splitext(x), filelist)		
