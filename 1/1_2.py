max = [0,0,0]
elf_calories = 0

with open ('input.txt', 'r') as f:
    for line in f:
        if (line == '\n'):
            max.sort()
            if max[0] < elf_calories:
                max[0] = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line.strip())
        
print(sum(max))     
