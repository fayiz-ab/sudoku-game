#sudoku_interface
import sudoku_fonctions as sf

print("Bienvenue")
jouer = input("Souhaitez-vous jouer ? (Oui/Non) : ")

while jouer.lower() not in ["oui", "non"] :
    print("Erreur : Veuillez répondre par 'Oui' ou 'Non'.")
    jouer = input("Souhaitez-vous jouer ? (Oui/Non) : ")

while jouer.lower() == "oui" :

    duel = input("Souhaitez-vous jouer en duel contre la machine? (Oui/Non) : ")
    while duel.lower() not in ["oui", "non"] :
        print("Erreur : Veuillez répondre par 'Oui' ou 'Non'.")
        duel = input("Souhaitez-vous jouer en duel ? (Oui/Non) : ")

    if duel.lower() == "non" :
        print("Trois niveaux sont disponibles : \n   - Débutant : tapez 1, \n   - Intermédiaire : tapez 2, \n   - Expérimenté : tapez 3.")
        niveau = - 1
        while niveau not in ["1", "2", "3"] :
            niveau = input("Veuillez choisir un niveau (1, 2 ou 3) : ")

        sf.jouer_partie(int(niveau))

    elif duel.lower() == "oui" :
        print("Le duel contre la machine commence !")
        sf.jouer_duel()

    while True :
        jouer = input("\nSouhaitez-vous rejouer ? (Oui/Non) : ")
        if jouer.lower() in ["oui", "non"] : 
            break
        else :
            print("Veuillez répondre par 'Oui' ou 'Non'.")


print("Au plaisir de vous retrouver pour une autre partie de sudoku !")
