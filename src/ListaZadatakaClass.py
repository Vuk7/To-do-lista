from datetime import date

class ListaZadataka(object):
    #Lista sa svim zadatcima za neki datum
    lista_zadataka = [] #Sadrži objekte klase Zadatak

    #Konstruktor ListaZadataka(datum)
    def __init__(self, datum):
        self.datum = datum
        self.lista_zadataka = []
    
    #Postavljamo datum na koji se lista odnosi
    def PostaviDatum(self, datum): 
        self.datum = datum

    #Vraćamo datum na koji se lista odnosi
    def VratiDatum(self):
        return self.datum

    #Dodajemo zadatak u listu zadataka
    def DodajZadatak(self, zadatak):
        self.lista_zadataka.append(zadatak)

    #Vraćamo listu zadataka
    def VratiListuZadataka(self):
        return self.lista_zadataka

    #Brišemo zadatak s liste
    def ObrisiZadatak(self, id):
        self.lista_zadataka.pop(id)


