import re

memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?do()mul(8,5)don't()mul(9,9)"

# Wzorzec do dopasowania
pattern = r"(?:do\(\)|don't\(\)).*?(?=do\(\)|don't\(\)|$)"

# Szukanie dopasowań
matches = re.findall(pattern, memory)

print(matches)
