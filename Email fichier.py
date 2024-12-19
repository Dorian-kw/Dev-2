# Classe Fichier
class Fichier:
    def __init__(self, nom, taille, type_fichier, email):
        self.__nom = nom
        self.__taille = taille
        self.__type = type_fichier
        self.__email = email  # Le fichier est lié à un email

# Classe Email
class Email:
    def __init__(self, titre, texte, expediteur, destination):
        self.__titre = titre
        self.__texte = texte
        self.__expediteur = expediteur
        self.__destination = destination
        self.__fichiers_joints = [] # Liste prise dans la classe Fichier

    def ajouter_fichier(self, fichier):
        # Le fichier est ajouté à l'email
        if fichier.__email == self:  # Assure que le fichier appartient à cet email
            self.__fichiers_joints.append(fichier)
        else:
            print("Le fichier doit appartenir à cet email.")

    def envoyer(self):
        print(f"Envoi de l'email de {self.__expediteur} à {self.__destination}.")
        print("Fichiers joints :")
        for fichier in self.__fichiers_joints:
            print(f"- {fichier.__nom} ({fichier.__taille} ko)")

# Exemple d'utilisation
email = Email("Sujet", "Corps du message", "expediteur@example.com", "destinataire@example.com")
fichier1 = Fichier("document.pdf", 200, "pdf", email)  # Le fichier est rattaché à l'email
fichier2 = Fichier("image.jpg", 500, "jpg", email)

email.ajouter_fichier(fichier1)
email.ajouter_fichier(fichier2)
email.envoyer()
