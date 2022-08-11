import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(964, 770)
        self.frame = QtWidgets.QFrame(Dialog)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame.setGeometry(QtCore.QRect(230, 20, 541, 741))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius:40px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 90, 541, 651))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 531, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(200, 410, 131, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 85, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 20, 531, 71))
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(140, 170, 321, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 270, 321, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 51, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(100, 270, 51, 51))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(150, 220, 301, 31))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(207, 0, 0);\n"
"background-color: rgb(0, 0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(160, 290, 281, 31))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(207, 0, 0);\n"
"background-color: rgb(255, 198, 202);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.page)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 350, 141, 31))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0,0,0,0);\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);\n"
"\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    \n"
"    color: rgb(0, 170, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.pushButton_10.raise_()
        self.label_6.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(0, 20, 531, 71))
        self.label_7.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 160, 321, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 520, 121, 51))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 85, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 250, 321, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 420, 321, 41))
        self.lineEdit_5.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 340, 321, 41))
        self.lineEdit_6.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(100, 140, 121, 21))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(69, 140, 51, 61))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(70, 230, 51, 61))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(100, 230, 121, 21))
        self.label_20.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(100, 320, 121, 21))
        self.label_21.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(100, 400, 121, 21))
        self.label_22.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(70, 320, 51, 61))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(70, 400, 51, 61))
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_7.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_20.raise_()
        self.label_10.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_23 = QtWidgets.QLabel(self.page_5)
        self.label_23.setGeometry(QtCore.QRect(0, 20, 531, 71))
        self.label_23.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_13.setGeometry(QtCore.QRect(150, 300, 241, 41))
        self.lineEdit_13.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_26 = QtWidgets.QLabel(self.page_5)
        self.label_26.setGeometry(QtCore.QRect(110, 280, 51, 61))
        self.label_26.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.page_5)
        self.label_27.setGeometry(QtCore.QRect(140, 280, 141, 21))
        self.label_27.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.page_5)
        self.label_28.setGeometry(QtCore.QRect(0, 170, 531, 41))
        self.label_28.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page_5)
        self.label_29.setGeometry(QtCore.QRect(0, 210, 531, 41))
        self.label_29.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page_5)
        self.label_30.setGeometry(QtCore.QRect(180, 330, 171, 41))
        self.label_30.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(207, 0, 0);\n"
"background-color: rgb(255, 198, 202);\n"
"border-radius:10px")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 470, 121, 51))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 85, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 294, 51, 51))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);\n"
"border-radius:20px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_31 = QtWidgets.QLabel(self.page_5)
        self.label_31.setEnabled(False)
        self.label_31.setGeometry(QtCore.QRect(390, 305, 61, 31))
        self.label_31.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.label_31.setMouseTracking(False)
        self.label_31.setTabletTracking(False)
        self.label_31.setAcceptDrops(False)
        self.label_31.setAutoFillBackground(False)
        self.label_31.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setScaledContents(False)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setWordWrap(False)
        self.label_31.setOpenExternalLinks(False)
        self.label_31.setObjectName("label_31")
        self.label_23.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.lineEdit_13.raise_()
        self.label_26.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.label_31.raise_()
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_32 = QtWidgets.QLabel(self.page_6)
        self.label_32.setGeometry(QtCore.QRect(0, 20, 531, 71))
        self.label_32.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 300, 321, 41))
        self.lineEdit_14.setStyleSheet("background-color: rgb(197, 206, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_33 = QtWidgets.QLabel(self.page_6)
        self.label_33.setGeometry(QtCore.QRect(99, 280, 51, 61))
        self.label_33.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"border-radius:10px")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.page_6)
        self.label_34.setGeometry(QtCore.QRect(130, 280, 161, 21))
        self.label_34.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 470, 141, 51))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 85, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_35 = QtWidgets.QLabel(self.page_6)
        self.label_35.setGeometry(QtCore.QRect(0, 170, 531, 41))
        self.label_35.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.page_6)
        self.label_36.setGeometry(QtCore.QRect(0, 210, 531, 41))
        self.label_36.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.label_63 = QtWidgets.QLabel(self.page_6)
        self.label_63.setGeometry(QtCore.QRect(180, 380, 181, 61))
        self.label_63.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 0);\n"
"background-color: rgb(199, 255, 193);\n"
"border-radius:10px")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.stackedWidget.addWidget(self.page_6)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 20, 331, 61))
        self.label_4.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 10, 21, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(227, 5, 9);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:10px")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 10, 21, 21))
        self.pushButton_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(229, 229, 0);\n"
"\n"
"border-radius:10px")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 10, 21, 21))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 211, 102);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"\n"
"border-radius:10px")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "LOGIN PAGE"))
        self.label_2.setText(_translate("Dialog", ""))
        self.label_3.setText(_translate("Dialog", ""))
        self.label_6.setText(_translate("Dialog", "Your password incorrect"))
        self.pushButton_10.setText(_translate("Dialog", "Forgot  password ?"))
        self.label_7.setText(_translate("Dialog", "SIGN UP PAGE"))
        self.pushButton_5.setText(_translate("Dialog", "Sing up"))
        self.label_8.setText(_translate("Dialog", "Username :"))
        self.label_9.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", ""))
        self.label_20.setText(_translate("Dialog", "Email :"))
        self.label_21.setText(_translate("Dialog", "Password :"))
        self.label_22.setText(_translate("Dialog", " Re-password :"))
        self.label_24.setText(_translate("Dialog", ""))
        self.label_25.setText(_translate("Dialog", ""))
        self.label_23.setText(_translate("Dialog", "Verification Your Email"))
        self.label_26.setText(_translate("Dialog", ""))
        self.label_27.setText(_translate("Dialog", "Verification code:"))
        self.label_28.setText(_translate("Dialog", "Check your email [ example@gmail.com ]"))
        self.label_29.setText(_translate("Dialog", "For verfication code."))
        self.label_30.setText(_translate("Dialog", "Code incorrect"))
        self.pushButton_8.setText(_translate("Dialog", "Verificate"))
        self.pushButton_9.setText(_translate("Dialog", ""))
        self.label_31.setText(_translate("Dialog", "0:59"))
        self.label_32.setText(_translate("Dialog", "Rest password"))
        self.label_33.setText(_translate("Dialog", ""))
        self.label_34.setText(_translate("Dialog", "Username or Email :"))
        self.pushButton_11.setText(_translate("Dialog", "Rest password"))
        self.label_35.setText(_translate("Dialog", "Check your email [ example@gmail.com ]"))
        self.label_36.setText(_translate("Dialog", "To rest your password"))
        self.label_63.setText(_translate("Dialog", "URLl sent to your Email"))
        self.label_4.setText(_translate("Dialog", "APP NAME"))
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())