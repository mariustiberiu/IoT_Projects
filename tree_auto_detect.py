import os

# Dossiers/fichiers à ignorer
EXCLUDE_DIRS = {".venv", "__pycache__", ".git", ".idea", ".vscode", "node_modules", "objects", "cleanup_backup_20251001_194936"}
EXCLUDE_FILES = {".pyc"}  # fichiers à ignorer

def print_tree(root, prefix=""):
    try:
        items = sorted(os.listdir(root))
    except PermissionError:
        return  # on ignore si pas d’accès

    # Filtrage
    items = [i for i in items if i not in EXCLUDE_DIRS and i not in EXCLUDE_FILES]

    for idx, name in enumerate(items):
        path = os.path.join(root, name)
        connector = "└─ " if idx == len(items) - 1 else "├─ "
        print(prefix + connector + name)

        if os.path.isdir(path):
            # Sous-niveau
            subprefix = prefix + ("   " if idx == len(items) - 1 else "│  ")
            print_tree(path, prefix=subprefix)

if __name__ == "__main__":
    project_name = os.path.basename(os.getcwd()) + "/"
    print(project_name)
    print_tree(".")
