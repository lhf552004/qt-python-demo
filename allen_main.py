from typing_extensions import Self
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QTime


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Allen_Main.ui", self)
        self.tasks = []
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
        with open("style/Adaptic.qss", "r") as fh:
            self.setStyleSheet(fh.read())
        self.addNewTaskButton.clicked.connect(self.addTask)
        self.completeTaskButton.clicked.connect(self.completeTask)
        self.taskTable.setColumnWidth(0, 160)
        self.taskTable.setColumnWidth(1, 170)
        self.progressBar.setValue(0)

    def addTask(self):
        taskName = self.newTaskInput.text()
        task = {'title': taskName, 'status': False}
        self.tasks.append(task)
        self.newTaskInput.clear()
        self.refreshTasks()
        self.updateProgess()

    def completeTask(self):
        print("Start complete task")
        selectedItems = self.taskTable.selectedItems()
        for item in selectedItems:
            for task in self.tasks:
                if task['title'] == item.text():
                    task['status'] = True
                    break
        self.refreshTasks()
        self.updateProgess()
        
    def updateProgess(self):
        theLen = len(self.tasks)
        theCounter = 0
        for cur in self.tasks:
            if cur['status']:
                theCounter += 1
        theValue = theCounter / theLen
        print("The progress value", theValue)
        self.progressBar.setValue(int(theValue * 100))

    def refreshTasks(self):
        # self.taskTable.clear()
        self.taskTable.setRowCount(len(self.tasks))
        for row, task in enumerate(self.tasks):
            self.taskTable.setItem(row, 0, QTableWidgetItem(task['title']))
            self.taskTable.setItem(row, 1, QTableWidgetItem("Finished" if task["status"] else "Unfinished"))
    

if __name__ == "__main__":
    MainUI.run_gui()