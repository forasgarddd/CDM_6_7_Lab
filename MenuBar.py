from tkinter import Menu

class MenuBar:

    def __init__(self, root):

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open")
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Close")

        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu = menubar)

