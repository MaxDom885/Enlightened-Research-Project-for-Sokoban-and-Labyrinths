# Enlightened Search Project for Sokoban and Mazes

This project aims to solve enlightened search problems using the A\* and modified Dijkstra algorithms. We apply these algorithms to solve the Sokoban problem and to find paths in mazes.

## Introduction

This project was carried out as part of the Artificial Intelligence course (LINGI2261). It focuses on solving enlightened search problems using the A\* and modified Dijkstra algorithms. We applied these algorithms to solve the Sokoban problem and to find paths in mazes.

## Installation

To run this project, you will need Python 3.x. You can install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Project Structure

The project is structured as follows:

```
sokoban-project/
│
├── sokoban.py # Implementation of the A* algorithm for Sokoban
├── test.py # Unit tests for Sokoban
├── map.py # Display of Sokoban maps
├── astar_dijkstra.py # Implementation of the A* and modified Dijkstra algorithms for mazes
├── test_mazes/ # Test files for mazes
│ ├── test01.xsb
│ ├── test02.xsb
│ └── ...
└── README.md # This file
```

## Usage

### Sokoban

To solve a Sokoban problem, run the file `sokoban.py` with the corresponding test file:

```bash
python sokoban.py test01.xsb
```

### Mazes

To run the A\* and modified Dijkstra algorithms on mazes, use the file `astar_dijkstra.py`:

```bash
python astar_dijkstra.py
```

## Implemented Algorithms

### Algorithm A\*

The A\* algorithm is used to solve the Sokoban problem and to find paths in mazes. It uses a Manhattan distance heuristic to guide the search.

### Modified Dijkstra Algorithm

The modified Dijkstra algorithm is used to find paths in mazes. It explores nodes based on the minimum cost and stops as soon as it reaches the target.

## Results and Analysis

### Sokoban

The unit test results for Sokoban are available in the `test.py` file. You can run the tests with the following command:

```bash
python -m unittest test.py
```

### Mazes

The results of the A\* and modified Dijkstra algorithms on mazes are displayed in the console. The positions explored by the algorithms are marked with asterisks (*).

## Authors

- ATTOH James
- BIAOU Marius
- HOUESSOU Kenny
- YACOUBOU Masmoud
