# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from Chapter03.firstMainWin import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.CB01.setChecked(False)
        self.CB01.clicked['bool'].connect(self.label.setEnabled)
        self.CB02.clicked['bool'].connect(self.lineEdit.setVisible)
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
