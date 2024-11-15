from datetime import datetime

class Epreuve:
    def __init__(self, intitule, debut, fin):
        self.intitule = intitule
        self.debut = datetime.strptime(debut, "%H:%M").time()
        self.fin = datetime.strptime(fin, "%H:%M").time()

        if self.debut > self.fin:
            self.debut, self.fin = self.fin, self.debut

    def __str__(self):
        return f"Epreuve de {self.intitule} ({self.debut} --> {self.fin})"

    def __lt__(self, other):
        return self.fin < other.fin
