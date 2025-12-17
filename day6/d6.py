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
    
    def read_input2(self, filename):
        """
        Get input data in column format
        
        :param self: Description
        :param filename: Description
        
        :return: output [([v01, v02, v0N], 'op1'), ([v11, v12, v1N], 'op2')]
        """

        with open(filename, 'r') as f:
            lines = [line.rstrip('\n').rstrip('\r') for line in f]
        
        width = max(len(line) for line in lines)
        grid = [line.ljust(width) for line in lines]

        problems = []

        tokens = []
        for col in zip(*grid):
            token = "".join(ch for ch in col if ch.isdigit() or ch in '+*')
            if token:
                tokens.append(token)

        problems = []
        values = []
        for token in reversed(tokens):
            if token[-1] in '+*':
                problems.append((values + [int(token[:-1])], token[-1]))
                values = []
            else:
                values.append(int(token))

        return problems

    
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
    problems = sol.read_input2(toy_input)
    print(problems)