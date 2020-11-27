from tkinter import *


def print_uppercase(self):

    self.root.title("Task 49")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    upper_textarea = string_textarea.upper()
    self.textArea.delete(1.0, END)
    self.textArea.insert(1.0, upper_textarea)
