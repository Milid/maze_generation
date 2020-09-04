
## Maze generation with iterative randomized DFS algorithm


import random

 

def getNeighbors(r,c, m, n):
	
	neighbors = ([(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if i in range(m) and j in range(n) ])
	random.shuffle(neighbors)
	return neighbors

def dfsBacktrackingMaze(m, n):
	i, j = random.randint(0, m-1), random.randint(0, n-1)
	stack = [(i,j)]
	visited = set([(i,j)])

	path = []
	
	while stack:
		i, j = stack.pop()
		path.append((i, j))
		
		neighbors = getNeighbors(i, j, m, n)
		if all(i in visited for i in neighbors):
			continue

		else:
			stack.append((i,j))
			for i in neighbors:
				if i not in visited:
					visited.add(i)
					stack.append(i)
					break

	return path

def convertIndex(i, cols):
	return divmod(i, cols)


	




