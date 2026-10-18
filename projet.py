# //////////////////////////////////////////////////*
# PROJET STRUCTURES DE DONNÉES - Projet fin Module
# ID-S2 / Rayane Jebari - Massine Benlahoucine ------
# //////////////////////////////////////////////////*


# Arbre
class Node:
    def _init_(self, val):
        self.val = val
        self.gauche = None
        self.droite = None


class ABR:
    def _init_(self):
        self.racine = None

    # insertion
    def inserer(self, val):
        if self.racine is None:
            self.racine = Node(val)
        else:
            self._inserer(self.racine, val)

    def _inserer(self, n, val):
        if val < n.val:
            if n.gauche is None:
                n.gauche = Node(val)
            else:
                self._inserer(n.gauche, val)
        else:
            if n.droite is None:
                n.droite = Node(val)
            else:
                self._inserer(n.droite, val)

    # rechercher la valeur (val)
    def rechercher(self, n, val):
        if n is None or n.val == val:
            return n
        if val < n.val:
            return self.rechercher(n.gauche, val)
        return self.rechercher(n.droite, val)

    # minimum 
    def _min_node(self, n):
        while n.gauche:
            n = n.gauche
        return n

    # suppression
    def supprimer(self, n, val):
        if n is None:
            return n

        if val < n.val:
            n.gauche = self.supprimer(n.gauche, val)
        elif val > n.val:
            n.droite = self.supprimer(n.droite, val)
        else:
            # cas 1 : feuille
            if n.gauche is None and n.droite is None:
                return None
            # cas 2 : un enfant
            if n.gauche is None:
                return n.droite
            if n.droite is None:
                return n.gauche
            # cas 3 : deux enfants
            temp = self._min_node(n.droite)
            n.val = temp.val
            n.droite = self.supprimer(n.droite, temp.val)

        return n

    # parcours
    # 1-parcours infixe
    def infixe(self, n):
        if n:
            self.infixe(n.gauche)
            print(n.val, end=" ")
            self.infixe(n.droite)
    # 2-parcours prefixe
    def prefixe(self, n):
        if n:
            print(n.val, end=" ")
            self.prefixe(n.gauche)
            self.prefixe(n.droite)
    # 3-parcours postfixe
    def postfixe(self, n):
        if n:
            self.postfixe(n.gauche)
            self.postfixe(n.droite)
            print(n.val, end=" ")
            
    # hauteur
    def hauteur(self, n):
        if n is None:
            return 0
        return 1 + max(self.hauteur(n.gauche), self.hauteur(n.droite))
    #nombre noeuds
    def nb_noeuds(self, n):
        if n is None:
            return 0
        return 1 + self.nb_noeuds(n.gauche) + self.nb_noeuds(n.droite)
    #nombre feuilles
    def nb_feuilles(self, n):
        if n is None:
            return 0
        if n.gauche is None and n.droite is None:
            return 1
        return self.nb_feuilles(n.gauche) + self.nb_feuilles(n.droite)
    #Minimum
    def minimum(self):
        n = self.racine
        while n.gauche:
            n = n.gauche
        return n.val
    #Maximum
    def maximum(self):
        n = self.racine
        while n.droite:
            n = n.droite
        return n.val



# *****
# GRAPHE
# *****

def ajouter_arete(G, a, b, w):
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    G[a].append((b, w))
    G[b].append((a, w))


def bfs(G, s):
    visites = []
    file = [s]

    while file:
        x = file.pop(0)
        if x not in visites:
            visites.append(x)
            for y, _ in G[x]:
                file.append(y)

    return visites


def dfs(G, s, visites=None):
    if visites is None:
        visites = []

    if s not in visites:
        visites.append(s)
        for y, _ in G[s]:
            dfs(G, y, visites)

    return visites


# Dijkstra avec chemin
def dijkstra(G, s):
    dist = {x: 9999 for x in G}
    prev = {x: None for x in G}

    dist[s] = 0
    visites = []

    while len(visites) < len(G):
        min_node = None
        for x in G:
            if x not in visites:
                if min_node is None or dist[x] < dist[min_node]:
                    min_node = x

        visites.append(min_node)

        for y, w in G[min_node]:
            if dist[min_node] + w < dist[y]:
                dist[y] = dist[min_node] + w
                prev[y] = min_node

    return dist, prev


def chemin(prev, debut, fin):
    path = []
    current = fin

    while current:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path


# -----------------
# KRUSKAL (ACM)
# -----------------

def kruskal(edges):
    edges.sort(key=lambda x: x[2])
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for u, v, _ in edges:
        parent[u] = u
        parent[v] = v

    mst = []
    total = 0

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            total += w

    return mst, total


# !!!!!!!!!!!!!!
# VISUALISATION
# !!!!!!!!!!!!!!

import networkx as nx
import matplotlib.pyplot as plt


def dessiner_graphe(edges, chemin=None, acm=None):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    if chemin:
        path_edges = list(zip(chemin, chemin[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)

    if acm:
        nx.draw_networkx_edges(G, pos, edgelist=acm, width=3)

    plt.show()


# //////***
# Essayer
# !!!!!!!!!!!

print("===== ARBRE =====")
arbre = ABR()

valeurs = [10, 5, 15, 3, 7, 12, 18]
for v in valeurs:
    arbre.inserer(v)

print("Infixe :")
arbre.infixe(arbre.racine)

print("\nRecherche 7 :", "Trouvé" if arbre.rechercher(arbre.racine, 7) else "Non trouvé")

# Tester la suppresion
arbre.racine = arbre.supprimer(arbre.racine, 5)
print("Après suppression de 5 :")
arbre.infixe(arbre.racine)

print("\nHauteur :", arbre.hauteur(arbre.racine))
print("Noeuds :", arbre.nb_noeuds(arbre.racine))
print("Feuilles :", arbre.nb_feuilles(arbre.racine))
print("Min :", arbre.minimum())
print("Max :", arbre.maximum())


print("\n===== GRAPHE =====")
G = {}

edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'D', 1),
    ('C', 'D', 3)
]

for a, b, w in edges:
    ajouter_arete(G, a, b, w)

print("BFS :", bfs(G, 'A'))
print("DFS :", dfs(G, 'A'))

dist, prev = dijkstra(G, 'A')
print("Distances :", dist)

p = chemin(prev, 'A', 'D')
print("Chemin A -> D :", p)

mst, cost = kruskal(edges)
print("ACM :", mst)
print("Coût total :", cost)

# Visualisation
dessiner_graphe(edges, chemin=p, acm=mst)
#@@@@@@@@@ 
# VISUALISATION
#@@@@@@@@@ 

import networkx as nx
import matplotlib.pyplot as plt


def dessiner_graphe(edges, chemin=None, acm=None, titre=""):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G)

    plt.figure()  
    plt.title(titre)

    # graphe de base
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500)

    # poids
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # chemin (rouge)
    if chemin:
        path_edges = list(zip(chemin, chemin[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

    # arbre couvrant minimal (vert)
    if acm:
        acm_edges = [(u, v) for u, v, w in acm]
        nx.draw_networkx_edges(G, pos, edgelist=acm_edges, edge_color='green', width=3)

    plt.show()


# /////////////
# TESTS
# ****

print("===== ARBRE =====")
arbre = ABR()

valeurs = [10, 5, 15, 3, 7, 12, 18]
for v in valeurs:
    arbre.inserer(v)

print("Infixe :")
arbre.infixe(arbre.racine)

print("\nRecherche 7 :", "Trouvé" if arbre.rechercher(arbre.racine, 7) else "Non trouvé")

# suppression test
arbre.racine = arbre.supprimer(arbre.racine, 5)
print("Après suppression de 5 :")
arbre.infixe(arbre.racine)

print("\nHauteur :", arbre.hauteur(arbre.racine))
print("Noeuds :", arbre.nb_noeuds(arbre.racine))
print("Feuilles :", arbre.nb_feuilles(arbre.racine))
print("Min :", arbre.minimum())
print("Max :", arbre.maximum())


print("\n===== GRAPHE =====")
G = {}

edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'D', 1),
    ('C', 'D', 3)
]

for a, b, w in edges:
    ajouter_arete(G, a, b, w)

print("BFS :", bfs(G, 'A'))
print("DFS :", dfs(G, 'A'))

dist, prev = dijkstra(G, 'A')
print("Distances :", dist)

p = chemin(prev, 'A', 'D')
print("Chemin A -> D :", p)

mst, cost = kruskal(edges)
print("ACM :", mst)
print("Coût total :", cost)



# 1️⃣ Graphe simple
dessiner_graphe(edges, titre="Graphe simple")

# 2️⃣ Plus court chemin (Dijkstra)
dessiner_graphe(edges, chemin=p, titre="Plus court chemin (Dijkstra)")

# 3️⃣ Arbre couvrant minimal (Kruskal)
dessiner_graphe(edges, acm=mst, titre="Arbre couvrant minimal (Kruskal)")
