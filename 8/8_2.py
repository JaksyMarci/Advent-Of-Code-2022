import numpy as np
from math import prod

trees = []
scenic_scores = []
max_scenic_score = 0
with open('input.txt', 'r') as f:
    for line in f:
        trees.append(list(line.strip()))

trees = np.array(trees)


for i in range(1, len(trees)-1):
    for j in range(1, len(trees)-1):
        currentTree = trees[i][j]
        scenic_scores = [1,1,1,1]
        k=1
        while (j+k < trees.shape[1]-1 and trees[i][j+k] < currentTree ): #the if is lazy
            scenic_scores[0] +=1
            k+=1
        k=1
        while (j-k > 0 and trees[i][j-k] < currentTree ):
            scenic_scores[1] +=1
            k+=1
        k=1
        while (i+k < trees.shape[0]-1 and trees[i+k][j] < currentTree ):
            scenic_scores[2] +=1
            k+=1
        k=1
        while (i-k > 0 and trees[i-k][j] < currentTree):
            scenic_scores[3] +=1
            k+=1
        
        score = prod(scenic_scores)
        
        max_scenic_score = score if score > max_scenic_score else max_scenic_score

print(max_scenic_score)
