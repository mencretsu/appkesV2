import sys, os
from typing import Set
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
import sqlite3
con = sqlite3.connect('profil.db')
cur = con.cursor()

from setting import Setng
class req(QWidget):
    def __init__(self, parent=None):
        super(req, self).__init__(parent)
        self.setWindowTitle("REgisterSkuy")
        self.setGeometry(450,150,350,600)
        self.setStyleSheet('font-size: 10pt;font-family:Lucida Sans')
        self.title=QLabel("Create account")
        self.title.setStyleSheet('color: green; font-size: 18pt;font-family:Lucida Sans')
        self.UI()
        self.show()
    def UI(self):
        self.textName = QLineEdit()
        self.textPass = QLineEdit()
        self.textPass2 = QLineEdit()
        self.cek=QCheckBox("Tampil/sembunyikan password")
    
        self.buttonDaftar= QPushButton("Register")
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.bottomlayout=QFormLayout()
        self.bottomlayout3= QVBoxLayout()
        #####
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addLayout(self.bottomlayout)
        self.mlayout.addLayout(self.bottomlayout3)
        #  aDD WIDGET TO LaYOUT
        self.toplayout.addStretch()
        self.toplayout.addWidget(self.title)
        self.toplayout.addStretch()
        self.toplayout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.bottomlayout.addRow("Nama Pengguna",self.textName)
        self.bottomlayout.addRow("Buat Password",self.textPass)
        #self.bottomlayout.addRow("Ulangi Password",self.textPass2)
        self.bottomlayout.addWidget(self.cek)
        self.bottomlayout3.addStretch()
        self.bottomlayout.addWidget(self.buttonDaftar)
        self.buttonDaftar.clicked.connect(self.handlereg)

        self.setLayout(self.mlayout)
    def handlereg(self):
        nama = self.textName.text()
        passwd = self.textPass.text()
        def kosong():
            nama=self.textName.setText("")
            passwd = self.textPass.setText("")
        if (nama!=""):
            try:
                query="INSERT INTO profil (username, password) VALUES(?,?)"
                cur.execute(query, (nama, passwd))
                con.commit()
                QMessageBox.information(self, "SUKSES","telah berhasil mendaftar")
                kosong()
                self.close()
            except:
                    QMessageBox.information(self, "Perhatian","Gagal mendaftar")
        else:
            QMessageBox.warning(self, "Perhatian!","Data Harus Terisi")

class Login(QWidget):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("LoginSkuy")
        self.setGeometry(450,150,350,600)
        self.setStyleSheet('font-size: 10pt;font-family:Lucida Sans')
        self.ui()
        self.show()

    def ui(self):
        self.title=QLabel("Skuy Login")
        self.title2=QLabel("Klik register untuk membuat akun baru")
        self.title.setStyleSheet('color: green; font-size: 18pt;font-family:Lucida Sans')
        self.title2.setAlignment(Qt.AlignHCenter)
        self.textName1=QLabel("Id")
        self.textPass1=QLabel("Password")
        self.textName2 = QLineEdit()
        self.textPass2 = QLineEdit()
        self.cek=QCheckBox("Tampil/sembunyikan password")
        self.buttonLogin = QPushButton("Login")
        self.buttonDaftar= QPushButton("Register")
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.bottomlayout=QFormLayout()
        #####
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addLayout(self.bottomlayout)
        self.mlayout.addStretch()
        #  aDD WIDGET TO LaYOUT
        self.toplayout.addStretch()
        self.toplayout.addWidget(self.title)
        self.toplayout.addStretch()
        self.bottomlayout.addRow(self.textName1,self.textName2)
        self.bottomlayout.addRow(self.textPass1,self.textPass2)
        self.bottomlayout.addWidget(self.cek)
        self.bottomlayout.addRow(self.buttonLogin,self.buttonDaftar)
        self.toplayout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonDaftar.clicked.connect(self.daftar)

        self.setLayout(self.mlayout)
    def closeEvent(self, event):
        self.mainwin=Setng()
    def handleLogin(self):
        nama = self.textName2.text()
        passwd = self.textPass2.text()
        result = con.execute("SELECT * FROM profil WHERE username = ? AND password = ?", (nama, passwd))
        if result.fetchall():
            QMessageBox.information(self, "SUKSES","Berhasil Login")
            self.close()
        else:
            QMessageBox.warning(self, "Perhatian!","Data Harus Terisi")
    def daftar(self):
        self.r=req()
def main():
    app=QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec_())
    from setting import Setng
    Setng.show()
if __name__ == '__main__':
    main()