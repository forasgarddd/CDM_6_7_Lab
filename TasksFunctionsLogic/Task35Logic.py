from tkinter import *


def palindrome_check(self):

    self.root.title("Task 35")
    self.file = None
    string_textarea = self.textArea.get(1.0, END).replace("\n", "")
    lc_string_textarea = string_textarea.lower()
    rev_stextarea = ''.join(reversed(lc_string_textarea))
    if len(lc_string_textarea.split()) > 1:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0,
                             "Введений текст не є вірним: " + "'" + string_textarea + "'" + "\nНеможливо обробити більше 1 слова")
    elif rev_stextarea == lc_string_textarea:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, "слово: " + "'" + string_textarea + "'" + " є паліндромом")
    elif rev_stextarea != lc_string_textarea:
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, "слово: " + "'" + string_textarea + "'" + " не є паліндромом")