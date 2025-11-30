import random


class Pilkarz:
    def __init__(self, imie: str, pozycja: str, numer: int, umiejetnosc:int, zmeczenie: int= 0) -> None:
        self.imie = imie
        self.pozycja = pozycja
        self.numer = numer
        self.umiejetnosc = umiejetnosc
        self.zmeczenie = zmeczenie

    def podnies_umiejetniosc(self):
        rand_skill = random.randint(5,15)
        print(f"Podnoszenie umiejętności o {rand_skill}")
        if int(self.umiejetnosc + rand_skill) > 100:
            self.umiejetnosc = 100
        else:
            self.umiejetnosc += rand_skill
        print(f"{self.imie} ma teraz {self.umiejetnosc}")
        

lewy = Pilkarz("Lewy", "Napad", 9, 88)

lewy.podnies_umiejetniosc()