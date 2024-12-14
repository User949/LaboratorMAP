# Ec de gr 2
import math

a = float(input("Introduceti coeficientul a: "))
b = float(input("Introduceti coeficientul b: "))
c = float(input("Introduceti coeficientul c: "))

delta = pow(b, 2) - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Ecuatia are doua solutii reale distincte: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Ecuatia are o singura solutie reala: x = {x}")
else:
    parteReala = -b / (2 * a)
    parteImaginara = math.sqrt(abs(delta)) / (2 * a)
    print(f"Ecuatia are doua solutii complexe: x1 = {parteReala} + {parteImaginara}i, x2 = {parteReala} - {parteImaginara}i")