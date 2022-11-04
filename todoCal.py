#Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from persiantools.jdatetime import JalaliDate
from datetime import date, datetime
import sqlite3
import sys

#Create a database or connect to one
conn = sqlite3.connect('mylist.db')
#Create a cursor
c = conn.cursor()

#Create a tabel
c.execute('CREATE TABLE IF NOT EXISTS ' +''+ 'todo_list(list_item text, date integer, time integer)')

#Commit the changes
conn.commit()

#Close our connection
conn.close()

#Base Structure
class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(721, 729)
        SecondWindow.setAutoFillBackground(False)
        SecondWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(198, 223, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 681))
        self.label.setTabletTracking(False)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/user/Desktop/todo-list-seamless-pattern-universal-background-vector-7561340.jpg"))
        self.label.setObjectName("label")
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(10, 15, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hello_label.setFont(font)
        self.hello_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.hello_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(242, 161, 4);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.hello_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.hello_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hello_label.setText("")
        self.hello_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hello_label.setObjectName("hello_label")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(10, 56, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.name_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(242, 161, 4);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.name_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.name_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_label.setText("")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 46, 161, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.show_label = QtWidgets.QLabel(self.centralwidget)
        self.show_label.setGeometry(QtCore.QRect(180, 10, 531, 121))
        self.show_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.show_label.setStyleSheet("QLabel{\n"
"    background-color: rgb(198, 223, 255);\n"
"    border-radius:15px;\n"
"}")
        self.show_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.show_label.setText("")
        self.show_label.setObjectName("show_label")
        self.day_label = QtWidgets.QLabel(self.centralwidget)
        self.day_label.setGeometry(QtCore.QRect(190, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(22)
        self.day_label.setFont(font)
        self.day_label.setStyleSheet("QLabel{\n"
"    color: rgb(240, 196, 63);\n"
"}")
        self.day_label.setText("")
        self.day_label.setObjectName("day_label")
        self.month_label = QtWidgets.QLabel(self.centralwidget)
        self.month_label.setGeometry(QtCore.QRect(280, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("QLabel{\n"
"    color: rgb(240, 196, 63);\n"
"}")
        self.month_label.setText("")
        self.month_label.setObjectName("month_label")
        self.year_label = QtWidgets.QLabel(self.centralwidget)
        self.year_label.setGeometry(QtCore.QRect(290, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(22)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("QLabel{\n"
"    color: rgb(240, 196, 63);\n"
"}")
        self.year_label.setText("")
        self.year_label.setObjectName("year_label")
        self.day_2_label = QtWidgets.QLabel(self.centralwidget)
        self.day_2_label.setGeometry(QtCore.QRect(500, 50, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(14)
        self.day_2_label.setFont(font)
        self.day_2_label.setStyleSheet("QLabel{\n"
"    color: rgb(240, 196, 63);\n"
"}")
        self.day_2_label.setText("")
        self.day_2_label.setObjectName("day_2_label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 351, 261))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    color: rgb(242, 255, 99);\n"
"    font: 11pt \"Swis721 Blk BT\";\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.input_calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.input_calendarWidget.setGeometry(QtCore.QRect(10, 30, 331, 221))
        self.input_calendarWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.input_calendarWidget.setStyleSheet("")
        self.input_calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.input_calendarWidget.setGridVisible(True)
        self.input_calendarWidget.setObjectName("input_calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 390, 351, 291))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    font: 11pt \"Swis721 Blk BT\";\n"
"    color: rgb(255, 112, 155);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.input_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_lineEdit.setGeometry(QtCore.QRect(10, 40, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_lineEdit.setFont(font)
        self.input_lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius:15px;\n"
"    background-color: rgb(196, 255, 201);\n"
"    color: rgb(104, 74, 255);\n"
"}")
        self.input_lineEdit.setFrame(False)
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.add_pushButton = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda: self.add_it())
        self.add_pushButton.setGeometry(QtCore.QRect(310, 40, 31, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.add_pushButton.setFont(font)
        self.add_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(79, 136, 85);\n"
"    background-color: rgb(255, 117, 154);\n"
"    border-radius:15px;\n"
"}")
        self.add_pushButton.setObjectName("add_pushButton")
        self.delete_pushButton = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda: self.delete_it())
        self.delete_pushButton.setGeometry(QtCore.QRect(20, 140, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(189, 217, 158);\n"
"    color: rgb(255, 133, 162);\n"
"}")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.clear_pushButton = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda: self.clear_it())
        self.clear_pushButton.setGeometry(QtCore.QRect(180, 140, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clear_pushButton.setFont(font)
        self.clear_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 133, 162);\n"
"    color: rgb(189, 217, 158); \n"
"}")
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.save_pushButton = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda: self.save_it())
        self.save_pushButton.setGeometry(QtCore.QRect(20, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 133, 162);\n"
"    color: rgb(189, 217, 158); \n"
"}")
        self.save_pushButton.setObjectName("save_pushButton")
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(10, 210, 321, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.exit_pushButton = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda: self.exit())
        self.exit_pushButton.setGeometry(QtCore.QRect(180, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_pushButton.setFont(font)
        self.exit_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(189, 217, 158);\n"
"    color: rgb(255, 133, 162);\n"
"}")
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(369, 130, 351, 191))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"    color: rgb(242, 255, 99);\n"
"    font: 11pt \"Swis721 Blk BT\";\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.t_label = QtWidgets.QLabel(self.groupBox_3)
        self.t_label.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(16)
        self.t_label.setFont(font)
        self.t_label.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 46);\n"
"}")
        self.t_label.setLocale(QtCore.QLocale(QtCore.QLocale.Embu, QtCore.QLocale.Kenya))
        self.t_label.setObjectName("t_label")
        self.input_timeEdit = QtWidgets.QTimeEdit(self.groupBox_3)
        self.input_timeEdit.setGeometry(QtCore.QRect(30, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.input_timeEdit.setFont(font)
        self.input_timeEdit.setStyleSheet("QTimeEdit{\n"
"    color: rgb(0, 170, 0);\n"
"}")
        self.input_timeEdit.setWrapping(False)
        self.input_timeEdit.setFrame(False)
        self.input_timeEdit.setCalendarPopup(False)
        self.input_timeEdit.setObjectName("input_timeEdit")
        self.line_5 = QtWidgets.QFrame(self.groupBox_3)
        self.line_5.setGeometry(QtCore.QRect(210, 100, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(10, 100, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.now_pushButton = QtWidgets.QPushButton(self.groupBox_3, clicked=lambda: self.today())
        self.now_pushButton.setGeometry(QtCore.QRect(60, 120, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(12)
        self.now_pushButton.setFont(font)
        self.now_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.now_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 116, 63);\n"
"    border-radius:15px;\n"
"}")
        self.now_pushButton.setObjectName("now_pushButton")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(355, 140, 21, 181))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.out_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.out_listWidget.setGeometry(QtCore.QRect(360, 330, 361, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.out_listWidget.setFont(font)
        self.out_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.out_listWidget.setStyleSheet("QListWidget{\n"
"    color: rgb(104, 74, 255);\n"
"    background-color: rgb(255, 211, 225);\n"
"}")
        self.out_listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.out_listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.out_listWidget.setObjectName("out_listWidget")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)
        self.actionTo_Do_List_Persian_Calendar = QtWidgets.QAction(SecondWindow)
        self.actionTo_Do_List_Persian_Calendar.setObjectName("actionTo_Do_List_Persian_Calendar")
        self.menuAbout.addAction(self.actionTo_Do_List_Persian_Calendar)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.input_calendarWidget.selectionChanged.connect(self.calendarDataChanged)

        #Add Scroll To listWidget
        self.out_listWidget.setDragDropMode(3)
        self.out_listWidget.setAutoScroll(True)
        self.out_listWidget.setWordWrap(True)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        #Grab all the items from database
        self.grab_all()
    #Grab the items from database
    def grab_all(self):
        #Create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        #Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")

        
        records = c.fetchall()
        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()

        #Loop thru records and add to screen
        for record in records:
            self.out_listWidget.addItem(str(record))

    def calendarDataChanged(self):
        dataSelected = self.input_calendarWidget.selectedDate().toPyDate()

    #Show Now Date and Time
    def today(self):
        today_day = JalaliDate.today().strftime("%d")
        self.day_label.setText(today_day)
        today_month = JalaliDate.today().strftime("%B")
        self.month_label.setText(today_month)
        today_year = JalaliDate.today().strftime("%Y")
        self.year_label.setText(today_year)
        today_day_name = JalaliDate.today().strftime("%A")
        current_time = datetime.now().strftime("%H:%M:%S") 
        self.day_2_label.setText(f'{today_day_name}  -  {current_time}')

    #Add Task To List
    def add_it(self):
        #Select Date
        dataSelected = self.input_calendarWidget.selectedDate().toPyDate()
        date_p = JalaliDate(dataSelected)
        #Select Time
        timeedit = self.input_timeEdit.time().toPyTime()
        #Grab Task From ListBox
        task = self.input_lineEdit.text()
        #Add Task to list with date & time
        self.out_listWidget.addItem(f'{task}           {date_p}           {timeedit}')
        #Clear the task box
        self.input_lineEdit.setText("")

    #Delete Task From List
    def delete_it(self):
        #Grab the selected row or current row
        clicked = self.out_listWidget.currentRow()
        #Delete selected row
        self.out_listWidget.takeItem(clicked)

    #Clear All Task From List
    def clear_it(self):
        self.out_listWidget.clear()

    #Save To The Database
    def save_it(self):
        #Create a database or connect to one
        conn = sqlite3.connect('mylist.db')
        #Create a cursor
        c = conn.cursor()

        #Delete everything in the database tabel
        c.execute('DELETE FROM todo_list;', )

        #Create Blank List To Hold Todo Tasks
        tasks = []
        #Loop through the listwidget and pull out each task
        for index in range(self.out_listWidget.count()):
            tasks.append(self.out_listWidget.item(index))
        
        for item in tasks:
            #print(item.text())
            #Add stuff to the tabel
            c.execute("INSERT INTO todo_list VALUES(:item)",
                {
                    'item': item.text(),
                }
                )

        #Commit the changes
        conn.commit()

        #Close our connection
        conn.close()

        #Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved Your Task!")
        msg.setText("Your Todo List Has Been Saved!")
        msg.setIcon(QMessageBox.Information)
        a = msg.exec_()

    #Exit From App
    def exit(self):
        #closing the window
        sys.exit(0)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "To-Do List"))
        self.groupBox.setTitle(_translate("SecondWindow", "Date"))
        self.groupBox_2.setTitle(_translate("SecondWindow", "To Do List"))
        self.input_lineEdit.setPlaceholderText(_translate("SecondWindow", "Enter a Task"))
        self.add_pushButton.setText(_translate("SecondWindow", "+"))
        self.delete_pushButton.setText(_translate("SecondWindow", "Delete Task"))
        self.clear_pushButton.setText(_translate("SecondWindow", "Clear List"))
        self.save_pushButton.setText(_translate("SecondWindow", "Save Tasks!"))
        self.exit_pushButton.setText(_translate("SecondWindow", "Exit"))
        self.groupBox_3.setTitle(_translate("SecondWindow", "Time"))
        self.t_label.setText(_translate("SecondWindow", "Time:"))
        self.now_pushButton.setText(_translate("SecondWindow", "Now!"))
        self.menuAbout.setTitle(_translate("SecondWindow", "About"))
        self.actionTo_Do_List_Persian_Calendar.setText(_translate("SecondWindow", "To Do List & Persian Calendar"))

#Initialize The App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
