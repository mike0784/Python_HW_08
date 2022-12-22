from tkinter import *
from database import operationBD

class readingForm:
    def __init__(self, struct, database, id):
        self.id = id
        self.dbName = database
        self.bd = operationBD(database)
        self.window = Tk()
        self.window.title("Редактирование БД")
        self.window.geometry("200x150")

        lst = self.bd.selectRecordId(id)
        print(lst)
        frame = LabelFrame(self.window)
        frame.grid(column=0, row=0)
        i = 0

        Label(frame, text=struct["surname"]).grid(column=0, row=0)
        self.surname = Entry(frame)
        self.surname.grid(column=1, row=0)
        self.surname.insert(0, lst[0][1])

        Label(frame, text=struct["name"]).grid(column=0, row=1)
        self.name = Entry(frame)
        self.name.grid(column=1, row=1)
        self.name.insert(0, lst[0][2])

        Label(frame, text=struct["patronymic"]).grid(column=0, row=2)
        self.patronymic = Entry(frame)
        self.patronymic.grid(column=1, row=2)
        self.patronymic.insert(0, lst[0][3])

        Label(frame, text=struct["phone"]).grid(column=0, row=3)
        self.phone = Entry(frame)
        self.phone.grid(column=1, row=3)
        self.phone.insert(0, lst[0][4])

        frameBtn = LabelFrame(self.window)
        frameBtn.grid(column = 0, row = 1)
        btn = Button(frameBtn, text="Записать", command=self.record)
        btn.grid(column = 2, row = 3)


    def record(self):
        print(self.surname.get())
        lst = {"id" : self.id, "surname" : self.surname.get(), "name" : self.name.get(), "patronymic" : self.patronymic.get(), "phone" : self.phone.get()}
        self.bd.updateRecord(lst)
        self.window.destroy()