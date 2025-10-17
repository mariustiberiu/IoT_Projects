# tree_pro_04.py
import os

# Dossiers à inclure et afficher
INCLUDE_DIRS = {"src", "data", "screenshots", ".venv"}

def print_tree(root, prefix=""):
    # Lister dossiers
    items = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    items = sorted(items, key=lambda x: (x not in INCLUDE_DIRS, x))  # dossiers inclus d'abord
    # Lister fichiers
    files_root = sorted([f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))])

    # Afficher fichiers à la racine
    for f in files_root:
        print(prefix + "├─ " + f)

    # Afficher dossiers et contenu (sauf .venv)
    for i, name in enumerate(items):
        path = os.path.join(root, name)
        connector = "└─ " if i == len(items) - 1 else "├─ "
        print(prefix + connector + name)

        # Si dossier .venv, ne pas détailler son contenu
        if name == ".venv":
            continue

        # Sous-fichiers
        subitems = sorted(os.listdir(path))
        for j, f in enumerate(subitems):
            sub_connector = "└─ " if j == len(subitems) - 1 else "├─ "
            print(prefix + "   " + sub_connector + f)

if __name__ == "__main__":
    print("03_Stockage_SQLite/")
    print_tree(".")
