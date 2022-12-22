from tkinter import *
from database import operationBD

class addForm:
    def __init__(self, struct, database):
        self.dbName = database
        self.bd = operationBD(database)
        self.window = Tk()
        self.window.title("Добавление в БД")
        self.window.geometry("200x150")

        frame = LabelFrame(self.window)
        frame.grid(column=0, row=0)
        i = 0
        Label(frame, text=struct["surname"]).grid(column=0, row=0)
        self.surname = Entry(frame)
        self.surname.grid(column=1, row=0)

        Label(frame, text=struct["name"]).grid(column=0, row=1)
        self.name = Entry(frame)
        self.name.grid(column=1, row=1)

        Label(frame, text=struct["patronymic"]).grid(column=0, row=2)
        self.patronymic = Entry(frame)
        self.patronymic.grid(column=1, row=2)

        Label(frame, text=struct["phone"]).grid(column=0, row=3)
        self.phone = Entry(frame)
        self.phone.grid(column=1, row=3)

        frameBtn = LabelFrame(self.window)
        frameBtn.grid(column = 0, row = 1)
        btn = Button(frameBtn, text="Записать", command=self.record)
        btn.grid(column = 2, row = 3)
        btnClose = Button(frameBtn, text="Закрыть", command=self.close)
        btnClose.grid(column = 3, row = 3)

    def record(self):
        lst = {"surname" : self.surname.get(), "name" : self.name.get(), "patronymic" : self.patronymic.get(), "phone" : self.phone.get()}
        self.bd.insertRecord(lst)
        self.surname.delete(0, END)
        self.name.delete(0, END)
        self.patronymic.delete(0, END)
        self.phone.delete(0, END)

    def close(self):
        del self.bd
        self.window.destroy()