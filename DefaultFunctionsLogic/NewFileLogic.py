from tkinter import *

def new_file(self):
    self.root.title("New File - Text Editor")
    self.file = None
    self.textArea.delete(1.0, END)