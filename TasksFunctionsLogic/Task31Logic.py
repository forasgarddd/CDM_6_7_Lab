from tkinter.filedialog import *
def a_to_a(self):
    self.root.title("Task 31")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    self.textArea.delete(1.0, END)
    line = " "
    while line != "":
        line = input("> ")
        chars = list(line)
        for i in range(len(chars)):
            if chars[i] == "a":
                chars[i] = "A"
            elif chars[i] == "A":
                chars[i] = "a"
        self.textArea.insert(1.0, chars)