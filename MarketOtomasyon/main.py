import sys
import PyQt5
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
from marketotomasyon import *
from PyQt5.QtWidgets  import QStatusBar
import main

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

import sqlite3

baglanti = sqlite3.connect("ürünler.db")
islem = baglanti.cursor()
baglanti.commit


table = islem.execute("create table if not exists ürün (urunAdi text,birimFiyat int, stokMiktari int, marka text, urunKodu int)")
baglanti.commit()

def kayit_listele():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Adı","Fiyat","Adet","Marka","Kod"))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    sorgu = "select * from ürün"
    islem.execute(sorgu)

    for indexSatir,kayitNumarasi in enumerate(islem):
        for indexSutun,kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

kayit_listele()

def kayit_ekle():
    UrunAdi = ui.lineEdit.text()
    BirimFiyat = int(ui.lineEdit_2.text())
    StokMiktari = int(ui.lineEdit_3.text())
    Marka = ui.lineEdit_4.text()
    UrunKodu = int(ui.lineEdit_5.text())

    try:
        ekle = "insert into ürün (urunAdi,birimFiyat,stokMiktari,marka,urunKodu) values (?,?,?,?,?)"
        islem.execute(ekle,(UrunAdi,BirimFiyat,StokMiktari,Marka,UrunKodu))
        baglanti.commit()
        kayit_listele()
        ui.statusBar.showMessage("Kayıt Ekleme başarılı",4000)
    except Exception as error:
        ui.statusBar.showMessage("Kayıt Eklenemedi === "+str(error))


def veri_sil():
    silmemesaji = QMessageBox.question(pencere,"Silme","Bu veriyi silmek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No)

    if silmemesaji == QMessageBox.Yes:
        secilen_veri = ui.tableWidget.selectedItems()
        silinecek_veri = secilen_veri[0].text()
        
        sorgu = "delete from ürün where UrunAdi = ?"
        try:
            islem.execute(sorgu,(silinecek_veri,))
            baglanti.commit()
            ui.statusBar.showMessage("veri silindi")
            kayit_listele()
        except Exception as error:
            ui.statusBar.showMessage("veri silinemedi = "+str(error))

    else:
        ui.statusBar.showMessage("silme iptal edildi")

def veri_guncelle():
    guncelle_mesaj = QMessageBox.question(pencere,"Güncelleme","Bu veriyi güncellemek istediğinize emin misiniz ?",QMessageBox.Yes | QMessageBox.No)

    if guncelle_mesaj == QMessageBox.Yes:
        try:
            UrunAdi = ui.lineEdit.text()
            BirimFiyat = ui.lineEdit_2.text()
            StokMiktari = ui.lineEdit_3.text()
            Marka = ui.lineEdit_4.text()
            UrunKodu = ui.lineEdit_5.text()

            islem.execute("update ürün set urunAdi = ?, birimFiyat = ? , stokMiktari = ?, Marka = ? where urunKodu = ?",(UrunAdi,BirimFiyat,StokMiktari,Marka,UrunKodu))
            baglanti.commit()
            kayit_listele()
            ui.statusBar.showMessage("Veri güncellendi")
        except Exception as error:
            ui.statusBar.showMessage("veri güncellenemdi === "+str(error))
    else:
        ui.statusBar.showMessage("Veri Güncelleme İptal Edildi")

#butonlar
ui.ekle.clicked.connect(kayit_ekle)
ui.listele.clicked.connect(kayit_listele)
ui.sil.clicked.connect(veri_sil)
ui.guncelle.clicked.connect(veri_guncelle)
ui.exitbtn.clicked.connect(pencere.close)

sys.exit(uygulama.exec_())