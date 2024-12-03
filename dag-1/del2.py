
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

left, right = [], []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

similarity_score = 0
for number in left:
    similarity_score += number * right.count(number)

print(similarity_score)
