import sys
from PyQt5 import QtWidgets
def Pencere():
    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")
    buton=QtWidgets.QPushButton(pencere)
    buton.setText("BURASI BİR BUTONDUR.")
    etiket=QtWidgets.QLabel(pencere)
    etiket.setText("MERHABA MERVAN DOĞAN İLHANLI")
    etiket.move(200,30)
    buton.move(210,80)

    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()
