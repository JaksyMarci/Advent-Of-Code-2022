
#A for Rock, B for Paper, and C for Scissors

points = 0
extrapoints = [1,2,3] #1 for Rock, 2 for Paper, and 3 for Scissors
startpos = {
    'A' : 0,
    'B' : 1,
    'C' : 2
}
shift = {
    'X' : -1,
    'Y' : 0,
    'Z' : -2 #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
}

shapes = { #0 if you lost, 3 if the round was a draw, and 6 if you won
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}

with open('input.txt', 'r') as f:
    for x in f:
        pair = tuple(x.strip().split(' '))
        points += extrapoints[ startpos[pair[0]] + shift[pair[1]] ] #indexing the extrapoints array starting from 'startpos' and shifting by 'shift'
        points += shapes[pair[1]]
        
print(points)


