from tkinter import *
from tkinter.filedialog import askopenfilename
import os

def open_file(self):
    self.file = askopenfilename(defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                           ("Text Documents", "*.txt")])
    if self.file == "":
        # no file to open
        self.file = None
    else:
        # try to open the file
        # set title
        self.root.title(os.path.basename(self.file) + " - Notepad")
        self.textArea.delete(1.0, END)
        ofile = open(self.file, "r")
        self.textArea.insert(1.0, ofile.read())
        ofile.close()