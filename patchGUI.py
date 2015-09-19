import Tkinter as tk

patch = tk.Tk()
patch.title("patch GUI")

buttons = [
'patch 1',  'patch 2',  'patch 3',  'patch 4']


# set up GUI
row = 1
col = 0
for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(patch, text = i, width = 7, height = 7, relief = button_style, command = action) \
        .grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 4:
        col = 0
        row += 1

display = tk.Entry(patch, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)



patch.mainloop()