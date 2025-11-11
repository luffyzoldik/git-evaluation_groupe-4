import sys
import random

def generate_expressions(num_expressions):
    """
    Génère le nombre spécifié d'expressions arithmétiques aléatoires.
    Les nombres sont dans l'intervalle [1, 1000].
    """
    operators = ['+', '-', '*', '/']
    
    for _ in range(num_expressions):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

        operator = random.choice(operators)
        print(f"{num1}{operator}{num2}")

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Erreur: Le programme generator prend un entier comme premier argument.\n")
        sys.stderr.write("Utilisation: ./generator <nombre_d_expressions_a_generer>\n")
        sys.exit(1)

    try:
        num_to_generate = int(sys.argv[1])
        if num_to_generate <= 0:
            sys.stderr.write("Erreur: Le nombre d'expressions doit être un entier positif.\n")
            sys.exit(1)
            
        generate_expressions(num_to_generate)
        
    except ValueError:
        sys.stderr.write(f"Erreur: '{sys.argv[1]}' n'est pas un entier valide.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()