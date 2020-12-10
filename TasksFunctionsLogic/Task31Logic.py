from tkinter import *
from tkinter.filedialog import *
def a_to_a(self):
    self.root.title("Task 31")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    sstextarea = list(string_textarea)
    for i in range(len(sstextarea)):
        if sstextarea[i] == "a":
            sstextarea[i] = "A"
    ssstextarea = ''.join(sstextarea)
    self.textArea.delete(1.0, END)
    self.textArea.insert(1.0, ssstextarea)