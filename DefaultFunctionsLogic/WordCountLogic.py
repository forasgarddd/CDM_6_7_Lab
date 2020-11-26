from tkinter import *

def find_word_count(self):
    if self.textArea.compare("end-1c", "!=", "1.0"):
        self.word_count_menu.entryconfig(0, label=str(str(len
                                                          (self.textArea.get(0.0, END).replace("\n", " ")
                                                           .split(" ")) - 1)
                                                      + " Words"))