import os

# Dossiers et fichiers à afficher dans le projet
INCLUDE_DIRS = ["src", "data", "screenshots"]
INCLUDE_FILES = [".gitignore", "README.md"]

def print_tree(root, prefix=""):
    items = sorted(os.listdir(root))
    
    # Séparer dossiers et fichiers
    dirs = [d for d in items if os.path.isdir(os.path.join(root, d)) and d in INCLUDE_DIRS]
    files = [f for f in items if os.path.isfile(os.path.join(root, f)) and f in INCLUDE_FILES]
    
    # Afficher fichiers à la racine
    for i, f in enumerate(files):
        connector = "└─ " if i == len(files) - 1 and not dirs else "├─ "
        print(prefix + connector + f)
    
    # Afficher dossiers
    for i, d in enumerate(dirs):
        connector = "└─ " if i == len(dirs) - 1 else "├─ "
        print(prefix + connector + d)
        
        # sous-fichiers dans le dossier
        sub_path = os.path.join(root, d)
        sub_items = sorted(os.listdir(sub_path))
        sub_files = [f for f in sub_items if os.path.isfile(os.path.join(sub_path, f))]
        
        for j, f in enumerate(sub_files):
            f_connector = "└─ " if j == len(sub_files) - 1 else "├─ "
            print(prefix + "   " + f_connector + f)
        
        # sous-dossiers récursifs
        sub_dirs = [sd for sd in sub_items if os.path.isdir(os.path.join(sub_path, sd))]
        if sub_dirs:
            print_tree(sub_path, prefix + "   ")

if __name__ == "__main__":
    print("03_Stockage_SQLite/")
    print_tree(".")
