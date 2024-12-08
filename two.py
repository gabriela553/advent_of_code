#Loading input and splitting reports
with open('inputs/2.txt', 'r') as file:
    input_data = file.read()

input_data = input_data.splitlines()
# Part 1
total = 0
for report in input_data:
    levels = report.split()
    levels = [int(x) for x in levels]
    if levels[0] > levels[1]:
        for level in range(len(levels)-1):
            if (levels[level] - levels[level+1]) in (1,2,3):
                continue
            else:
                break
        else:
            total += 1
    elif levels[0] < levels[1]:
        for level in range(len(levels) - 1):
            if (levels[level + 1] - levels[level]) in (1, 2, 3):
                continue
            else:
                break
        else:
            total += 1

print(total)