import csv
import os
from settings import *
from MainWindow import mainWindow


class application:
    def __init__(self):
        self.bd = operationBD(database)
        self.mWindow = mainWindow(struct)



if __name__ == "__main__":
    app = mainWindow(struct, database)

