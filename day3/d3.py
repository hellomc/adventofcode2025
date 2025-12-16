"""
Docstring for day3.d3
"""

class Solution():
    debug = True

    def read_input(self, filename):
        """
        Docstring for read_input
        
        :param self: Description
        :param filename: Description

        :return: List of IDs
        """
        banks = []
        with open(filename, 'r') as f:
            for line in f:
                banks.append(int(line.strip()))
        return banks
    
    def eval_batteries(self, banks):
        """
        Docstring for eval_batteries
        
        :param self: Description
        :param banks: Description

        :return: Total battery capacity
        """
        max_joltage = []

        for bank in banks:
            max_val = 0
            battery = str(bank)
            len_battery = len(battery)
            
            for i in range(0, len_battery - 1):
                for j in range (i + 1, len_battery):
                    joltage = battery[i] + battery[j]
                    if int(joltage) > max_val:
                        max_val = int(joltage)
            
            max_joltage.append(max_val)

        return max_joltage
    
    def eval_batteries2(self, banks):
        """
        Docstring for eval_batteries2
        
        :param self: Description
        :param banks: Description

        :return: Max voltage for a battery with length of 12
        """
        max_joltage = []

        for bank in banks:
            battery = str(bank)
            len_battery = len(battery)
            joltage = []
            to_drop = len_battery - 12

            # find max value of length 12
            for batt in battery:
                while to_drop > 0 and joltage and joltage[-1] < batt:
                    joltage.pop()
                    to_drop -= 1
                joltage.append(batt)
            
            max_joltage.append(int("".join(joltage[:12])))

        return max_joltage

    def total_joltage(self, max_joltage):
        """
        Docstring for total_joltage
        
        :param self: Description
        :param max_joltage: Description

        :return: Sum of total output joltage
        """
        total = sum(max_joltage)
        return total

if __name__ == "__main__":
    sol = Solution()

    """ Part 1 """
    toy_input = 'toy_input.txt'
    banks = sol.read_input(toy_input)
    max_joltage = sol.eval_batteries(banks)
    if Solution.debug:
        print(banks)
        print(max_joltage)
    total_output = sol.total_joltage(max_joltage)
    print(f"Total output joltage: {total_output}")

    # Answer for toy_input 357

    input1 = 'input.txt'
    banks1 = sol.read_input(input1)
    max_joltage1 = sol.eval_batteries(banks1)
    total_output1 = sol.total_joltage(max_joltage1)
    if Solution.debug:
        print(banks1)
        print(max_joltage1)
    print(f"Total output joltage: {total_output1}")

    # Answer for part 1 17524

    """ Part 2 """
    toy_input = 'toy_input.txt'
    banks = sol.read_input(toy_input)
    max_joltage = sol.eval_batteries2(banks)
    if Solution.debug:
        print(banks)
        print(max_joltage)
    total_output = sol.total_joltage(max_joltage)
    print(f"Total output joltage (part 2): {total_output}")

    # Answer for toy input 3121910778619

    input1 = 'input.txt'
    banks1 = sol.read_input(input1)
    max_joltage2 = sol.eval_batteries2(banks1)
    total_output2 = sol.total_joltage(max_joltage2)
    if Solution.debug:
        print(banks1)
        print(max_joltage2)
    print(f"Total output joltage (part 2): {total_output2}")

    # Answer for input 173848577117276