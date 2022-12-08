import numpy as np

STACKS_MAX_HEIGHT = 8

crates = []
buffer = []
index = 0
with open('input.txt', 'r') as f:
    for line in f:
        if (index < STACKS_MAX_HEIGHT):
            #read input stacks
            crates.append([*line[1::4]])
            index+=1
        elif (index == STACKS_MAX_HEIGHT):
            #arrange data
            crates = np.fliplr(np.transpose(crates))
            crates = list(map(lambda elem : list(elem[elem != ' ']), crates)) 
            index+=1
        elif (index < STACKS_MAX_HEIGHT + 2): #skip all remaining lines until instructions
            index+=1
            print(crates)
            continue
        else:
            #execute instructions
            instructions = tuple(line.strip().replace('move', ' ').replace('from',' ').replace('to',' ').replace('  ', '').split(' '))
            for i in range(int(instructions[0])):
                buffer.append(crates[int(instructions[1]) -1].pop())
            
            crates[int(instructions[2]) -1].extend(buffer)
            buffer.clear()
            
for x in crates:
    buffer.append(x.pop()) if len(x) > 0 else buffer.append('')
print(''.join(buffer))
