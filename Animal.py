# Classe Habitat
class Habitat:
    def __init__(self, type, description):
        self.type = type
        self.description = description

# Classe TypeAnimal
class TypeAnimal:
    def __init__(self, herbivore, carnivore):
        self.herbivore = herbivore
        self.carnivore = carnivore

# Classe Membre
class Membre:
    def __init__(self, type_membre, longueur):
        self.type = type_membre
        self.longueur = longueur

# Classe Animal
class Animal:
    def __init__(self, nom, type_animal, habitat):
        self.nom = nom
        self.type_animal = type_animal
        self.habitat = habitat
        self.membres = []  # Liste de membres de l'animal

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def manger(self):
        print(f"{self.nom} mange.")

    def deplacer(self):
        print(f"{self.nom} se déplace.")

# Sous-classes Lapin et Mouton héritant d'Animal
class Lapin(Animal):
    def __init__(self, nom, couleur_pelage):
        super().__init__(nom, "Herbivore", None)  # Par défaut, type "Herbivore"
        self.couleur_pelage = couleur_pelage

    def creuser_terrier(self):
        print(f"{self.nom} creuse un terrier.")

class Mouton(Animal):
    def __init__(self, nom, longueur_laide):
        super().__init__(nom, "Herbivore", None)  # Par défaut, type "Herbivore"
        self.longueur_laide = longueur_laide

    def produire_laine(self):
        print(f"{self.nom} produit de la laine.")

# Création d'exemples
habitat = Habitat("Forêt", "Un espace verdoyant")
lapin = Lapin("Léo", "Blanc")
lapin.ajouter_membre(Membre("Pattes", 20))

# Affichage d'une action
lapin.manger()
lapin.creuser_terrier()