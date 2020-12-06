from tkinter.filedialog import *


def a_more_than_b(self):

    self.root.title("Task 7")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    a_count = string_textarea.count("a") + string_textarea.count("A")
    b_count = string_textarea.count("b") + string_textarea.count("B")
    self.textArea.delete(1.0, END)
    if a_count > b_count:
        self.textArea.insert(1.0, "\n" + string_textarea)
        self.textArea.insert(1.0, "true")
    else:
        self.textArea.insert(1.0, "\n" + string_textarea)
        self.textArea.insert(1.0, "false")