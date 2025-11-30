import random


class Pilkarz:

    __kontuzjowany: bool = False

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
        return f"<{self.__class__.__name__} imie={self.imie} pozycja={self.pozycja} numer={self.numer} umiejetnosc={self.umiejetnosc} zmeczenie={self.zmeczenie} kontuzjowany={self.__kontuzjowany}>"

class Bramkarz(Pilkarz):
    def __init__(self, imie: str, pozycja: str, numer: int, umiejetnosc: int, refleks: int, zmeczenie: int = 0) -> None:
        self.refleks = refleks
        super().__init__(imie, pozycja, numer, umiejetnosc, zmeczenie)

class Napastnik(Pilkarz):
    def __init__(self, imie: str, pozycja: str, numer: int, umiejetnosc: int, wykonczenie: int, zmeczenie: int = 0) -> None:
        self.refleks = wykonczenie
        super().__init__(imie, pozycja, numer, umiejetnosc, zmeczenie)
        

class Druzyna:
    def __init__(self, nazwa:str, zawodnicy: list = None):
        self.nazwa = nazwa
        self.zawodnicy = zawodnicy if zawodnicy is not None else []

    def dodaj_zawodnika(self, zawodnik):
        self.zawodnicy.append(zawodnik)

    def usun_zawodnika(self, identyfikator: str | int):
        
        for idx, pilkarz in enumerate(self.zawodnicy):
            if isinstance(identyfikator, str) and pilkarz.imie == identyfikator:
                self.zawodnicy.pop(idx)
                print(f"Usunieto zawodnika o imieniu {identyfikator}")
                return True
            elif isinstance(identyfikator, int) and pilkarz.id == identyfikator:
                self.zawodnicy.pop(idx)
                print(f"Usunieto zawodnika o nr: {identyfikator}")
                return True
        return False

    def znajdz_zawodnika(self, identyfikator: str| int):
        for pilkarz in self.zawodnicy:
            if isinstance(identyfikator, str) and pilkarz.imie == identyfikator:
                print(f"Znaleziono zawodnika o imieniu: {identyfikator}")
                return True
            elif isinstance(identyfikator, int) and pilkarz.numer == identyfikator:
                print(f"Znaleziono zawodnika o nr: {identyfikator}")
                return True
        return False

    def lista_zawodnikow_gotowych(self):
        gotowy_do_gry =[]
        for pilkarz in self.zawodnicy:
            if pilkarz.zmeczenie < 70 and not pilkarz._Pilkarz__kontuzjowany: #gotowy do gry
                gotowy_do_gry.append(pilkarz)
        print("-------- Gotowi Zawodnicy --------")
        for pilkarz in gotowy_do_gry:
            print(f"{pilkarz.imie} ({pilkarz.numer}) - {pilkarz.pozycja} - gotowy")
        print("----------------------------------")
        return gotowy_do_gry

    
    def raport(self):
        print("------- Raport Druzyny ---------")
        for pilkarz in self.zawodnicy:
            print(pilkarz)
        print("---------------------------------")


class Mecz:
    def __init__(self, druzyna1, druzyna2):
        self.druzyna1 = druzyna1
        self.druzyna2 = druzyna2
        print("------ Rozpoczęcie meczu ------")
        print(f"({self.druzyna1.nazwa}) - ({self.druzyna2.nazwa})")

    def rozegraj_mecz(self):
        pkt_druzyny1 = self.policz_punkty(self.druzyna1)
        print(pkt_druzyny1)
        # pkt_druzyny2 = policz_punkty(self.druzyna2)
        pkt_druzyny1 = 15
        pkt_druzyny2 = 5
        # warunki wygranej
        
        if pkt_druzyny1 > pkt_druzyny2:
            print(f"DRUZYNA {self.druzyna1.nazwa} wygrała pojedynek")
        elif pkt_druzyny2 > pkt_druzyny1:
            print(f"DRUZYNA {self.druzyna2.nazwa} wygrała pojedynek")
        else:
            print("Doszło do remisu! Gratulacje dla obu drużyn")

    def policz_punkty(self, druzyna):
        punkty: int = 0
        print(druzyna)
        for pilkarz in druzyna.zawodnicy:
            punkty += pilkarz.umiejetnosc
            punkty -= (pilkarz.zmeczenie // 2)

        return punkty


lewy = Napastnik("Lewy", "Napad", 9, 86, 99, 80)
prawy = Pilkarz("Prawy", "Skrzydło", 12, 99, 25)
baks = Bramkarz("Bravos", "Bramkarz", 99, 76, 78, 15)

# lewy.podnies_umiejetniosc()
# lewy.wycieczenie(5)
# lewy.zawodnik()
# lewy.daj_kontuzje()
# lewy.sprawdz_kontuzje()
# print(lewy)


zespol = [lewy, prawy, baks]

druzyna = Druzyna("Barca")
druzyna2 = Druzyna("Messia")

druzyna.zawodnicy.extend(zespol)
druzyna2.zawodnicy.extend(zespol)

# druzyna.pokaz_druzyne()
print("------------------")
druzyna.lista_zawodnikow_gotowych()

druzyna.raport()

mecz = Mecz(druzyna, druzyna2)

mecz.rozegraj_mecz()