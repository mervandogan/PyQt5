import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar=self.menuBar()

        dosya=menubar.addMenu("Dosya")
        düzenle=menubar.addMenu("Düzenle")

        dosya_ac=QAction("Dosya Aç",self)
        dosya_ac.setShortcut("ctrl+s")                   #kısayoldan açmak için

        dosya_kaydet=QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("ctrl+a")

        cikis=QAction("Çıkış",self)
        cikis.setShortcut("ctrl+q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)



        ara_ve_degistir=düzenle.addMenu("Ara Ve Değiştir")
        ara=QAction("Ara",self)
        degistir=QAction("Değiştir",self)
        temizle=QAction("Temizle",self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)
        düzenle.addAction(temizle)



        cikis.triggered.connect(self.cikis_yap)
        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menüler")

        self.show()

    def cikis_yap(self):
        qApp.quit()                   #sayfanın kapanmasını sağlar
    def response(self,action):

        if action.text()=="Dosya Aç":
            print("Dosya Aç'a Basıldı.")
        elif action.text()=="Dosya Kaydet":
            print("Dosya Kaydet'e Basıldı.")
        elif action.text()=="Çıkış":
            print("Çıkış'a Basıldı")



app=QApplication(sys.argv)
menu=Menu()
sys.exit(app.exec_())
