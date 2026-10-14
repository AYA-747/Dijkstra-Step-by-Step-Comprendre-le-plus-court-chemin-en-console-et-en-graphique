import networkx as nx
import matplotlib.pyplot as plt

def visualiser_dijkstra(n, matrice, depart, arrivee, dist, pred, etapes):


    G = nx.Graph()

    for i in range(n):
        for j in range(i, n):   
            if matrice[i][j] != float('inf') and i != j:
                G.add_edge(i, j, weight=matrice[i][j])

    pos = nx.spring_layout(G, seed=42)

    plt.ion()
    fig, ax = plt.subplots(figsize=(8,6))

    sommets_traites = []

    for u in etapes:

        sommets_traites.append(u)

        node_colors = []
        for node in G.nodes():
            if node == u:
                node_colors.append("blue")      
            elif node in sommets_traites:
                node_colors.append("gray")     
            else:
                node_colors.append("lightgray")

        ax.clear()
        nx.draw(G, pos, with_labels=True,
                node_color=node_colors,
                node_size=900,
                font_color="white",
                edge_color="black",
                width=2,
                ax=ax)

        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=nx.get_edge_attributes(G, 'weight'),
            ax=ax
        )

        ax.set_title(f"Traitement du sommet {u}")
        plt.pause(5)

    chemin = []
    if dist[arrivee] != float('inf'):
        curr = arrivee
        while curr is not None:
            chemin.append(curr)
            curr = pred[curr]
        chemin.reverse()

    node_colors = ["green" if node in chemin else "lightgray"
                   for node in G.nodes()]

    edge_colors = []
    widths = []

    for (a, b) in G.edges():
        if b in chemin and pred[b] == a:
            edge_colors.append("green")
            widths.append(5)
        elif a in chemin and pred[a] == b:
            edge_colors.append("green")
            widths.append(5)
        else:
            edge_colors.append("black")
            widths.append(2)

    ax.clear()
    nx.draw(G, pos, with_labels=True,
            node_color=node_colors,
            node_size=900,
            font_color="white",
            edge_color=edge_colors,
            width=widths,
            ax=ax)

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=nx.get_edge_attributes(G, 'weight'),
        ax=ax
    )

    ax.set_title("Chemin le plus court")
    plt.ioff()
    plt.show()