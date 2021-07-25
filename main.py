import sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image, ImageCms

import sqlite3
con = sqlite3.connect('skuyisi.db')
cur = con.cursor()
#pm = sqlite3.connect('profil.db')

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my project")
        self.setGeometry(350,85,850,700)
        self.setMaximumSize(850,700)
        self.otw()
        self.ui()
        self.show()
    def otw(self):
        pass
        
    def ui(self):
        self.mdesign()
        self.layouts()
        self.getskuyisi()
       # self.displayfirst()
    def mdesign(self):
        oImage = QImage("images/bgg.jpg")                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        borderstyle=("border-style:outset; border-width: 1.2px;border-radius: 10px;border-color: green;padding: 4px;")
        self.setPalette(palette)
        self.setStyleSheet("font-size:11pt; font-family:Lucida Sans; font-style:Bold; color:green;")
        self.title=QLabel("HOME")
        self.icon=QLabel()
        self.icon.setPixmap(QPixmap("images/homeicon.png"))
        self.employelist=QListWidget()
        self.listtampil=QListWidget()
        self.employelist.setStyleSheet(borderstyle)
        self.listtampil.setStyleSheet(borderstyle)
        self.listtampil.setWordWrap(True)
        self.employelist.itemClicked.connect(self.singleclick)
        self.cek=QCheckBox("pilih semua")
        self.btn = QPushButton("Menu Kalkulasi")
        self.btn.setStyleSheet(borderstyle)
        self.btnnew=QPushButton("NEW")
        self.btnupdate=QPushButton("UPDATE")
        self.btndel=QPushButton("DELETE")
        self.btndel.setStyleSheet(borderstyle)
        self.btnnew.setStyleSheet(borderstyle)
        self.btnupdate.setStyleSheet(borderstyle)
        self.btnset=QPushButton("HOME")
        self.btnset.setStyleSheet(borderstyle)
        self.btnset.setIcon(QIcon("images/homeicon.png"))
        self.btnset.clicked.connect(self.set)
        self.btnnew.clicked.connect(self.addEmployee)
        self.btndel.clicked.connect(self.delemployee)
        self.btnupdate.clicked.connect(self.updateemployee)
        self.btn.clicked.connect(self.kalkulasi) 
    def layouts(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QHBoxLayout()
        self.bottomlayout=QVBoxLayout()###
        self.midlayot=QFormLayout()
        self.bottomlayout1=QVBoxLayout()
        self.bottomlayout2=QHBoxLayout()
        self.bottomlayout3=QHBoxLayout()
        self.mplayout=QFormLayout()
        #BaGI LAYOUT
        self.mlayout.addLayout(self.toplayout,20)
        #self.mlayout.addLayout(self.midlayot)
        self.mlayout.addLayout(self.bottomlayout,60)
#       main layout set
        self.bottomlayout.addLayout(self.bottomlayout1)
        self.bottomlayout.addLayout(self.bottomlayout2)
        self.bottomlayout.addLayout(self.bottomlayout3)
        #3######
        self.toplayout.addWidget(self.btnset)
        self.toplayout.addStretch()
        self.toplayout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.title.setStyleSheet('color: green;font-size:12pt;font-family:Lucida Sans')
        #bottom
        self.bottomlayout1.addWidget(self.btn)
        self.title2=QLabel("MENU")
        self.title2lbl=QLabel()
        self.title2lbl.setPixmap(QPixmap("images/menusy.png"))
        self.title2.setStyleSheet("font-size:18pt")
        self.bottomlayout1.addWidget(self.title2)
        self.bottomlayout1.addWidget(self.title2lbl)
        self.title2.setAlignment(Qt.AlignHCenter)
        self.title2lbl.setAlignment(Qt.AlignHCenter)
        self.bottomlayout2.addWidget(self.employelist,60)
        self.bottomlayout2.addWidget(self.listtampil, 40)
        self.bottomlayout3.addWidget(self.btnnew)
        self.bottomlayout3.addWidget(self.btnupdate)
        self.bottomlayout3.addWidget(self.btndel)
        self.setLayout(self.mlayout)
   
    def val(self):pass
    
    def singleclick(self):
        for i in reversed(range(self.midlayot.count())):
            widget = self.midlayot.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.employee = self.employelist.currentItem().text()
        self.id = self.employee.split(("-"))[0]
        self.query = "SELECT * FROM skuyisi WHERE id = ?"
        self.person = cur.execute(self.query, (self.id,)).fetchone()

        img =QLabel()
        img.setPixmap(QPixmap("images/"+self.person [5]))
        img.setAlignment(Qt.AlignCenter)
        name =   "Nama      :  "+self.person[1]
        jeniss=  "Jenis       :  "+ self.person[2]
        ukuran = "Ukuran   :  "+ self.person[3]
        jumlah = "Jumlah   :  "+self.person[4]
        infoo =  "keterangan :  "+self.person[6] 

        itemsu=QListWidgetItem()
        size = QSize(100,100)
        itemsu.setSizeHint(size)

        self.listtampil.clear()
        self.listtampil.addItem(itemsu)
        self.listtampil.setSpacing(5)
        self.listtampil.addItem(name)
        self.listtampil.addItem(jeniss)
        self.listtampil.addItem(ukuran)
        self.listtampil.addItem(jumlah)
        self.listtampil.addItem(infoo)
        self.listtampil.setItemWidget(itemsu, img)
        self.listtampil.addItem(itemsu)
        
    def delemployee(self):
        if self.employelist.selectedIndexes():
            mbox = QMessageBox.question(self, "WaRNING", "apa anda ingin menghapus data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM skuyisi WHERE id=?"
                    cur.execute(query, (self.id,))
                    con.commit() 
                    QMessageBox.information(self, "yeay","Data berhasil dihapus")
             
                    self.employelist.clear()
                    self.listtampil.clear()
                    self.getskuyisi()
                except:
                    QMessageBox.information(self,"warning","Data tidak dihapus")
        else:
            QMessageBox.information(self,"perhaatian","pilih dulu data yang akan dihapus")

    def addEmployee(self):
        from addNew import addEmployee
        self.newEmployee=addEmployee()
        self.close()
    def getAll(self):
        pass

    def getskuyisi(self):
        query = "SELECT id, nama, ukuran FROM skuyisi"
        skuyisi = cur.execute(query).fetchall()
        for skuyisi in skuyisi:
            self.employelist.addItem(str(skuyisi[0])+" - "+skuyisi[1]+" - "+skuyisi[2])
    def updateemployee(self):
        if self.employelist.selectedItems():
            person= self.employelist.currentItem().text()
            id_person = self.employee.split(("-"))[0]

            query=" SELECT * FROM skuyisi WHERE id =?"
            person=cur.execute(query, (id_person,)).fetchone()
            img="images/"+self.person[5]
            name=self.person[1]
            jeniss=self.person[2]
            ukuran=self.person[3]
            jumlah=self.person[4]
            infoo=self.person[6]

            from update import updates
            self.ubah=updates()

            self.ubah.imgadd.setPixmap(QPixmap(img))
            self.ubah.namaimg.setText(self.person[5])
            self.ubah.identry.setText(id_person)
            self.ubah.nameentry.setText(name)
            self.ubah.jenisBox.setCurrentText(jeniss)
            self.ubah.ukuranentry.setSpecialValueText(ukuran)
            self.ubah.jumlahentry.setText(jumlah)
            self.ubah.infoeditor.setText(infoo)
            self.close()
        else:
            QMessageBox.information(self, "perhatian","Pilih dulu data yang akan di update")

    def set(self):
        from setting import Setng
        self.oke=Setng()
        self.close()
    def kalkulasi(self):
        from kalkulasi import Kalkulasi
        self.gas=Kalkulasi()
        self.close()

def main():
    app=QApplication(sys.argv)
    window=Main()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()