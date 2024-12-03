
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

left, right = [], []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
