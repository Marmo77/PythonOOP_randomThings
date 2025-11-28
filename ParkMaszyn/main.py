#LORE
# Fabula (krótko)

# Jesteś inżynierem w warsztacie przemysłowym „Park Maszyn”. Twoim zadaniem jest napisać prostą symulację obsługi i konserwacji maszyn: masz bazową klasę Machine oraz konkretne typy maszyn (Lathe, Grinder), menedżera warsztatu Workshop. Symulacja ma pokazać: tworzenie obiektów, operacje (zwiększanie czasu pracy), sprawdzanie potrzeby konserwacji, wykonywanie konserwacji i raport.

# Celem: przećwiczyć podstawy Pythona + OOP: konstruktory, pola instancji i klasowe, metody, właściwości (properties), prywatne atrybuty, wyjątki, dziedziczenie, polimorfizm, klasowe/ statyczne metody, listy, pętle, list comprehensions i proste wywołanie demonstracyjne.

# Szacowany czas wykonania: ~40 minut (implementacja + krótkie testy).


import time


class Machine:

    MAINTENANCE_THRESHOLD: float = 100.00

    def __init__(self, id: str, model: str, runtime:float = 0.0):
        self.id = id
        self.model = model
        self.runtime = float(runtime)

        self.last_maintance = 0.0 #ostatnia konserwacja
        self._status: str = "stopped" # albo "running"
    
    
    def start(self):
        self._status = "running"
    
    def stop(self):
        self._status = "stopped"

    def operate(self, hours: int):
        if self._status == "running":
            if hours > 0:   
                self.runtime += hours
                # self.last_maintance = hours # ostatnia konserwcja
                print("Maszyna pracuje...")
                # time.sleep(1.5)
                print(f"{self.model} przepracowała {hours}h")
                print(f"*(Przepracowane godziny: {self.runtime})*")
        else:
            raise RuntimeError("maszyna nie jest włączona!")

    def needs_maintance(self) -> bool:
        return (self.runtime - self.last_maintance) >= self.MAINTENANCE_THRESHOLD

    def perform_maintance(self):
        # konserwacja
        if self._status == "running":
            raise RuntimeError("Maszyna dalej pracuje... musisz ją wyłączyć")
        self.last_maintance = self.runtime
        print(f"Pomyślna konserwacja - *(ostatnia konserwacja: {self.last_maintance})*")
        return True

    @property
    def uptime(self):
        return self.runtime

    @classmethod
    def from_dict(cla, d):
        m = cla(d["id"], d.get("model", "unknown"), d.get("runtime", 0.0))
        m.last_maintance = d.get("last_maintance", 0.0)
        return m

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id} model={self.model} runtime={self.runtime} status={self._status}>"


class Lathe(Machine):
    MAINTENANCE_THRESHOLD: float = 90.00

    def __init__(self, id: str, model: str, runtime: float = 0,precision_level: int =5):
        super().__init__(id, model, runtime)
        self.precision_level = precision_level

class Grinder(Machine):
    MAINTENANCE_THRESHOLD: float = 120.00

    def __init__(self, id: str, model: str, runtime: float = 0, wheel_size: int = 6):
        super().__init__(id, model, runtime)
        self.wheel_size = wheel_size


class Workshop:
    def __init__(self):
        self.machines = []

    def add_machine(self, machine: Machine):
        self.machines.append(machine)
    
    def remove_machine(self, id: str):
        self.machines = [m for m in self.machines if m.id != id]

    def list_machines(self):
        # return ", ".join(str(x) for x in self.machines)
        return list(self.machines)

    def machines_needing_maintenance(self):
        needing_list = [m for m in self.machines if m.runtime >= m.MAINTENANCE_THRESHOLD]
        return needing_list

    def perform_maintenance_all(self):
        done = []
        for machine in self.machines_needing_maintenance():
            try:
                machine.perform_maintance()
                done.append(machine.id)
            except RuntimeError:
                machine.stop()
                machine.perform_maintance()
                done.append(machine.id)
        return done

    def total_runtime(self):
        return sum(m.runtime for m in self.machines)
        
###############################################################

warsztat = Workshop()


tokarka = Lathe("TOK-1", "Tooksun", 85)
szlifierka = Grinder("GR-99", "Szlifir", 35)
maszyna = Machine("WIRR", "Meszin", 120)

maszyny = [tokarka, szlifierka, maszyna]

for m in maszyny:
    warsztat.add_machine(m)

tokarka.start(), szlifierka.start()
tokarka.operate(10), szlifierka.operate(15)
szlifierka.stop, tokarka.stop()

time.sleep(1)
print("--- Przed konserwacją ---")
for m in warsztat.list_machines():
    print(f"- {m.id} ({m.model}): runtime={m.runtime:.1f}, last_maint={m.last_maintance} needs={m.needs_maintance()}")

print("MASZYNY DO KONSERWACJI: ")
time.sleep(1)
need_meint =[]
for m in warsztat.list_machines():
    if m.needs_maintance():
        need_meint.append(f"({m.id}, {m.model})")
print(", ".join(str(m) for m in need_meint))

print("Konserwowanie...")
time.sleep(1)
mentained = []
for m in warsztat.machines_needing_maintenance():
    print(f"*Zatrzymano prace {m.id}*")
    m.stop()
    m.perform_maintance()
    mentained.append(f"({m.id}, {m.model})")
print("WYKONANO KONSERWACJE DLA:")
print(", ".join(str(m) for m in mentained))

print("--- Status po konserwacji ---")
for m in warsztat.list_machines():
    print(f"- ({m.id} - {m.model}) runtime={m.runtime} last_maint={m.last_maintance} {"NIE OK" if m.needs_maintance() else "OK"}")