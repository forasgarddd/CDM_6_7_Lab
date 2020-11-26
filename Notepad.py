from tkinter.filedialog import *
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

    # adding menus
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    countMenu = Menu(menuBar, tearoff=0)
    task5Menu = Menu(menuBar, tearoff=0)
    task7Menu = Menu(menuBar, tearoff=0)

    # adding scrollbar
    scrollBar = Scrollbar(textArea, command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.pack(side=RIGHT, fill=Y)
    file = None

    # <<<Functions executions>>>

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
        self.line_count_menu = Menu(self.countMenu, tearoff=0, postcommand=self.find_line_count)
        self.word_count_menu = Menu(self.countMenu, tearoff=0, postcommand=self.find_word_count)

        self.countMenu.add_cascade(label="Line count", menu=self.line_count_menu)
        self.countMenu.add_cascade(label="Word count", menu=self.word_count_menu)

        self.line_count_menu.add_command(label="0 Lines", command=None)
        self.word_count_menu.add_command(label="0 Words", command=None)

        # task 5 menu cascade and execution
        self.menuBar.add_cascade(label="Task 5", menu=self.task5Menu)
        self.task5Menu.add_command(label="Print A->Z", command=self.eng_alph_print)

        # task 7 menu cascade and execution
        self.menuBar.add_cascade(label="Task 7", menu=self.task7Menu)
        self.task7Menu.add_command(label="Is 'a' more than 'b'?", command=self.a_more_than_b)

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
    def find_line_count(self):
        if self.textArea.compare("end-1c", "!=", "1.0"):
                self.line_count_menu.entryconfig(0, label=str(str(int
                                                                  (self.textArea.index('end').split('.')[0]) - 1)
                                                              + " Lines"))

    # to count words
    def find_word_count(self):
        if self.textArea.compare("end-1c", "!=", "1.0"):
                self.word_count_menu.entryconfig(0, label=str(str(len
                                                                  (self.textArea.get(0.0, END).replace("\n", " ").split(" ")) - 1)
                                                              + " Words"))

    # task 5 logic
    def eng_alph_print(self):
        self.root.title("Task 5")
        self.file = None
        self.textArea.delete(1.0, END)
        self.textArea.insert(1.0, ascii_uppercase)

    # task 7 logic
    def a_more_than_b(self):
        self.root.title("Task 7")
        self.file = None
        stextarea = self.textArea.get("1.0", END)
        a_count = stextarea.count("a") + stextarea.count("A")
        b_count = stextarea.count("b") + stextarea.count("B")
        self.textArea.delete(1.0, END)
        if a_count > b_count:
            self.textArea.insert(1.0, "\n" + stextarea)
            self.textArea.insert(1.0, "true")
        else:
            self.textArea.insert(1.0, "\n" + stextarea)
            self.textArea.insert(1.0, "false")

    # app run function
    def run(self):
        self.root.mainloop()
