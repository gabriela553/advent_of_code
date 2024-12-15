import re
with open('inputs/3.txt', 'r') as file:
    memory = file.read()

#Part 1
def look_for_mul(memory):
    matches = re.findall(r"mul\(\d+,\d+\)", memory)
    total = 0
    for match in matches:
        num1 = re.search(r'\d+', match)[0]
        num2 = re.findall(r'\d+', match)[1]
        total += int(num1)*int(num2)

    return total

#Part 2
pattern = r"(?:do\(\)|don't\(\)).*?(?=do\(\)|don't\(\)|$)"

all = re.findall(pattern, memory)
numbers = 0
for match in all:
    if re.match(r"don't\(\)", match):
        pass
    else:
        res = look_for_mul(match)
        numbers += res

print(numbers)
