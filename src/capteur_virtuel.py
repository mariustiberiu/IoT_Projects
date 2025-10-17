import os

def rename_screenshots(base_dir):
    """
    Parcours tous les sous-dossiers et renomme les screenshots
    pour qu'ils aient un nom cohérent : screenshot_{chapter}_{sub}_{num}.png
    """
    for chapter in os.listdir(base_dir):
        chapter_path = os.path.join(base_dir, chapter)
        if not os.path.isdir(chapter_path):
            continue

        for sub in os.listdir(chapter_path):
            sub_path = os.path.join(chapter_path, sub)
            if not os.path.isdir(sub_path):
                continue

            screenshots_path = os.path.join(sub_path, "screenshots")
            if not os.path.exists(screenshots_path):
                continue

            count = 1
            for file in os.listdir(screenshots_path):
                old_file = os.path.join(screenshots_path, file)
                if os.path.isfile(old_file) and file.lower().endswith((".png", ".jpg", ".jpeg")):
                    new_file_name = f"screenshot_{chapter}_{sub}_{count:02d}.png"
                    new_file = os.path.join(screenshots_path, new_file_name)
                    os.rename(old_file, new_file)
                    count += 1
                    print(f"✅ Renommé: {file} -> {new_file_name}")

    print("✅ Tous les screenshots ont été renommés avec succès.")

if __name__ == "__main__":
    base_dir = os.getcwd()  # ou chemin vers ton dossier principal
    rename_screenshots(base_dir)
