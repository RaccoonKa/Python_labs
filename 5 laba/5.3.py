with open("children.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

ages = [int(line.split()[2]) for line in lines]
oldest_child = max(ages)
youngest_child = min(ages)

with open("oldest_child.txt", "w") as file:
    for line in lines:
        if int(line.split()[2]) == oldest_child:
            file.write(line)

with open("youngest_child.txt", "w") as file:
    for line in lines:
        if int(line.split()[2]) == youngest_child:
            file.write(line)
