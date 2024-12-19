# Classe Personne 
class Personne:
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

# Classe Professeur héritant de Personne
class Professeur(Personne):
    def __init__(self, nom, prenom, matiere_enseignee, annees_experience):
        super().__init__(nom, prenom)
        self.__matiere_enseignee = matiere_enseignee
        self.__annees_experience = annees_experience

    def enseigner(self):
        print(f"{self.__nom} enseigne {self.__matiere_enseignee}.")

# Classe Eleve héritant de Personne
class Eleve(Personne):
    def __init__(self, nom, prenom, niveau_scolaire, notes):
        super().__init__(nom, prenom)
        self.__niveau_scolaire = niveau_scolaire
        self.__notes = notes

    def afficher_notes(self):
        print(f"{self.__nom} a les notes suivantes : {self.__notes}")

# Classe Classe
class Classe:
    def __init__(self, professeur, eleves):
        self.__professeur = professeur
        self.__eleves = eleves  # Les élèves sont passés en paramètre lors de la création de la classe

    def ajouter_eleve(self, eleve):
        if len(self.__eleves) < 30:
            self.__eleves.append(eleve)
            print(f"{eleve.__nom} a été ajouté à la classe.")
        else:
            print("La classe est pleine.")

    def afficher_eleves(self):
        print(f"Liste des élèves de la classe:")
        for eleve in self.__eleves:
            print(f"- {eleve.__nom} {eleve.__prenom}")

# Exemple d'utilisation
prof = Professeur("Mme Dupont", "Clara", "Mathématiques", 5)
eleve1 = Eleve("Jean", "Michel", "Seconde", [15, 16, 17])
eleve2 = Eleve("Paul", "Durand", "Seconde", [18, 19, 20])

classe = Classe(prof, [eleve1, eleve2])
classe.afficher_eleves()
