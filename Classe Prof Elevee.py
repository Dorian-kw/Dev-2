# Classe Adresse
class Adresse:
    def __init__(self, rue, code_postal, ville):
        self.__rue = rue
        self.__code_postal = code_postal
        self.__ville = ville

# Classe Personne
class Personne:
    def __init__(self, nom, prenom, etat_civil, coordonnees):
        self.__nom = nom
        self.__prenom = prenom
        self.__etat_civil = etat_civil
        self.__coordonnees = coordonnees

# Classe Professeur héritant de Personne
class Professeur(Personne):
    def __init__(self, nom, prenom, etat_civil, coordonnees, matiere_enseignee, annees_experience):
        super().__init__(nom, prenom, etat_civil, coordonnees)
        self.__matiere_enseignee = matiere_enseignee
        self.__annees_experience = annees_experience

    def enseigner(self):
        print(f"{self.__nom} enseigne {self.__matiere_enseignee}.")

# Classe Eleve héritant de Personne
class Eleve(Personne):
    def __init__(self, nom, prenom, etat_civil, coordonnees, niveau_scolaire, notes):
        super().__init__(nom, prenom, etat_civil, coordonnees)
        self.__niveau_scolaire = niveau_scolaire
        self.__notes = notes

    def enseigner(self):
        print(f"{self.__nom} suit un cours.")

# Classe Classe
class Classe:
    def __init__(self, professeur, eleves):
        self.__professeur = professeur
        self.__eleves = eleves  # Les élèves sont passés en paramètre

    def ajouter_eleve(self, eleve):
        if len(self.__eleves) < 30:
            self.__eleves.append(eleve)
            print(f"{eleve.__nom} a été ajouté à la classe.")
        else:
            print("La classe est pleine.")

# Exemple d'utilisation
adresse = Adresse("123 Rue Exemple", "75000", "Paris")
prof = Professeur("Mme Dupont", "Clara", "Célibataire", adresse, "Mathématiques", 5)
eleve = Eleve("Jean", "Michel", "Célibataire", adresse, "Seconde", [15, 16, 17])

classe = Classe(prof, [eleve])
classe.ajouter_eleve(Eleve("Paul", "Durand", "Célibataire", adresse, "Seconde", [18, 19, 20]))
