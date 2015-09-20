import Tkinter as tk
from threading import Thread
import time
import myo_api.myo_api as myo_api
import MIDIConverter.MIDIConverter as MIDIConverter

root = tk.Tk()
root.title("MIDI GUI")

'''
CC# + Pitch Bend
'''
NUMBER_OF_PATCHES = 4

X = 'X'
Y = 'Y'
Z = 'Z'
ANGLE = 'ANGLE'

MYO_PARAMETERS = [X, Y, Z, ANGLE]
patchButtons = [None] * NUMBER_OF_PATCHES
patches = [None] * NUMBER_OF_PATCHES

PATCH_PREFIX = 'Patch '
for i in range(NUMBER_OF_PATCHES):
    patchButtons[i] = PATCH_PREFIX + str(i + 1)
    myoParamDict = dict()
    for myoParameter in MYO_PARAMETERS:
        myoParamDict[myoParameter] = None
    patches[i] = myoParamDict


# set up GUI

for i in range(len(patchButtons)):
    buttonName = patchButtons[i]
    button_style = 'raised'
    action = lambda x = buttonName: clickPatch_event(x)
    button = tk.Button(root, text=buttonName, width=20, height=15, relief=button_style, command=action)
    button.grid(row=1, column = 1 + i, sticky='nesw', )

for i in range(len(MYO_PARAMETERS)):
    e = tk.Label(root, text=MYO_PARAMETERS[i])
    e.grid(row=2+i, column=0)

display = tk.Entry(root, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)
display.insert(tk.END, "No Patch Selected Yet")

allDropDowns = [[None for j in range(len(MYO_PARAMETERS))] for i in range(NUMBER_OF_PATCHES)]

options = ["Pitch"] + map(str, range(1,128))
Vars = [[tk.StringVar() for j in range(len(MYO_PARAMETERS))] for i in range(NUMBER_OF_PATCHES)]

for patchNumber in range(NUMBER_OF_PATCHES):
    for myoParameterIndex in range(len(MYO_PARAMETERS)):

        var = Vars[patchNumber][myoParameterIndex]
        dropDownMenu = apply(tk.OptionMenu, (root, var) + tuple(options))
        dropDownMenu.grid(row = 2 + myoParameterIndex, column = 1 + patchNumber)

        allDropDowns[patchNumber][myoParameterIndex] = dropDownMenu


def clickPatch_event(key):

    display.delete(0, tk.END)
    display.insert(tk.END, key)

print patches
print Vars
'''
For use by Midi Converter
'''
def getValue(patchNumber, myoParam):
    index = MYO_PARAMETERS.index(myoParam)
    if index == -1:
        raise Exception("Myo Parameter: %s not valid" \
            %(myoParam))

    value = Vars[patchNumber][index].get()
    if value == '':
        return None
    else:
        return value

def mainLoop():
    myoInfo = myo_api.get_myo_info_object()
    midi = MIDIConverter.MidiConverter()
    while True:
        x = myoInfo.get("yaw") * 127
        y = myoInfo.get("pitch") * 127
        z = myoInfo.get("roll") * 127

        ccForX = getValue(1, X)
        ccForY = getValue(1, Y)
        ccForZ = getValue(1, Z)

        print "x", x
        print "y", y
        print "z", z

        print "ccForX", ccForX
        print "ccForY", ccForY
        print "ccForZ", ccForZ

        if ccForX != None:
            midi.sendCCMessage(int(ccForX), x)
        if ccForY != None:
            midi.sendCCMessage(int(ccForY), y)
        if ccForZ != None:
            midi.sendCCMessage(int(ccForZ), z)

        #print "Pitch",myoInfo.get("pitch")
        time.sleep(0.1)

thread = Thread(target=mainLoop)
thread.daemon = True
thread.start()

# RUNTIME
root.mainloop()
