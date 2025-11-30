import random


class Pilkarz:

    __kontuzjowany: bool

    def __init__(self, imie: str, pozycja: str, numer: int, umiejetnosc:int, zmeczenie: int= 0) -> None:
        self.imie = imie
        self.pozycja = pozycja
        self.numer = numer
        self.umiejetnosc = umiejetnosc
        self.zmeczenie = zmeczenie

    def podnies_umiejetniosc(self):
        rand_skill = random.randint(5,15)
        print(f"Podnoszenie umiejętności o {rand_skill}")
        self.umiejetnosc += rand_skill
        if int(self.umiejetnosc) > 100:
            self.umiejetnosc = 100
        print(f"{self.imie} ma teraz {self.umiejetnosc}")

    def wycieczenie(self, zmeczenie):
        # dodanie zmeczenia
        self.zmeczenie += zmeczenie

        if self.zmeczenie > 100:
            self.zmeczenie = 100
        elif self.zmeczenie < 0:
            self.zmeczenie = 0
        print(f"{self.imie} zmęczneie teraz wynosi: {self.zmeczenie}")

    def zawodnik(self):
        print("----------------------")
        print(f"Imię: {self.imie}")
        print(f"Pozycja: {self.pozycja}")
        print(f"Numer: {self.numer}")
        print(f"Umiejętności: {self.umiejetnosc}")
        print("----------------------")

    def daj_kontuzje(self):
        # na podstawie umiejętności szanse na kontuzje
        daj_kontuzje = random.randint(0,100)
        
        if daj_kontuzje > self.umiejetnosc:
            self.__kontuzjowany = True
            print("Zawodnik został kontuzjowany 🦴")
        else:
            self.__kontuzjowany = False

        return self.__kontuzjowany
    
    def sprawdz_kontuzje(self):
        
        if self.__kontuzjowany:
            print("Zawodnik jest kontuzjowany 😵")
        else:
            print("Zawodnik nie jest kontuzjowany 🏋️")

    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} imie={self.imie} pozycja={self.pozycja} numer={self.numer} umiejetnosc={self.umiejetnosc} zmeczenie={self.zmeczenie}>"


        

lewy = Pilkarz("Lewy", "Napad", 9, 86)

lewy.podnies_umiejetniosc()
lewy.wycieczenie(5)
lewy.zawodnik()
lewy.daj_kontuzje()
lewy.sprawdz_kontuzje()
print(lewy)

class Druzyna:
    def __init__(self, nazwa:str, zawodnicy: list = []):
        self.nazwa = nazwa
        self.zawodnicy = zawodnicy

    def dodaj_zawodnika(self, zawodnik):
        self.zawodnicy.append(zawodnik)
    
    def pokaz_druzyne(self):
        print(self.zawodnicy)

druzyna = Druzyna("Barca")

druzyna.dodaj_zawodnika(lewy)

druzyna.pokaz_druzyne()