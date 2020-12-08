import math
from tkinter import END
from tkinter.filedialog import *


def convert(self):
    self.root.title("Task 20")
    self.file = None
    string_textarea = self.textArea.get(1.0, END)
    self.textArea.delete(1.0, END)
    try:
        i = (int) (string_textarea) - 1
        while i > 0:
            ternaryConverter(self, i)
            self.textArea.insert(1.0, "\n")
            i = i - 1
    except ValueError:
        self.textArea.insert(1.0, "Введений текст не є числом")



def ternaryConverter(self, number):
    arrayWith120 = []
    while number >= 1:
        digit = number % 3
        arrayWith120.append(digit)
        number = (number - digit) / 3

    i = 0
    while i < len(arrayWith120):
        self.textArea.insert(1.0, math.floor(arrayWith120[i]))
        i = i +1