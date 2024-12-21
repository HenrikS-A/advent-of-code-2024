
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

def find_x_mas():
    occurrences = 0

    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[y]) - 1):
            if lines[y][x] == "A":
                mas1 = False
                mas2 = False

                if lines[y-1][x-1] in ["M", "S"] and lines[y+1][x+1] in ["M", "S"] and lines[y-1][x-1] != lines[y+1][x+1]:
                    mas1 = True
                if lines[y-1][x+1] in ["M", "S"] and lines[y+1][x-1] in ["M", "S"] and lines[y-1][x+1] != lines[y+1][x-1]:
                    mas2 = True

                if mas1 and mas2:
                    occurrences += 1
    
    return occurrences

print(find_x_mas())
                    
