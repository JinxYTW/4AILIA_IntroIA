from epreuve import Epreuve

class ListeEpreuves:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.liste = []
        self.lire_fichier_epreuves(nom_fichier)

    def lire_fichier_epreuves(self, fichier):
        try:
            with open(fichier, "r") as f:
                for ligne in f:
                    if not ligne.startswith("#"):
                        tokens = ligne.split()
                        nom = tokens[0]
                        debut = tokens[1]
                        fin = tokens[2]
                        epreuve = Epreuve(nom, debut, fin)
                        self.liste.append(epreuve)
        except IOError as e:
            print(e)

    def eliminer_conflits(self, epreuve):
        # À compléter...
        pass

    def tri_par_heure_fin(self):
        self.liste.sort(key=lambda ep: ep.fin)

    def get(self, i):
        return self.liste[i]

    def set(self, i, epreuve):
        if i < len(self.liste):
            self.liste[i] = epreuve
        else:
            self.liste.append(epreuve)

    def remove(self, i):
        if i < len(self.liste):
            del self.liste[i]

    def __str__(self):
        return "\n".join(str(epreuve) for epreuve in self.liste)
