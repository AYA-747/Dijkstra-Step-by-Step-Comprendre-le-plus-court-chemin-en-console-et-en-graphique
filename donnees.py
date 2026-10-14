import os

INF = float('inf')

def charger_graphe(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            lignes = f.readlines()
        
        if not lignes:
            print("Erreur : Fichier vide.")
            return None, None
        
        n = int(lignes[0].strip())
        
        if n > 5:
            print(f"Erreur : Max 5 sommets autorisés (vous en avez {n}).")
            return None, None

        matrice = [[INF for _ in range(n)] for _ in range(n)]

        for i in range(n):
            matrice[i][i] = 0
            
        for ligne in lignes[1:]:
            parties = ligne.split()
            if len(parties) >= 3:
                depart = int(parties[0])
                arrivee = int(parties[1])
                poids = int(parties[2])

                if depart < n and arrivee < n:
                    matrice[depart][arrivee] = poids
                    matrice[arrivee][depart] = poids

        return n, matrice

    except FileNotFoundError:
        print(f"Erreur : Fichier '{nom_fichier}' introuvable.")
        return None, None
    except ValueError:
        print("Erreur : Format invalide dans le fichier.")
        return None, None