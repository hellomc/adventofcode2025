"""
Docstring for day5.d5
"""

class Solution():
    debug = False

    def read_input(self, filename):
        ranges = []
        ids = []
        with open(filename, 'r') as f:
            for line in f:
                strip_line = line.strip()
                if "-" in strip_line:
                    start, end = strip_line.split("-")
                    ranges.append([int(start), int(end)])
                if strip_line.isdigit():
                    ids.append(int(strip_line))

        return ranges, ids
    
    def is_fresh(self, ids, ranges):
        fresh_ids = []

        for id in ids:
            for start, end in ranges:
                if start <= id <= end:
                    fresh_ids.append(id)
                    break

        return fresh_ids
    
    def is_fresh2(self, ranges):
        count = 0

        # merge intervals
        ranges.sort()
        merged = [ranges[0]]

        for interval in ranges[1:]:
            if interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        for interval in merged:
            start, end = interval
            count += (end - start + 1)

        # count number of ids
        
        return count
    
    def count_fresh(self, ids):
        return len(ids)

if __name__ == "__main__":
    sol = Solution()

    """ Part 1 """
    toy_input = 'toy_input.txt'
    ranges, ids = sol.read_input(toy_input)
    if sol.debug:
        print("Ranges:", ranges)
        print("IDs:", ids)
    fresh_ids = sol.is_fresh(ids, ranges)
    fresh_count = sol.count_fresh(fresh_ids)
    print("Number of fresh IDs in toy input:", fresh_count)

    # Answer for toy input: 3

    input1 = 'input.txt'
    ranges1, ids1 = sol.read_input(input1)
    fresh_ids1 = sol.is_fresh(ids1, ranges1)
    fresh_count1 = sol.count_fresh(fresh_ids1)
    print("Number of fresh IDs in input:", fresh_count1)

    # Answer for input part 1: 701

    """ Part 2 """

    fresh_count_toy2 = sol.is_fresh2(ranges)
    print("Number of fresh IDs in toy input (part 2):", fresh_count_toy2)

    # Answer for toy input part 2: 14

    fresh_count2 = sol.is_fresh2(ranges1)
    print("Number of fresh IDs in input (part 2):", fresh_count2)

    # Answer for input part 2: 352340558684863
