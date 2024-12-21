
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def find_horizontal():
    word = "XMAS"
    occurrences = 0
    for line in lines:
        for i in range(len(line) - len(word) + 1):
            # Forlengs
            if line[i] == word[0] and line[i+1] == word[1] and line[i+2] == word[2] and line[i+3] == word[3]:
                occurrences += 1
            # Og baklengs
            if line[i] == word[-1] and line[i+1] == word[-2] and line[i+2] == word[-3] and line[i+3] == word[-4]:
                occurrences += 1
    return occurrences

def find_vertical():
    word = "XMAS"
    occurrences = 0
    for y in range(len(lines) - len(word) + 1):
        for x in range(len(lines[y])):
            if lines[y][x] == word[0] and lines[y+1][x] == word[1] and lines[y+2][x] == word[2] and lines[y+3][x] == word[3]:
                occurrences += 1
            if lines[y][x] == word[-1] and lines[y+1][x] == word[-2] and lines[y+2][x] == word[-3] and lines[y+3][x] == word[-4]:
                occurrences += 1

    return occurrences

def find_diagonal_1():
    # Diagonalt fra oppe til venstre og nedover til høyre
    word = "XMAS"
    occurrences = 0
    for y in range(len(lines) - len(word) + 1):
        for x in range(len(lines[y]) - len(word) + 1):
            if lines[y][x] == word[0] and lines[y+1][x+1] == word[1] and lines[y+2][x+2] == word[2] and lines[y+3][x+3] == word[3]:
                occurrences += 1
            if lines[y][x] == word[-1] and lines[y+1][x+1] == word[-2] and lines[y+2][x+2] == word[-3] and lines[y+3][x+3] == word[-4]:
                occurrences += 1
    return occurrences

def find_diagonal_2():
    # Diagonalt fra oppe til høyre og nedover til venstre
    word = "XMAS"
    occurrences = 0
    for y in range(len(lines) - len(word) + 1):
        for x in range(len(word) - 1, len(lines[y])):
            if lines[y][x] == word[0] and lines[y+1][x-1] == word[1] and lines[y+2][x-2] == word[2] and lines[y+3][x-3] == word[3]:
                occurrences += 1
            if lines[y][x] == word[-1] and lines[y+1][x-1] == word[-2] and lines[y+2][x-2] == word[-3] and lines[y+3][x-3] == word[-4]:
                occurrences += 1
    return occurrences




tot = find_horizontal() + find_vertical() + find_diagonal_1() + find_diagonal_2()
print(tot)
