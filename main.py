from argparse import ArgumentParser
from subprocess import Popen, STDOUT, PIPE


class IPFile:
    def __init__(self, filename: str = "ip.txt"):
        """
        Fonction initiale qui va prendre le nom de fichier en entrée
        :param filename: nom du fichier à ouvrir
        """
        self.file = filename

    def __read_file(self) -> list:
        """
        Méthode utilisable que au sein de la fonction
        !!! ET NON VIA L'OBJET DECLARE !!!
        qui permet de lire un fichier et de split à chaque saut de ligne
        """
        with open(
                file=self.file,
                mode="r",
                encoding="utf-8"
        ) as config:
            return config.readlines()

    def to_list(self) -> list:
        """
        Methode qui va renvoyer la liste des IP sous forme de list
        """
        result = []
        for line in self.__read_file():
            result.append(line.strip())
        return result

    def to_json(self, data: list = None) -> dict:
        """
        Méthode qui permet de renvoyer une liste d'IP sous la forme de dictionnaire
        l'argument data permet de renvoyer un dictionnaire d'une source de type liste, sinon c'est un dictionnaire du fichier qui sera renvoyé

        data UTILE quand vous modifiez la valeur de __read_line()
        """
        result = {}
        for [index, line] in enumerate(self.__read_file() if data is None else data):
            result[index] = str(line).strip()
        return result

    def to_raw(self, data: list = None) -> str:
        """
        Méthode qui permet de renvoyer une liste d'IP sous la forme de string
        l'argument data permet de renvoyer un dictionnaire d'une source de type liste, sinon c'est une string du fichier qui sera renvoyé

        data UTILE quand vous modifiez la valeur de __read_line()
        """
        result = ""
        for line in self.__read_file() if data is None else data:
            result += f"{line}\n"
        return result[:-1]

    def add_ip(self, ip: str):
        """
        Permet de rajouter une addresse IP dans le fichier ip.txt
        """
        if ip not in self.to_list():
            with open(
                    file=self.file,
                    mode="a",
                    encoding="utf-8"
            ) as file:
                file.write(f"\n{ip}")
                print(f"{ip} > SUCCESS_IP_ADD")
        else:
            print(f"{ip} > IP_ALREADY_ENCODED")

    def remove_ip(self, ip: str):
        """
        Permet de supprimer une IP du fichier ip.txt
        """
        if ip in self.to_list():
            data = self.to_list()
            data.remove(ip)
            with open(
                    file=self.file,
                    mode="w",
                    encoding="utf-8"
            ) as file:
                file.write(self.to_raw(data=data))
                print(f"{ip} > SUCCESS_IP_REMOVED")
        else:
            print(f"{ip} > IP_NOT_ENCODED")


class Log:
    @staticmethod
    def record(output_file: str, data: str):
        with open(
                file=output_file,
                mode="a",
                encoding="utf-8"
        ) as log:
            log.write(data)


class Traceroute(Log):
    def __init__(self, ip: str, output_file: str):
        self.ip = ip
        self.output_file = output_file
        self.output = output_file is not None

    def run_detached(self):
        if self.output:
            self.record(output_file=self.output_file, data=f"\n[ --- Analyse de l'IP {self.ip} --- ]")
        print(f"[ --- Tracert de l'IP {self.ip} --- ]")
        process = Popen(
            args=["tracert", self.ip],
            stdout=PIPE,
            stderr=STDOUT,
            text=True,
            encoding="cp850"
        )
        for line in process.stdout:
            print(line.strip(), end="\n")
            if self.output:
                Log().record(output_file=self.output_file, data=f"{line.strip()}\n")
        process.wait()


if __name__ == "__main__":
    args = ArgumentParser()
    ip_file = IPFile()
    args.add_argument("-p", "--progressive", action="store_true", help="Affichage en temps réel")
    args.add_argument("-o", "--output", help="Enregistrer les résultats dans un fichier")
    args.add_argument("-a", "--add", help="Ajouter une addresse IP")
    args.add_argument("-r", "--remove", help="Supprimer une addresse IP")
    args = args.parse_args()

    if args.add is not None:
        ip_file.add_ip(ip=args.add)
    elif args.remove is not None:
        ip_file.remove_ip(ip=args.remove)
    elif args.progressive:
        for ip in ip_file.to_list():
            Traceroute(ip=ip, output_file=args.output).run_detached()
