import time
import rtmidi
from random import randint

#Settings
portName = "MyoMIDI"
currentTime = lambda: int(round(time.time() * 1000))


class MidiConverter:

	def __init__(self):
		print "MidiConverter setting up"
		startTime = currentTime()
		self.midiout = rtmidi.MidiOut()
		self.midiout.open_virtual_port(portName)
		elapsedTime = currentTime() - startTime
		print "MidiConverter finished setting up:", elapsedTime, "ms"

# available_ports = midiout.get_ports()

# print available_ports

# if available_ports:
#     midiout.open_port(0)
# else:

	#Value should be int 0-127
	def sendCCMessage(self, cc, value):
		message = [0xB0, cc, value]
		self.midiout.send_message(message)

	#Value should be float 0-1
	def sendPitchBendMessage(self, value):
		#-1 becomes 0
		#1 becomes 1
		#0 becomes 0.5
		adjustedValue = 0.5* (1 + value)
		integerRepresentation = min(16384-1, int(adjustedValue * 16384))
		msb = integerRepresentation >> 7 
		lsb = integerRepresentation & (2^7 - 1) 
		message = [0xE0, lsb, msb]
		self.midiout.send_message(message)


	def sendNote(self):
		randomNote = randint(65,90)

		note_on = [0x90, randomNote, 112] # channel 1, random note, velocity 112
		note_off = [0x80, randomNote, 0]
		self.midiout.send_message(note_on)
		time.sleep(0.1)
		self.midiout.send_message(note_off)
		time.sleep(0.1)


	def close(self):
		del midiout

midiConverter = MidiConverter()

while(True):
	randomValue = randint(0,127)
	midiConverter.sendCCMessage(11, randomValue)
	midiConverter.sendPitchBendMessage(randomValue/127.0)
	time.sleep(0.1)



