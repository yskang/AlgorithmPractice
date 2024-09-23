#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#
from typing import List


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        current_position = (0, 0)
        current_direction = 'bottom'
        max_distance = 0
        for c in commands:
            if c == -1:
                if current_direction == 'top':
                    current_direction = 'left'
                elif current_direction == 'left':
                    current_direction = 'bottom'
                elif current_direction == 'bottom':
                    current_direction = 'right'
                elif current_direction == 'right':
                    current_direction = 'top'
            elif c == -2:
                if current_direction == 'top':
                    current_direction = 'right'
                elif current_direction == 'right':
                    current_direction = 'bottom'
                elif current_direction == 'bottom':
                    current_direction = 'left'
                elif current_direction == 'left':
                    current_direction = 'top'
            else:
                if current_direction == 'top':
                    while c > 0:
                        c -= 1
                        current_position = (current_position[0], current_position[1]-1)
                        if current_position in obstacles:
                            current_position = (current_position[0], current_position[1]+1)
                            break
                elif current_direction == 'right':
                    while c > 0:
                        c -= 1
                        current_position = (current_position[0]+1, current_position[1])
                        if current_position in obstacles:
                            current_position = (current_position[0]-1, current_position[1])
                            break
                elif current_direction == 'bottom':
                    while c > 0:
                        c -= 1
                        current_position = (current_position[0], current_position[1]+1)
                        if current_position in obstacles:
                            current_position = (current_position[0], current_position[1]-1)
                            break
                elif current_direction == 'left':
                    while c > 0:
                        c -= 1
                        current_position = (current_position[0]-1, current_position[1])
                        if current_position in obstacles:
                            current_position = (current_position[0]+1, current_position[1])
                            break
                max_distance = max(max_distance, current_position[0]**2 + current_position[1]**2)                
        return max_distance
# @lc code=end


def main():
    sol = Solution()
    commands = [4,-1,3]
    obstacles = []
    print(sol.robotSim(commands, obstacles))
    commands = [4,-1,4,-2,4]
    obstacles = [[2 , 4]]
    print(sol.robotSim(commands, obstacles))


if __name__ == "__main__":
    main()
