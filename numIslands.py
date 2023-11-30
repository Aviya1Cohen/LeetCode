class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: #base case
            return 0
        counter = 0 #counter to keep of the number of islands
        visited = set() #set to keep track of visited positions.

        
        def bfs(grid, i, j):#create a bfs function starting from a given positions
            queue = deque() #initialize a queue
            queue.append((i, j)) #add the first position
            positions = [(1, 0), (-1, 0), (0, 1), (0,-1)] #positions to move up, down, left right
            #BFS LOOP
            while queue:
                row, col = queue.popleft() #dequeue curr position
                #loop over possible positions to move
                for pr, pc in positions:
                    #calc the new position
                    newRow = row + pr
                    newCol = col + pc

                    #check if the new position is in the grid range, not visited and is "1"
                    if (
                        newRow >= 0 and newRow < len(grid) and
                        newCol >= 0 and newCol < len(grid[0]) and
                        (newRow, newCol) not in visited and
                        grid[newRow][newCol] == '1'
                    ): #if so, add the new position to the queue and mark as visited
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))

        #loop over rows and colms of the grid
        for i in range(len(grid)): #loop over rows
            for j in range(len(grid[0])): #loop over cols
                #check if the curr position contain 1 and not in visited
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j))#mark as visited
                    counter += 1 #increse counter
                    #perform bfs from the curr position
                    bfs(grid, i, j)
        return counter
