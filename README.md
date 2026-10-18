# Structures de données et graphes en Python

Projet de fin de module **Structures de données** réalisé en binôme au semestre 2 du DUT Ingénierie des données, à l'École Supérieure de Technologie de Dakhla (2026).

L'objectif était d'implémenter nous-mêmes, sans bibliothèque toute faite, deux structures fondamentales de l'informatique : l'**arbre binaire de recherche** et le **graphe pondéré**, puis d'y appliquer les algorithmes classiques de parcours, de plus court chemin et d'arbre couvrant minimal.

## Contenu

### Arbre binaire de recherche (ABR)

Classes `Node` et `ABR`, avec :

- insertion, recherche et suppression d'une valeur (y compris le cas d'un nœud à deux enfants, remplacé par le minimum de son sous-arbre droit) ;
- parcours infixe, préfixe et postfixe ;
- calcul de la hauteur, du nombre de nœuds et du nombre de feuilles ;
- recherche du minimum et du maximum.

### Graphe pondéré non orienté

Le graphe est représenté par une liste d'adjacence (un dictionnaire `sommet -> [(voisin, poids), ...]`).

| Algorithme | Fonction | Rôle |
|---|---|---|
| Parcours en largeur | `bfs(G, s)` | Visite les sommets niveau par niveau à partir de `s` |
| Parcours en profondeur | `dfs(G, s)` | Explore chaque branche jusqu'au bout avant de revenir en arrière |
| Dijkstra | `dijkstra(G, s)` + `chemin(prev, debut, fin)` | Calcule la distance minimale de `s` vers chaque sommet et reconstruit le chemin |
| Kruskal | `kruskal(edges)` | Construit l'arbre couvrant minimal, avec une structure Union-Find (compression de chemin) |

### Visualisation

La fonction `dessiner_graphe` affiche le graphe avec **NetworkX** et **Matplotlib** :

- le graphe simple avec le poids de chaque arête ;
- le plus court chemin trouvé par Dijkstra, en rouge ;
- l'arbre couvrant minimal trouvé par Kruskal, en vert.

## Installation et exécution

Le projet nécessite Python 3 et deux bibliothèques pour la partie visualisation.

```bash
pip install networkx matplotlib
python projet.py
```

Le script lance automatiquement les tests sur l'arbre et sur le graphe, affiche les résultats dans le terminal, puis ouvre les trois fenêtres de visualisation.

## Exemple

Graphe utilisé pour les tests :

```
A ──2── B
│       │
4       1
│       │
C ──3── D
```

Sortie obtenue :

```
===== ARBRE =====
Infixe :
3 5 7 10 12 15 18
Recherche 7 : Trouvé
Après suppression de 5 :
3 7 10 12 15 18
Hauteur : 3
Noeuds : 6
Feuilles : 3
Min : 3
Max : 18

===== GRAPHE =====
BFS : ['A', 'B', 'C', 'D']
DFS : ['A', 'B', 'D', 'C']
Distances : {'A': 0, 'B': 2, 'C': 4, 'D': 3}
Chemin A -> D : ['A', 'B', 'D']
ACM : [('B', 'D', 1), ('A', 'B', 2), ('C', 'D', 3)]
Coût total : 6
```

## Ce que ce projet nous a appris

- Manipuler la récursivité sur des structures chaînées (insertion, suppression, parcours d'arbre).
- Choisir une représentation adaptée pour un graphe et comprendre la différence entre un parcours en largeur et en profondeur.
- Passer d'un algorithme vu en cours (Dijkstra, Kruskal) à un code qui fonctionne, puis le vérifier visuellement.

## Auteurs

- **Rayane Jebari**
- **Massine Benlahoucine**

Étudiants en DUT Ingénierie des données, EST Dakhla.
