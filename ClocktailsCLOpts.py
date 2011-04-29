from optparse import OptionParser
from CTException import CTException

class CLOpts:
	def __init__(self, args):
		self.__origargs = args
		self.__args = None
		self.__options = None
		self.nameStructOpt = "namestruct"
		self.drinkStructOpt = "drinkstruct"
		self.multiProbOpt = "multiprob"
		self.parseCLOpts()
		self.checkOpts()
	
	def parseCLOpts(self):
		parser = OptionParser()
		parser.add_option("-1", "--name-structures", dest=self.nameStructOpt, default="namestruct.txt", help="name of file containing clockfail name grammars")
		parser.add_option("-2", "--drink-structures", dest=self.drinkStructOpt, default="drinkstruct.txt", help="name of file containing clockfail drink grammers")
		parser.add_option("-p", "--multi-prob", default=0.2, dest=self.multiProbOpt, help="Probability of generating multiples")

		(options, args) = parser.parse_args(self.__origargs)
		self.__options = vars(options)
		self.__args = args

	def checkOpts(self):
		s = self[self.nameStructOpt]
		d = self[self.drinkStructOpt]
		if s == None or d == None:
			raise CTException("-s -d required")

	def __getitem__(self, key):
		return self.__options[key]
