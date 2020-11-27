from tkinter.filedialog import *
from string import ascii_uppercase

def eng_alph_print(self):
    self.root.title("Task 5")
    self.file = None
    self.textArea.delete(1.0, END)
    self.textArea.insert(1.0, ascii_uppercase)