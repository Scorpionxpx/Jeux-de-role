import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Nécessite d'installer Pillow : pip install pillow

# Données du bestiaire
bestiary = {
    "A": ["Les abobinables hommes des neiges", "Les araignées géantes", "Les automates"],
    "B": ["Les banshees", "les balrogs", "les barghests", "Les basilics", "le béhémoth", "les boggarts", "les bondins"],
    "C": ["Les cadavres", "Les capitans", "les cattis", "Les cauchemars", "les centaures", "Les chauve souris", "les chimères", "les chonchons", "les crascs", "les cyclopes"],
    "D": ["Les démons", "les Djinn", "Les Dullahan", "les duplicants", "Les dragons", "les dryades"],
    "E": ["Les ectoplasmes", "Les élémentaux", "Les elfes", "les ents"],
    "F": ["Les fantômes", "les farfadets", "les faunes", "les fongoïdes", "les fossoyeurs", "les furgolins"],
    "G": ["Les gargouilles", "Les géants des glace", "les génies des arbres", "Les gnomes", "Les gobelins", "les golems", "les goules", "les gorgones", "les gremlins", "les griffons"],
    "H": ["les harpies", "les hellions", "les hellrots", "les hippogriffes", "Les hobbits", "les Hobgobelins", "les hydres"],
    "I": ["itikar"],
    "K": ["les kappas", "le kraken"],
    "L": ["les lacodons", "les licornes", "Les loups", "les loup-garous", "les lutins"],
    "M": ["les manticores", "les minotaures", "Les momies", "les morts vivants"],
    "N": ["Les nains", "les nécrochores", "le Nuckelavee", "les nymphes"],
    "O": ["Les obsidiaques", "les ondines", "Les orcs", "Les ogres", "les onis"],
    "P": ["Les pazuzus", "le phénix"],
    "R": ["les rakshahs", "Les revenants"],
    "S": ["Les scorpions géants", "les selkies", "les sirènes", "les sorcières", "les spectres", "les sphinx", "les spriggans", "Les squelettes", "les stryges", "Les sufiriades"],
    "T": ["les tarasques", "Les têtes de mort", "les titans", "les tourmenteurs", "les triades", "les trolls"],
    "V": ["les vampires", "les vivernes", "les volcrates"],
    "Z": ["les zombies"]
}

# Fonction pour changer de page
def change_page(letter):
    monster_list.delete(0, tk.END)
    if letter in bestiary:
        for monster in bestiary[letter]:
            monster_list.insert(tk.END, monster)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Bestiaire")
root.geometry("900x600")  # Augmenter la taille pour plus d'espace

# Charger l'image en tant que fond
bg_image = Image.open("./livre.jpg")
bg_image = bg_image.resize((900, 600), Image.LANCZOS)  # Ajuster la taille
bg_photo = ImageTk.PhotoImage(bg_image)

# Créer un canevas pour afficher le fond
canvas = tk.Canvas(root, width=900, height=600)
canvas.pack(fill="both", expand=True)

# Afficher l'image de fond
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Titre
title_label = tk.Label(root, text="Bestiaire", font=("Arial", 30, "bold"), bg="#fdf5e6", fg="brown", relief="solid", bd=2)
title_window = canvas.create_window(450, 50, window=title_label)

# Liste des monstres
monster_list = tk.Listbox(root, font=("Arial", 14), width=40, height=15, bg="#fffbe0", fg="black", highlightthickness=0, bd=2, relief="solid")
list_window = canvas.create_window(450, 250, window=monster_list)

# Afficher les monstres de la première lettre par défaut
change_page("A")

# Cadre pour les marque-pages sur les côtés
bookmark_frame_left = tk.Frame(root, bg="#fdf5e6", padx=10, pady=10)
bookmark_frame_left.place(x=10, y=100)  # Placer à gauche

bookmark_frame_right = tk.Frame(root, bg="#fdf5e6", padx=10, pady=10)
bookmark_frame_right.place(x=800, y=100)  # Placer à droite

# Créer des boutons pour chaque lettre, disposés en deux colonnes
letters = sorted(bestiary.keys())
half = len(letters) // 2

for i, letter in enumerate(letters):
    button = ttk.Button(bookmark_frame_left, text=letter, command=lambda l=letter: change_page(l), width=5, padding=5)
    button.grid(row=i, column=0, padx=5, pady=5, sticky="w")

for i, letter in enumerate(letters[half:]):
    button = ttk.Button(bookmark_frame_right, text=letter, command=lambda l=letter: change_page(l), width=5, padding=5)
    button.grid(row=i, column=0, padx=5, pady=5, sticky="w")

# Lancer l'application
root.mainloop()
