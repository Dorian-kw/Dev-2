# Classe Fichier
class Fichier:
    def __init__(self, nom, taille, type_fichier):
        self.nom = nom
        self.taille = taille
        self.type = type_fichier

# Classe Email
class Email:
    def __init__(self, titre, texte, expediteur, destination):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier(self, fichier):
        self.fichiers_joints.append(fichier)

    def retirer_fichier(self, fichier):
        if fichier in self.fichiers_joints:
            self.fichiers_joints.remove(fichier)

    def envoyer(self):
        print(f"Envoi de l'email de {self.expediteur} à {self.destination}.")

# Exemple d'utilisation
fichier1 = Fichier("document.pdf", 200, "pdf")
fichier2 = Fichier("image.jpg", 500, "jpg")
email = Email("Sujet", "Corps du message", "expediteur@example.com", "destinataire@example.com")

email.ajouter_fichier(fichier1)
email.ajouter_fichier(fichier2)
email.envoyer()

print(f"Fichiers joints : {[fichier.nom for fichier in email.fichiers_joints]}")
