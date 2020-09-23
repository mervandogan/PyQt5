import sys
from PyQt5 import QtWidgets
def Pencere():
    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    pencere.setWindowTitle("PYQT DERS 1")
    pencere.show()

    sys.exit(app.exec_())
Pencere()