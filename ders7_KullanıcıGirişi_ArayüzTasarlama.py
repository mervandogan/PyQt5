import sys
import _sqlite3
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.init_ui()
        self.baglanti_olustur()
    def baglanti_olustur(self):
        baglanti=_sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        baglanti.commit()





    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)  #aynı FACEBOOK'a girermiş gibi)parolayı saklıyoruz bu bölümde parola gizli oluyor.
        self.kayıt_ol=QtWidgets.QPushButton("KAYIT OL")
        self.giris=QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani=QtWidgets.QLabel("")
        self.yazı = QtWidgets.QLabel("KAYIT OL")
        self.kullanici_ismi = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_tekrar = QtWidgets.QLineEdit()
        self.sifre_tekrar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.islemi_tamamla = QtWidgets.QPushButton("İŞLEMİ TAMAMLA")
        self.yazı = QtWidgets.QLabel("")


        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.kayıt_ol)
        v_box.addWidget(self.giris)

        v_box.addWidget(self.kullanici_ismi)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.sifre_tekrar)
        v_box.addStretch()
        v_box.addWidget(self.islemi_tamamla)
        v_box.addWidget(self.yazı)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.kayıt_ol.clicked.connect(self.click)

        self.show()

    def login(self):
        adi=self.kullanici_adi.text()
        par=self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı=? and parola=?",(adi,par))
        data=self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Böyle Bir Kullanıcı Bulunmuyor\n Lütfen tekrar deneyin")
        else:
            self.yazi_alani.setText("HOŞGELDİNİZ "  + adi)

    def click(self):
        sender=self.sender()

        if sender.text()=="Kayıt Ol":

            V_box=QtWidgets.QVBoxLayout()

            V_box.addWidget(self.kullanici_ismi)
            V_box.addWidget(self.sifre)
            V_box.addWidget(self.sifre_tekrar)
            V_box.addStretch()
            V_box.addWidget(self.yazı)

            self.setLayout(V_box)
            self.show()








app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())