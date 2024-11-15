from typing import List

class Bipartition:
    
    # Vous pouvez utiliser d'autres structures de données, notamment les List
    E = [2, 10, 3, 8, 5, 7, 9, 5, 3, 2]
    F = [771, 121, 281, 854, 885, 734, 486, 1003, 83, 62]
    
    sListe1 = []
    sListe2 = []

    @staticmethod
    def main():
        liste = Bipartition.F

        print("Liste initiale : ", end="")
        liste.sort(reverse=True)
        Bipartition.afficher(liste)

        # Remplacez `utiliserMotieSommeCommeRepere` avec `completerSousEnsembleLePulsPetit` si nécessaire
        Bipartition.completerSousEnsembleLePulsPetit(liste)

        print("Sous-liste 1 : ", end="")
        Bipartition.afficher(Bipartition.sListe1)

        print("Sous-liste 2 : ", end="")
        Bipartition.afficher(Bipartition.sListe2)

    # Méthode 1 : Trier par ordre décroissant, puis ajouter chaque élément au sous-ensemble avec la somme la plus petite.
    @staticmethod
    def completerSousEnsembleLePulsPetit(liste: List[int]):
        liste.sort(reverse=True)
        for i in liste:
            if sum(Bipartition.sListe1) <= sum(Bipartition.sListe2):
                Bipartition.sListe1.append(i)
            else:
                Bipartition.sListe2.append(i)

    # Méthode 2 : Calculer la somme de la liste, diviser par 2 pour un repère, trier par ordre décroissant,
    # puis remplir la première sous-liste sans dépasser la moitié de la somme.
    @staticmethod
    def utiliserMotieSommeCommeRepere(liste: List[int]):
        total = Bipartition.somme(liste) / 2
        liste.sort(reverse=True)
        for i in liste:
            if sum(Bipartition.sListe1) + i <= total:
                Bipartition.sListe1.append(i)
            else:
                Bipartition.sListe2.append(i)

    @staticmethod
    def somme(liste: List[int]) -> int:
        return sum(liste)

    @staticmethod
    def afficher(liste: List[int]):
        print(", ".join(map(str, liste)) + f" ({Bipartition.somme(liste)})")

# Appeler la méthode principale
if __name__ == "__main__":
    Bipartition.main()
