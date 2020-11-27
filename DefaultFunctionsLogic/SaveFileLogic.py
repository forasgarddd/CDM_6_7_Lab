from tkinter import *
from tkinter.filedialog import asksaveasfilename

def save_file(self):
    if self.file == None:
        # save as new file
        self.file = asksaveasfilename(initialfile='Untitled.txt',
                                      defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            # try to save the file
            file = open(self.file, "w")
            file.write(self.textArea.get(1.0, END))
            file.close()
            # change title
            self.root.title(os.path.basename(self.file) + " - Notepad")
    else:
        file = open(self.file, "w")
        file.write(self.textArea.get(1.0, END))
        file.close()