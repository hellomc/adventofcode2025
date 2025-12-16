"""
Docstring for day6.d6
"""

class Solution():
    debug = True

    def read_input(self, filename):
        values = []
        operators = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().split()
                first = line[0]
                if first.isnumeric():
                    values.append(line)
                elif '+' in line or '*' in line:
                    operators = line

        return values, operators
    
    def calculate(self, values, operators):
        num_probs = len(operators)
        num_values = len(values)
        print(num_probs, num_values)

        total_sum = 0

        for i in range(num_probs):
            if operators[i] == '+':
                answer = 0
            elif operators[i] == '*':
                answer = 1
            for j in range(num_values):
                if operators[i] == '+':
                    answer += int(values[j][i])
                elif operators[i] == '*':
                    answer *= int(values[j][i])
        
            total_sum += answer

        return total_sum
    
if __name__ == "__main__":
    sol = Solution()

    """ Part 1"""
    toy_input = 'toy_input.txt'
    values, operators = sol.read_input(toy_input)
    total_sum = sol.calculate(values, operators)
    print(f'Toy input total sum: {total_sum}')

    # Answer toy input part 1: 4277556

    input1 = 'input.txt'
    val1, ops1 = sol.read_input(input1)
    total_sum1 = sol.calculate(val1, ops1)
    print(f'Input total sum: {total_sum1}')

    # Answer input part 1: 6957525317641

    """ Part 2 """
    