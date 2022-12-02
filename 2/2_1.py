#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won

#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors
winning = [('A', 'Y'), ('B','Z'), ('C', 'X')]
drawn = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
points = 0
shapes = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

with open('input.txt', 'r') as f:
    for x in f:
        pair = tuple(x.strip().split(' '))
        if pair in winning:
            points += 6
        elif pair in drawn:
            points += 3
        
        points += shapes[pair[1]]
        
print(points)


