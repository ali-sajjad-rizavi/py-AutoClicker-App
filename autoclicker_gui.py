# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autoclicker_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, application):
        self.applicationHandle = application
        self.mainWindowHandle = MainWindow
        #----------------------------------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 251)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("robot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #--------------------------------------------------------------------
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.showFileBrowseDialog)
        #--------------------------------------------------------------------
        self.imagepath_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.imagepath_lineEdit.setEnabled(False)
        self.imagepath_lineEdit.setGeometry(QtCore.QRect(100, 20, 201, 20))
        self.imagepath_lineEdit.setObjectName("imagepath_lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(70, 110, 91, 51))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.applicationHandle.start_clicker_Thread)
        #-------------------------------------------------------------
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(190, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #-------------------------------------------------------------------
        self.waitingTime_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.waitingTime_spinBox.setGeometry(QtCore.QRect(210, 60, 61, 22))
        self.waitingTime_spinBox.setObjectName("waitingTime_spinBox")
        self.waitingTime_spinBox.setValue(5)
        #-------------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Clicker"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Image file:"))
        self.start_button.setText(_translate("MainWindow", "Start Auto-click"))
        self.status_label.setText(_translate("MainWindow", "Status: N/A"))
        self.label_3.setText(_translate("MainWindow", "Note: To stop the application, move your mouse\n"
"to the top-left corner of the screen."))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>Number of seconds to wait each time for the picture to appear on screen.</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Wait time (sec.)"))
        self.waitingTime_spinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Number of seconds to wait each time for the picture to appear on screen.</p></body></html>"))

    def showFileBrowseDialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.mainWindowHandle, 'Open file', '.',"Image files (*.jpg *.png)")[0]
        self.imagepath_lineEdit.setText(fname)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, None)
    MainWindow.show()
    sys.exit(app.exec_())
