#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *

from window import Ui_MainWindow
import syntax

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        infile = open('pynoob.py', 'r')
        highlight = syntax.PythonHighlighter(self.ui.editor.document())
        self.ui.editor.document().setDefaultFont(QFont("Monospace", 10, QFont.Normal))
        self.ui.editor.setPlainText(infile.read())

def main():
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()
