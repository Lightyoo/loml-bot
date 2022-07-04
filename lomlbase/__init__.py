import re

'''
pt : ("pron.","v.")
xpt : (("pron.",),("v",))
exps : "pron.v."
string : "I eat"
'''

def format_exps_pt(exps):

	return tuple(re.findall(r"\w+\.",exps))

def format_string_xpt(string):
	string_split = string.lower().split(" ")

	for index,word in enumerate(string_split):
		pro = []
		if word in [word.split for word in Words.NOUNS]:
			pro.append("n.") 
		elif word in [word.split for word in Words.PRONOUN]:
			pro.append("pron.") 
		elif word in [word.split for word in Words.NUMERAL]:
			pro.append("num.") 
		elif word in [word.split for word in Words.ADJECTIVE]:
			pro.append("adj.") 
		elif word in [word.split for word in Words.ADVERB]:
			pro.append("adv.") 
		elif word in [word.split for word in Words.VERB]:
			pro.append("v.") 
		elif word in [word.split for word in Words.ARTICLE]:
			pro.append("art.") 
		elif word in [word.split for word in Words.PREPOSITION]:
			pro.append("prep.") 

		string_split[index] = tuple(pro)

	return tuple(string_split)


# the same property will return True
def matching(xpt,model_pt):

	for index,word in enumerate(xpt):
		if model_pt[index] not in word:
			return False
	else:
		return True



class Words:

	class W:
		def __init__(self,split,mean=""):
			self.split = split.lower()
			self.mean  = mean.lower()

	# n.
	NOUNS = [W("apple"),W("pear")]

	# pron.
	PRONOUN = [W("i")]

	# num.
	NUMERAL = [W("two"),W("three"),W("four")]

	# adj.
	ADJECTIVE = []

	# adv.
	ADVERB = []

	# v.
	VERB = [W("eat"),W("buy"),W("throw")]

	################ FAKE WORD

	# art.
	ARTICLE = [W("an")]

	# prep.
	PREPOSITION = []


class Model:
	MODEL_ALL = []
	# the type of the exps in this list is "<class 'list'>" 
	# like [('pron.',"v.","art.","n.")]

	def __init__(self):
		# 1 get 2 reply
		self.adds("pron.v.art.n.","pron.v.art.n.")

	def adds(self,exps,result_exps):
		Model.MODEL_ALL.append((format_exps_pt(exps),format_exps_pt(result_exps)))

	def search_model(self,xpt):
		fit = [model_[1] for model_ in Model.MODEL_ALL if matching(xpt,model_[0])]

		return fit


	


