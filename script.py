import os

# Données du bestiaire
bestiary = {
    "A": ["Les abobinables hommes des neiges", "Les araignées géantes", "Les automates"],
    "B": ["Les banshees", "les balrogs", "les barghests", "Les basilics", "le béhémoth", "les boggarts", "les bondins"],
    "C": ["Les cadavres", "Les capitans", "les cattis", "Les cauchemars", "Les centaures", "Les chauve souris", "Les chimères", "Les chonchons", "Les crascs", "Les cyclopes"],
    "D": ["Les démons", "les Djinn", "les Dullahan", "les duplicants", "Les dragons", "les dryades"],
    "E": ["Les ectoplasmes", "Les élémentaux", "Les elfes", "les ents"],
    "F": ["Les fantômes", "les farfadets", "les faunes", "les fongoïdes", "les fossoyeurs", "les furgolins"],
    "G": ["Les gargouilles", "Les géants des glace", "les génies des arbres", "Les gnomes", "Les gobelins", "les golems", "les goules", "les gorgones", "les gremlins", "les griffons"],
    "H": ["les harpies", "les hellions", "les hellrots", "les hippogriffes", "Les hobbits", "les Hobgobelins", "les hydres"],
    "I": ["itikar"],
    "K": ["les kappas", "le kraken"],
    "L": ["les lacodons", "les licornes", "Les loups", "les loup-garous", "les lutins"],
    "M": ["les manticores", "les minotaures", "Les momies", "les morts vivants"],
    "N": ["Les nains", "les nécrochores", "le Nuckelavee", "les nymphes"],
    "O": ["Les obsidiaques", "les ondines", "les orcs", "les ogres", "les onis"],
    "P": ["Les pazuzus", "le phénix"],
    "R": ["les rakshahs", "Les revenants"],
    "S": ["Les scorpions géants", "les selkies", "les sirènes", "les sorcières", "les spectres", "les sphinx", "les spriggans", "Les squelettes", "les stryges", "Les sufiriades"],
    "T": ["les tarasques", "Les têtes de mort", "les titans", "les tourmenteurs", "les triades", "les trolls"],
    "V": ["les vampires", "les vivernes", "les volcrates"],
    "Z": ["les zombies"]
}

# Dossier pour sauvegarder les fichiers HTML
output_dir = "monsters_html"
os.makedirs(output_dir, exist_ok=True)

# Fonction pour créer un fichier HTML pour chaque monstre
def create_monster_html(monster_name):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{monster_name}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0e8d0;
                color: #4b3f26;
                margin: 0;
                padding: 0;
                text-align: center;
            }}
            .container {{
                margin-top: 50px;
                padding: 20px;
                background-color: #fffbe0;
                border-radius: 10px;
                width: 80%;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }}
            h1 {{
                font-size: 2rem;
                color: #8b5a2b;
            }}
            p {{
                font-size: 1.2rem;
            }}
            .back-link {{
                margin-top: 20px;
                display: inline-block;
                font-size: 1rem;
                color: #8b5a2b;
                text-decoration: none;
                padding: 10px;
                background-color: #f5e1c2;
                border-radius: 5px;
                margin-top: 20px;
            }}
            .back-link:hover {{
                background-color: #d6b28f;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{monster_name}</h1>
            <p>Voici un monstre très intéressant, qui peut avoir des pouvoirs étonnants et des caractéristiques surprenantes.</p>
            <a href="../index.html" class="back-link">Retour à la liste des monstres</a>
        </div>
    </body>
    </html>
    """
    
    # Nom du fichier HTML
    filename = os.path.join(output_dir, f"{monster_name}.html")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)

# Fonction pour créer la page principale avec des liens vers chaque monstre
def create_main_page():
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bestiaire</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0e8d0;
                color: #4b3f26;
                margin: 0;
                padding: 0;
                text-align: center;
            }}
            .container {{
                margin-top: 50px;
                padding: 20px;
                background-color: #fffbe0;
                border-radius: 10px;
                width: 80%;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
            }}
            h1 {{
                font-size: 2.5rem;
                color: #8b5a2b;
            }}
            .monster-list {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
                gap: 20px;
                padding: 0;
                list-style-type: none;
            }}
            .monster-item {{
                background-color: #f5e1c2;
                border-radius: 10px;
                padding: 15px;
                text-align: center;
                font-size: 1.1rem;
                transition: background-color 0.3s ease;
            }}
            .monster-item a {{
                text-decoration: none;
                color: #4b3f26;
            }}
            .monster-item:hover {{
                background-color: #d6b28f;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bestiaire - Liste des Monstres</h1>
            <p>Explorez les monstres de notre bestiaire en cliquant sur leurs noms ci-dessous :</p>
            <ul class="monster-list">
    """
    
    # Ajouter un lien pour chaque monstre dans une "carte"
    for letter, monsters in bestiary.items():
        for monster in monsters:
            html_content += f'''
                <li class="monster-item">
                    <a href="{monster}.html">{monster}</a>
                </li>
            '''

    html_content += """
            </ul>
        </div>
    </body>
    </html>
    """
    
    # Créer le fichier index.html
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as file:
        file.write(html_content)

# Créer la page principale
create_main_page()

# Créer un fichier HTML pour chaque monstre
for letter, monsters in bestiary.items():
    for monster in monsters:
        create_monster_html(monster)

print("Fichiers HTML créés avec succès.")
