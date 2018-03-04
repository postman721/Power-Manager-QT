# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#Power manager-QT v.7 Copyright (c) 2017 JJ Posti <techtimejourney.net> 
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
        try:
            subprocess.Popen(['gksudo', 'poweroff'])
        except Exception as e:
            print("Error: gksudo not installed.")

#Reboot function
    def reb(self,widget):
        try:
            subprocess.Popen(['gksudo', 'reboot'])
        except Exception as e:
            print("Error: gksudo not installed.")
#Suspend function
    def sus(self,widget):
        try:
            subprocess.Popen(['gksudo', 'pm-suspend'])        
        except Exception as e:
            print("Error: gksudo not installed.")

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
        try:
            subprocess.Popen(['i3lock', '-c', '202020', '-n'])  
        except Exception as e:
            print("Error i3clock is not installed.")
			
    def setupUi(self, power_manager):
        power_manager.setObjectName(_fromUtf8("power_manager"))
        power_manager.setFixedSize(330, 175)

        power_manager.setStyleSheet("background-color:#575656; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
        self.gridLayout = QGridLayout(power_manager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.lock = QPushButton(power_manager)
        self.lock.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")   
        self.lock.setObjectName(_fromUtf8("lock"))
        self.verticalLayout.addWidget(self.lock)
        self.lock.clicked.connect(self.lockme)
        
        self.out = QPushButton(power_manager)
        self.out.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")   
        self.out.setObjectName(_fromUtf8("out"))
        self.verticalLayout.addWidget(self.out)
        self.out.clicked.connect(self.out1)

        self.suspend = QPushButton(power_manager)
        self.suspend.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")   
        self.suspend.setObjectName(_fromUtf8("suspend"))
        self.verticalLayout.addWidget(self.suspend)
        self.suspend.clicked.connect(self.sus)

        self.reboot = QPushButton(power_manager)
        self.reboot.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")   
        self.reboot.setObjectName(_fromUtf8("reboot"))
        self.verticalLayout.addWidget(self.reboot)
        self.reboot.clicked.connect(self.reb)

        self.shut = QPushButton(power_manager)
        self.shut.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}")   
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
