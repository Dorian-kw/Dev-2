from fraction import Fraction  

def main():
    print("----- Tests de la classe Fraction -----")

    try:
        # Test de création et d'affichage
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        print(f"Fraction 1 : {f1}")  # Attendu : "3/4"
        print(f"Fraction 2 : {f2}")  # Attendu : "2/5"

        # Test des opérations arithmétiques
        print(f"Addition : {f1} + {f2} = {f1 + f2}")
        print(f"Soustraction : {f1} - {f2} = {f1 - f2}")
        print(f"Multiplication : {f1} * {f2} = {f1 * f2}")
        print(f"Division : {f1} / {f2} = {f1 / f2}")

        # Test des propriétés
        print(f"{f1} est-il nul ? {f1.is_zero()}")
        print(f"{f1} est-il un entier ? {f1.is_integer()}")
        print(f"{f1} est-il propre ? {f1.is_proper()}")
        print(f"{f1} est-il une fraction unitaire ? {f1.is_unit()}")

        # Test de nombre mixte
        f3 = Fraction(7, 3)
        print(f"Nombre mixte de {f3} : {f3.as_mixed_number()}")

        # Test de comparaison
        f4 = Fraction(7, 3)
        print(f"{f3} est-il égal à {f4} ? {f3 == f4}")

        # Test de la méthode is_adjacent_to
        f5 = Fraction(4, 3)
        print(f"{f3} est-il adjacent à {f5} ? {f3.is_adjacent_to(f5)}")

        # Test d'exception ZeroDivisionError
        try:
            f6 = Fraction(1, 0)
        except ZeroDivisionError as e:
            print(f"Erreur attendue : {e}")

        # Test d'exception TypeError
        try:
            print(f1.is_adjacent_to(5))  # 5 n'est pas une fraction.
        except TypeError as e:
            print(f"Erreur attendue : {e}")

        # Test de puissance
        print(f"{f1} élevé à la puissance 2 : {f1 ** 2}")
        print(f"{f1} élevé à la puissance -1 : {f1 ** -1}")

        # Test de conversion en flottant
        print(f"Valeur flottante de {f1} : {float(f1)}")

    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()
