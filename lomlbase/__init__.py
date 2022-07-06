import re


# create lots of Words

class Words:
	class W:
		def __init__(self,split,antisense="",complex="",present=""):
			self.split = split.lower()
			self.antisense = antisense.lower()
			self.complex = complex.lower()
			self.present = present.lower()

	# n.
	NOUNS = [
		W(split="apple",complex="apples"),
		W("pear"),
		W(split="pig",complex="pigs")
		]

	# pron.
	PRONOUN = [
		W("i",antisense="you"),
		W("you",antisense="i")
		]

	# num.
	NUMERAL = [
		W("an"),
		W("two"),
		W("three"),
		W("four"),
		W("five"),
		W("six")
		]

	# adj.
	ADJECTIVE = []

	# adv.
	ADVERB = []

	# v.
	VERB = [
		W(split="eat",present="eating"),
		W(split="love"),
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


	W_PROPERTY = ["split","antisense","complex","present"]
	ALL_PROPERTIES = [NOUNS,PRONOUN,NUMERAL,ADJECTIVE,ADVERB,VERB,ARTICLE,PREPOSITION]


def format(string=""):
	string = tuple(string.lower().split(" "))
	# ("i","eat","an","apple")
	
	'''
	the program will walk the whole tuple
	'''

	for word in string:
		# word -> i | eat | an | apple
		# if word in the large words list , the program will turn the common word string into difficult WordObj
		# for example(if we dont know what's 'apple')
		# (i , eat , an ,apple)
		# and after handling,it becomes ["i"]

if __name__ == '__main__':
	string = "I eat an apple"





























































# def format_string(string):
# 	result = tuple(string.lower().split(" "))

# 	new = []

# 	for i in range(len(result)):
# 		new.append([])
# 	'''
# 	[[],[],[],[]]
# 	'''

# 	new_empty_index = []

# 	for index,word in enumerate(result):
# 		# word -> i or eat or an or ...
# 		# search it in the whole words

# 		for property_of_wordlist in Words.ALL_PROPERTIES:
# 			# property_of_wordlist -> NOUNS,PRONOUN,NUMERAL,ADJECTIVE,ADVERB,VERB,ARTICLE,PREPOSITION

# 			for wordobj in property_of_wordlist:
# 				# wordobj -> W("eat"),W("buy"),W("throw")

# 				for attr in Words.W_PROPERTY:
# 					# attr -> "split","antisense"

# 					if getattr(wordobj,attr) == word:
# 						property_ = ""

# 						if property_of_wordlist == Words.NOUNS:
# 							property_ = "n."

# 						elif property_of_wordlist == Words.PRONOUN:
# 							property_ = "pron."

# 						elif property_of_wordlist == Words.NUMERAL:
# 							property_ = "num."

# 						elif property_of_wordlist == Words.ADJECTIVE:
# 							property_ = "adj."

# 						elif property_of_wordlist == Words.ADVERB:
# 							property_ = "adv."

# 						elif property_of_wordlist == Words.VERB:
# 							property_ = "v."

# 						elif property_of_wordlist == Words.ARTICLE:
# 							property_ = "art."

# 						elif property_of_wordlist == Words.PREPOSITION:
# 							property_ = "prep."

# 						new[index].append([property_,attr,wordobj])
# 						# break # jump out of attr in Words.W_PROPERTY

# 		if new[index] == []:
# 			new_empty_index.append(index)


# 	for empty_index in new_empty_index:
# 		del new[empty_index]

# 	# for index,e in enumerate(new):
# 	# 	if e == []:
# 	# 		del new[index]

# 	return new



# class Model:
# 	def __init__(self):
# 		self.MODEL_ALL = []

# 		self.add_model("$1pron.split$ $1v.split$ $1art.split$ $1n.split$","yes, $1pron.antisense$ $1v.split$")
# 		self.add_model("$1pron.split$ $1v.split$ $1art.split$ $1n.split$","$1pron.antisense$ $1v.split$ $1art.split$ $1n.split$?")
# 		self.add_model("$1pron.split$ $1v.split$ $1art.split$ $1adj.split$ $1n.split$","$1pron.antisense$ $1v.split$ $1art.split$ $1n.split$?")
# 		self.add_model("do $1pron.split$","yes")

# 	def add_model(self,s_expresssion,reply_s_expession):
# 		self.MODEL_ALL.append([self.format_model(s_expresssion),reply_s_expession])

# 	def format_model(self,s_expresssion):
# 		'''
# 		(('1pron.', '1v.', '1art.', '1n.'), 'yes, $1pron.antisense$ $1v.split$')

# 		'''

# 		return re.findall(r"\$([0-9]+)(\w+\.)(\w+)\$",s_expresssion)

# 	def match(self,format_string,format_model):
# 		'''
# 		[[('pron.', 'split', <__main__.Words.W object at 0xffffaecb7340>)], 
# 		[('v.', 'split', <__main__.Words.W object at 0xffffaecabee0>)], [(
# 		'num.', 'split', <__main__.Words.W object at 0xffffaecb71f0>), ('ar
# 		t.', 'split', <__main__.Words.W object at 0xffffaecabd60>)], [('n.'
# 		, 'split', <__main__.Words.W object at 0xffffaecb75b0>)]]

# 		((('1', 'pron.', 'split'), ('1', 'v.', 'split'), ('1', 'art.', 'split'), ('1', 'n.', 'split')), 'yes, $1pron.antisense$ $1v.split$')
# 		'''
# 		print(format_model)


# 		if len(format_string) == len(format_model[0]):
# 			for index,list_p_a_w in enumerate(format_string):
# 				# list_p_a_w -> [('pron.', 'split', <__main__.Words.W object at 0xffff9a2d12e0>)]
# 				for p_a_w in list_p_a_w:
# 					# p_a_w -> ('pron.', 'split', <__main__.Words.W object at 0xffff9a2d12e0>)

# 					if format_model[0][index][1] == p_a_w[0] and format_model[0][index][2] == p_a_w[1]:

# 						format_model[0][index] = format_model[0][index][0],format_model[0][index][1],p_a_w[2]

# 						if str(type(p_a_w[2])) != "<class 'str'>":
# 							break

# 				else:
# 					return None
# 		else:
# 			return None

# 		return format_model

# 	def search(self,format_string):
# 		fit = []

# 		for format_model in self.MODEL_ALL:
# 			result = self.match(format_string,format_model)
# 			if result != None:
# 				print(result)
# 				fit.append(result)

# 		return tuple(fit)

# 	def replace(self,format_info,reply_s_expession):
# 		'''
# 		reply_expression : "$1pron.split$ $1v.split$"
# 		numproperty_wordobj_tuple : ((("1pron.",),(Word(split="i"),)),)

# 		'''

# 		print(format_info)
# 		print(reply_s_expession)

# 		needto_sub = dict(re.findall(r"\$([0-9]+\w+\.)(\w+)\$",reply_s_expession))
# 		# print(needto_sub)

# 		for replaced in needto_sub:
# 			'''
# 			replaced : ("1","pron.","antisense")
# 			'''
# 			...

# 		for p_a_w in format_info:
# 			if f"{p_a_w[0]}{p_a_w[1]}" in needto_sub:
# 				reply_s_expession = re.sub(rf"\${p_a_w[0]}{p_a_w[1]}\w+\$",getattr(p_a_w[2],needto_sub[f"{p_a_w[0]}{p_a_w[1]}"],"x"),reply_s_expession)

# 		return reply_s_expession

		

# def auto_reply(string):
# 	# print(format_string("I love eating apples"))
# 	string = format_string(string)
# 	print(string)

# 	model = Model()
# 	print("all the models",model.MODEL_ALL)

# 	all_reply = []

# 	for i in model.search(string):
# 		all_reply.append(model.replace(i[0],i[1]))

# 	return all_reply





# if __name__ == '__main__':
# 	print(auto_reply("I love eating you"))






