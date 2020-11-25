from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Title test")

#New file function
def new_file():
    my_text.delete("1.0", END)
    root.title("New File")

#Open file function
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfile(initialdir="C:/Desktop", title="Open File", filetypes=(("Text files", "*.txt"), ("All Files", "*.*")))

    text_file = open(text_file, "r")
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

my_frame = Frame(root)
my_frame.pack(pady=5)

my_text = Text(my_frame, width=97, height=25, selectbackground="white", selectforeground="black", undo=True)
my_text.pack()

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add File menu
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#MenuBar(root)
root.mainloop()
