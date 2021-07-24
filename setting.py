import sys, os
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
import sqlite3
con = sqlite3.connect('profil.db')
cur = con.cursor()
img="images/icon.png"

from main import Main

class Setng(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("pengaturan")
        self.setGeometry(350,85,600,700)
        self.setStyleSheet("font-family:Lucida Sans;font-style:Bold;font-size:10pt")
        self.ui()        
        self.show()
    def ui(self):
        self.mdesign()
        self.layouts()
    def mdesign(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.bottomlayout=QVBoxLayout()
        self.mlayout.addLayout(self.toplayout,30)
        self.mlayout.addLayout(self.bottomlayout,90)
        self.toplayout.setAlignment(Qt.AlignCenter)
        #create widget
        self.label=QLabel()
        self.lalbelgif=QMovie("gif/pp.gif")
        self.label.setMovie(self.lalbelgif)
        self.lalbelgif.start()

        self.btnlogin=QPushButton("Login?")
        self.btnlogout=QPushButton("Logout?")

        self.userid=QLabel("user : ")
        query = "SELECT username FROM profil"
        profil = cur.execute(query).fetchall()
        for profil in profil:
            self.userid.setText(str(profil[0]))
            self.btnlogin.hide()
            self.btnlogout.show()

        self.btnoke=QPushButton("Oke")
        self.btnoke.hide()
        self.backbtn=QPushButton("Kembali")
        self.tentang=QPushButton("Tentang aplikasi ini")
        self.list=QListWidget()
        text=open('tentang.txt').read()
        self.list.addItem(text)
        self.list.addItem("")
        self.list.hide()
    def layouts(self):
        #add widget to layout
        self.toplayout.addWidget(self.label)
        self.toplayout.addWidget(self.userid)
        self.toplayout.addWidget(self.btnlogin)
        self.toplayout.addWidget(self.btnlogout)
        self.bottomlayout.addWidget(self.list)
        self.bottomlayout.addWidget(self.backbtn)
        self.bottomlayout.addWidget(self.tentang)
        self.bottomlayout.addWidget(self.btnoke)
        self.btnlogin.clicked.connect(self.login)
        self.btnlogout.clicked.connect(self.logout)
        self.tentang.clicked.connect(self.tampil)
        self.btnoke.clicked.connect(self.lanjut)
        self.backbtn.clicked.connect(self.kembali)

        self.setLayout(self.mlayout)
    def login(self):
        from sign import Login
        self.ok=Login()
        self.close()
    def logout(self):
        self.userid.setText("")
        QMessageBox.information(self,"Siap", "Anda Telah logout")
        self.btnlogout.hide()
        self.btnlogin.show()
    def kembali(self):
        from main import Main
        self.gas= Main()
        self.gas.show()
        self.close()
    def tampil(self):
        self.list.show()
        self.tentang.hide()
        self.btnoke.show()
        self.backbtn.hide()
    def lanjut(self):
        self.list.hide()
        self.tentang.show()
        self.btnoke.hide()
        self.backbtn.show()
def main():
    app = QApplication(sys.argv)
    w = Setng()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()