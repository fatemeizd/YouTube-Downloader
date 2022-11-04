#Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from todoCal import Ui_SecondWindow

#Base Strcture
class Ui_MainWindow(object):
    #Open Second Window
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()  
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.ui.hello_label.setText("HELLO !!")
        thing = self.user_lineEdit.text()
        #Assign thing to second window label
        self.ui.name_label.setText(f'{thing} :)')
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 230)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(189, 189, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_lineEdit.setGeometry(QtCore.QRect(30, 70, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(237, 241, 255);\n"
"    color: rgb(255, 93, 158);\n"
"    border-radius:15px;\n"
"}")
        self.user_lineEdit.setFrame(False)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 93, 158);\n"
"    background-color: rgb(139, 131, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(20, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.user_label.setFont(font)
        self.user_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_label.setStyleSheet("QLabel{\n"
"    color:rgb(232, 74, 95);\n"
"    background-color: rgb(189, 189, 255);\n"
"}")
        self.user_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.user_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 120, 301, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 384, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Let\'s Go"))
        self.user_label.setText(_translate("MainWindow", "Enter Your Name:"))

#Initialize The App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
