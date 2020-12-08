
from tkinter import *
from string import ascii_uppercase

from tkinter.filedialog import *



class Notepad:
    from DefaultFunctionsLogic.OpenFileLogic import open_file
    from DefaultFunctionsLogic.NewFileLogic import new_file
    from DefaultFunctionsLogic.SaveFileLogic import save_file
    from DefaultFunctionsLogic.LineCountLogic import find_line_count
    from DefaultFunctionsLogic.WordCountLogic import find_word_count
    from TasksFunctionsLogic.Task5Logic import eng_alphabet_print
    from TasksFunctionsLogic.Task7Logic import a_more_than_b
    from TasksFunctionsLogic.Task35Logic import palindrome_check
    from TasksFunctionsLogic.Task49Logic import print_uppercase
    from TasksFunctionsLogic.Task20Logic import convert
    from TasksFunctionsLogic.Task38Logic import twoSimilarLetters
    from TasksFunctionsLogic.Task56Logic import decimalToRoman

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
    task35Menu = Menu(menuBar, tearoff=0)
    task49Menu = Menu(menuBar, tearoff=0)
    task20Menu = Menu(menuBar, tearoff=0)
    task38Menu = Menu(menuBar, tearoff=0)
    task56Menu = Menu(menuBar, tearoff=0)

    # adding scrollbar
    scrollBar = Scrollbar(textArea, command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)
    scrollBar.pack(side=RIGHT, fill=Y)

    file = None

    # app run function
    def run(self):
        self.root.mainloop()

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
        self.task5Menu.add_command(label="Print A->Z", command=self.eng_alphabet_print)

        # task 7 menu cascade and execution
        self.menuBar.add_cascade(label="Task 7", menu=self.task7Menu)
        self.task7Menu.add_command(label="Is 'a' more than 'b'?", command=self.a_more_than_b)

        # task 35 menu cascade and execution
        self.menuBar.add_cascade(label="Task 35", menu=self.task35Menu)
        self.task35Menu.add_command(label="Is palindrome?", command=self.palindrome_check)

        # task 49 menu cascade and execution
        self.menuBar.add_cascade(label="Task 49", menu=self.task49Menu)
        self.task49Menu.add_command(label="Print uppercase", command=self.print_uppercase)

        # task 20 menu cascade and execution
        self.menuBar.add_cascade(label="Task 20", menu=self.task20Menu)
        self.task20Menu.add_command(label="Convert to trinary all before it", command=self.convert)

        # task 38 menu cascade and execution
        self.menuBar.add_cascade(label="Task 38", menu=self.task38Menu)
        self.task38Menu.add_command(label="Find two similar letters", command=self.twoSimilarLetters)

        # task 56 menu cascade and execution
        self.menuBar.add_cascade(label="Task 56", menu=self.task56Menu)
        self.task56Menu.add_command(label="Convert decimal to roman", command=self.decimalToRoman)


        # config menu
        self.root.config(menu=self.menuBar)
