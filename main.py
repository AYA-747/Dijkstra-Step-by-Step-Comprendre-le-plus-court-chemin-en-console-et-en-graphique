import os
import time
from donnees import charger_graphe, INF
from algorithme import dijkstra
from affichage import Couleurs
from visualisation_graphique import visualiser_dijkstra

def reconstruire_chemin(pred, depart, arrivee):
    chemin = []
    curr = arrivee

    if pred[arrivee] is None and arrivee != depart:
        return []

    while curr is not None:
        chemin.append(curr)
        if curr == depart:
            break
        curr = pred[curr]

    chemin.reverse()
    return chemin

if __name__ == "__main__":

    dossier_script = os.path.dirname(os.path.abspath(__file__))
    chemin_complet = os.path.join(dossier_script, "graphe.txt")

    n, matrice = charger_graphe(chemin_complet)

    if not n:
        exit()

    print(f"Graphe chargé ({n} sommets).")

    try:
        depart = int(input(f"Sommet de départ (0-{n-1}) : "))
        arrivee = int(input(f"Sommet d'arrivée (0-{n-1}) : "))

        dist, pred, etapes = dijkstra(n, matrice, depart)

        print(f"\n{Couleurs.CYAN}--- RÉSULTATS ---{Couleurs.RESET}")

        if dist[arrivee] == INF:
            print(f"{Couleurs.ROUGE}Aucun chemin entre {depart} et {arrivee}.{Couleurs.RESET}")
        else:
            chemin = reconstruire_chemin(pred, depart, arrivee)
            chemin_str = " -> ".join(map(str, chemin))

            print(f"Chemin le plus court : {Couleurs.VERT}{chemin_str}{Couleurs.RESET}")
            print(f"Coût total : {Couleurs.VERT}{dist[arrivee]}{Couleurs.RESET}")

        print("\nVisualisation graphique dans 5 secondes...")
        time.sleep(5)

        visualiser_dijkstra(n, matrice, depart, arrivee, dist, pred, etapes)

    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")