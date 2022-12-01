max = 0
elf_calories = 0

with open ('input.txt', 'r') as f:
    for line in f: #is it line tho
        if (line == '\n'):
            if (max < elf_calories):
                max = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line.strip())
        
print(max)     
