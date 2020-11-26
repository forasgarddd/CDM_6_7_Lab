from tkinter.filedialog import *

def a_more_than_b(self):
    self.root.title("Task 7")
    self.file = None
    stextarea = self.textArea.get(1.0, END)
    a_count = stextarea.count("a") + stextarea.count("A")
    b_count = stextarea.count("b") + stextarea.count("B")
    self.textArea.delete(1.0, END)
    if a_count > b_count:
        self.textArea.insert(1.0, "\n" + stextarea)
        self.textArea.insert(1.0, "true")
    else:
        self.textArea.insert(1.0, "\n" + stextarea)
        self.textArea.insert(1.0, "false")