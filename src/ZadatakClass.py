
class Zadatak(object):
    #Svojstva svakog zadatka
    tekst = "" #tekst zadatka 
    dovrseno = False #govori nam je li dovršen ili ne

    #Konstruktor Zadatak(tekst,dovrseno)
    def __init__(self, tekst="", dovresno=False):
        self.tekst = tekst
        self.dovrseno = dovresno

    #Vraćamo tekst zadatka
    def VratiTekst(self):
        return self.tekst

    #Postavljamo tekst zadatka
    def PostaviTekst(self, tekst):
        self.tekst = tekst

    #Vraćamo stanje - je li zadatak dovršen ili ne
    def VratiStanje(self):
        return self.dovrseno
    
    #Postavljamo stanje zadatka (True - dovršen, False - nedovršen)
    def PostaviStanje(self, stanje):
        self.dovrseno = stanje
