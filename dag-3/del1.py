import re
import math

with open("input.txt", "r") as file:
    contents = file.read()

sequences = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", contents)

products = []
for sequence in sequences:
    factors = re.findall(r"[0-9]+", sequence)
    factors = [int(f) for f in factors]
    products.append(math.prod(factors))

print(sum(products))
