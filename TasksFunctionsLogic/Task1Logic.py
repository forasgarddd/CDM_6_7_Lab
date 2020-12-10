from tkinter.filedialog import *

def indexCount(self):
    self.root.title("Task 1")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    lower_stextarea = string_textarea.lower()
    sstextarea = list(lower_stextarea)
    output = []
    for character in sstextarea:
        number = ord(character) - 96
        output.append(number)

    output.pop()
    sumo = sum(output)
    self.textArea.delete(1.0, END)
    self.textArea.insert(1.0, sumo)