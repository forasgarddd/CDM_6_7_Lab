from tkinter import *

root = Tk()
root.title("Title test")

text = Text(width = 100, height = 40, bg="white", fg="black", wrap=WORD)
text.pack()

#root.resizable(0,0)

root.mainloop()
