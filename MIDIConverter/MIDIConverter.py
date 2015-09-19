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
	midiConverter.sendNote()




