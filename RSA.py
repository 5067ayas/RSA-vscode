import math

# Fonction pour calculer le PGCD (plus grand commun diviseur)
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fonction pour calculer l'inverse modulaire (algorithme d'Euclide étendu)
def inverse_modulaire(e, phi):
    d, x1, x2 = 0, 0, 1
    y1, y2 = 1, 0
    while phi != 0:
        quotient = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2 - quotient * x1, x1
        y1, y2 = y2 - quotient * y1, y1
    if e == 1:
        return x2

# Fonction pour tester si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Fonction principale
def rsa_interactif():
    print("Bienvenue dans le programme intélligente de calcul RSA !")
    print("Nous allons générer les clés RSA et expliquer chaque étape.\n")

    # Étape 1 : Entrée des nombres premiers p et q
    while True:
        try:
            p = int(input("Entrez un nombre premier p : "))
            if not est_premier(p):
                print(f"{p} n'est pas un nombre premier. Veuillez réessayer.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    while True:
        try:
            q = int(input("Entrez un nombre premier q (différent de p) : "))
            if not est_premier(q) or p == q:
                print(f"{q} n'est pas un nombre premier ou est égal à p. Veuillez réessayer.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    print("\nÉtape 1 : Vous avez choisi p =", p, "et q =", q)

    # Étape 2 : Calcul de n et φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    print("\nÉtape 2 : Calcul de n et φ(n)")
    print(f"n = p * q = {p} * {q} = {n}")
    print(f"φ(n) = (p-1) * (q-1) = ({p}-1) * ({q}-1) = {phi}")

    # Étape 3 : Choix de e
    while True:
        try:
            e = int(input(f"\nÉtape 3 : Entrez un exposant public e tel que 1 < e < {phi} et pgcd(e, φ(n)) = 1 : "))
            if 1 < e < phi and pgcd(e, phi) == 1:
                break
            else:
                print(f"e doit être compris entre 1 et {phi}, et pgcd(e, φ(n)) doit être 1. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    print(f"\nVous avez choisi e = {e}.")
    print(f"pgcd(e, φ(n)) = pgcd({e}, {phi}) = {pgcd(e, phi)} (OK)")

    # Étape 4 : Calcul de d (inverse modulaire de e modulo φ(n))
    d = inverse_modulaire(e, phi)
    print("\nÉtape 4 : Calcul de d (inverse modulaire de e modulo φ(n))")
    print(f"d * e ≡ 1 (mod φ(n)) => d * {e} ≡ 1 (mod {phi})")
    print(f"Le résultat est d = {d}.")

    # Clés générées
    cle_publique = (e, n)
    cle_privee = (d, n)
    print("\nClés générées :")
    print(f"Clé publique : (e, n) = {cle_publique}")
    print(f"Clé privée : (d, n) = {cle_privee}")

    # Étape 5 : Chiffrement d'un message
    message = input("\nÉtape 5 : Entrez un message à chiffrer (texte ou nombre) : ")
    message_chiffre = []
    print("\nChiffrement du message caractère par caractère :")
    for char in message:
        M = ord(char)  # Convertir le caractère en son code ASCII
        C = pow(M, e, n)  # Chiffrement : C = M^e mod n
        message_chiffre.append(C)
        print(f"Caractère : '{char}' -> Code ASCII : {M} -> Chiffré : {C}")

    print("\nMessage chiffré :", message_chiffre)

    # Étape 6 : Déchiffrement du message
    print("\nÉtape 6 : Déchiffrement du message :")
    message_dechiffre = ""
    for C in message_chiffre:
        M = pow(C, d, n)  # Déchiffrement : M = C^d mod n
        char = chr(M)  # Convertir le code ASCII en caractère
        message_dechiffre += char
        print(f"Chiffré : {C} -> Déchiffré : {M} -> Caractère : '{char}'")

    print("\nMessage déchiffré :", message_dechiffre)

# Exécution du programme
if __name__ == "__main__":
    rsa_interactif ()
