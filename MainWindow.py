from tkinter import *
from tkinter import ttk
from functools import partial
from database import operationBD
from addForm import addForm
from readingForm import readingForm

class mainWindow:

    def __init__(self, struct, database):
        self.dbName = database
        self.bd = operationBD(database)
        self.struct = struct
        self.buildWindow()


    def buildWindow(self):
        self.window = Tk()
        self.window.title("Управление БД")
        self.window.geometry('1200x400')
        ss = self.tableFrame()
        ss.grid(column=1, row=0, columnspan=3, pady=5)

        frame = LabelFrame(self.window)
        frame.grid(column=1, row=1, columnspan=3, pady=5)

        btn1 = Button(frame, text="Вставить", command = self.addRecord)
        btn2 = Button(frame, text="Экспорт в CSV", command = self.exportRecord)
        btn3 = Button(frame, text="Импорт CSV", command = self.importRecord)
        btn1.grid(column=0, row=1)
        btn2.grid(column=1, row=1)
        btn3.grid(column=2, row=1)

        self.window.mainloop()

    def tableFrame(self):
        bd = operationBD(self.dbName)
        lst = bd.selectRecord()
        del bd

        self.TableFrame = LabelFrame(self.window)
        i = 0
        coll = 0
        rows = 0
        for item in self.struct:
            e = Label(self.TableFrame, width=20, fg='red', font=("Arial", 12, 'bold'), text=self.struct[item])
            e.grid(column = coll + 2, row = 0)
            coll = coll + 1
        for rows in range(len(lst)):
            Button(self.TableFrame, text="Редактировать", command=partial(self.readingRecord, lst[rows][0])).grid(column=0, row=rows+1)
            Button(self.TableFrame, text="Удалить", command=partial(self.deleteRecord, lst[rows][0])).grid(column=1, row=rows+1)
            for j in range(len(lst[0])):
                e = Entry(self.TableFrame, width=20, fg='blue', font=("Arial", 12, 'bold'))
                e.grid(column=j + 2, row=rows+1)
                e.insert(0, lst[rows][j])
        rows = rows + len(lst)
        return self.TableFrame

    def addRecord(self):
        form = addForm(self.struct, self.dbName)

    def readingRecord(self, id):
        form = readingForm(self.struct, self.dbName, id)

    def deleteRecord(self, id):
        bd = operationBD(self.dbName)
        bd.deleteRecord(id)
        del bd
        self.reloadFrame()

    def reloadFrame(self):
        self.TableFrame.destroy()
        ss = self.tableFrame()
        ss.grid(column=1, row=0, columnspan=3, pady=5)

    def exportRecord(self):
        fields = list(self.struct.keys())
        del fields[0]
        bd = operationBD(self.dbName)
        lst = {}
        lst = bd.selectRecord()
        del bd

        result = {}
        i = 1
        for row in lst:
            text = list(row)
            del text[0]
            ss = dict(zip(fields, text))
            result[i] = ss
            i = i + 1

        from settings import csvFile
        import csv
        with open(csvFile, 'w', newline = '') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fields)
            writer.writeheader()
            for row in result:
                writer.writerow(result[row])

    def importRecord(self):
        from settings import csvFile
        import csv
        result = {}
        bd = operationBD(self.dbName)
        with open(csvFile, 'r', newline='', encoding='cp1251') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
            for row in reader:
                bd.insertRecord(row)
        del bd
        self.reloadFrame()

