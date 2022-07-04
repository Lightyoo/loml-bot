import re



def property_expression_to_property_f1tuple(property_expression):
	'''
	"pron.v.art.n." 
	to
	("pron.","v.","art.","n.")
	'''
	return tuple(re.findall(r"\w+\.",property_expression))



class Words:
	class W:
		def __init__(self,split,antisense=""):
			self.split = split.lower()
			self.antisense = antisense.lower()

	# n.
	NOUNS = [
		W("apple"),
		W("pear")
		]

	# pron.
	PRONOUN = [
		W("i",antisense="you")
		]

	# num.
	NUMERAL = [
		W("an"),
		W("two"),
		W("three"),
		W("four")
		]

	# adj.
	ADJECTIVE = []

	# adv.
	ADVERB = []

	# v.
	VERB = [
		W("eat"),
		W("buy"),
		W("throw")
		]

	################ FAKE WORD

	# art.
	ARTICLE = [
		W("an")
		]

	# prep.
	PREPOSITION = []



	W_PROPERTY = ["split","antisense"]
	ALL_PROPERTIES = [NOUNS,PRONOUN,NUMERAL,ADJECTIVE,ADVERB,VERB,ARTICLE,PREPOSITION]


class Model:
	def __init__(self):
		self.MODEL_ALL = []

		self.add_model("pron.v.art.n.","yes, $1pron.antisense$ $1v.split$")
		self.add_model("pron.v.art.n.","$1pron.antisense$ $1v.split$ $1art.split$ $1n.split$?")

	def add_model(self,property_expression,reply_expession):
		property_f1tuple = property_expression_to_property_f1tuple(property_expression)
		self.MODEL_ALL.append((property_f1tuple,reply_expession))

	def match(self,model_property_f1tuple,property_f2tuple):
		'''
		('pron.', 'v.', 'art.', 'n.')
		&
		(('pron.',), ('v.',), ('art.',), ('n.',))
		=
		True
		return ...
		'''
		for index,property_tuple in enumerate(property_f2tuple):
			if model_property_f1tuple[index] not in property_tuple:
				return False
		else:
			return True

	def search(self,property_f2tuple):
		fit = []

		for model in self.MODEL_ALL:
			if self.match(model[0],property_f2tuple):
				fit.append(model[1])

		return tuple(fit)

	def replace(self,reply_expession,numproperty_wordobj_tuple):
		'''
		reply_expression : "$1pron.split$ $1v.split$"
		numproperty_wordobj_tuple : ((("1pron.",),(Word(split="i"),)),)

		'''

		all_sub = re.findall(r"(\w+\.)(\w+)",reply_expession)
		
		reply = reply_expession

		for numproperty,value in all_sub:
			for np_wo_f2tuple in numproperty_wordobj_tuple:
				for index,numproperty_in_f2tuple in enumerate(np_wo_f2tuple[0]):
					if numproperty == numproperty_in_f2tuple:
						reply = re.sub(f"\${numproperty}{value}\$",getattr(np_wo_f2tuple[1][index],value,"x"),reply)

		return reply


def format_string(string):
	result = tuple(string.lower().split(" "))

	new = []
	'''
	[[],[],[],[]]
	'''

	for index,word in enumerate(result):
		# word -> i or eat or an or ...
		# search it in the whole words
		new.append([])
		for property_of_wordlist in Words.ALL_PROPERTIES:
			# property_of_wordlist -> NOUNS,PRONOUN,NUMERAL,ADJECTIVE,ADVERB,VERB,ARTICLE,PREPOSITION

			for wordobj in property_of_wordlist:
				# wordobj -> W("eat"),W("buy"),W("throw")

				for attr in Words.W_PROPERTY:
					# attr -> "split","antisense"

					if getattr(wordobj,attr) == word:
						if property_of_wordlist == Words.NOUNS:
							property_ = "n."

						elif property_of_wordlist == Words.PRONOUN:
							property_ = "pron."

						elif property_of_wordlist == Words.NUMERAL:
							property_ = "num."

						elif property_of_wordlist == Words.ADJECTIVE:
							property_ = "adj."

						elif property_of_wordlist == Words.ADVERB:
							property_ = "adv."

						elif property_of_wordlist == Words.VERB:
							property_ = "v."

						elif property_of_wordlist == Words.ARTICLE:
							property_ = "art."

						elif property_of_wordlist == Words.PREPOSITION:
							property_ = "prep."

						else:
							property_ = "none."

						new[index].append(("index",property_,attr,wordobj))

	return new



def string_to_numproperty_wordobj_tuple(split_string):
	# numproperty_wordobj_tuple : (("1pron.",Word(split="i")),)
	numproperty_wordobj_list = []

	n = 0
	pron = 0
	num = 0
	adj = 0
	adv = 0
	v = 0
	art = 0
	prep = 0

	for index,word in enumerate(split_string):
		pro = []
		word_obj = []
		if word in [word.split for word in Words.NOUNS]:
			n += 1
			pro.append(f"{n}n.") 
			word_obj.append([wordobj for wordobj in Words.NOUNS if wordobj.split == word][0])
		if word in [word.split for word in Words.PRONOUN]:
			pron += 1 
			pro.append(f"{pron}pron.") 
			word_obj.append([wordobj for wordobj in Words.PRONOUN if wordobj.split == word][0])
		if word in [word.split for word in Words.NUMERAL]:
			num += 1
			pro.append(f"{num}num.") 
			word_obj.append([wordobj for wordobj in Words.NUMERAL if wordobj.split == word][0])
		if word in [word.split for word in Words.ADJECTIVE]:
			adj += 1
			pro.append(f"{adj}adj.") 
			word_obj.append([wordobj for wordobj in Words.ADJECTIVE if wordobj.split == word][0])
		if word in [word.split for word in Words.ADVERB]:
			adv += 1
			pro.append(f"{adv}adv.") 
			word_obj.append([wordobj for wordobj in Words.ADVERB if wordobj.split == word][0])
		if word in [word.split for word in Words.VERB]:
			v += 1
			pro.append(f"{v}v.") 
			word_obj.append([wordobj for wordobj in Words.VERB if wordobj.split == word][0])
		if word in [word.split for word in Words.ARTICLE]:
			art += 1
			pro.append(f"{art}art.")
			word_obj.append([wordobj for wordobj in Words.ARTICLE if wordobj.split == word][0]) 
		if word in [word.split for word in Words.PREPOSITION]:
			prep += 1
			pro.append(f"{prep}prep.") 
			word_obj.append([wordobj for wordobj in Words.PREPOSITION if wordobj.split == word][0])

		numproperty_wordobj_list.append((tuple(pro),tuple(word_obj)))

	return tuple(numproperty_wordobj_list)

def to_property_f2tuple(split_string):
	'''
	('i', 'eat', 'an', 'apple')
	become 
	(('pron.',), ('v.',), ('art.',), ('n.',))
	'''
	property_list = []

	for index,word in enumerate(split_string):
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

		property_list.append(tuple(pro))

	return tuple(property_list)

def auto_apply(string):
	# lower string
	string = format_string(string)
	print(string)

	'''
	(
	    (
	    	('1pron.',), (<__main__.Words.W object at 0xffffa4579040>,)
	    ),(
	    	('1v.',), (<__main__.Words.W object at 0xffffa456de80>,)
	    ),(
	    	('1art.',), (<__main__.Words.W object at 0xffffa456dc70>,)
	    ),(
	    	('1n.',), (<__main__.Words.W object at 0xffffa4579490>,)
	    )
	)
	'''
	numproperty_wordobj_tuple = string_to_numproperty_wordobj_tuple(string)

	# (('pron.',), ('v.',), ('art.',), ('n.',))
	string = to_property_f2tuple(string)

	model = Model()
	model_all = model.MODEL_ALL

	# ('yes, $1pron.antisense$ $1v.split$', '$1pron.antisense$ $1v.split$ $1art.split$ $1n.split$?')
	search_result = model.search(string)

	return tuple([model.replace(search_r,numproperty_wordobj_tuple) for search_r in search_result])




if __name__ == '__main__':
	string = "I eat an apple"
	print(auto_apply(string))
