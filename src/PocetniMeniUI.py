from PyQt5 import QtCore, QtGui, QtWidgets


class Meni_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 649)
        Dialog.setFixedSize(930,649)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, 721))
        self.widget.setStyleSheet("background-color: rgb(44, 49, 61);\n"
        "color: red;\n"
        "font-family: \\\'Times New Roman\\\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 40px;\n"
        "border: 1px solid rgb(51, 122, 183);\n"
        "border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.naslov_tekst = QtWidgets.QLabel(self.widget)
        self.naslov_tekst.setGeometry(QtCore.QRect(0, 110, 931, 111))
        self.naslov_tekst.setAlignment(QtCore.Qt.AlignCenter)
        self.naslov_tekst.setObjectName("naslov_tekst")
        self.ucitaj_listu = QtWidgets.QPushButton(self.widget)
        self.ucitaj_listu.setGeometry(QtCore.QRect(320, 260, 301, 51))
        self.ucitaj_listu.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \\\'Times New Roman\\\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 20px;\n"
        "border-radius: 5px;")
        self.ucitaj_listu.setObjectName("ucitaj_listu")
        self.kreiraj_listu = QtWidgets.QPushButton(self.widget)
        self.kreiraj_listu.setGeometry(QtCore.QRect(320, 340, 301, 51))
        self.kreiraj_listu.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \\\'Times New Roman\\\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 20px;\n"
        "border-radius: 5px;")
        self.kreiraj_listu.setObjectName("kreiraj_listu")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "To/do lista meni"))
        self.naslov_tekst.setWhatsThis(_translate("Dialog", "Naziv aplikacije."))
        self.naslov_tekst.setText(_translate("Dialog", "To/do lista"))
        self.ucitaj_listu.setWhatsThis(_translate("Dialog", "Tipka koja otvara izbornik za otvaranje postojeće liste."))
        self.ucitaj_listu.setText(_translate("Dialog", "UČITAJ LISTU"))
        self.kreiraj_listu.setWhatsThis(_translate("Dialog", "Tipka koja otvara izbornik za kreiranje nove liste."))
        self.kreiraj_listu.setText(_translate("Dialog", "KREIRAJ NOVU LISTU"))
