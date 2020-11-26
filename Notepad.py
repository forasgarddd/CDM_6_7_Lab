from tkinter import *
from string import ascii_uppercase


class Notepad:
    # <<<Editor window parameters>>>

    root = Tk()
    root.geometry("800x500")
    root.resizable(1, 1)

    # default window settings
    textArea = Text(root, undo=True, wrap=None, height=300, width=300)
    textArea.grid(row=0, sticky=N + E + S + W)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # adding menu
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    countMenu = Menu(menuBar, tearoff=0)
    Task5Menu = Menu(menuBar, tearoff=0)

    # adding scrollbar
    scrollBar = Scrollbar(textArea, command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.pack(side=RIGHT, fill=Y)
    file = None

    # <<<Functions applications>>>

    def __init__(self):

        # set title
        self.root.title("Text Editor")

        # file menu cascade
        self.menuBar.add_cascade(label="File",
                                 menu=self.fileMenu)

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

        # count menu cascade
        self.menuBar.add_cascade(label="Count", menu=self.countMenu)

        # some functions to count menu
        self.line_count_menu = Menu(self.countMenu, tearoff=0, postcommand=self.findlinecount)
        self.word_count_menu = Menu(self.countMenu, tearoff=0, postcommand=self.findwordcount)

        self.countMenu.add_cascade(label="Line count", menu=self.line_count_menu)
        self.countMenu.add_cascade(label="Word count", menu=self.word_count_menu)

        self.line_count_menu.add_command(label="0 Lines", command=None)
        self.word_count_menu.add_command(label="0 Words", command=None)

        # Task5 menu cascade
        self.menuBar.add_cascade(label="Task 5", menu=self.Task5Menu)
        self.Task5Menu.add_command(label="Print A->Z", command=self.engalphprint)


        # config menu
        self.root.config(menu=self.menuBar)

    # <<<Functions logic>>>

    # to open file
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

    # to create a new file
    def new_file(self):
        self.root.title("New File - Text Editor")
        self.file = None
        self.textArea.delete(1.0, END)

    # to save file
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

    # to count lines
    def findlinecount(self):
        if self.textArea.compare("end-1c", "!=", "1.0"):
                self.line_count_menu.entryconfig(0, label=str(str(int
                                                                  (self.textArea.index('end').split('.')[0]) - 1)
                                                              + " Lines"))

    # to count words
    def findwordcount(self):
        if self.textArea.compare("end-1c", "!=", "1.0"):
                self.word_count_menu.entryconfig(0, label=str(str(len
                                                                  (self.textArea.get(0.0, END).replace("\n", " ").split(" ")) - 1)
                                                              + " Words"))

    #Task 5 logic
    def engalphprint(self):
        self.root.title("Task 5")
        self.file = None
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, ascii_uppercase)

    # app run function
    def run(self):
        self.root.mainloop()
