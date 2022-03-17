from asyncio.windows_events import NULL
from ListaDatumaClass import ListaDatuma
from SqlBazaClass import SqlBaza
from ToDoListUI import Ui_Dialog
from ZadatakClass import Zadatak
from ListaZadatakaClass import ListaZadataka
from PocetniMeniUI import Meni_Dialog

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import sys, os

class ToDoList(QtWidgets.QDialog):
    #Definiramo boje za stavke prikazane na listi zadataka
    BOJA_DOVRSENIH = "#754e4b" #6b5c5b
    BOJA_NEDOVRSENIH = "#ffffff"

    #Svojstva koja koristimo u klasi 
    datotekazaucitati = [""]
    datotekazakreirati = [""]
    izabrani_datum = None
    lista_datuma = None
    baza = None

    #Konstruktor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Pokretanje korisničkog sučelja
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Prikazuje početni meni za odabir otvaranja ili kreiranja liste
        self.PrikaziMeni()

        #Kreiramo evente za danas
        self.ui.danas_dodaj.clicked.connect(self.DodajZadatakDanas)
        self.ui.danas_upis.setPlainText("")

        self.ui.danas_obrisi.clicked.connect(self.ObrisiZadatakDanas)

        self.ui.danas_dovrseno.clicked.connect(self.DovrsiZadatakDanas)

        #Kreiramo evente za datum
        self.ui.kalendar.clicked.connect(self.PromjeniDatum)
        self.ui.datum_upis.setPlainText("")

        self.ui.datum_dodaj.clicked.connect(self.DodajZadatakDatum)

        self.ui.datum_obrisi.clicked.connect(self.ObrisiZadatakDatum)

        self.ui.datum_dovrseno.clicked.connect(self.DovrsiZadatakDatum)

    #Kalendar i izabrani datum postavlja na dan nakon danasnjeg
    def PocetniSetup(self):
        dat = QtCore.QDate.currentDate().addDays(1)
        self.izabrani_datum = "{0}/{1}/{2}".format(dat.day(), dat.month(), dat.year())
        self.ui.kalendar.setSelectedDate(dat)
        self.ui.datum_label.setText(self.izabrani_datum)

    #Poziva se kada se pritisne tipka dodaj i dodaje novi zadatak na današnju listu
    def DodajZadatakDanas(self):
        self.ProvjeriBazu()

        if(self.ui.danas_upis.toPlainText().strip() == ""):
            self.ui.danas_upis.setPlainText("")
            return

        try:
            zad = Zadatak(self.ui.danas_upis.toPlainText(), False)

            if(self.lista_datuma.PostojiDatum(self.VratiDanasnjiDan()) == False):
                self.lista_datuma.KreirajDatum(self.VratiDanasnjiDan())
                self.baza.BazaDodajDatum(self.VratiDanasnjiDan(),self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka())

            self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].DodajZadatak(zad)
            
            self.baza.BazaSacuvajDatum(self.VratiDanasnjiDan(),self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka())

            self.ui.danas_upis.setPlainText("")
            item = QtWidgets.QListWidgetItem(zad.VratiTekst())
            item.setForeground(QtGui.QColor(self.BOJA_NEDOVRSENIH)) 
            self.ui.danas_lista.addItem(item)
        except:
            return
    
    #Poziva se kada se pritisne tipka obriši i briše označenu stavku s liste
    def ObrisiZadatakDanas(self):
        self.ProvjeriBazu()

        try:
            izabrana_stavka = self.ui.danas_lista.currentRow()

            if(izabrana_stavka == -1):
                return
            
            self.ui.danas_lista.takeItem(izabrana_stavka)
            self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].ObrisiZadatak(izabrana_stavka)

            self.baza.BazaSacuvajDatum(self.VratiDanasnjiDan(),self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka())
        except:
            return
    
    #Poziva se kada korisnik izabere drugi datum
    def PromjeniDatum(self, datum):
        self.ProvjeriBazu()

        self.izabrani_datum = "{0}/{1}/{2}".format(datum.day(), datum.month(), datum.year())

        if(self.izabrani_datum == self.VratiDanasnjiDan()):
            dat = QtCore.QDate.currentDate().addDays(1)
            self.izabrani_datum = "{0}/{1}/{2}".format(dat.day(), dat.month(), dat.year())
            self.ui.kalendar.setSelectedDate(dat)
            self.ui.datum_label.setText(self.izabrani_datum)

        self.ui.datum_label.setText(self.izabrani_datum)
        self.ui.datum_lista.clear()

        self.UpdatePopis(self.izabrani_datum)

    #Poziva se kada se pritisne tipka dodaj i dodaje novi zadatak na današnju listu
    def DodajZadatakDatum(self):
        self.ProvjeriBazu()

        if(self.ui.datum_upis.toPlainText().strip() == ""):
            self.ui.datum_upis.setPlainText("")
            return

        try:
            zad = Zadatak(self.ui.datum_upis.toPlainText(), False)

            if(self.lista_datuma.PostojiDatum(self.izabrani_datum) == False):
                self.lista_datuma.KreirajDatum(self.izabrani_datum)
                self.baza.BazaDodajDatum(self.izabrani_datum,self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka())

            self.lista_datuma.VratiDict()[self.izabrani_datum].DodajZadatak(zad)
            self.baza.BazaSacuvajDatum(self.izabrani_datum,self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka())

            self.ui.datum_upis.setPlainText("")
            item = QtWidgets.QListWidgetItem(zad.VratiTekst())
            item.setForeground(QtGui.QColor(self.BOJA_NEDOVRSENIH)) 
            self.ui.datum_lista.addItem(item)
        except:
            return
    
    #Poziva se kada se pritisne tipka obriši i briše označenu stavku s liste
    def ObrisiZadatakDatum(self):
        self.ProvjeriBazu()

        try:
            izabrana_stavka = self.ui.datum_lista.currentRow()

            if(izabrana_stavka == -1):
                return
            
            self.ui.datum_lista.takeItem(izabrana_stavka)
            
            self.lista_datuma.VratiDict()[self.izabrani_datum].ObrisiZadatak(izabrana_stavka)
            self.baza.BazaSacuvajDatum(self.izabrani_datum,self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka())
        except:
            return

    #Prikazuje korisniku meni s opcijama za ucitavanje ili kreiranje liste
    def PrikaziMeni(self):
        self.datotekazaucitati = [""]
        self.datotekazakreirati = [""]

        self.dial = QtWidgets.QDialog(self)
        meni = Meni_Dialog()
        meni.setupUi(self.dial)

        meni.ucitaj_listu.clicked.connect(self.UcitajListuPath)
        meni.kreiraj_listu.clicked.connect(self.KreirajListuPath)

        self.dial.exec()

    #Nudi korisniku opciju za odabir datoteke koju zeli otvoriti (.db koja sadrzi listu)
    def UcitajListuPath(self):
        self.datotekazaucitati = QtWidgets.QFileDialog.getOpenFileName(self, "Izaberite vašu listu")
        
        if(self.datotekazaucitati[0] == ""):
            return

        path = os.path.splitext(str(self.datotekazaucitati))
        if(path[1][0:3].strip().lower() != ".db"):
            return

        self.dial.close()
        self.UcitajBazu()

    #Nudi korisniku opciju za odabir mjesta na kojem ce kreirati novu listu
    def KreirajListuPath(self):
        self.datotekazakreirati = QtWidgets.QFileDialog.getSaveFileName(self, "Izaberite", os.getcwd(), ".db")

        if(self.datotekazakreirati[0] == ""):
            return

        path = os.path.splitext(str(self.datotekazakreirati))
        if(path[1][0:3].strip().lower() != "" and path[1][0:3].strip().lower() != ".db"):
            return

        self.dial.close()
        self.UcitajBazu()
    
    #Ucitava ili kreira novu bazu na temelju odabira u meniju
    def UcitajBazu(self):
        #Provjera je li korisnik pravilno iskoristio meni
        if(str(self.datotekazakreirati[0]) == "" and str(self.datotekazaucitati[0]) == ""):
            QtWidgets.QApplication(sys.argv).closeAllWindows()

        #Kreiramo ili otvaramo bazu
        if(str(self.datotekazaucitati[0]) != ""):
            self.baza = SqlBaza(True, str(self.datotekazaucitati[0]))
            self.lista_datuma = ListaDatuma()
            self.PocetniSetup()
            self.lista_datuma.UveziListu(self.baza.BazaUcitajDatume())

        else:
            self.baza = SqlBaza(False, str(self.datotekazakreirati[0]))
            self.lista_datuma = ListaDatuma()
            self.PocetniSetup()

        self.UpdatePopis(self.VratiDanasnjiDan())
        self.UpdatePopis(self.izabrani_datum)

    #Provjeravamo ima li korisnik otvorenu bazu
    def ProvjeriBazu(self):
        if(self.baza == None): 
            QtWidgets.QApplication(sys.argv).closeAllWindows()

    #Vraca danasnji datum u stringu ("D/M/G")
    def VratiDanasnjiDan(self):
        dat = QtCore.QDate.currentDate()
        return "{0}/{1}/{2}".format(dat.day(), dat.month(), dat.year())

    #Brisemo sve s liste zeljenog datuma i stavljamo na nju sve iz liste zadataka za taj datum
    def UpdatePopis(self, datum):
        if(datum == self.VratiDanasnjiDan()):
            self.ui.danas_lista.clear()
            
            if(self.lista_datuma.PostojiDatum(datum) == True):
                id = self.lista_datuma.VratiDict()[datum].VratiListuZadataka()
                
                for i in id:
                    item = QtWidgets.QListWidgetItem(i.VratiTekst())
                    if(i.VratiStanje() == True):
                        item.setForeground(QtGui.QColor(self.BOJA_DOVRSENIH)) 
                    else:
                        item.setForeground(QtGui.QColor(self.BOJA_NEDOVRSENIH)) 
                    self.ui.danas_lista.addItem(item)

        else:
            self.ui.datum_lista.clear()
         
            if(self.lista_datuma.PostojiDatum(datum) == True):
                id = self.lista_datuma.VratiDict()[datum].VratiListuZadataka()
            
                for i in id:
                    item = QtWidgets.QListWidgetItem(i.VratiTekst())
                    if(i.VratiStanje() == True):
                        item.setForeground(QtGui.QColor(self.BOJA_DOVRSENIH)) 
                    else:
                        item.setForeground(QtGui.QColor(self.BOJA_NEDOVRSENIH)) 
                    self.ui.datum_lista.addItem(item)

    #Poziva se kada se pritisne tipka označi kao dovršeno i označava označeni zadatak na listi danas dovršenim
    def DovrsiZadatakDanas(self):
        self.ProvjeriBazu()

        try:
            izabrana_stavka = self.ui.danas_lista.currentRow()
            if(izabrana_stavka == -1):
                return
            
            dodaj = False
            if(izabrana_stavka == (len(self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka())-1)):
                dodaj = True
            
            id = self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka()[izabrana_stavka]
            
            if(id.VratiStanje() == False):
                self.ui.danas_lista.takeItem(izabrana_stavka)
                id.PostaviStanje(True)
                
                item = QtWidgets.QListWidgetItem(id.VratiTekst())
                item.setForeground(QtGui.QColor(self.BOJA_DOVRSENIH)) 
                
                if(dodaj == True):
                    self.ui.danas_lista.addItem(item)
                else: 
                    self.ui.danas_lista.insertItem(izabrana_stavka,item)

                self.baza.BazaSacuvajDatum(self.VratiDanasnjiDan(),self.lista_datuma.VratiDict()[self.VratiDanasnjiDan()].VratiListuZadataka())
        except:
            return
    
    #Poziva se kada se pritisne tipka označi kao dovršeno i označava označeni zadatak na listi datuma dovršenim
    def DovrsiZadatakDatum(self):
        self.ProvjeriBazu()

        try:
            izabrana_stavka = self.ui.datum_lista.currentRow()
            if(izabrana_stavka == -1):
                return

            dodaj = False
            if(izabrana_stavka == (len(self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka())-1)):
                dodaj = True

            id = self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka()[izabrana_stavka]

            if(id.VratiStanje() == False):
                self.ui.datum_lista.takeItem(izabrana_stavka)
                id.PostaviStanje(True)
                
                item = QtWidgets.QListWidgetItem(id.VratiTekst())
                item.setForeground(QtGui.QColor(self.BOJA_DOVRSENIH))
                
                if(dodaj == True):
                    self.ui.datum_lista.addItem(item)
                else: 
                    self.ui.datum_lista.insertItem(izabrana_stavka,item)
                
                self.baza.BazaSacuvajDatum(self.izabrani_datum,self.lista_datuma.VratiDict()[self.izabrani_datum].VratiListuZadataka())
        except:
            return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    aplikacija = ToDoList()
    aplikacija.show()
    sys.exit(app.exec_())

