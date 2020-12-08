from tkinter import END
from tkinter.filedialog import *

def decimalToRoman (self):
    self.root.title("Task 20")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    self.textArea.delete(1.0, END)
    number = int(string_textarea)
    num = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
    summ = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            self.textArea.insert(2.0, summ[i])
            div -= 1
        i -= 1