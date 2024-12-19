# Classe TypeAnimal
class TypeAnimal:
    def __init__(self, type_animal):
        self.__type_animal = type_animal  # "herbivore" ou "carnivore"

    def __str__(self):
        return self.__type_animal

# Classe Animal
class Animal:
    def __init__(self, nom, type_animal):
        self.__nom = nom
        self.__type_animal = type_animal  # Instance de TypeAnimal
        self.__habitats = []  # Liste d'habitats

    def ajouter_habitat(self, habitat):
        self.__habitats.append(habitat)

    def afficher_habitats(self):
        print(f"{self.__nom} vit dans les habitats suivants:")
        for habitat in self.__habitats:
            print(f"- {habitat.__type} : {habitat.__description}")

    def afficher_type(self):
        print(f"{self.__nom} est un animal de type {self.__type_animal}")

# Sous-classes Lapin et Mouton héritant d'Animal
class Lapin(Animal):
    def __init__(self, nom, couleur_pelage):
        # "herbivore" est une instance de TypeAnimal
        super().__init__(nom, TypeAnimal("Herbivore"))
        self.__couleur_pelage = couleur_pelage

    def creuser_terrier(self):
        print(f"{self.__nom} creuse un terrier.")

class Mouton(Animal):
    def __init__(self, nom, longueur_laide):
        # "herbivore" est une instance de TypeAnimal
        super().__init__(nom, TypeAnimal("Herbivore"))
        self.__longueur_laide = longueur_laide

    def produire_laine(self):
        print(f"{self.__nom} produit de la laine.")



    

# Création d'exemples
habitat = Habitat("Forêt", "Un espace verdoyant")
lapin = Lapin("Léo", "Blanc")
lapin.ajouter_habitat(habitat)

# Affichage d'une action
lapin.manger()
lapin.creuser_terrier()
lapin.afficher_habitats()
lapin.afficher_type()  # Affiche le type d'animal
