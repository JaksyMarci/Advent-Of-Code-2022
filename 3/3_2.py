matching_letters = []
letter_values = []
group = []
groupcounter = 0


with open('input.txt','r') as f:
    for line in f:
        line = line.strip()
        group.append(line)
        groupcounter +=1
        if (groupcounter == 3):
            matching_letters.append(set(group[0]).intersection(group[1]).intersection(group[2]).pop())
            groupcounter = 0
            group = []
        
        

        

for x in matching_letters:
    if ord(x) < 91: #nagybetű
        letter_values.append(ord(x) - 38)
    else:
        letter_values.append(ord(x)- 96)

print(sum(letter_values))