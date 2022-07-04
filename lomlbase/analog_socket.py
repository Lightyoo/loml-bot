import time
import queue
from threading import Thread


class Talk:
	class Message:
		def __init__(self,name,content,time,*args):
			self._name = name
			self._content = content
			self._time = time

		@ property
		def name(self):
			return self._name

		@ property
		def content(self):
			return self._content
			
		@ property
		def time(self):
			return self._time

	def __init__(self):
		self.flow = queue.Queue()
		self._speakers = []

		print("Talk:Create a talk,and the flow is",self.flow)
		print("Talk:If you want to know persons that join this talk,you can use talk.speakers")

	@ property
	def speakers(self):
		return self._speakers

	def listen(self):
		print("Talkloop: start loop,tell and receive")
		while True:
			if not self.flow.empty():
				_msg = self.flow.get()

				if _msg[0] == "joined": # <- someone joined the talk
					# tuple : ("joined",speaker's flow)
					self._speakers.append(_msg[1])
					print("Talkloop:",_msg[2],"joins this talk,his flow is",_msg[1])

				else:  # <- someone spoke
					name     = _msg[0]
					content  = _msg[1]
					time     = _msg[2]

					print("Talkloop:",name,"says:",content,"at",time)
					for sflow in self._speakers:
						sflow.put(Talk.Message(name=name,content=content,time=time))

	def start(self):
		t = Thread(target=self.listen)
		t.start()


class Speaker:
	def __init__(self,name):
		self._joined_talk_flow = None
		self.flow = queue.Queue()

		self.name = name

		t = Thread(target=self.listen)
		t.start()

	def join_talk(self,talk_obj):
		talk_obj.flow.put(("joined",self.flow,self.name))
		self._joined_talk_flow = talk_obj.flow

	def say(self,content):
		self._joined_talk_flow.put((self.name,content,time.time()))

	def listen(self):
		while True:
			if not self.flow.empty():
				_msg = self.flow.get() # Message obj
				if self.name != _msg.name:
					# print(self.name,":",_msg.name,"says:",_msg.content)
					self.brain(_msg.name,_msg.content)

	def brain(self,speaker_name,speaker_content):
		pass
