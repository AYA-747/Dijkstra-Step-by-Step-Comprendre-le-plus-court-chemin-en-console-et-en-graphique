from donnees import INF
from affichage import afficher_etape

def dijkstra(n, matrice, depart):
    dist = [INF] * n
    pred = [None] * n
    visites = [False] * n
    etapes = []  

    dist[depart] = 0

    for _ in range(n):
        u = -1
        min_val = INF

        for i in range(n):
            if not visites[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i

        if u == -1:
            break

        afficher_etape(n, dist, pred, visites, sommet_actuel=u)
        input("\nAppuyez sur Entrée pour l'étape suivante...")

        visites[u] = True
        etapes.append(u)  

        for v in range(n):
            poids = matrice[u][v]
            if poids != INF and not visites[v]:
                new_dist = dist[u] + poids
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    pred[v] = u

    afficher_etape(n, dist, pred, visites)
    print("Algorithme terminé.")

    return dist, pred, etapes   