# tree_full_03.py
import os

# Dossiers à ignorer ou afficher sans détailler
IGNORE_DIRS = {".venv"}
INCLUDE_DIRS = {"src", "data", "screenshots", ".git", ".gitignore"}

def print_tree(root, prefix=""):
    # Lister tous les éléments
    try:
        items = sorted(os.listdir(root))
    except PermissionError:
        return

    # Séparer fichiers et dossiers
    files = [f for f in items if os.path.isfile(os.path.join(root, f))]
    dirs = [d for d in items if os.path.isdir(os.path.join(root, d))]

    # Afficher fichiers à ce niveau
    for i, f in enumerate(files):
        connector = "└─ " if i == len(files) - 1 and not dirs else "├─ "
        print(prefix + connector + f)

    # Afficher dossiers
    for i, d in enumerate(dirs):
        connector = "└─ " if i == len(dirs) - 1 else "├─ "
        print(prefix + connector + d)
        path = os.path.join(root, d)

        # Si dossier à ignorer, ne pas détailler
        if d in IGNORE_DIRS:
            continue

        # Sous-niveau
        new_prefix = prefix + ("   " if connector == "└─ " else "│  ")
        print_tree(path, new_prefix)

if __name__ == "__main__":
    print("03_Stockage_SQLite")
    print_tree(".")
