from liste_epreuves import ListeEpreuves
from epreuve import Epreuve

def main():
    fichier_epreuves = "./Epreuves.txt"
    
    liste_epreuves = ListeEpreuves(fichier_epreuves)
    liste_epreuves_pour_question_6 = ListeEpreuves(fichier_epreuves)
    liste_epreuves_pour_question_7 = ListeEpreuves(fichier_epreuves)

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

    # On choisit une epreuve parmi les epreuves triees (0 pour physique et 4 pour espagnol)
    e = liste_epreuves.get(4) 
    # On elimine les conflits de l'epreuve choisie, cependant, l'épreuve aussi est supprimée, 
    # mais l'a rajoute par la suite et on réexecute le tri par heure de fin
    liste_epreuves.eliminer_conflits(e) 
    
    print("#################################################")
    print("#  Epreuves apres suppression des conflits de   #")
    print(f"#              l'epreuve de {e.intitule}             #")
    print("#################################################")
    print(liste_epreuves)
    print()
    
    planning = []
    
    # Trie par horaire proche pour la question 6

    liste_epreuves_pour_question_6.tri_par_heure_fin()
    for epreuve in liste_epreuves_pour_question_6.liste:
        if len(planning) == 0:
            planning.append(epreuve)
        else:
            if epreuve.debut >= planning[-1].fin:
                planning.append(epreuve)
    

    
    planning.sort(key=lambda ep: ep.fin)
    
    print("#################################################")
    print("#             Planning des epreuves             #")
    print("#################################################")
    
    for epreuve in planning:
        print(epreuve)


    #Trie par durée pour la question 7

    planning7 = []
    liste_epreuves_pour_question_7.tri_par_duree()
    while liste_epreuves_pour_question_7.liste:
        epreuve = liste_epreuves_pour_question_7.liste[0]  
        planning7.append(epreuve)  
        liste_epreuves_pour_question_7.eliminer_conflits7(epreuve)
    
    planning7.sort(key=lambda ep: ep.fin)
    
    
    
    print("#################################################")
    print("#    Planning des epreuves pour question 7      #")
    print("#################################################")

    for epreuve in planning7:
        print(epreuve)

if __name__ == "__main__":
    main()
