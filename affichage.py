import os

class Couleurs:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    ROUGE = "\033[91m"
    VERT = "\033[92m"
    JAUNE = "\033[93m"
    BLEU = "\033[94m"
    CYAN = "\033[96m"
    GRIS = "\033[90m"

def nettoyer_ecran():
    """Efface la console pour faire une animation fluide"""
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_etape(n, dist, pred, visites, sommet_actuel=None):
    """Affichage High-Tech avec couleurs et cadres"""
    nettoyer_ecran()
    

    print(f"{Couleurs.CYAN}╔══════════════════════════════════════════════════════╗{Couleurs.RESET}")
    if sommet_actuel is not None:
        titre = f"TRAITEMENT DU SOMMET : {sommet_actuel}"
        print(f"{Couleurs.CYAN}║{Couleurs.JAUNE} {titre:^52} {Couleurs.CYAN}║{Couleurs.RESET}")
    else:
        print(f"{Couleurs.CYAN}║{Couleurs.VERT}              ALGORITHME TERMINÉ                    {Couleurs.CYAN}║{Couleurs.RESET}")
    print(f"{Couleurs.CYAN}╚══════════════════════════════════════════════════════╝{Couleurs.RESET}")
    print("")


    top_border = "┌────────┬" + ("──────┬" * n)
    top_border = top_border[:-1] + "┐"
    print(f"{Couleurs.GRIS}{top_border}{Couleurs.RESET}")
    

    header = "│ SOMMET │"
    for i in range(n):
        if i == sommet_actuel:
            header += f"{Couleurs.JAUNE}{Couleurs.BOLD}  {i}   {Couleurs.RESET}{Couleurs.GRIS}│{Couleurs.RESET}"
        else:
            header += f"  {i}   {Couleurs.GRIS}│{Couleurs.RESET}"
    print(header)
    
    mid_border = "├────────┼" + ("──────┼" * n)
    mid_border = mid_border[:-1] + "┤"
    print(f"{Couleurs.GRIS}{mid_border}{Couleurs.RESET}")


    ligne_dist = f"│ {Couleurs.BOLD}DIST{Couleurs.RESET}   {Couleurs.GRIS}│{Couleurs.RESET}"
    for d in dist:
        if d == float('inf'):
            valeur = "INF"
            c = Couleurs.ROUGE
        else:
            valeur = str(d)
            c = Couleurs.CYAN
        ligne_dist += f"{c}{valeur:^6}{Couleurs.RESET}{Couleurs.GRIS}│{Couleurs.RESET}"
    print(ligne_dist)

    ligne_pred = f"│ {Couleurs.BOLD}PRED{Couleurs.RESET}   {Couleurs.GRIS}│{Couleurs.RESET}"
    for p in pred:
        valeur = "-" if p is None else str(p)
        ligne_pred += f"{Couleurs.BLEU}{valeur:^6}{Couleurs.RESET}{Couleurs.GRIS}│{Couleurs.RESET}"
    print(ligne_pred)


    print(f"{Couleurs.GRIS}{mid_border}{Couleurs.RESET}")
    ligne_etat = f"│ {Couleurs.BOLD}ETAT{Couleurs.RESET}   {Couleurs.GRIS}│{Couleurs.RESET}"
    for i in range(n):
        if visites[i]:
            etat = "OK"
            c = Couleurs.VERT
        elif i == sommet_actuel:
            etat = "<<"
            c = Couleurs.JAUNE
        else:
            etat = "."
            c = Couleurs.GRIS
        ligne_etat += f"{c}{etat:^6}{Couleurs.RESET}{Couleurs.GRIS}│{Couleurs.RESET}"
    print(ligne_etat)

    bot_border = "└────────┴" + ("──────┴" * n)
    bot_border = bot_border[:-1] + "┘"
    print(f"{Couleurs.GRIS}{bot_border}{Couleurs.RESET}")
    
    print("\nLégende : " + f"{Couleurs.VERT}OK{Couleurs.RESET} = Visité, " + 
          f"{Couleurs.JAUNE}<<{Couleurs.RESET} = En cours, " + 
          f"{Couleurs.ROUGE}INF{Couleurs.RESET} = Inaccessible")
    
    
        