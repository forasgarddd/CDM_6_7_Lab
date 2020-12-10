from tkinter import *
from tkinter.ttk import Combobox

def zodiak(self):
    def clicked():
        if (20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31) == ("Января"):
            res1 = "Твой знак зодиака: Водолей"
            lbl4.configure(text=res1)

    window = Tk()
    window.title("Знак зодиака")
    window.geometry('800x500')

    lbl = Label(window, text="Добро пожаловать! Давай узнаем кто ты по знаку зодиака!", font=("Arial Bold", 12))
    lbl.grid(column=0, row=0)

    lbl1 = Label(window, text="Введи день своего рождения:", font=("Arial Bold", 12))
    lbl1.grid(column=0, row=1)

    lbl2 = Label(window, text="Введи месяц своего рождения:", font=("Arial Bold", 12))
    lbl2.grid(column=0, row=2)

    lbl3 = Label(window, text="", font=("Arial Bold", 12))
    lbl3.grid(column=0, row=4)

    lbl4 = Label(window, text="", font=("Arial Bold", 12))
    lbl4.grid(column=0, row=5)

    combo1 = Combobox(window)
    combo1['values'] = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
    combo1.current(1)
    combo1.grid(column=1, row=1)

    combo2 = Combobox(window)
    combo2['values'] = (
    "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
    "Декабря")
    combo2.current(2)
    combo2.grid(column=1, row=2)

    btn = Button(window, text="Клик", bg="yellow", fg="blue", command=clicked)
    btn.grid(column=0, row=3)

    window.mainloop()