from MIDIConverter.MIDIConverter import MidiConverter
import myo_api.myo_api
from random import randint


import time


print "Hello"

midiConverter = MidiConverter()

#init GUI
#init Myo
a, b = 1, 1
while(True):

	#poll GUI
	#poll MYO
	#send data

	a += 2
	b += 19

	#a, b = b, (a + b) % (128 * 40)
	randomValue = b % 128
	randomNote = 40 + (b % 49)
	midiConverter.sendNoteOn(randomNote)
	midiConverter.sendCCMessage(7, randomValue)
	midiConverter.sendPitchBendMessage(randomValue/127.0)

	#sleep
	time.sleep(0.1)
	midiConverter.sendNoteOff(randomNote)
	time.sleep(0.05)
