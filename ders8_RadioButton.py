import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QPushButton,QRadioButton

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        self.radio_yazisi=QLabel("Hangi Dili Daha Çok Seviyorsun?")

        self.java=QRadioButton("JAVA")
        self.python=QRadioButton("PYTHON")
        self.php=QRadioButton("PHP")
        self.yazi_alanı=QLabel("")
        self.buton=QPushButton("Gönder")


        v_box=QVBoxLayout()

        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alanı)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(lambda: self.click(self.python.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alanı))
        self.setWindowTitle("Radio Buton")
        self.show()
    def click(self,python,java,php,yazi_alani):
        if python:
            yazi_alani.setText("PYTHON")
        if php:
            yazi_alani.setText("php")
        if java:
            yazi_alani.setText("java")











app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())