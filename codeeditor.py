# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CodeEditor(QPlainTextEdit):
    def keyPressEvent(self, e):
        # <TAB> key
        if e.key() == Qt.Key_Tab:
            pos = self.textCursor().positionInBlock()
            toNext = 4 - (pos%4)
            self.insertPlainText(" "*toNext)

        # <BACKSPACE> key
        elif e.key() == Qt.Key_Backspace:
            pos = self.textCursor().positionInBlock()
            if pos > self.getBeginOfCurrentLine():
                self.textCursor().deletePreviousChar()
            elif pos > 0:
                prevIndent = pos - ((pos-1)%4)
                while pos >= prevIndent:
                    self.textCursor().deletePreviousChar()
                    pos -= 1
            else:
                self.textCursor().deletePreviousChar()

        # <RETURN> key
        elif e.key() == Qt.Key_Return:
            pos = self.getBeginOfCurrentLine()
            nni = self.nextNeedIndent()
            super(CodeEditor, self).keyPressEvent(e)
            self.insertPlainText(" "*pos)
            if nni:
                self.insertPlainText(" "*4)

        # OTHER
        else:
            super(CodeEditor, self).keyPressEvent(e)

    def getCurrentLine(self):
        cur = self.textCursor()
        return cur.block().text()

    def getBeginOfCurrentLine(self):
        string = self.getCurrentLine()
        p = string.indexOf(QRegExp("\\S"))
        if p < 0:
            return self.textCursor().positionInBlock()
        else:
            return p

    def nextNeedIndent(self):
        string = self.getCurrentLine()
        string = string.trimmed()
        last_char = QString( string.at( string.length()-1 ) )
        if last_char == ":":
            return True
        return False
