# cleanup_generated.py
import os, shutil, datetime

BASE = os.getcwd()
now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(BASE, f"cleanup_backup_{now}")

# Règles heuristiques : fichiers root suspects et dossiers créés automatiquement
root_file_patterns = [
    "script_centralise", "script_template", "script_centralise_generer_auto",
    "script_centralise_v", "script_centralise full", "script_centralise_full_auto",
    "tree_auto_detect", "tree_full", "tree_pro", "tree_simple", "generate_"
]

candidate_paths = []

# 1) fichiers à la racine correspondant aux patterns
for name in sorted(os.listdir(BASE)):
    path = os.path.join(BASE, name)
    if os.path.isfile(path):
        low = name.lower()
        if any(p in low for p in root_file_patterns):
            candidate_paths.append(path)

# 2) dossiers duplicates/ostensiblement créés automatiquement (ex : Ch6_Cloud_Edge_Computing)
for name in sorted(os.listdir(BASE)):
    path = os.path.join(BASE, name)
    if os.path.isdir(path):
        if name.lower().endswith("_computing") or name.lower().startswith("ch6_cloud_edge_computing"):
            candidate_paths.append(path)

# 3) détecter dossiers qui contiennent des fichiers 'sample.csv', 'sample.json', 'main.py' créés en masse
for root, dirs, files in os.walk(BASE):
    # n'explorer que deux niveaux pour éviter /venv
    rel = os.path.relpath(root, BASE)
    if rel.startswith(".venv") or rel.startswith(".git"):
        continue
    for fname in files:
        if fname.lower() in ("sample.csv", "sample.json", "main.py"):
            # proposer le dossier parent comme candidat (évite listing fichier à fichier)
            candidate_paths.append(root)
            break

# déduplication et tri
candidate_paths = sorted(set(candidate_paths))

if not candidate_paths:
    print("✅ Aucun élément suspect détecté par les règles automatiques. Rien à faire.")
    raise SystemExit(0)

print("⚠️ Éléments identifiés comme générés/à vérifier :\n")
for i, p in enumerate(candidate_paths, 1):
    print(f"{i:3d}. {p}")

print("\nOptions :")
print("  1) Déplacer TOUS les éléments ci-dessus vers un dossier de backup (recommandé)")
print("  2) Supprimer TOUS les éléments ci-dessus (IRRÉVERSIBLE)")
print("  3) Annuler (ne rien faire)")

choice = input("\nQue veux-tu faire ? (1=déplacer / 2=supprimer / 3=annuler) : ").strip()

if choice == "3" or choice == "":
    print("✋ Annulé par l'utilisateur. Aucune modification faite.")
    raise SystemExit(0)

if choice == "1":
    os.makedirs(backup_folder, exist_ok=True)
    for p in candidate_paths:
        name = os.path.basename(p.rstrip(os.sep))
        dst = os.path.join(backup_folder, name)
        # si dst existe, ajouter suffixe
        if os.path.exists(dst):
            dst = dst + "_" + now
        print(f"Déplacement : {p} -> {dst}")
        shutil.move(p, dst)
    print(f"\n✅ Déplacé dans : {backup_folder}")
elif choice == "2":
    confirm = input("CONFIRME suppression permanente de tous ces éléments ? tape 'OUI' pour confirmer : ")
    if confirm == "OUI":
        for p in candidate_paths:
            if os.path.isfile(p):
                os.remove(p); print(f"Supprimé fichier: {p}")
            else:
                shutil.rmtree(p); print(f"Supprimé dossier: {p}")
        print("\n✅ Suppressions effectuées.")
    else:
        print("Annulé (confirmation manquante). Aucune suppression faite.")
else:
    print("Option non reconnue. Annulé.")
