# Classe Adresse
class Adresse:
    def __init__(self, rue, code_postal, ville):
        self.rue = rue
        self.code_postal = code_postal
        self.ville = ville

# Classe Personne
class Personne:
    def __init__(self, nom, prenom, etat_civil, coordonnees):
        self.nom = nom
        self.prenom = prenom
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

# Classe Professeur héritant de Personne
class Professeur(Personne):
    def __init__(self, nom, prenom, etat_civil, coordonnees, matiere_enseignee, annees_experience):
        super().__init__(nom, prenom, etat_civil, coordonnees)
        self.matiere_enseignee = matiere_enseignee
        self.annees_experience = annees_experience

    def enseigner(self):
        print(f"{self.nom} enseigne {self.matiere_enseignee}.")

# Classe Eleve héritant de Personne
class Eleve(Personne):
    def __init__(self, nom, prenom, etat_civil, coordonnees, niveau_scolaire, notes):
        super().__init__(nom, prenom, etat_civil, coordonnees)
        self.niveau_scolaire = niveau_scolaire
        self.notes = notes

    def enseigner(self):
        print(f"{self.nom} suit un cours.")

# Classe Classe
class Classe:
    def __init__(self, professeur, eleves):
        self.professeur = professeur
        self.eleves = eleves

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
            print(f"{eleve.nom} a été ajouté à la classe.")
        else:
            print("La classe est pleine.")

# Exemple d'utilisation
adresse = Adresse("123 Rue Exemple", "75000", "Paris")
prof = Professeur("Mme Dupont", "Clara", "Célibataire", adresse, "Mathématiques", 5)
eleve = Eleve("Jean", "Michel", "Célibataire", adresse, "Seconde", [15, 16, 17])

classe = Classe(prof, [eleve])
classe.ajouter_eleve(Eleve("Paul", "Durand", "Célibataire", adresse, "Seconde", [18, 19, 20]))
