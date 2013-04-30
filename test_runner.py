#!/usr/bin/env python

import unittest
import sys
from pynoob import PythonRunner
from StringIO import StringIO
from PyQt4.QtGui import *

from pynoob import Window

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()

    def test_helloworld_python(self):
        src = "print('hello world !')"
        runner = PythonRunner(self.output)
        runner.execute(src)
        self.output.seek(0)
        self.assertEqual(self.output.read(), "hello world !\n")

class TestWindowRun(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)

    def test_load_text(self):
        w = Window()
        fd = StringIO("Hello")
        w.load(fd)
        self.assertEqual(w.currentText(), "Hello")

    def test_execute_action(self):
        w = Window()
        fd = StringIO("print('Hello world !')")
        w.load(fd)
        w.ui.actionRun.trigger()
        self.assertEqual(w.ui.console.toPlainText(), "Hello world !\n")

if __name__ == "__main__":
    unittest.main()
