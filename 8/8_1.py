import numpy as np

trees = []
visible = 0
with open('input.txt', 'r') as f:
    for line in f:
        trees.append(list(line.strip()))

trees = np.array(trees)

visible = trees.shape[0] * trees.shape[1]
for i in range(1, len(trees)-1):
    for j in range(1, len(trees)-1):
        currentTree = trees[i][j]
        if (
         max(np.take(trees, i, axis=0)[:j]) >= currentTree and
         max(np.take(trees, i,axis=0)[j+1:]) >= currentTree and 
         max(np.take(trees, j, axis=1)[:i]) >= currentTree and 
         max(np.take(trees,j,axis=1)[i+1:]) >= currentTree):
            
             visible-=1

print(visible)
