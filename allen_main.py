from typing_extensions import Self
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QTime
from create import Creator
from PyQt5 import QtGui

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Allen_Main.ui", self)
        self.__tasks = []
        self.initUI()

    @staticmethod
    def run_gui():
        app = QApplication([])
        ex = MainUI()
        app.exec_()

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("Hello World")
        self.show()

        self.setWindowIcon(QtGui.QIcon('images\Southlands.png'))

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

        with open("style/Adaptic.qss", "r") as fh:
            self.setStyleSheet(fh.read())
        self.addNewTaskButton.clicked.connect(self.addTask)
        self.completeTaskButton.clicked.connect(self.completeTask)
        self.newTaskInput.returnPressed.connect(self.addTask)
        self.addNewPlayerButton.clicked.connect(self.addPlayer)
        self.taskTable.setColumnWidth(0, 160)
        self.taskTable.setColumnWidth(1, 170)
        self.progressBar.setValue(0)

    def displayTime(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        self.currentTime.display(displayTxt)

    def addPlayer(self):
        create = Creator(self)

    def addTask(self):
        taskName = self.newTaskInput.text()
        task = {'title': taskName, 'status': False}
        self.__tasks.append(task)
        self.newTaskInput.clear()
        self.refreshTasks()
        self.updateProgess()

    def completeTask(self):
        print("Start complete task")
        selectedItems = self.taskTable.selectedItems()
        for item in selectedItems:
            for task in self.__tasks:
                if task['title'] == item.text():
                    task['status'] = True
                    break
        self.refreshTasks()
        self.updateProgess()
        
    def updateProgess(self):
        theLen = len(self.__tasks)
        theCounter = 0
        for cur in self.__tasks:
            if cur['status']:
                theCounter += 1
        theValue = theCounter / theLen
        print("The progress value", theValue)
        self.progressBar.setValue(int(theValue * 100))

    def refreshTasks(self):
        self.taskTable.setRowCount(0)
        self.taskTable.setRowCount(len(self.__tasks))
        for row, task in enumerate(self.__tasks):
            self.taskTable.setItem(row, 0, QTableWidgetItem(task['title']))
            self.taskTable.setItem(row, 1, QTableWidgetItem("Finished" if task["status"] else "Unfinished"))
    

if __name__ == "__main__":
    MainUI.run_gui()