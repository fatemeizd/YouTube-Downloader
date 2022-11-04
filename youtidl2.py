#Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pytube import YouTube

#Base Structure
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 508)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(62, 22, 57);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/user/Desktop/F7FKVFK034.png"))
        self.label.setObjectName("label")
        self.url_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.url_lineEdit.setGeometry(QtCore.QRect(50, 40, 601, 41))
        font = QtGui.QFont()
        font.setFamily("MRT_Furat")
        font.setPointSize(11)
        self.url_lineEdit.setFont(font)
        self.url_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius:20px;\n"
"    background-color: rgb(255, 221, 251);\n"
"}")
        self.url_lineEdit.setFrame(False)
        self.url_lineEdit.setObjectName("url_lineEdit")
        self.save_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_lineEdit.setGeometry(QtCore.QRect(50, 110, 521, 41))
        font = QtGui.QFont()
        font.setFamily("MRT_Furat")
        font.setPointSize(11)
        self.save_lineEdit.setFont(font)
        self.save_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius:20px;\n"
"    background-color: rgb(255, 221, 251);\n"
"}")
        self.save_lineEdit.setFrame(False)
        self.save_lineEdit.setObjectName("save_lineEdit")
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_loc())
        self.save_pushButton.setGeometry(QtCore.QRect(580, 110, 71, 41))
        self.save_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(252, 217, 255);\n"
"    border-radius:15px;\n"
"}")
        self.save_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/icons/folderloc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_pushButton.setIcon(icon)
        self.save_pushButton.setIconSize(QtCore.QSize(40, 40))
        self.save_pushButton.setObjectName("save_pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 160, 771, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        self.pic_label.setGeometry(QtCore.QRect(210, 180, 321, 81))
        self.pic_label.setStyleSheet("")
        self.pic_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pic_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic_label.setText("")
        self.pic_label.setPixmap(QtGui.QPixmap("C:/Users/user/Desktop/HD-wallpaper-youtube-violet-logo-violet-brickwall-youtube-logo-brands-youtube-neon-logo-youtube-thumbnail.jpg"))
        self.pic_label.setObjectName("pic_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 771, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 280, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton.setStyleSheet("QRadioButton{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::pressed{\n"
"    color: rgb(244, 216, 255);\n"
"    background-color: rgb(216, 180, 181);\n"
"}\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 30, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::pressed{\n"
"    color: rgb(244, 216, 255);\n"
"    background-color: rgb(216, 180, 181);\n"
"}\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.dl_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.download_it())
        self.dl_pushButton.setGeometry(QtCore.QRect(70, 400, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dl_pushButton.setFont(font)
        self.dl_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dl_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(212, 154, 229);\n"
"    border-radius:15px;\n"
"}")
        self.dl_pushButton.setObjectName("dl_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionYouTube_Downloader = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/icons/youtube.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYouTube_Downloader.setIcon(icon1)
        self.actionYouTube_Downloader.setObjectName("actionYouTube_Downloader")
        self.actionYouTube_Downloader_2 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/icons/yotube2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYouTube_Downloader_2.setIcon(icon2)
        self.actionYouTube_Downloader_2.setObjectName("actionYouTube_Downloader_2")
        self.menuAbout.addAction(self.actionYouTube_Downloader_2)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_loc(self):
        save_loc, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save as', '*.*')
        self.save_lineEdit.setText(str(save_loc))


    def download_it(self):
        if self.radioButton.isChecked() == True:
            url = self.url_lineEdit.text()
            save_path = self.save_lineEdit.text()
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            print(stream)
            stream.download(output_path = save_path)

            #Pop up box
            msg = QMessageBox()
            msg.setWindowTitle("Downloaded!")
            msg.setText("Your Video Downloaded!")
            msg.setIcon(QMessageBox.Information)
            a = msg.exec_()

        if self.radioButton_2.isChecked() == True:
            url = self.url_lineEdit.text()
            save_path = self.save_lineEdit.text()
            video = YouTube(url)
            stream = video.streams.get_audio_only()
            stream.download(output_path = save_path)

            #Pop up box
            msg = QMessageBox()
            msg.setWindowTitle("Downloaded!")
            msg.setText("Your Music Downloaded!")
            msg.setIcon(QMessageBox.Information)
            a = msg.exec_()

        self.url_lineEdit.setText("")
        self.save_lineEdit.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloade"))
        self.url_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter URL Of Video"))
        self.save_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Your Location For Save"))
        self.groupBox.setTitle(_translate("MainWindow", "Format"))
        self.radioButton.setText(_translate("MainWindow", "MP4"))
        self.radioButton_2.setText(_translate("MainWindow", "MP3(only audio)"))
        self.dl_pushButton.setText(_translate("MainWindow", "Start Download"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionYouTube_Downloader.setText(_translate("MainWindow", "YouTube Downloader"))
        self.actionYouTube_Downloader_2.setText(_translate("MainWindow", "YouTube Downloader"))

#Initialize The App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
