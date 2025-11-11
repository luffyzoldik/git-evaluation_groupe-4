!/usr/bin/env python3
# Reste du code Python
import sys
import re

def calculate(expression):
    """
    Analyse l'expression, effectue l'opération, gère la division par zéro et la syntaxe.
    """
    clean_expression = expression.strip()
    
    match = re.fullmatch(r'(\d*\.?\d+)\s*([\+\-\*/])\s*(\d*\.?\d+)', clean_expression)
    
    if not match:
        sys.stderr.write(f'Erreur de syntaxe pour le calcul: "{clean_expression}"\n')
        sys.exit(1)

    num1_str, operator, num2_str = match.groups()
    num1 = float(num1_str)
    num2 = float(num2_str)
    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            sys.stderr.write("Division par zéro\n")
            sys.exit(1)
        result = num1 / num2
    
    return result

def main():
    for line in sys.stdin:
        expression = line.strip()
        
        if not expression:
            continue

        result = calculate(expression)
        
        if result is not None:
            if result == int(result):
                print(int(result))
            else:
                print(f"{result:.2f}")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        sys.exit(1)