from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(928, 717)
        Dialog.setFixedSize(928,717)
        self.pozadina = QtWidgets.QWidget(Dialog)
        self.pozadina.setGeometry(QtCore.QRect(0, 0, 931, 721))
        self.pozadina.setStyleSheet("background-color:rgb(27, 29, 35);")
        self.pozadina.setObjectName("pozadina")
        self.danas_label = QtWidgets.QLabel(self.pozadina)
        self.danas_label.setGeometry(QtCore.QRect(10, 20, 331, 41))
        self.danas_label.setStyleSheet("background-color: rgb(44, 49, 61);\n"
        "color: red;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 40px;\n"
        "border: 1px solid rgb(51, 122, 183);\n"
        "border-radius: 5px;")
        self.danas_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.danas_label.setTextFormat(QtCore.Qt.AutoText)
        self.danas_label.setScaledContents(False)
        self.danas_label.setAlignment(QtCore.Qt.AlignCenter)
        self.danas_label.setObjectName("danas_label")
        self.danas_lista = QtWidgets.QListWidget(self.pozadina)
        self.danas_lista.setGeometry(QtCore.QRect(10, 70, 331, 281))
        self.danas_lista.setStyleSheet("background-color: rgb(44, 49, 61);\n"
        "color: white;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-size: 20px;\n"
        "border: 1px solid rgb(130, 135, 144);\n"
        "border-radius: 5px;")
        self.danas_lista.setObjectName("danas_lista")
        item = QtWidgets.QListWidgetItem()
        self.danas_lista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.danas_lista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.danas_lista.addItem(item)
        self.danas_upis = QtWidgets.QPlainTextEdit(self.pozadina)
        self.danas_upis.setGeometry(QtCore.QRect(10, 360, 331, 51))
        self.danas_upis.setStyleSheet("background-color: rgb(26, 29, 37);\n"
        "color: white;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 12px;\n"
        "border: 1px solid rgb(78, 165, 255);\n"
        "border-radius: 5px;\n"
        "")
        self.danas_upis.setObjectName("danas_upis")
        self.danas_obrisi = QtWidgets.QPushButton(self.pozadina)
        self.danas_obrisi.setGeometry(QtCore.QRect(180, 420, 161, 31))
        self.danas_obrisi.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.danas_obrisi.setObjectName("danas_obrisi")
        self.danas_dodaj = QtWidgets.QPushButton(self.pozadina)
        self.danas_dodaj.setGeometry(QtCore.QRect(10, 420, 161, 31))
        self.danas_dodaj.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.danas_dodaj.setObjectName("danas_dodaj")
        self.danas_dovrseno = QtWidgets.QPushButton(self.pozadina)
        self.danas_dovrseno.setGeometry(QtCore.QRect(90, 470, 161, 31))
        self.danas_dovrseno.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.danas_dovrseno.setObjectName("danas_dovrseno")
        self.kalendar = QtWidgets.QCalendarWidget(self.pozadina)
        self.kalendar.setGeometry(QtCore.QRect(530, 20, 371, 211))
        self.kalendar.setStyleSheet("background-color:rgb(44, 49, 61);\n"
        "alternate-background-color: rgb(44, 49, 61);\n"
        "color:white;\n"
        "border-bottom: 1px solid rgb(78, 165, 255);\n"
        "font-weight: bold;")
        self.kalendar.setObjectName("kalendar")
        self.datum_lista = QtWidgets.QListWidget(self.pozadina)
        self.datum_lista.setGeometry(QtCore.QRect(530, 280, 371, 211))
        self.datum_lista.setStyleSheet("background-color: rgb(44, 49, 61);\n"
        "color: white;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-size: 20px;\n"
        "border: 1px solid rgb(130, 135, 144);\n"
        "border-radius: 5px;")
        self.datum_lista.setObjectName("datum_lista")
        item = QtWidgets.QListWidgetItem()
        self.datum_lista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.datum_lista.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.datum_lista.addItem(item)
        self.datum_label = QtWidgets.QLabel(self.pozadina)
        self.datum_label.setGeometry(QtCore.QRect(530, 240, 371, 31))
        self.datum_label.setStyleSheet("background-color: rgb(44, 49, 61);\n"
        "color: red;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 30px;\n"
        "border: 1px solid rgb(51, 122, 183);\n"
        "border-radius: 5px;")
        self.datum_label.setTextFormat(QtCore.Qt.AutoText)
        self.datum_label.setScaledContents(False)
        self.datum_label.setAlignment(QtCore.Qt.AlignCenter)
        self.datum_label.setObjectName("datum_label")
        self.datum_dodaj = QtWidgets.QPushButton(self.pozadina)
        self.datum_dodaj.setGeometry(QtCore.QRect(550, 560, 161, 31))
        self.datum_dodaj.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.datum_dodaj.setObjectName("datum_dodaj")
        self.datum_obrisi = QtWidgets.QPushButton(self.pozadina)
        self.datum_obrisi.setGeometry(QtCore.QRect(720, 560, 161, 31))
        self.datum_obrisi.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.datum_obrisi.setObjectName("datum_obrisi")
        self.datum_dovrseno = QtWidgets.QPushButton(self.pozadina)
        self.datum_dovrseno.setGeometry(QtCore.QRect(630, 610, 161, 31))
        self.datum_dovrseno.setStyleSheet("background-color: rgb(78, 165, 255);\n"
        "color: black;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "border-radius: 5px;")
        self.datum_dovrseno.setObjectName("datum_dovrseno")
        self.datum_upis = QtWidgets.QPlainTextEdit(self.pozadina)
        self.datum_upis.setGeometry(QtCore.QRect(530, 500, 371, 51))
        self.datum_upis.setStyleSheet("background-color: rgb(26, 29, 37);\n"
        "color: white;\n"
        "font-family: \'Times New Roman\', serif;\n"
        "font-weight: bold;\n"
        "font-size: 12px;\n"
        "border: 1px solid rgb(78, 165, 255);\n"
        "border-radius: 5px;\n"
        "")
        self.datum_upis.setObjectName("datum_upis")
        self.widget = QtWidgets.QWidget(self.pozadina)
        self.widget.setGeometry(QtCore.QRect(570, 80, 1, 144))
        self.widget.setMaximumSize(QtCore.QSize(1, 200))
        self.widget.setStyleSheet("background-color: rgb(78, 164, 254);")
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "To-do lista"))
        self.danas_label.setText(_translate("Dialog", "DANAS"))
        self.danas_lista.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Lista stvari koje namjeravate obaviti danas.</p></body></html>"))
        __sortingEnabled = self.danas_lista.isSortingEnabled()
        self.danas_lista.setSortingEnabled(False)
        item = self.danas_lista.item(0)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        item = self.danas_lista.item(1)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        item = self.danas_lista.item(2)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        self.danas_lista.setSortingEnabled(__sortingEnabled)
        self.danas_upis.setWhatsThis(_translate("Dialog", "Prostor za upisati što želite dodati na listu."))
        self.danas_upis.setPlainText(_translate("Dialog", "Upišite što želite dodati na današnju listu.\n"
    ""))
        self.danas_obrisi.setWhatsThis(_translate("Dialog", "Tipka za obrisati stvar sa današnje liste."))
        self.danas_obrisi.setText(_translate("Dialog", "OBRIŠI"))
        self.danas_dodaj.setWhatsThis(_translate("Dialog", "Tipka za dodati stvar na današnju listu."))
        self.danas_dodaj.setText(_translate("Dialog", "DODAJ"))
        self.danas_dovrseno.setWhatsThis(_translate("Dialog", "Tipka za označiti stvar na današnjoj listi kao obavljenu."))
        self.danas_dovrseno.setText(_translate("Dialog", "OZNAČI KAO DOVRŠENO"))
        self.kalendar.setWhatsThis(_translate("Dialog", "Kalendar na kojem možete izabrati datum za koji želite uređivati listu."))
        self.datum_lista.setWhatsThis(_translate("Dialog", "Lista stvari koje namjeravate obaviti na odabrani datum."))
        __sortingEnabled = self.datum_lista.isSortingEnabled()
        self.datum_lista.setSortingEnabled(False)
        item = self.datum_lista.item(0)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        item = self.datum_lista.item(1)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        item = self.datum_lista.item(2)
        item.setText(_translate("Dialog", "Pogreška u učitavanju programa, pokrenite ponovno!"))
        self.datum_lista.setSortingEnabled(__sortingEnabled)
        self.datum_label.setWhatsThis(_translate("Dialog", "Izabrani datum."))
        self.datum_label.setText(_translate("Dialog", "21.10.2021."))
        self.datum_dodaj.setWhatsThis(_translate("Dialog", "Tipka za dodati stvar na listu za odabrani datum."))
        self.datum_dodaj.setText(_translate("Dialog", "DODAJ"))
        self.datum_obrisi.setWhatsThis(_translate("Dialog", "Tipka za obrisati stvar sa liste za odabrani datum."))
        self.datum_obrisi.setText(_translate("Dialog", "OBRIŠI"))
        self.datum_dovrseno.setWhatsThis(_translate("Dialog", "Tipka za označiti stvar na listi za odabrani datum kao obavljenu."))
        self.datum_dovrseno.setText(_translate("Dialog", "OZNAČI KAO DOVRŠENO"))
        self.datum_upis.setWhatsThis(_translate("Dialog", "Tipka za dodati stvar na današnju listu.\n"
    ""))
        self.datum_upis.setPlainText(_translate("Dialog", "Upišite što želite dodati na listu.\n"
    ""))

