from typing import Text
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtCore import center, right
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PIL import Image
import sys, os

import sqlite3
con = sqlite3.connect('skuyisi.db')
cur = con.cursor()

defaultImage = "icon8.png" 
from main import Main 
class addEmployee(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("add skuyisi")
        self.setGeometry(350,85,850,700)
        self.setStyleSheet('font-size: 16pt;font-family:Lucida Sans')
        self.ui()
        self.show()
    def ui(self):
        self.mdesign()
        self.layouts()
    def closeEvent(self, event):
        self.mainwin=Main()
    def layouts(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QHBoxLayout()
        self.bottomlayout=QFormLayout()
        self.hbox=QHBoxLayout()
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addLayout(self.bottomlayout)
        #  aDD WIDGET TO LaYOUT
        self.toplayout.addStretch()
        self.toplayout.addWidget(self.imgadd)
        self.toplayout.addWidget(self.title)
        self.toplayout.addStretch()
        self.toplayout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        # aDDING WIDGET TO BOTTOM LaYOUT########################################
        self.bottomlayout.addRow(self.namelbl, self.nameentry)
        self.bottomlayout.addRow(self.jenislbl, self.jenisBox)
        self.bottomlayout.addRow(self.hbox)
        self.hbox.addWidget(self.ukuranlbl)
        self.hbox.addWidget(QLabel("        "))
        self.hbox.addWidget(self.ukuranentry)
        self.hbox.addWidget(self.gram)
        self.hbox.addWidget(self.kg)
        self.hbox.addStretch()
        self.bottomlayout.addRow(self.jumlahLbl, self.jumlahentry)
        self.bottomlayout.addRow(self.imglbl, self.imgbutton)
        self.bottomlayout.addRow(self.infolbl, self.infoeditor)
        self.bottomlayout.addRow(self.backbtn,self.addbtn)

        self.setLayout(self.mlayout)
    def mdesign(self):
       #TITLE
        self.imgadd=QLabel()
        self.imgadd.setPixmap(QPixmap("images/addicon.png"))
        self.title=QLabel("Tambah Menu Baru")
        self.title.setStyleSheet('color: green;font-size: 18pt;font-family:Lucida Sans')
        # BOTTOM LaYOUT WIDGET#######################################################################
        self.setStyleSheet("font-size:11pt; font-family:Lucida Sans; font-style:Bold; color:green;")
        self.namelbl=QLabel("Nama")
        self.jenislbl=QLabel("Jenis")
        self.ukuranlbl=QLabel("Ukuran")
        self.jumlahLbl=QLabel("Jumlah")
        self.imglbl=QLabel("Tambah Foto")
        self.infolbl=QLabel("Keterangan")
        ####
        self.nameentry=QLineEdit()
        self.nameentry.setPlaceholderText("Masukkan nama makanan")
        self.jenisBox=QComboBox()
        self.jenisBox.addItems(["Makanan","Minuman","Camilan","Buah","Junk Food","Gk ngerti"])
        self.ukuranentry=QSpinBox()
        self.ukuranentry.setRange(1,1000)
        self.ukuranentry.setSpecialValueText(" Pilih Ukuran ")
        self.ukuranentry.setAccelerated(True)
        self.ukuranentry.valueChanged.connect(self.val)
        self.gram=QRadioButton("Gram")
        self.kg=QRadioButton("Kilogram")
        self.gram.setChecked(True)
        self.labelberat=QLabel()

        self.jumlahentry=QLineEdit()
        self.jumlahentry.setPlaceholderText("masukkan jumlah(satuan)")
        self.imgbutton=QLabel()
        self.infoeditor=QTextEdit()
        self.infoeditor.setPlaceholderText("Masukkkan informasi")
        
        self.imgbutton=QPushButton("Browse")
        self.imgbutton.clicked.connect(self.uploadImage)
        self.addbtn=QPushButton("Add")
        self.addbtn.clicked.connect(self.addEmployee)
        self.addbtn.setStyleSheet('background:green;color:white;font:bold')
        self.backbtn=QPushButton("Back")
        self.backbtn.setStyleSheet('background:green;color:white;font:bold')
        self.backbtn.clicked.connect(self.close)
    def val(self):#RADIO BUTTON 
        self.a = str(self.ukuranentry.value())
        if self.gram.isChecked() ==True:
            self.labelberat.setText(self.a+" gram")
        else:
            self.labelberat.setText(self.a+" kilogram")
    def uploadImage(self):
        global defaultImage
        self.size=(90,90)
        self.fileName,ok = QFileDialog.getOpenFileName(self, "Upload Image", '','Image Files (*.jpg *.png')
        if ok:
            defaultImage=os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img=img.resize(self.size)
            img.save("images/{}".format(defaultImage))
    def addEmployee(self):
        global defaultImage
        name = self.nameentry.text()
        jeniss = self.jenisBox.currentText()
        ukuran = self.labelberat.text()
        jumlah = self.jumlahentry.text()
        img = defaultImage
        infoo = self.infoeditor.toPlainText()
        def kosong():
            name=self.nameentry.setText("")
            jeniss= self.jenisBox.currentText()
            ukuran = self.ukuranentry.value()
            jumlah =self.jumlahentry.setText("")
            infoo = self.infoeditor.setText("")

        if (name!=""):
            try:
                query="INSERT INTO skuyisi (nama, jenis, ukuran, warna, img, jumlah) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (name, jeniss, ukuran, jumlah, img, infoo))
                con.commit()
                QMessageBox.information(self, "SUKSES","Data Berhasil Tersimpan ^^")
                kosong()
                self.close()
            except:
                    QMessageBox.information(self, "Perhatian","Data Tidak Dapat Tersimpan")
        else:
            QMessageBox.warning(self, "Perhatian!","Data Harus Terisi")
                

def main():
    app=QApplication(sys.argv)
    window = addEmployee()
    sys.exit(app.exec_())
    from main import Main
    Main.show()
    
if __name__ == '__main__':
    main()