from MIDIConverter import MidiConverter
from random import randint


import time


print "Hello"

midiConverter = MidiConverter()

#init GUI
#init Myo

while(True):

	#poll GUI
	#poll MYO
	#send data

	randomValue = randint(0,127)
	midiConverter.sendCCMessage(11, randomValue)
	midiConverter.sendPitchBendMessage(randomValue/127.0)

	#sleep
	time.sleep(0.1)