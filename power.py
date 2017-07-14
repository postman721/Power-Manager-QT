# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Power manager-QT v.5.1 Copyright (c) 2017 JJ Posti <techtimejourney.net> 
#This is a power manager application.The program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991 This is the QT5 version" )
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QPushButton, QVBoxLayout, QMessageBox, QGridLayout 	
from PyQt5.QtGui import QBrush, QPalette, QColor, QFont,  QPixmap
import os, sys, subprocess, time
from subprocess import Popen 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QApplication.UnicodeUTF8
    
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_power_manager(object):
	#Shutdown function
    def powe(self,widget):
        subprocess.Popen(['gksudo', 'poweroff'])
#Reboot function
    def reb(self,widget):
        subprocess.Popen(['gksudo', 'reboot'])
#Suspend function
    def sus(self,widget):
        subprocess.Popen(['gksudo', 'pm-suspend'])        
#Logout function
    def out1(self, event):        
        reply = QMessageBox.question(None, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            subprocess.Popen(['openbox', '--exit'])    
        if reply == QMessageBox.No:            
            pass                            
#Lock screen
    def lockme(self,widget):
        subprocess.Popen(['i3lock', '-c', '202020', '-n'])  
		
    def setupUi(self, power_manager):
        power_manager.setObjectName(_fromUtf8("power_manager"))
        power_manager.setFixedSize(330, 175)

        self.gridLayout = QGridLayout(power_manager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.lock = QPushButton(power_manager)
        self.lock.setObjectName(_fromUtf8("lock"))
        self.verticalLayout.addWidget(self.lock)
        self.lock.clicked.connect(self.lockme)
        
        self.out = QPushButton(power_manager)
        self.out.setObjectName(_fromUtf8("out"))
        self.verticalLayout.addWidget(self.out)
        self.out.clicked.connect(self.out1)

        self.suspend = QPushButton(power_manager)
        self.suspend.setObjectName(_fromUtf8("suspend"))
        self.verticalLayout.addWidget(self.suspend)
        self.suspend.clicked.connect(self.sus)

        self.reboot = QPushButton(power_manager)
        self.reboot.setObjectName(_fromUtf8("reboot"))
        self.verticalLayout.addWidget(self.reboot)
        self.reboot.clicked.connect(self.reb)

        self.shut = QPushButton(power_manager)
        self.shut.setObjectName(_fromUtf8("shut"))
        self.verticalLayout.addWidget(self.shut)
        self.shut.clicked.connect(self.powe)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(power_manager)
        QtCore.QMetaObject.connectSlotsByName(power_manager)

    def retranslateUi(self, power_manager):
        power_manager.setWindowTitle(_translate("power_manager", "Power Manager", None))
        self.lock.setText(_translate("power_manager", "Lock screen", None))
        self.out.setText(_translate("power_manager", "Logout ", None))
        self.suspend.setText(_translate("power_manager", "Suspend", None))
        self.reboot.setText(_translate("power_manager", "Reboot", None))
        self.shut.setText(_translate("power_manager", "Power off", None))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    power_manager = QWidget()
    ui = Ui_power_manager()
    ui.setupUi(power_manager)
    power_manager.show()
    sys.exit(app.exec_())
