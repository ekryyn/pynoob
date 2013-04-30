#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from window import Ui_MainWindow
import syntax
import sys
import subprocess
from StringIO import StringIO

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        highlight = syntax.PythonHighlighter(self.ui.editor.document())
        self.ui.editor.document().setDefaultFont(QFont("Monospace", 10, QFont.Normal))

        self.connect(self.ui.actionRun, SIGNAL("triggered()"), self.on_run_program)

    def load(self, fd):
        self.ui.editor.setPlainText(fd.read())

    def currentText(self):
        return self.ui.editor.toPlainText()

    def on_run_program(self):
        out = StringIO()
        runner = PythonRunner(out)
        runner.execute(str(self.currentText()))
        out.seek(0)
        self.ui.console.insertPlainText(out.read())

class PythonRunner(object):
    def __init__(self, out):
        self.out = out

    def execute(self, python_code):
        old_out = sys.stdout
        sys.stdout = self.out
        exec(python_code)
        sys.stdout = old_out


def main():
    app = QApplication([])
    w = Window()

    f = open("syntax.py", 'r')
    w.load(f)

    w.show()
    app.exec_()

if __name__ == "__main__":
    main()
