matching_letters = []
letter_values = []

with open('input.txt','r') as f:
    for line in f:
        line = line.strip()
        compartmentsize = int(len(line) / 2)
        
        comp1 = line[:compartmentsize]
        comp2 = line[compartmentsize:]

        matching_letters.append(set(comp1).intersection(comp2).pop())

for x in matching_letters:
    if ord(x) < 91: #nagybetű
        letter_values.append(ord(x) - 38)
    else:
        letter_values.append(ord(x)- 96)

print(sum(letter_values))