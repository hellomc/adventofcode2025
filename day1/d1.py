class Solution():
    debug = False

    def readinput(self, filename):
        try:
            direction = []
            distance = []
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    # get first character of each line
                    direction.append(line[0])
                    distance.append(int(line[1:].strip()))
        
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except ValueError:
            print(f"Error processing teh file {filename}.")

        return direction, distance
    
    "Counts when dial lands on 0"
    def turndial(self, start, direction, distance):
        pwd_count = 0
        current = start

        for dx, dist in zip(direction, distance):
            if dx == 'R':
                current += dist
            elif dx == 'L':
                current -= dist
            if current < 0 or current > 99:
                current %= 100
            if current == 0:
                pwd_count += 1

            if Solution.debug:
                print(f"Rotation: {dx}, Distance: {dist}, Current position: {current}, Password count: {pwd_count}")
            
        return pwd_count

    "Counts every time the dial passes 0 and lands at 0"
    def turndial2(self, start, direction, distance):
        pwd_count = 0
        current = start

        for dx, dist in zip(direction, distance):
            full_rotations = dist // 100
            rem = dist % 100

            pwd_count += full_rotations

            if dx == "R":
                if current + rem >= 100:
                    pwd_count += 1
                current = (current + rem) % 100
            elif dx == "L":
                if current > 0 and current - rem <= 0:
                    pwd_count += 1
                current = (current - rem) % 100

            if Solution.debug:
                print(f"Rotation: {dx}{dist}, Current: {current}, Password Count: {pwd_count}")

        return pwd_count

if __name__ == "__main__":
    """Part 1"""
    
    filename = "toy_input.txt"
    print(f"Reading input from {filename}")
    dx, dist = Solution().readinput(filename)
    if Solution().debug:
        print(dx)
        print(dist)
    result = Solution().turndial(50, dx, dist)
    print(f"Result: {result}")

    filename2 = "input.txt"
    print(f"Reading input from {filename2}")
    dx2, dist2 = Solution().readinput(filename2)
    if Solution().debug:
        print(len(dx2))
        print(len(dist2))
    result = Solution().turndial(50, dx2, dist2)
    print(f"Result: {result}")
    
    # 251 is too low
    # Answer: 1018


    """Part 2"""

    print(f"Reading input from {filename}")
    result = Solution().turndial2(50, dx, dist)
    print(f"Result: {result}")

    filename3 = "toy_input2.txt"
    dx3, dist3 = Solution().readinput(filename3)
    result = Solution().turndial2(60, dx3, dist3)
    print(f"Result: {result}")
    
    filename4 = "input.txt"
    print(f"Reading input from {filename4}")
    dx4, dist4 = Solution().readinput(filename4)
    result = Solution().turndial2(50, dx4, dist4)
    print(f"Result: {result}")

    # 5795 is too low
    # 6813 is too high
    # 6221 is too high
    # 4232 is wrong
    # 6162 is wrong
    # Answer 5815