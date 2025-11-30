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
        print("------- ZAWODNIK -------")
        print(f"Imię: {self.imie}")
        print(f"Pozycja: {self.pozycja}")
        print(f"Numer: {self.numer}")
        print(f"Umiejętności: {self.umiejetnosc}")
        print(f"Kontuzjowany: {"Tak" if self.__kontuzjowany else "Nie"}")

    def daj_kontuzje(self):
        # na podstawie umiejętności szanse na kontuzje
        daj_kontuzje = random.randint(0,100)
        
        if daj_kontuzje > self.umiejetnosc:
            self.__kontuzjowany = True
            print(f"Zawodnik {self.imie} został kontuzjowany 🦴")
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
        return gotowy_do_gry

    def wypisz_gotowych_zawodnikow(self):
        gotowy_do_gry = self.lista_zawodnikow_gotowych()
        print(f"-------- Gotowi Zawodnicy {self.nazwa} --------")
        for pilkarz in gotowy_do_gry:
            print(f"{pilkarz.imie} ({pilkarz.numer}) - {pilkarz.pozycja} - gotowy")
        print("----------------------------------")

    
    def raport(self):
        print(f"------- Raport Druzyny {self.nazwa} ---------")
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
        pkt_druzyny2 = self.policz_punkty(self.druzyna2)

        # warunki wygranej  
        print("--------------- MECZ SIĘ SKOŃCZYŁ ---------------")
        if pkt_druzyny1 > pkt_druzyny2:
            print(f"Drużyna {self.druzyna1.nazwa} wygrała mecz.")
            print(f"{pkt_druzyny1} pkt. > {pkt_druzyny2} pkt.")
        elif pkt_druzyny2 > pkt_druzyny1:
            print(f"Drużyna {self.druzyna2.nazwa} wygrała mecz.")
            print(f"{pkt_druzyny2} pkt. > {pkt_druzyny1} pkt.")
        else:
            print("Doszło do remisu! Gratulacje dla obu drużyn.")
        print("------------------------------------------------")

    #liczenie punktów na bazie umiejętności zawodników i poziomu zmęczenia
    def policz_punkty(self, druzyna):
        punkty: int = 0
        for pilkarz in druzyna.lista_zawodnikow_gotowych(): #tylko nie kontuzjowani i ktorych poziom ponizej < 70 zmeczenia
            punkty += pilkarz.umiejetnosc
            punkty -= (pilkarz.zmeczenie // 2)
        return punkty





#tworzenie klubów (druzyn)
barca = Druzyna("Barca")
mesierra = Druzyna("Messiara")

zawodnicy_barca = [
    Bramkarz("Barks", "Bramkarz", 1, 80, refleks=88),
    Napastnik("Lewando", "Napastnik", 9, 91, wykonczenie=95),

    Pilkarz("Garcia", "Obrońca", 2, 76, 20),
    Pilkarz("Mendes", "Obrońca", 3, 79, 10),
    Pilkarz("Arujo", "Obrońca", 4, 83, 30),
    Pilkarz("Balde", "Obrońca", 5, 78, 15),

    Pilkarz("Gavi", "Pomocnik", 6, 85, 20),
    Pilkarz("Pedri", "Pomocnik", 8, 87, 25),
    Pilkarz("De Jong", "Pomocnik", 21, 88, 35),

    Pilkarz("Ferran", "Skrzydło", 11, 82, 40),
    Pilkarz("Yamalando", "Skrzydło", 27, 86, 18),
]
#DOdaj zawodników do drużyna Barca
for z in zawodnicy_barca:
    barca.dodaj_zawodnika(z)


zawodnicy_mesierra = [

    Bramkarz("Ortez", "Bramkarz", 1, 78, refleks=83),

    Napastnik("Kiros", "Napastnik", 10, 88, wykonczenie=93),

    Pilkarz("Ramos", "Obrońca", 3, 80, 25),
    Pilkarz("Silva", "Obrońca", 4, 77, 10),
    Pilkarz("Piquez", "Obrońca", 5, 79, 30),
    Pilkarz("Vargas", "Obrońca", 15, 72, 15),

    Pilkarz("Moralez", "Pomocnik", 6, 82, 20),
    Pilkarz("Tevez", "Pomocnik", 7, 84, 10),
    Pilkarz("Rico", "Pomocnik", 17, 80, 35),

    Pilkarz("Santos", "Skrzydło", 11, 83, 25),
    Pilkarz("Mora", "Skrzydło", 22, 81, 18),
]

print("------------- KONTUZJE ---------------")
#skontuzjuj zawodnika (przechodzi przez kazdego zawodnika z obu klubow i losowo kontuzjuje z losowania)
for z in zawodnicy_barca:
    z.daj_kontuzje()
for z in zawodnicy_mesierra:
    z.daj_kontuzje()


print("--------- ZAWODNICY ZESPOLOW -----------")
print(f"---- Drużyna {barca.nazwa} ----")
for z in zawodnicy_barca:
    z.zawodnik()
print("---------------")
print(f"---- Drużyna {mesierra.nazwa} ----")
for z in zawodnicy_mesierra:
    z.zawodnik()
print("---------------")
#dodaj zawodników do Drużyny Mesierra
for z in zawodnicy_mesierra:
    mesierra.dodaj_zawodnika(z)

#Wypisuje raport do każdego zawodnika
zespoly = [barca, mesierra]
for zes in zespoly:
    # zes.raport() #raport lub wypisanie gotowych zawodnikow
    zes.wypisz_gotowych_zawodnikow()



mecz1 = Mecz(barca, mesierra)
mecz1.rozegraj_mecz()