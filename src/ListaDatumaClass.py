import imp
from ListaZadatakaClass import ListaZadataka
from datetime import date
from PyQt5 import QtCore

class ListaDatuma(object):
    #Dictionary koji sadrži listu zadataka za svaki korišteni datum 
    dict = { } #Sadrži datume i objekte klase ListaZadataka

    def __init__(self):
        self.dict = { }

    #Mijenja dictionary sa željenim dictionaryem (koristi se kod citanja postojece liste)
    def UveziListu(self, lista = { }):
        self.dict = lista

    #Dodajemo novi datum u dictionary
    def KreirajDatum(self, datum):
        self.dict.update({ datum : ListaZadataka(datum) })

    #Provjeravamo postoji li datum u dictionaryu
    def PostojiDatum(self, datum):
        if datum in self.dict:
            return True
        return False

    #Vraćamo dictionary
    def VratiDict(self):
        return self.dict
