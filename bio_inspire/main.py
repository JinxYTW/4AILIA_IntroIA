from liste_epreuves import ListeEpreuves
from epreuve import Epreuve

def main():
    fichier_epreuves = "./Epreuves.txt"
    
    liste_epreuves = ListeEpreuves(fichier_epreuves)

    print("#################################################")
    print("# Toutes les epreuves inscrites dans le fichier #")
    print("#################################################")
    print(liste_epreuves)
    print()
    
    liste_epreuves.tri_par_heure_fin()
    
    print("#################################################")
    print("# Epreuves triees par horaires de fin croissant #")
    print("#################################################")
    print(liste_epreuves)
    print()
    
    e = liste_epreuves.get(0)
    liste_epreuves.eliminer_conflits(e)
    
    print("#################################################")
    print("#  Epreuves apres suppression des conflits de   #")
    print(f"#              l'epreuve de {e.intitule}             #")
    print("#################################################")
    print(liste_epreuves)
    print()
    
    planning = []
    
    # Implementez votre algorithme de planification efficace des epreuves.
    # Les epreuves retenues seront ajoutees, au fur et a mesure dans "planning"
    
    planning.sort(key=lambda ep: ep.fin)
    
    print("#################################################")
    print("#             Planning des epreuves             #")
    print("#################################################")
    
    for epreuve in planning:
        print(epreuve)

if __name__ == "__main__":
    main()
