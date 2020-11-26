from tkinter.filedialog import *


class Notepad:
    root = Tk()
    root.geometry("800x500")
    root.resizable(1, 1)

    # default window width and height
    textArea = Text(root, undo=True, wrap=None, height=300, width=300)
    textArea.grid(row=0, sticky=N + E + S + W)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # adding menu
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)

    # adding scrollbar
    scrollBar = Scrollbar(textArea, command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.pack(side=RIGHT, fill=Y)
    file = None

    def __init__(self):

        # set title
        self.root.title("Text Editor")

        # new file
        self.fileMenu.add_command(label="New",
                                  command=self.new_file)

        # open file
        self.fileMenu.add_command(label="Open",
                                  command=self.open_file)

        # save file
        self.fileMenu.add_command(label="Save",
                                  command=self.save_file)

        self.fileMenu.add_separator()

        # close app
        self.fileMenu.add_command(label="Exit",
                                  command=self.root.quit)

        self.menuBar.add_cascade(label="File",
                                 menu=self.fileMenu)

        self.root.config(menu=self.menuBar)

    def open_file(self):

        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                               ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # try to open the file
            # set title
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.textArea.delete(1.0, END)

            ofile = open(self.file, "r")

            self.textArea.insert(1.0, ofile.read())

            ofile.close()

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.textArea.delete(1.0, END)

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

    def run(self):

        # Run main application
        self.root.mainloop()

    # Run main application


notepad = Notepad()
notepad.run()
