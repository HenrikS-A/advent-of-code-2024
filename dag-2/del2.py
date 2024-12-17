
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

reports = [[int(level) for level in line.split()] for line in lines]


def safe_report(report: list[int]):
    increasing = False
    decreasing = False

    for i in range(len(report) - 1):
        delta = report[i] - report[i+1]
        if delta == 0 or abs(delta) > 3:
            return False
        elif delta > 0:
            decreasing = True
        else:
            increasing = True
    if not(increasing and decreasing):
            return True


safe_reports = 0
for report in reports:
    if safe_report(report):
        safe_reports += 1
    else:
        tolerated = []
        for i in range(len(report)):
            modified_report = report.copy()
            modified_report.pop(i)
            tolerated.append(safe_report(modified_report))

        if any(tolerated):
            safe_reports += 1

print(safe_reports)
