# tree_simple_04.py
import os

# Dossiers à inclure
INCLUDE_DIRS = {"src", "data", "screenshots"}

def print_tree(root, prefix=""):
    items = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    items = [d for d in items if d in INCLUDE_DIRS]  # garder seulement ceux qu'on veut

    # Affichage des fichiers à la racine
    files_root = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    for f in sorted(files_root):
        print(prefix + "├─ " + f)

    for i, name in enumerate(sorted(items)):
        path = os.path.join(root, name)
        connector = "└─ " if i == len(items) - 1 else "├─ "
        print(prefix + connector + name)
        # sous-niveaux : fichiers dans le dossier
        subitems = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for j, f in enumerate(sorted(subitems)):
            sub_connector = "└─ " if j == len(subitems) - 1 else "├─ "
            print(prefix + "   " + sub_connector + f)

if __name__ == "__main__":
    print("04_ExportCSV_Visualisation/")
    print_tree(".")
