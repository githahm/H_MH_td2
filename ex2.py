#la meilleure organization des livraisons des contenaires pour un cout minimal est : 
#D1 : 5-----> M2: cout 15
#     3-----> M1: cout 15
#D2 : 8-----> M3: cout 16
#     1-----> M1: cout 6 
# cout total minimal : 52  

import copy

cout = [[5, 3, 4], [6, 7, 2]]
demande = [4, 5, 8]
capacite = [8, 9]

def cout_total(solution):
    return sum(solution[i][j] * cout[i][j] for i in range(2) for j in range(3))

def solution_initiale():
    solution = [[0,0,0],[0,0,0]]
    for j in range(3):
        reste = demande[j]
        for i in range(2):
            envoi = min(reste, capacite[i] - sum(solution[i]))
            solution[i][j] = envoi
            reste -= envoi
    return solution

def recherche_taboue():
    solution_actuelle = solution_initiale()
    meilleure_solution = copy.deepcopy(solution_actuelle)
    liste_taboue = []
    for _ in range(50):
        meilleur_voisin, meilleur_cout, meilleur_mouvement = None, float('inf'), None
        for i1 in range(2):
            for j1 in range(3):
                if solution_actuelle[i1][j1] > 0:
                    for i2 in range(2):
                        for j2 in range(3):
                            if (i1,j1) != (i2,j2):
                                voisin = copy.deepcopy(solution_actuelle)
                                voisin[i1][j1] -= 1
                                voisin[i2][j2] += 1
                                if any(sum(voisin[i]) > capacite[i] for i in range(2)) or any(sum(voisin[i][j] for i in range(2)) != demande[j] for j in range(3)):
                                    continue
                                c = cout_total(voisin)
                                mouvement = ((i1,j1),(i2,j2))
                                if (mouvement[1], mouvement[0]) not in liste_taboue or c < cout_total(meilleure_solution):
                                    if c < meilleur_cout:
                                        meilleur_voisin, meilleur_cout, meilleur_mouvement = voisin, c, mouvement
        if meilleur_voisin:
            solution_actuelle = meilleur_voisin
            liste_taboue.append((meilleur_mouvement[1], meilleur_mouvement[0]))
            if len(liste_taboue) > 5:
                liste_taboue.pop(0)
            if cout_total(solution_actuelle) < cout_total(meilleure_solution):
                meilleure_solution = copy.deepcopy(solution_actuelle)
    return meilleure_solution

solution = recherche_taboue()
print(solution)
print(cout_total(solution))