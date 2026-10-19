import random
import math

distances = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17, (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13
}

cost = {}
for (a, b), d in distances.items():
    cost[a, b] = d
    cost[b, a] = d

initial = [1, 2, 3, 4, 5, 6, 7, 8]

def distance(tour):
    total = 0
    for i in range(len(tour)):
        a = tour[i]
        b = tour[(i + 1) % len(tour)]
        if (a, b) not in cost:
            return float("inf")
        total += cost[a, b]
    return total

def voisins(tour):
    result = []
    for i in range(1, 7):
        for j in range(i + 1, 8):
            v = tour.copy()
            v[i], v[j] = v[j], v[i]
            if distance(v) != float("inf"):
                result.append(v)
    return result

def recherche_taboue():
    actuelle = initial.copy()
    meilleure = actuelle.copy()
    taboue = []
    for _ in range(100):
        candidats = voisins(actuelle)
        if not candidats:
            break
        candidats.sort(key=distance)
        choisi = None
        for v in candidats:
            if v not in taboue or distance(v) < distance(meilleure):
                choisi = v
                break
        if choisi is None:
            break
        actuelle = choisi
        if distance(actuelle) < distance(meilleure):
            meilleure = actuelle.copy()
        taboue.append(actuelle)
        if len(taboue) > 5:
            taboue.pop(0)
    return meilleure

def recuit_simule():
    actuelle = initial.copy()
    meilleure = actuelle.copy()
    for T in [20, 15, 10, 5, 2]:
        candidats = voisins(actuelle)
        if not candidats:
            break
        v = random.choice(candidats)
        delta = distance(v) - distance(actuelle)
        if delta < 0 or random.random() < math.exp(-delta / T):
            actuelle = v
        if distance(actuelle) < distance(meilleure):
            meilleure = actuelle.copy()
    return meilleure

print(recherche_taboue(), distance(recherche_taboue()))
print(recuit_simule(), distance(recuit_simule()))