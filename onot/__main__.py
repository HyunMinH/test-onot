#!/usr/bin/env python3
from PyQt6.QtGui import QAction, QIcon

# SPDX-FileCopyrightText: Copyright 2022 SK TELECOM CO., LTD. <haksung@sk.com>
# SPDX-FileCopyrightText: Copyright (c) 2022 Kakao Corp. https://www.kakaocorp.com
#
# SPDX-License-Identifier: Apache-2.0

from onot.tools import create_notice
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QTextEdit, QMainWindow, QPushButton, QBoxLayout
import sys


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        fileOpenButton = QPushButton('Open File', self)
        fileOpenButton.clicked.connect(self.showDialog)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
    create_notice.main()


if __name__ == '__main__':
    main()