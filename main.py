from tkinter import *
from MenuBar import MenuBar

root = Tk()
root.title("Title test")

text = Text(width = 100, height = 40, bg="white", fg="black", wrap=WORD)
text.pack()
"""
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")

mainmenu.add_cascade(label="File", menu=filemenu)
"""
MenuBar(root)
root.mainloop()
