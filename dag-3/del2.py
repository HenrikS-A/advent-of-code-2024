import re
import math

with open("input.txt", "r") as file:
    contents = file.read()

sequences = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", contents)  # | er 'or' operatoren

products = []
disable = False
for sequence in sequences:
    if sequence == "don't()":
        disable = True
    elif sequence == "do()":
        disable = False
        continue

    if not disable:
        factors = re.findall(r"[0-9]+", sequence)
        factors = [int(f) for f in factors]
        products.append(math.prod(factors))


print(sum(products))
