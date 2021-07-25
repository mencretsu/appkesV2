import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image, ImageCms

import sqlite3
con = sqlite3.connect('kalkulasi.db')
cur = con.cursor()
defaultImage="icon.png"
from main import Main 
class Kalkulasi(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("KALKULASI")
        self.setGeometry(350,85,850,700)
        self.ui()
        self.show()
    def ui(self):
        self.mdesign()
        self.layouts()
    def closeEvent(self, event):
        self.mainwin=Main()
    def layouts(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.bottomlayout=QHBoxLayout()
        self.rightlayout=QFormLayout()
        self.leftlayout=QVBoxLayout()
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addStretch()
        self.mlayout.addLayout(self.bottomlayout)
        self.bottomlayout.addLayout(self.leftlayout,25)
        self.bottomlayout.addLayout(self.rightlayout,70)
        self.mlayout.addStretch()
        self.mlayout.addWidget(self.btnback)

        self.toplayout.addWidget(self.title)
        self.toplayout.setAlignment(Qt.AlignHCenter)
        self.leftlayout.addWidget(self.listtampil)
        self.leftlayout.addWidget(self.qmbbox)
        self.rightlayout.addRow(self.lblnama, self.nameentry)
        self.rightlayout.addRow(self.lblnamabelakang, self.lblnamabelakangentry)
        self.rightlayout.addWidget(self.label)
        self.rightlayout.addRow(self.tb,self.slid)
        self.rightlayout.addWidget(self.label2)
        self.rightlayout.addRow(self.bb, self.slid2)
        self.rightlayout.addRow(self.foto, self.fotoentry)
        self.rightlayout.addWidget(self.btneks)
        
        self.rightlayout.setSpacing(10)
        self.setLayout(self.mlayout)
    def mdesign(self):
        borderstyle=("border-style:outset; border-width: 1.2px;border-radius: 10px;border-color: green;padding: 4px;")
        self.title=QLabel("kalkulasi")
        self.title.setStyleSheet('color: green;font-size: 18pt;font-family:Lucida Sans')
        self.setStyleSheet("font-size:11pt; font-family:Lucida Sans; font-style:Bold; color:green;")
        self.lblnama=QLabel("Nama depan")
        self.nameentry=QLineEdit()
        self.lblnamabelakang=QLabel("Nama belakang")
        self.lblnamabelakangentry=QLineEdit() 
        self.tb=QLabel("Tinggi badan")
        self.bb=QLabel("Berat badan")
        self.foto=QLabel("Tambah foto")
        self.fotoentry=QPushButton("browse")
        self.fotoentry.setStyleSheet(borderstyle)
        self.fotoentry.clicked.connect(self.tambahfoto)
        self.fotoentrylbl=QLabel()
        #TINGGI BADAN
        self.slid=QSlider(self)
        self.slid.setOrientation(Qt.Horizontal)
        self.slid.setRange(1,200)
        self.slid.valueChanged.connect(self.labelslid)
        #BERAT BADAN
        self.slid2=QSlider(self)
        self.slid2.setOrientation(Qt.Horizontal)
        self.slid2.setRange(1,200)
        self.slid2.valueChanged.connect(self.labelslid2)

        self.label=QLabel()
        self.label2=QLabel()

        self.qmbbox=QComboBox()
        self.qmbbox.addItems(["Info detail skor","18.4 <= berat badan kurang","24.9 <= ideal","29.9 <= kelebihan berat badan","34.9 <= obesitas","39,9 <= hyper obesitas"])
        
        self.btneks=QPushButton("simpan")
        self.btneks.setStyleSheet(borderstyle)

        self.btneks.clicked.connect(self.hasil)
        self.btnback=QPushButton("kembali")
        self.btnback.setStyleSheet(borderstyle)
        self.btnback.clicked.connect(self.close)

        self.listtampil=QListWidget()
        self.listtampil.setStyleSheet(borderstyle)

    def labelslid(self):
        self.a = str(self.slid.value())
        self.label.setText(self.a)
    def labelslid2(self):
        self.b = str(self.slid2.value())
        self.label2.setText(self.b)
    def hasil(self):
        global defaultImage
        self.listtampil.clear()
        self.listtampil.setWordWrap(True)
        #global defaultImage # how to cara nampilin foto langsung dari hasil eksekusi tanpa database?
        img =QLabel()
        img.setPixmap(QPixmap("images/icon.png"))
        img.setAlignment(Qt.AlignCenter)

        itemsu=QListWidgetItem()
        size = QSize(90,90)
        itemsu.setSizeHint(size)

        a = self.nameentry.text()
        b = self.lblnamabelakangentry.text()
        z = self.label2.text()
        w = self.label.text()

        if (z and w!=""):
            try:
                self.listtampil.addItem(itemsu)
                self.listtampil.setItemWidget(itemsu, img)
                self.listtampil.addItem(itemsu)
                self.listtampil.addItem("Nama depan      : "+a)
                self.listtampil.addItem("Nama belakang  : "+b)
                self.z = int(self.label2.text())
                self.w = int(self.label.text())
                self.oke =self.z/((self.w/100)**2)
                self.output="Skor anda : "+str(self.oke)+"\n\n"+"Keterangan : "
                if self.oke <= 18.4:
                    self.listtampil.addItem(self.output+"anda gizi buruk")
                elif self.oke <= 24.9:
                    self.listtampil.addItem(self.output+ "anda mantap manusia idaman ukhty")
                elif self.oke <= 29.9:
                    self.listtampil.addItem(self.output + "anda kurang diet")
                elif self.oke <= 34.9:
                    self.listtampil.addItem(self.output+"anda gk pernah diet")
                elif self.oke <=39.9:
                    self.listtampil.addItem(self.output + "anda makan 3 mie instan setiap 1 jam")
                else:
                    self.listtampil.addItem(self.output+ "anda tidak pernah berhenti makan 1 detik pun")
            except:
                QMessageBox.information(self, "Perhatian","Data tidak dapat tersimpan")
        else:
            QMessageBox.warning(self, "Perhatian!","Isi data dengan benar")
    def tambahfoto(self):
        global defaultImage
        self.size=(90,90)
        self.fileName,ok = QFileDialog.getOpenFileName(self, "Upload Image", '','Image Files (*.jpg *.png')
        if ok:
            defaultImage=os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img=img.resize(self.size)
            img.save("images/{}".format(defaultImage))

def main():
    app=QApplication(sys.argv)
    window = Kalkulasi()
    sys.exit(app.exec_())
    from main import Main
    Main.show()
    
if __name__ == '__main__':
    main()