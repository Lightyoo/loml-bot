'''
Dont read my code
and dont give advice 
Do your things 
Please....

'''

from lomlbase import *
from lomlbase.analog_socket import Talk,Speaker


class Loml(Speaker):
	def __init__(self):
		Speaker.__init__(self,"loml")

	def brain(self,speaker_name,speaker_content):
		

		
		# content = speaker_content.lower()
		# content_split = content.split()

		# if matching(content,"pron.v.art.n.") or matching(content,"pron.v.num.n."):
		# 	if content_split[0] == "i":
		# 		self.say(f"You {content_split[1]} {content_split[2]} {content_split[3]}?")


if __name__ == '__main__':
	talk = Talk()
	talk.start()

	light = Speaker("light")
	light.join_talk(talk)

	lomlbot = Loml()
	lomlbot.join_talk(talk)

	light.say("I throw an pear")



