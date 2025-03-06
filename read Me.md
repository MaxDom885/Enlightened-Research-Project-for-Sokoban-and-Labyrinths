
# Projet de Recherche Éclairée pour Sokoban et Labyrinthes

Ce projet vise à résoudre des problèmes de recherche éclairée en utilisant les algorithmes A\* et Dijkstra modifié. Nous appliquons ces algorithmes pour résoudre le problème de Sokoban et pour trouver des chemins dans des labyrinthes.


## Introduction

Ce projet a été réalisé dans le cadre du cours d'Intelligence Artificielle (LINGI2261). Il se concentre sur la résolution de problèmes de recherche éclairée en utilisant les algorithmes A\* et Dijkstra modifié. Nous avons appliqué ces algorithmes pour résoudre le problème de Sokoban et pour trouver des chemins dans des labyrinthes.

## Installation

Pour exécuter ce projet, vous aurez besoin de Python 3.x. Vous pouvez installer les dépendances nécessaires en utilisant `pip` :

```bash
pip install -r requirements.txt
```

## Structure du Projet

Le projet est structuré comme suit :

```
projet-sokoban/
│
├── sokoban.py           # Implémentation de l'algorithme A* pour Sokoban
├── test.py              # Tests unitaires pour Sokoban
├── carte.py             # Affichage des cartes de Sokoban
├── astar_dijkstra.py    # Implémentation des algorithmes A* et Dijkstra modifié pour les labyrinthes
├── test_labyrinthes/    # Fichiers de test pour les labyrinthes
│   ├── test01.xsb
│   ├── test02.xsb
│   └── ... 
└── README.md            # Ce fichier
```

## Utilisation

### Sokoban

Pour résoudre un problème de Sokoban, exécutez le fichier `sokoban.py` avec le fichier de test correspondant :

```bash
python sokoban.py test01.xsb
```

### Labyrinthes

Pour exécuter les algorithmes A\* et Dijkstra modifié sur les labyrinthes, utilisez le fichier `astar_dijkstra.py` :

```bash
python astar_dijkstra.py
```

## Algorithmes Implémentés

### Algorithme A\*

L'algorithme A\* est utilisé pour résoudre le problème de Sokoban et pour trouver des chemins dans les labyrinthes. Il utilise une heuristique de distance de Manhattan pour guider la recherche.

### Algorithme de Dijkstra Modifié

L'algorithme de Dijkstra modifié est utilisé pour trouver des chemins dans les labyrinthes. Il explore les nœuds en fonction du coût minimal et s'arrête dès qu'il atteint la cible.

## Résultats et Analyses

### Sokoban

Les résultats des tests unitaires pour Sokoban sont disponibles dans le fichier `test.py`. Vous pouvez exécuter les tests avec la commande suivante :

```bash
python -m unittest test.py
```

### Labyrinthes

Les résultats des algorithmes A\* et Dijkstra modifié sur les labyrinthes sont affichés dans la console. Les positions explorées par les algorithmes sont marquées par des astérisques (*).

## Auteurs

- ATTOH James
- BIAOU Marius
- HOUESSOU Kenny
- YACOUBOU Masmoud
