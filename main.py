import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMainWindow,QMessageBox
import sqlite3
from PyQt5 import (QtWidgets, uic, QtCore, QtGui)
import victoria
class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        uic.loadUi("main.ui",self)
        self.setWindowTitle("Victoria")
        self.listen.clicked.connect(self.list)
        self.Exit.clicked.connect(self.exit)
    def list(self):
        victoria.main()
    def exit(self):
        exit()



class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.setWindowTitle("Victoria - Login")
        self.login.clicked.connect(self.loginCheck)
        self.sign.clicked.connect(self.signCheck)
        self.label_3.show()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def signCheck(self):
        sign = Sign()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(sign)
        widget.setFixedHeight(254)
        widget.setFixedWidth(484)
        widget.setWindowTitle("Victoria - Sign")
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginCheck(self):
        username = self.username.text()
        password = self.password.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME= ? AND PASSWORD = ?",(username,password))
        if (len(result.fetchall())>0):
            mai1n = main()
            widget.addWidget(mai1n)
            widget.setFixedHeight(154)
            widget.setFixedWidth(436)
            widget.setWindowTitle("Victoria")
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        else:
            self.showMessageBox("Warning","Invalid Username or Password")
    def showMessageBox(self,title,message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
    
class Sign(QDialog):
    def __init__(self):
        super(Sign,self).__init__()
        loadUi("sign.ui",self)
        self.setWindowTitle("Victoria - Sign")
        self.pushButton.clicked.connect(self.insertData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def insertData(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
        connection.commit()
        connection.close()
        log = Login()
        widget.addWidget(log)
        widget.setCurrentIndex(widget.currentIndex()+1)



app = QApplication(sys.argv)
login = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login)
widget.setWindowTitle("Victoria - Login")
widget.setFixedHeight(375)
widget.setFixedWidth(348)
widget.show()
app.exec()