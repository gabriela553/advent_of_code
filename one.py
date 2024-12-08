#Loading input and splitting lists

with open('inputs/1.txt', 'r') as file:
    location_list= file.read()

location_list = location_list.splitlines()
list1 = []
list2 = []
for pair in location_list:
    parts = pair.split()
    list1.append(parts[0])
    list2.append(parts[1])

# Part 2
tot = 0
for i in list1:
    quantity = list2.count(i)
    mult = int(i)*quantity
    tot += mult
print('Similarity score: ' + str(tot))

# Part 1

total = 0
for i in range(len(list1)):
    min1 = min(list1)
    min2 = min(list2)
    dist = int(min1) - int(min2)
    dist = abs(dist)
    list1.remove(min1)
    list2.remove(min2)
    total += dist
print('Total distance: ' + str(total))


