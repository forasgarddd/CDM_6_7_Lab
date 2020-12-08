from tkinter.filedialog import *
from tkinter import *
i =0

def twoSimilarLetters(self):
    self.root.title("Task 38")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    self.textArea.delete(1.0, END)
    for i in range (len(string_textarea)):
        for b in range (i+1, len(string_textarea)):
            if string_textarea[i] == string_textarea[b]:
                self.textArea.insert(1.0, "The letter is "+ string_textarea[b])
