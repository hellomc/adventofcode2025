"""
Docstring for day7.d7
"""

class Solution():
    debug = True

    def read_input(self, filename):
        grid = []

        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                grid.append(list(line))
        
        return grid
    
    def find_start(self, grid):
        NR = len(grid)
        NC = len(grid[0])

        for r_index in range(NR):
            for c_index in range(NC):
                if grid[r_index][c_index] == 'S':
                    return [r_index, c_index]
        
        return None
    
    def total_splits(self, grid, start):
        total_splits = 0

        new_grid = [line for line in grid]

        NR = len(grid)
        NC = len(grid[0])
        
        path = {}
        for nr in range(NR):
            path[nr] = []

        r = 1
        path[0].append(start)
        while (r < NR):
            nodes = path[r-1]
            for node in nodes:
                nr = node[0] + 1
                nc = node[1]
                if 0 <= nr < NR and 0 <= nc < NC:
                    if grid[nr][nc] == '.':
                        new_grid[nr][nc] = '|'
                        path[r].append([nr, nc])
                    elif grid[nr][nc] == '^':
                        total_splits += 1
                        left = nc - 1
                        right = nc + 1
                        new_grid[nr][left] = '|'
                        new_grid[nr][right] = '|'
                        path[r].append([nr, left])
                        path[r].append([nr, right])
            r += 1

        if Solution.debug:
            for row in new_grid:
                print(row)

        return total_splits
    
if __name__ == "__main__":
    sol = Solution()

    """ Part 1 """

    toy_input = 'toy_input.txt'
    toy_grid = sol.read_input(toy_input)
    toy_start = sol.find_start(toy_grid)
    if sol.debug:
        for row in toy_grid:
            print(row)
        print(f'Start: {toy_start}')
    toy_splits = sol.total_splits(toy_grid, toy_start)
    print(f'Toy input total splits: {toy_splits}')

    # Answer for toy input part 1: 21

    input1 = 'input.txt'
    grid = sol.read_input(input1)
    grid_start = sol.find_start(grid)
    if sol.debug:
        print(f'Start: {grid_start}')
    grid_splits = sol.total_splits(grid, grid_start)
    print(f'Input total splits: {grid_splits}')

    # Answer for input part 1: 1590

    """ Part 2 """
