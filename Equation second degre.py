import math

def solve_quadratic(a, b, c):
    """
    Résout une équation du second degré de la forme ax^2 + bx + c = 0.
    Retourne les solutions sous forme de tuple.
    """
    if a == 0:
        if b == 0:
            return "Pas une équation valide" if c != 0 else "Infinité de solutions"
        return (-c / b,)  # Équation linéaire

    # Calcul du discriminant
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        # Deux solutions réelles
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Une solution réelle (racine double)
        root = -b / (2 * a)
        return root,
    else:
        # Pas de solution réelle
        return "Pas de solution réel"

# Exemple d'utilisation
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

solutions = solve_quadratic(a, b, c)
print("Solutions :", solutions)