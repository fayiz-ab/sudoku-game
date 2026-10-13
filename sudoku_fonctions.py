#sudoku_fonctions 
from random import *
import sudoku_bdd as bdd

def affiche_grille(grille):
    print("\n    1 2   3 4")
    print("  +-----+-----+")
    for i in range(4):
        print(f"{i+1} |", end=" ")
        for j in range(4):
            val = grille[i][j]
            print("." if val == 0 else val, end=" ")
            if j == 1:
                print("|", end=" ")
        print("|")
        if i == 1 or i == 3:
            print("  +-----+-----+")

def case_vide(grille, ligne, colonne):
    if grille[ligne][colonne] == 0 : 
        return True
    else : 
        return False

def case_fixe(grille, ligne, colonne) :
    if grille[ligne][colonne] != 0 :
        return True
    else:
        return False

def absent_colonne(grille, colonne, n) :
    test = True
    for i in range(len(grille)) : 
        if grille[i][colonne] == n : 
            test = False
    return test

def absent_bloc(grille, n, l, c):
    test = True
    debut_bloc_ligne = (l // 2) * 2
    debut_bloc_colonne = (c // 2) * 2
    for i in range(debut_bloc_ligne, debut_bloc_ligne + 2) :
        for j in range(debut_bloc_colonne, debut_bloc_colonne + 2) :
            if grille[i][j] == n : 
                test = False
    return test

def grille_complete(grille) :
    test = True
    for i in range(len(grille)) :
        for j in range(len(grille[i])) :
            if grille[i][j] == 0 :
                test = False
    return test

def absent_ligne(grille, ligne,n) :
    test = True
    for i in range(len(grille)) :
        if grille[ligne][i] == n : 
            test = False
    return test


def grille_correcte(grille) :
    test = True
    n = len(grille)
    liste = [i for i in range(1, n+1)]

    # On vérifie si les lignes sont correctes
    for ligne in range(len(grille)) :
        for n in liste : 
            if absent_ligne(grille, ligne, n) :
                test = False
                return test

    # On vérifie si les colonnes sont correctes    
    for colonne in range(len(grille)) :
        for n in liste : 
            if absent_colonne(grille, colonne, n) :
                test = False
                return test

    # On vérifie si les blocs sont corrects
    liste_cases = [(0,0), (0, 2), (2, 0), (2, 2)]
    for i, j in liste_cases :
        for k in range(1, 5) :
            if absent_bloc(grille, k, i, j) :
                test = False
                return test

    # Si les lignes, les colonnes et les blocs sont corrects, la grille est correcte est on renvoie True
    return test

def calculer_score(coups_valides, erreurs):
    """Calcule le score final du joueur en fonction des coups valides et des erreurs."""
    score = coups_valides * 10 - erreurs * 5
    if score < 0:
        score = 0
    return score  

def jouer_partie(niveau):
    """Gère la boucle principale d'une partie de Sudoku."""
    
    # Initialisation des grilles
    grille_initiale = choice(bdd.NIVEAUX[niveau])
    grille = [ligne.copy() for ligne in grille_initiale]
    
    coups_valides = 0
    erreurs = 0
    
    # Boucle de jeu
    while not grille_complete(grille):
        affiche_grille(grille)
        
        # Demande de saisie avec conversion directe en entier
        ligne = int(input("Numéro de ligne (1-4) : ")) - 1
        colonne = int(input("Numéro de colonne (1-4) : ")) - 1
        valeur = int(input("Valeur à insérer (1-4) : "))
        
        # Vérifications de la validité de l'entrée
        if not (0 <= ligne <= 3 and 0 <= colonne <= 3 and 1 <= valeur <= 4):
            print("Erreur : Les valeurs doivent être comprises entre 1 et 4.")
            continue
            
        if case_fixe(grille_initiale, ligne, colonne):
            print("Erreur : Cette case est fixe, vous ne pouvez pas la modifier !")
            continue
            
        # Vérification des règles du Sudoku
        if absent_ligne(grille, ligne, valeur) and absent_colonne(grille, colonne, valeur) and absent_bloc(grille, valeur, ligne, colonne):
            grille[ligne][colonne] = valeur
            print("Coup valide !")
            coups_valides += 1
            print(f"Score actuel : {calculer_score(coups_valides, erreurs)} points.")

        else:
            print("Coup invalide : Cette valeur ne respecte pas les règles.")
            erreurs += 1
            print(f"Score actuel : {calculer_score(coups_valides, erreurs)} points.")

    # Fin de partie
    affiche_grille(grille)
    if grille_correcte(grille):
        print("\nFélicitations, la grille est correcte !")
    else:
        print("\nLa grille est remplie mais contient des erreurs.")
        
    score = calculer_score(coups_valides, erreurs)
    print(f"Bravo, vous avez terminé la partie ! Votre score est de {score} points.")


# Deuxième implémentation

def lst_cases_vides(grille) :
    n = len(grille)
    cases_vides = []
    for i in range(n):
        for j in range(n):
            if case_vide(grille, i, j):
                cases_vides.append((i, j))
    return cases_vides

def candidats(grille, ligne, colonne) :
    candidats_possibles = []
    for n in range(1, 5) :
        if absent_ligne(grille, ligne, n) and absent_colonne(grille, colonne, n) and absent_bloc(grille, n, ligne, colonne) :
            candidats_possibles.append(n)
    return candidats_possibles

def jouer_duel():
    """Gère la partie compétitive entre l'humain et la machine."""
    grille_choisie, solution_choisie = choice(bdd.DUELS) 

    grille = [ligne.copy() for ligne in grille_choisie]
    grille_initiale = [ligne.copy() for ligne in grille_choisie]
    
    score_humain = 0
    score_machine = 0
    
    # 1. Choisir aléatoirement qui commence
    tour_humain = choice([True, False])
    
    print("L'humain commence !" if tour_humain else "La machine commence !")
    
    # La boucle continue tant que la grille n'est pas pleine
    while not grille_complete(grille) :
        affiche_grille(grille)
        print(f"Scores : Humain : {score_humain} | Machine : {score_machine}")
        
        if tour_humain :
            print("\n> Votre tour !")
            ligne = int(input("Ligne (1-4) : ")) - 1
            colonne = int(input("Colonne (1-4) : ")) - 1
            valeur = int(input("Valeur (1-4) : "))
            
            # Vérifications : si erreur, on passe le tour (pas de 'continue' ici !)
            if not (0 <= ligne <= 3 and 0 <= colonne <= 3 and 1 <= valeur <= 4) :
                print("Coup incorrect, ces coordonnées n'existent pas ! Vous passez votre tour.")
            elif case_fixe(grille_initiale, ligne, colonne) :
                print("Coup incorrect, il s'agit d'une case fixe ! Vous passez votre tour.")
            elif not case_vide(grille, ligne, colonne) :
                print("Coup incorrect, cette case est déjà remplie ! Vous passez votre tour.")
            elif not absent_ligne(grille, ligne, valeur):
                print("Coup incorrect, cette valeur est déjà dans la ligne ! Vous passez votre tour.")
            elif not absent_colonne(grille, colonne, valeur):
                print("Coup incorrect, cette valeur est déjà dans la colonne ! Vous passez votre tour.")
            elif not absent_bloc(grille, valeur, ligne, colonne):
                print("Coup incorrect, cette valeur est déjà dans le bloc ! Vous passez votre tour.")
            elif valeur == solution_choisie[ligne][colonne] :
                # C'est la bonne valeur !
                print("Coup correct, vous gagnez 1 point !")
                grille[ligne][colonne] = valeur
                score_humain += 1
            else :
                # C'est une valeur valide mathématiquement, mais pas celle de la solution
                print("Coup incorrect, ce n'est pas la bonne valeur ! Vous passez votre tour.")
                
        else :
            print("\n> Tour de la machine !")
            # La machine cherche toutes les cases vides
            liste_cases_vides = lst_cases_vides(grille)
            
            # Elle en choisit une au hasard
            choix_l, choix_c = choice(liste_cases_vides)
            liste_candidats = candidats(grille, choix_l, choix_c)
            if not liste_candidats:           # sécurité : aucune valeur possible
                liste_candidats = [1, 2, 3, 4]
            valeur_jouee = choice(liste_candidats)
            bonne_valeur = solution_choisie[choix_l][choix_c]
            
            if valeur_jouee == bonne_valeur :
                grille[choix_l][choix_c] = valeur_jouee
                score_machine += 1
                print(f"La machine a joué {valeur_jouee} à la case ({choix_l + 1}, {choix_c + 1}). C'est correct !")
            else :
                print(f"La machine a joué {valeur_jouee} à la case ({choix_l + 1}, {choix_c + 1}) et s'est trompée !")
        # 8. Alterner les tours
        tour_humain = not tour_humain
        
    # Fin de partie
    affiche_grille(grille)
    print("\nLa grille est complète, la partie est terminée !")
    print(f"Score final : Humain : {score_humain} | Machine : {score_machine}")
    
    if score_humain > score_machine:
        print("Félicitations, vous avez battu la machine !")
    elif score_machine > score_humain:
        print("Dommage, la machine a gagné. L'IA prend le contrôle !")
    else:
        print("Égalité parfaite !")
