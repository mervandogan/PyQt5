import sys
from PyQt5 import QtWidgets,QtGui
def Pencere():
    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 DERS 2")
    etiket1=QtWidgets.QLabel(pencere)
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket1.setText("Burası Bir yazıdır.")
    etiket2.move(30,70)
    etiket1.move(200,30)
    pencere.setGeometry(100,100,500,500)
    pencere.show()

    sys.exit(app.exec_())
Pencere()