"""
Docstring for day4.d4
"""

class Solution():
    debug = False

    def read_input(self, filename):
        grid = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                grid.append(list(line.strip()))
        return grid
    
    def get_rolls(self, grid):
        NR = len(grid)
        NC = len(grid[0])
        new_grid = [row.copy() for row in grid]
        roll_count = 0
        
        for r in range(NR):
            for c in range(NC):
                # print(f"Checking cell ({r}, {c}): {grid[r][c]}")
                if grid[r][c] == '@':
                    accessible = self.access(grid, r, c)
                    # print(f"  Accessible: {accessible}")
                    if accessible:
                        roll_count += 1
                        new_grid[r][c] = 'X'
                else:
                    continue
        
        if Solution.debug:
            print(f"Final grid after rolls:")
            for row in new_grid:
                print("".join(row))

        return roll_count
    
    def get_rolls2(self, grid):
        NR = len(grid)
        NC = len(grid[0])

        new_grid = [row.copy() for row in grid]
        search = True
        total_count = 0

        while search:
            roll_count = 0
            for r in range(NR):
                for c in range(NC):
                    # print(f"Checking cell ({r}, {c}): {grid[r][c]}")
                    if grid[r][c] == '@':
                        accessible = self.access(grid, r, c)
                        # print(f"  Accessible: {accessible}")
                        if accessible:
                            roll_count += 1
                            new_grid[r][c] = 'X'
                    elif grid[r][c] == 'X':
                        new_grid[r][c] = '.'
                    else:
                        continue

            total_count += roll_count

            if roll_count == 0:
                search = False
                        
            grid = [row.copy() for row in new_grid]
            new_grid = [row.copy() for row in grid]
            if Solution.debug:
                print(f"Final grid after rolls:")
                for row in new_grid:
                    print("".join(row))
                print(f"  Roll count this iteration: {roll_count}")

        return total_count
    
    def access(self, grid, r, c):
        paper_count = 0
        access_bool = False

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]:
            # checks valid grid position for paper roll
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '@':
                # print(f"    Found paper roll at ({nr}, {nc}): {grid[nr][nc]}")
                paper_count += 1
        
        # print(f"  Paper count around ({r}, {c}): {paper_count}")
        if paper_count < 4:
            access_bool = True

        return access_bool

if __name__ == "__main__":
    sol = Solution()

    """ Part 1 """
    toy_input = 'toy_input.txt'
    grid = sol.read_input(toy_input)
    if sol.debug:
        print(f'Input from {toy_input}:')
        for row in grid:
            print("".join(row))
    rolls = sol.get_rolls(grid)
    print(f'Toy input access rolls: {rolls}')

    # Answer for toy_input 13
    
    input1 = 'input.txt'
    grid1 = sol.read_input(input1)
    if sol.debug:
        print(f'Input from {input1}:')
        for row in grid1:
            print("".join(row))
    rolls1 = sol.get_rolls(grid1)
    print(f'Input1 access rolls: {rolls1}')
    
    # 12268 too high
    # Answer for input1 1549

    """ Part 2 """
    toy_input = 'toy_input.txt'
    grid2 = sol.read_input(toy_input)
    if sol.debug:
        print(f'Input from {toy_input}:')
        for row in grid2:
            print("".join(row))
    rolls2 = sol.get_rolls2(grid2)
    print(f'Toy input access rolls (part 2): {rolls2}')

    # Answer for toy input part 2: 43

    input1 = 'input.txt'
    grid3 = sol.read_input(input1)
    if sol.debug:
        print(f'Input from {input1}:')
        for row in grid3:
            print("".join(row))
    rolls3 = sol.get_rolls2(grid3)
    print(f'Input1 access rolls (part 2): {rolls3}')

    # Answer for input1 part 2: 8887