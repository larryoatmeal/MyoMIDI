import Tkinter as tk
 
root = tk.Tk()
root.title("MIDI GUI")

'''
CC# + Pitch Bend
'''
NUMBER_OF_PATCHES = 4
MYO_PARAMETERS = ['X', 'Y', 'Z', 'ANGLE']
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

def displayParameters():
    options = ["Pitch"] + map(str, range(1,128))
    for patchNumber in range(NUMBER_OF_PATCHES):
        for myoParameterIndex in range(len(MYO_PARAMETERS)):

            var = tk.StringVar()
            dropDownMenu = apply(tk.OptionMenu, (root, var) + tuple(options))
            dropDownMenu.grid(row = 2 + myoParameterIndex, column = 1 + patchNumber)


displayParameters()


def clickPatch_event(key):

    display.delete(0, tk.END)
    display.insert(tk.END, key)




'''
For use by Midi Converter
'''
def getValue(patchNumber, myoParam):
    if patches[myoParam] == None:
        raise Exception("failed to set the patch + param value for Patch: %s, Myo Parameter: %s" \
            %(pathNumber, myoParam))
    return patches[myoParam]



# RUNTIME
root.mainloop()







'''
    # = -> rootulate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
            
        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
            
    # C -> clear display        
    elif key == 'C':
        display.delete(0, tk.END)
        
        
    # $ -> clear display        
    elif key == '$':
        display.delete(0, tk.END)
        display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")
        

    # @ -> clear display        
    elif key == '@':
        display.delete(0, tk.END)
        display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")        

        
    # neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

    # clear display and start new input     
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)
'''