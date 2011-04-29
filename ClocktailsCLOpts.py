from optparse import OptionParser
from CTException import CTException

class CLOpts:
	def __init__(self, args):
		self.__origargs = args
		self.__args = None
		self.__options = None
		self.nameStructOpt = "namestruct"
		self.drinkStructOpt = "drinkstruct"
		self.drinkSpiritOpt = "spirit"
		self.drinkMixerOpt = "mixer"
		self.nameNounOpt = "noun"
		self.nameVerbOpt = "verb"
		self.nameAdjOpt = "adj"
		self.nameTitleOpt = "title"
		self.nameNameOpt = "name"
		self.parseCLOpts()
		self.checkOpts()
	
	def parseCLOpts(self):
		parser = OptionParser()
		parser.add_option("-1", "--name-structures", dest=self.nameStructOpt, help="name of file containing clockfail name grammars")
		parser.add_option("-2", "--drink-structures", dest=self.drinkStructOpt, help="name of file containing clockfail drink grammers")
		parser.add_option("-n", "--name-nouns", dest=self.nameNounOpt, help="name of file containing nouns")
		parser.add_option("-v", "--name-verbs", dest=self.nameVerbOpt, help="name of file containing verbs")
		parser.add_option("-a", "--name-adjs", dest=self.nameAdjOpt, help="name of file containing adjectives")
		parser.add_option("-t", "--name-titles", dest=self.nameTitleOpt, help="name of file containing titles")
		parser.add_option("-N", "--name-names", dest=self.nameNameOpt, help="name of file containing names")
		parser.add_option("-s", "--drink-spirits", dest=self.drinkSpiritOpt, help="name of file containing spirits")
		parser.add_option("-m", "--drink-mixers", dest=self.drinkMixerOpt, help="name of file containing mixers")

		(options, args) = parser.parse_args(self.__origargs)
		self.__options = vars(options)
		self.__args = args

	def checkOpts(self):
		s = self[self.nameStructOpt]
		n = self[self.nameNounOpt]
		v = self[self.nameVerbOpt]
		a = self[self.nameAdjOpt]
		N = self[self.nameNameOpt]
		t = self[self.nameTitleOpt]
		if s == None or n == None or v == None or a == None or N == None or t == None:
			raise CTException("-s -n -v -a -N -t required")

	def __getitem__(self, key):
		return self.__options[key]
