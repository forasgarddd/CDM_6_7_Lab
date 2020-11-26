from tkinter import *

def palindrome_check(self):
    self.root.title("Task 35")
    self.file = None
    stextarea = self.textArea.get(1.0, END).replace("\n", "")
    lcstextarea = stextarea.lower()
    rev_stextarea = ''.join(reversed(lcstextarea))
    if len(lcstextarea.split()) > 1:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0,
                             "Введений текст не є вірним: " + "'" + stextarea + "'" + "\nНеможливо обробити більше 1 слова")
    elif rev_stextarea == lcstextarea:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, "слово: " + "'" + stextarea + "'" + " є паліндромом")
    elif rev_stextarea != lcstextarea:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, "слово: " + "'" + stextarea + "'" + " не є паліндромом")