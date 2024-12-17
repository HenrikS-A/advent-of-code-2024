
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

reports = [[int(level) for level in line.split()] for line in lines]

safe_reports = 0
for report in reports:
    increasing = False
    decreasing = False

    for i in range(len(report) - 1):
        delta = report[i] - report[i+1]
        if delta == 0 or abs(delta) > 3:
            break
        elif delta > 0:
            decreasing = True
        else:
            increasing = True
    else:
        if not(increasing and decreasing):
            safe_reports += 1

print(safe_reports)
