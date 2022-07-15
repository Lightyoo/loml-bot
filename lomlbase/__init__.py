import re
from collections import OrderedDict

# create lots of Words

class Words:
	class W:
		def __init__(self,split,antisense="",complex="",present=""):
			self.split = split.lower()
			self.antisense = antisense.lower()
			self.complex = complex.lower()
			self.present = present.lower()

			self.wp = ""

	# n.
	_NOUNS = [
		W(split="apple",complex="apples"),
		W("pear"),
		W(split="pig",complex="pigs"),
		W("world")
		]

	# pron.
	_PRONOUN = [
		W("i",antisense="you"),
		W("you",antisense="i")
		]
	
	# num.
	_NUMERAL = [
		W("an"),
		W("two"),
		W("three"),
		W("four"),
		W("five"),
		W("six")
		]

	# adj.
	_ADJECTIVE = [
		W("nice"),
		W("terrible"),
		W("excited"),
		W("quiet"),
		W("rude")
		]

	# adv.
	_ADVERB = []

	# v.
	_VERB = [
		W(split="eat",present="eating"),
		W(split="love"),
		W("buy"),
		W("throw"),
		W("hello")
		]

	################ FAKE WORD

	# art.
	_ARTICLE = [
		W("an")
		]

	# prep.
	_PREPOSITION = [
		W("on"),
		W("in")
		]


	W_PROPERTY = ["split","antisense","complex","present"]

	_ALL_PROPERTIES = {
		"n."   :  _NOUNS,
		"pron.":  _PRONOUN,
		"num." :  _NUMERAL,
		"adj." :  _ADJECTIVE,
		"adv." :  _ADVERB,
		"v."   :  _VERB,
		"art." :  _ARTICLE,
		"prep" :  _PREPOSITION
		}

	for wp_,word_list in _ALL_PROPERTIES.items():
		
		for word in word_list:
			word.wp = wp_

	WORD_LIST = _NOUNS + _PRONOUN + _NUMERAL + _ADJECTIVE + _ADVERB + _VERB + _ARTICLE + _PREPOSITION



class Model:
	ALL_MODEL = [
		("pron.split v.split art.split n.split.",{"reply":"0.antisense 1.split 2.split 3.split"})
	]


	def search(self,handled_result,model=ALL_MODEL[0]):
		models = re.findall(r"(\w+\.\w+)",model[0])
		print(models,"\n")

		to_match = [(code,handled_result[0][str(code)]["object"]) for code in re.findall("[0-9]+",handled_result[1])]
		print(to_match,"\n")

		new = []

		if len(models) == len(handled_result[0]):
			for index,i in enumerate(models):
				for m,obj in to_match[index][1]:
					if m == i:
						handled_result[1] = re.sub(to_match[index][0],m,handled_result[1])
						new.append((index,obj))
						break

		print(handled_result[1],"\n")

		print(new,"\n")

		replys = dict(re.findall(r"([0-9]+)\.(\w+)",model[1]["reply"]))
		print(replys)

		for num,obj in new:
			model[1]["reply"] = re.sub(rf"{num}.{replys[str(num)]}",getattr(obj,replys[str(num)]),model[1]["reply"])

		print(model[1]["reply"])



string = "I eat an apple."

string = string.lower()

pattern_word = r"\b\w+\b"

# ['apple', 'eat', 'an', 'i']
all_word_list = sorted(list(set(re.findall(pattern_word,string))),key=lambda x:x.__len__(),reverse=True)

dictionary = dict()

for index,word in enumerate(all_word_list):
	string = re.sub(word,str(index),string)
	dictionary[str(index)] = {"name":word,"object":list()}

	for word_obj in Words.WORD_LIST:
		for pro in Words.W_PROPERTY:
			if word == getattr(word_obj,pro):
				dictionary[str(index)]["object"].append((f"{word_obj.wp}{pro}",word_obj))


handled_result = [dictionary,string]

print(handled_result,"\n")

model = Model()
model.search(handled_result)





























# class Model:
# 	def __init__(self):
# 		self.ALL_MODEL = [
# 			(r"$1v.split$ $1n.split$",r"$1v.split$ $1n.split$ ? ? ?"),
# 			(r"$1v.split$ a $1n.split$",r"$1v.split$ $1n.split$")
# 			]

# 		'''
		
# 		'''
# 		self._turn()


# 	def _turn(self):
# 		'''
# 		cut the s_expression
# 		and they will become some lists and tuples
# 		it's easy to opearte
# 		'''
# 		def splited(s_expression):
# 			pattern_s_expression = r"\$([0-9]+)(\w+\.)(\w+)\$"

# 			return [list(i) for i in re.findall(pattern_s_expression,s_expression)]

# 		for index,(s_expression,reply_s_expression) in enumerate(self.ALL_MODEL):
# 			self.ALL_MODEL[index] = splited(s_expression),reply_s_expression


# 	def match(self,deal_string,turned_model):
# 		model_appearence = turned_model[0]
# 		model_reply = turned_model[1]

# 		print("")
# 		print(deal_string)
# 		print(model_appearence)

# 		# above all
# 		# judge whether the model_appearence's length is the same to deal_string's length
# 		if model_appearence.__len__() == deal_string.__len__():

# 			for index,fg in enumerate(deal_string):

# 				if str(type(fg)) == "<class 'list'>":
# 					for element in fg:
# 						if element[1] == model_appearence[index][1] and element[2] == model_appearence[index][2]: 
# 							model_appearence[index][2] = element[3]

# 					if str(type(model_appearence[index][2])) == "<class 'str'>":
# 						return False

# 				elif str(type(fg)) == "<class 'str'>":
# 					print("str type element")
# 					return False

# 		else:
# 			print("the lengths are different!")
# 			return False

# 		return model_reply



# def format_glo(string=""):
# 	string = tuple(string.split(" "))
# 	# ("i","eat","an","apple")
	
# 	'''
# 	the program will walk the whole tuple
# 	'''

# 	print(string)

# 	result = []

# 	for i in range(len(string)):
# 		result.append([])

# 	for index,word in enumerate(string):
# 		# word -> i | eat | an | apple
# 		# if word in the large words list , the program will turn the common word string into difficult WordObj
# 		# for example(if we dont know what's 'apple')
# 		# (i , eat , an ,apple)
# 		# and after handling,it becomes [[("pron.","split",wobj),("pron.","antisense",wobj)]]

# 		for property_str,word_list in Words.ALL_PROPERTIES.items():
# 			# word_list -> many Wo(Wobject)
# 			# property_str -> use string to express the word's property

# 			for wo in word_list:
# 				# the wo
# 				# like W("nice")
# 				# their all properties is included in Words.W_PROPERTY
# 				for wo_pro in Words.W_PROPERTY:
# 					# wo_pro -> the properties Wo includes

# 					value = getattr(wo,wo_pro) # the value of the property of Wo

# 					if word == value:
# 						# we need to turn it into global appearence
# 						# like ("pron.","split",wo)

# 						'''
# 						first {
# 							pron. -> property_str

# 						second{
# 							split -> wo_pro

# 						third{
# 							wo    -> wo

# 						'''
# 						result[index].append([word,property_str,wo_pro,wo])
# 						# word represents itself
# 						# property_str represents its word's property 
# 						# wo_pro represents its property in the Word Object
# 						# wo represents its Word Object

# 		if result[index] == []:
# 			print(f"{word} is unknown,so I turn the list into string")
# 			result[index] = word

# 		elif result[index] != []:
# 			print(f"'{word} it has {len(result[index])} meaning,so we create{result[index]}")

# 	print("")

# 	return result




# def auto(string):
# 	# (1)
# 	# keep the first data
# 	# Like "i eat an apple"
# 	# but we should lower
# 	string = string
# 	print(string,"\n")


# 	# (2)
# 	# turn the data into global format
# 	# but global format is not fit to splited s_expression
# 	deal_string = format_glo(string)
# 	print("final result is:",deal_string,"\n")


# 	# (3)
# 	model = Model()
# 	print("Loading all the models: ",model.ALL_MODEL)


# 	# (4)
# 	print(model.match(deal_string,model.ALL_MODEL[1]))
# 	# the model I choose the first for now



# if __name__ == '__main__':
# 	string = "Hello a world"
# 	auto(string)











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




