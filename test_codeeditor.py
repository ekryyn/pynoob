#!/usr/bin/env python

import sys
import unittest
from codeeditor import CodeEditor
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *


class TestIndentation(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)

    def test_simpleTyping(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "hello world")
        self.assertEqual(editor.toPlainText(), "hello world")

    def test_tabkey_fourspaces(self):
        editor = CodeEditor()
        QTest.keyClick(editor, Qt.Key_Tab)
        QTest.keyClicks(editor, "hello")
        self.assertEqual(editor.toPlainText(), "    hello")

    def test_tabkey_middle_twospaces(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "he")
        QTest.keyClick(editor, Qt.Key_Tab)
        QTest.keyClicks(editor, "llo")
        self.assertEqual(editor.toPlainText(), "he  llo")

    def test_beginOfLine_simple(self):
        editor = CodeEditor()
        editor.setPlainText("Hello !")
        self.assertEqual(editor.getBeginOfCurrentLine(), 0)

    def test_beginOfLine_blank(self):
        editor = CodeEditor()
        editor.setPlainText("        ")
        self.assertEqual(editor.getBeginOfCurrentLine(), 0)

    def test_beginOfLine_indented(self):
        editor = CodeEditor()
        editor.setPlainText("    Hello !")
        self.assertEqual(editor.getBeginOfCurrentLine(), 4)

    def test_backspace_RemovePrevious(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "hello worlde")
        QTest.keyClick(editor, Qt.Key_Backspace)
        self.assertEqual(editor.toPlainText(), "hello world")

    def test_backspace_RemoveIndent_on_LineBegin(self):
        editor = CodeEditor()
        editor.setPlainText("    if x == 1:")
        editor.moveCursor(QTextCursor.StartOfLine)
        editor.moveCursor(QTextCursor.Right)
        editor.moveCursor(QTextCursor.Right)
        editor.moveCursor(QTextCursor.Right)
        editor.moveCursor(QTextCursor.Right)
        QTest.keyClick(editor, Qt.Key_Backspace)
        self.assertEqual(editor.toPlainText(), "if x == 1:")

    def test_backspace_beginToPreviousLine(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "hello world")
        QTest.keyClick(editor, Qt.Key_Return)
        QTest.keyClick(editor, Qt.Key_Backspace)
        self.assertEqual(editor.toPlainText(), "hello world")

    def test_return_to_indented(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "    hello world")
        QTest.keyClick(editor, Qt.Key_Return)
        QTest.keyClicks(editor, "I'm indented")
        self.assertEqual(editor.toPlainText(), "    hello world\n    I'm indented")

    def test_next_line_need_indent(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "if x > 10:")
        assert(editor.nextNeedIndent())

    def test_return_to_indentedPlusOne_onNewBlock(self):
        editor = CodeEditor()
        QTest.keyClicks(editor, "if x > 10:")
        QTest.keyClick(editor, Qt.Key_Return)
        QTest.keyClicks(editor, "pass")
        self.assertEqual(editor.toPlainText(), "if x > 10:\n    pass")


if __name__ == "__main__":
    #suite = TestLoader().loadTestsFromTestCase(TestTab)
    #TextTestRunner(verbosity=2).run(suite)
    unittest.main()
