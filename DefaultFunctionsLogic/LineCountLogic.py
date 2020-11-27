from tkinter import *

def find_line_count(self):
    if self.textArea.compare("end-1c", "!=", "1.0"):
        self.line_count_menu.entryconfig(0, label=str(str(int
                                                          (self.textArea.index('end')
                                                           .split('.')[0]) - 1)
                                                      + " Lines"))