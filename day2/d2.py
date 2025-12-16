"""
d2.py


"""

class Solution():
    debug = False

    def read_input(self, filename):
        """
        read_input
        
        :param self: Description
        :param filename: Description

        :return: List of tuples of ranges [(start0, end0), ... (startN, endN)]
        """
        ranges = []
        ids = []
        with open(filename, 'r') as f:
            line = f.readline()
            ranges = line.split(',')

            for range in ranges:
                s, e = range.split('-')
                ids.append([int(s), int(e)])
        
        return ids

    def invalid_ids(self, input_ids):
        """
        Docstring for invalid_ids
        
        :param self: Description
        :param input_ids: Description

        :return: List of invalid ids
        """
        invalid = []

        for pair in input_ids:
            start, end = pair[0], pair[1]

            for id in range(start, (end + 1)):
                id_string = str(id)
                if len(id_string) % 2 == 0:
                    mid = len(id_string) // 2
                    left = id_string[:mid]
                    right = id_string[mid:]
                    if left == right:
                        invalid.append(id)

        return invalid
    
    def invalid_ids2(self, input_ids):
        """
        Docstring for invalid_ids2
        
        :param self: Description
        :param input_ids: Description

        :return: List of invalid ids where sequence of digits repeats at least twice
        """
        invalid = []

        for pair in input_ids:
            start, end = pair[0], pair[1]

            for id in range(start, (end + 1)):
                id_string = str(id)
                length = len(id_string)
                median = length // 2

                # sequence of digits of any length repeats at least twice in string
                invalid_seq = False
                for seq_len in range(1, (median + 1)):
                    # print(f"Checking ID {id} for sequence length of {seq_len}")
                    if (length % seq_len) == 0 or (length // seq_len) == length:
                        for i in range(0, (length - seq_len), seq_len):
                            seq = id_string[i:i + seq_len]
                            next_seq = id_string[i + seq_len: i + seq_len + seq_len]
                            # print(f"  Comparing seq {seq} with next_seq {next_seq}")
                            if seq == next_seq:
                                invalid_seq = True
                            else:
                                invalid_seq = False
                                break
                    if invalid_seq:
                        invalid.append(id)
                        break

        return invalid
    
    def sum_invalid(self, invalid_ids):
        """
        Docstring for sum_invalid
        
        :param self: Description
        :param invalid_ids: Description

        :return: Sum of invalid ids
        """
        total = sum(invalid_ids)

        return total
        


if __name__ == "__main__":
    sol = Solution()

    toy_input = 'toy_input.txt'
    ids = sol.read_input(toy_input)
    invalid_ids = sol.invalid_ids(ids)
    if Solution.debug:
        print(ids)
        print(invalid_ids)
    total_invalid = sol.sum_invalid(invalid_ids)
    print(f"Sum of invalid IDs: {total_invalid}")

    # Answer for toy_input.txt 1227775554

    input1 = 'input.txt'
    ids1 = sol.read_input(input1)
    invalid_ids1 = sol.invalid_ids(ids1)
    total_invalid1 = sol.sum_invalid(invalid_ids1)
    if Solution.debug:
        print(ids1)
        print(invalid_ids1)
    print(f"Sum of invalid IDs: {total_invalid1}")

    # Answer for input.txt 26255179562

    """ Part 2 """
    toy_invalid_ids = sol.invalid_ids2(ids)
    toy_total_invalid = sol.sum_invalid(toy_invalid_ids)
    if Solution.debug:
        print(toy_invalid_ids)
    print(f"Sum of invalid IDs (part 2): {toy_total_invalid}")

    # Answer for toy_input.txt 4174379265

    invalid_ids2 = sol.invalid_ids2(ids1)
    total_invalid2 = sol.sum_invalid(invalid_ids2)
    if Solution.debug:
        print(invalid_ids2)
    print(f"Sum of invalid IDs (part 2): {total_invalid2}")

    # Answer for input.txt part 2 31680313976