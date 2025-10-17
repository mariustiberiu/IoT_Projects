import os

# Liste des fichiers/dossiers à ignorer
IGNORER = {'.pyc', '__pycache__'}

# Dossiers spécifiques à exclure
EXCLUSIONS = {"Ch6_Cloud_Edge_Computing"}

# Dossiers spécifiques à s'assurer qu'ils apparaissent
INCLUSIONS_SPECIALES = ["Ch5_Securite_IoT/04"]

def afficher_arborescence(racine, prefix="", lignes=None, compteur=[1]):
    """Affiche l'arborescence avec numérotation, exclusions et inclusions spéciales."""
    if lignes is None:
        lignes = []

    try:
        contenus = os.listdir(racine)
    except PermissionError:
        lignes.append(f"{prefix}[Accès refusé] {racine}")
        return lignes

    fichiers = []
    dossiers = []

    for item in sorted(contenus):
        if item in EXCLUSIONS or item in IGNORER:
            continue
        chemin = os.path.join(racine, item)
        if os.path.isdir(chemin):
            dossiers.append(item)
        else:
            fichiers.append(item)

    for i, dossier in enumerate(dossiers):
        est_dernier = (i == len(dossiers) - 1) and not fichiers
        ligne = f"{prefix}{compteur[0]:02d} - {dossier}/"
        lignes.append(ligne)
        compteur[0] += 1
        nouveau_prefix = prefix + ("    " if est_dernier else "│   ")
        afficher_arborescence(os.path.join(racine, dossier), nouveau_prefix, lignes, compteur)

    for i, fichier in enumerate(fichiers):
        est_dernier = (i == len(fichiers) - 1)
        ligne = f"{prefix}{compteur[0]:02d} - {fichier}"
        lignes.append(ligne)
        compteur[0] += 1

    return lignes

def ajouter_inclusions_speciales(dossier_racine, lignes):
    """S'assure que les dossiers spécifiques sont présents dans l'arborescence."""
    for chemin_rel in INCLUSIONS_SPECIALES:
        chemin_abs = os.path.join(dossier_racine, *chemin_rel.split("/"))
        if os.path.exists(chemin_abs):
            lignes.append(f"** Inclusion spéciale : {chemin_rel} **")
    return lignes

if __name__ == "__main__":
    dossier_racine = input("Chemin du projet à analyser : ").strip()
    if os.path.exists(dossier_racine):
        lignes = afficher_arborescence(dossier_racine)
        lignes = ajouter_inclusions_speciales(dossier_racine, lignes)

        # Supprimer les doublons éventuels
        lignes_uniques = list(dict.fromkeys(lignes))

        # Affichage dans la console
        for ligne in lignes_uniques:
            print(ligne)

        # Export automatique vers un fichier TXT
        fichier_sortie = os.path.join(dossier_racine, "arborescence_projet_final.txt")
        with open(fichier_sortie, "w", encoding="utf-8") as f:
            for ligne in lignes_uniques:
                f.write(ligne + "\n")

        print(f"\n✅ Arborescence finale exportée dans : {fichier_sortie}")
    else:
        print("❌ Le chemin spécifié n'existe pas.")
