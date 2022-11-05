from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication,
                             QMainWindow, QPushButton, QDialog, QCheckBox, QRadioButton)

from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer

import json
import copy


class Creator(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        loadUi('create.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Creating New...')
        self.show()


