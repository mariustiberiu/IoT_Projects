import argparse
import matplotlib.pyplot as plt
from .export_csv import export_data

def main():
    print("=== Chapitre 4 : Export & Visualisation CSV ===")

    # Arguments CLI (facultatif)
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true", help="Utiliser des données simulées")
    parser.add_argument("--rows", type=int, default=20, help="Nombre de lignes à exporter")
    parser.add_argument("--output", type=str, default="../exports/data.csv", help="Chemin du fichier exporté")
    args = parser.parse_args()

    # Demander si simulation si pas d'option CLI
    simulate = args.simulate
    if not args.simulate:
        choix = input("Utiliser des données SIMULÉES ? (o/n) : ").strip().lower()
        simulate = (choix == "o")

    # Export CSV et récupération du DataFrame
    df = export_data(
        simulate=simulate,
        rows=args.rows,
        output_path=args.output
    )

    print(df.head())

    # Boucle interactive pour afficher le graphique
    while True:
        choix = input("Voulez-vous afficher le graphique ? (o/n) : ").strip().lower()
        if choix == "o":
            try:
                df["timestamp"] = df["timestamp"].astype(str)
                plt.figure(figsize=(10, 5))

                # Sélectionne toutes les colonnes numériques sauf l'id
                numeric_cols = df.select_dtypes(include="number").columns.tolist()
                numeric_cols = [col for col in numeric_cols if col != "id"]

                if numeric_cols:
                    for col in numeric_cols:
                        plt.plot(df["timestamp"], df[col], marker="o", label=col)
                else:
                    print("⚠ Aucune colonne numérique à tracer, affichage générique :")
                    print(df.head())
                    df.plot()

                plt.xticks(rotation=45, ha="right")
                plt.legend()
                plt.title("Évolution des données CSV")
                plt.tight_layout()
                plt.show()

            except Exception as e:
                print(f"❌ Impossible d'afficher le graphique : {e}")

        else:
            quitter = input("Voulez-vous quitter le programme ? (o/n) : ").strip().lower()
            if quitter == "o":
                print("👋 Fin du programme.")
                break
            # sinon on boucle et redemande

if __name__ == "__main__":
    main()







    
