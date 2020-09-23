import sys
from PyQt5 import QtWidgets
def Pencere():
    app=QtWidgets.QApplication(sys.argv)

    okey=QtWidgets.QPushButton("tamam")
    cancel=QtWidgets.QPushButton("iptal")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okey)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 DERS 4")
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)

    pencere.show()
    sys.exit(app.exec_())

Pencere()