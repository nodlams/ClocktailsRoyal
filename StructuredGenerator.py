import random

class GeneratorElement:
	def __init__(self, stringSet, prefix="", postfix="", timesToRepeat=1, multipleProb=0.2):
		self.stringSet = stringSet
		self.timesToRepeat = timesToRepeat
		if self.timesToRepeat == -1:
			self.timesToRepeat = 1
			while True:
				if random.random() < multipleProb:
					self.timesToRepeat += 1
				else:
					break
		self.prefix = prefix
		self.postfix = postfix
		
	def generateString(self):
		ret = self.prefix 

		for i in range(0, self.timesToRepeat-1):
			ret += random.choice(self.stringSet) + " "
		ret += random.choice(self.stringSet)

		ret += self.postfix + " "

		return ret

class StringElement:
	def __init__(self, string):
		self.string = string

	def generateString(self):
		return self.string + " "

class StructuredGenerator:
	def __init__(self, line, stringSets, multipleProb):
		self.multipleProb = multipleProb
		self.elements = self.parseStructString(line, stringSets)	

	def getPrefix(self, token, placeholder):
		firstInd = token.find(placeholder)
		return token[0:firstInd]		
		
	def getPostfix(self, token, placeholder):
		afterPHInd = token.find(placeholder) + len(placeholder)
		return token[afterPHInd:]

	def parsePostfix(self, postFix):
		if postFix == "*":
			return ("", -1)	
		if len(postFix) > 0 and postFix[0] == "+":
			return ("", int(postFix[1:]))
		return (postFix, 1)
	
	def parseToken(self, token, stringSets):
		multiple = 1 

		for name, strings in stringSets.items():
			if name in token:
				tagName = "<" + name + ">"
				postFix = self.getPostfix(token,tagName)
				(postFix, multiple) = self.parsePostfix(postFix)	
				return GeneratorElement(strings, self.getPrefix(token, tagName), postFix, multiple, self.multipleProb)
		return StringElement(token)

	def parseStructString(self, line, stringSets):
		elements = []
		for token in line.split(" "):
			elements.append(self.parseToken(token, stringSets))

		return elements

	def generateString(self):
		ret = ""
		for e in self.elements:
			s = e.generateString()
			ret += s
		return ret

	def __repr__(self):
		return str(self.elements)

