def read_file(filename):
    # Lit un fichier contenant une carte Sokoban et retourne une liste de listes représentant la carte
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]

def print_map(map):
    # Affiche la carte Sokoban ligne par ligne
    for row in map:
        print(''.join(row))

def main():
    # Boucle sur les fichiers de test "test01.xsb" à "test20.xsb"
    for i in range(1, 21):
        filename = f'test{i:02d}.xsb'
        print(f"Carte provenant de {filename} :")  # Modification en français
        initial_map = read_file(filename)
        print_map(initial_map)
        print()  # Ajoute une ligne vide après chaque carte

if __name__ == "__main__":
    # Point d'entrée principal du programme
    main()
