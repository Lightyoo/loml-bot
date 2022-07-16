import re
import random
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
		W("hello"),
		W("kill"),
		W("see"),
		W("fuck"),
		W("is"),
		W("am",complex="are")
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
		("pron.split v.split art.split n.split.",{"reply":["0.antisense 1.complex 2.split 3.split?","But 0.antisense 1.complex a bitch","2.split 3.split?","Ah!0.antisense 1.complex","Ok,I know","Oh I see","oh,I see!"]})
	]


	def match(self,handled_result,model=ALL_MODEL[0]):
		# print(handled_result)
		# print(model)

		# print("\n\n")


		models = re.findall(r"(\w+\.\w+)",model[0])
		# print(models,"\n")

		num_order = [(num,handled_result[0][num]['object']) for num in re.findall(r"[0-9]+",handled_result[1])]
		# print(num_order,"\n")

		if len(models) == len(handled_result[0]):
			for index,element in enumerate(models):

				for t,obj in num_order[index][1]:
					if t == element:
						handled_result[0][num_order[index][0]]["object"] = obj
						handled_result[1] = re.sub(num_order[index][0],t,handled_result[1])

		# print(handled_result,"\n")

		new = [handled_result[0][num]["object"] for num in re.findall(r"[0-9]+",handled_result[2])]
		# print(new,"\n")

		all_replys = []

		if handled_result[1] == model[0]:
			# print("# match:",model[0])

			for freply in model[1]["reply"]:
				r = freply
				for num,attr in re.findall(r"([0-9]+)\.(\w+)",r):
					if hasattr(new[int(num)],attr):
						if getattr(new[int(num)],attr) != "":
							r = re.sub(f"{num}.{attr}",getattr(new[int(num)],attr),r)
						else:
							break
					else:
						break
				else:
					all_replys.append(r)

		return all_replys

	def search(self,handled_result):
		all_replys = []
		for element in Model.ALL_MODEL:
			result = self.match(handled_result,element)
			if result != []:
				all_replys = all_replys + result

		return all_replys





def auto_reply(string):
	string = string.lower()

	# ['apple', 'eat', 'an', 'i']
	all_word_list = sorted(list(set(re.findall(r"\b\w+\b",string))),key=lambda x:x.__len__(),reverse=True)

	dictionary = dict()

	for index,word in enumerate(all_word_list):
		string = re.sub(word,str(index),string)
		dictionary[str(index)] = {"name":word,"object":list()}

		for word_obj in Words.WORD_LIST:
			for pro in Words.W_PROPERTY:
				if word == getattr(word_obj,pro):
					dictionary[str(index)]["object"].append((f"{word_obj.wp}{pro}",word_obj))

	handled_result = [dictionary,string,string]


	model = Model()
	return model.search(handled_result)


string = "I am an apple."

print(auto_reply(string))






