# Importation des modules nécessaires
import sys
from search import Problem, astar_search, breadth_first_graph_search

# Définition de la classe du problème Sokoban
class SokobanProblem(Problem):
    def __init__(self, initial):
        # Initialisation avec l'état initial du jeu
        super().__init__(self.state_to_string(initial))
        self.initial_state = initial
        self.goal = self.generate_goal(initial)

    def actions(self, state):
        # Détermine les actions possibles à partir d'un état donné
        state = self.string_to_state(state)
        actions = []
        player_pos = self.find_player(state)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Droite, Bas, Haut, Gauche
        for direction in directions:
            new_pos = (player_pos[0] + direction[0], player_pos[1] + direction[1])
            if self.is_valid_move(state, player_pos, new_pos):
                actions.append(direction)
        print(f"Actions disponibles pour cet état : {actions}")  # Modification en français
        return actions

    def result(self, state, action):
        # Applique une action à l'état courant et retourne le nouvel état
        state = self.string_to_state(state)
        new_state = [row[:] for row in state]
        player_pos = self.find_player(new_state)
        new_pos = (player_pos[0] + action[0], player_pos[1] + action[1])
        new_state[player_pos[0]][player_pos[1]] = ' '
        new_state[new_pos[0]][new_pos[1]] = '@'
        if new_state[new_pos[0]][new_pos[1]] == '$':
            new_state[new_pos[0] + action[0]][new_pos[1] + action[1]] = '$'
        result_state = self.state_to_string(new_state)
        print(f"Nouvel état après l'action {action} : {result_state}")  # Modification en français
        return result_state

    def goal_test(self, state):
        # Vérifie si l'état courant atteint l'objectif
        state = self.string_to_state(state)
        goal_state = self.string_to_state(self.state_to_string(self.goal))
        print(f"Test de l'objectif : {self.find_boxes_and_targets(state) == self.find_boxes_and_targets(goal_state)}")  # Modification en français
        return self.find_boxes_and_targets(state) == self.find_boxes_and_targets(goal_state)

    def h(self, node):
        # Fonction heuristique pour l'A* basée sur la distance de Manhattan
        state = self.string_to_state(node.state)
        boxes, targets = self.find_boxes_and_targets(state)
        heuristic_value = sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in zip(boxes, targets))
        print(f"Valeur heuristique : {heuristic_value}")  # Modification en français
        return heuristic_value

    def find_player(self, state):
        # Trouve la position du joueur (@) dans l'état
        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                if cell == '@':
                    return (i, j)
        return None

    def find_boxes_and_targets(self, state):
        # Identifie les positions des boîtes ($) et des cibles (.)
        boxes = []
        targets = []
        for i, row in enumerate(state):
            for j, cell in enumerate(row):
                if cell == '$':
                    boxes.append((i, j))
                elif cell == '.':
                    targets.append((i, j))
        return sorted(boxes[:len(targets)]), sorted(targets[:len(boxes)])

    def is_valid_move(self, state, player_pos, new_pos):
        # Vérifie si un déplacement est valide
        if new_pos[0] < 0 or new_pos[0] >= len(state) or new_pos[1] < 0 or new_pos[1] >= len(state[0]):
            return False
        if state[new_pos[0]][new_pos[1]] == '#':
            return False
        if state[new_pos[0]][new_pos[1]] == '$':
            push_pos = (new_pos[0] + new_pos[0] - player_pos[0], new_pos[1] + new_pos[1] - player_pos[1])
            if push_pos[0] < 0 or push_pos[0] >= len(state) or push_pos[1] < 0 or push_pos[1] >= len(state[0]):
                return False
            if state[push_pos[0]][push_pos[1]] == '#' or state[push_pos[0]][push_pos[1]] == '$':
                return False
        return True

    def generate_goal(self, initial):
        # Génère l'état objectif basé sur l'état initial
        goal = [row[:] for row in initial]
        for i, row in enumerate(goal):
            for j, cell in enumerate(row):
                if cell == '$':
                    goal[i][j] = '.'
        return goal

    def state_to_string(self, state):
        # Convertit un état en chaîne de caractères
        return '\n'.join(''.join(row) for row in state)

    def string_to_state(self, string):
        # Convertit une chaîne de caractères en état
        return [list(line) for line in string.split('\n')]

def read_file(filename):
    # Lit un fichier et retourne l'état initial du jeu
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]

def main(argv):
    # Fonction principale pour lire l'état initial et résoudre le problème
    initial_state = read_file(argv[1])
    problem = SokobanProblem(initial_state)
    solution = astar_search(problem)
    if solution:
        for action in solution.solution():
            print(action)  # Affichage en français déjà implémenté
    else:
        print("Aucune solution trouvée !")  # Modification en français

if __name__ == "__main__":
    main(sys.argv)
