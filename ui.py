# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 295)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(50, 20, 95, 13))
        self.title.setObjectName("title")
        self.result = QtWidgets.QLabel(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(50, 50, 102, 13))
        self.result.setObjectName("result")
        self.use_letters = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.use_letters.setGeometry(QtCore.QRect(30, 130, 155, 17))
        self.use_letters.setObjectName("use_letters")
        self.use_numbers = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.use_numbers.setGeometry(QtCore.QRect(30, 180, 147, 17))
        self.use_numbers.setObjectName("use_numbers")
        self.generate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(60, 220, 75, 23))
        self.generate.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.generate.setStyleSheet("background: white;\n"
"font-size: 12px;\n"
"font-family: sans-serif;")
        self.generate.setObjectName("generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.result.setText(_translate("MainWindow", "тут буде результат"))
        self.use_letters.setText(_translate("MainWindow", "використовувати алфавіт"))
        self.use_numbers.setText(_translate("MainWindow", "використовувати цифри"))
        self.generate.setText(_translate("MainWindow", "Згенерувати"))
