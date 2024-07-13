#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# when on same position, 
# they will collide, die low health robot, decrase health by -1 of high health robot
# same health, both die
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []
        for i in range(len(positions)):
            robots.append((positions[i], healths[i], directions[i], i)) # (position, health, direction, number)
        robots.sort(key=lambda x: x[0]) # sort by position
        robots = deque(robots)
        stack = []
        while robots:
            position, health, direction, number = robots.popleft()
            if direction == 'R':
                stack.append((position, health, direction, number))
            else:
                if not stack:
                    stack.append((position, health, direction, number))
                elif stack[-1][2] == 'L':
                    stack.append((position, health, direction, number))
                elif stack[-1][2] == 'R':
                    if stack[-1][1] == health:
                        stack.pop()
                    elif stack[-1][1] > health:
                        p, h, d, n = stack.pop()
                        stack.append((p, h-1, d, n))
                    else:
                        while stack and stack[-1][1] < health and stack[-1][2] == 'R':
                            stack.pop()
                            health -= 1
                        if not stack:
                            stack.append((position, health, direction, number))
                        elif stack[-1][1] == health and stack[-1][2] == 'R':
                            stack.pop()
                        elif stack[-1][1] > health and stack[-1][2] == 'R':
                            p, h, d, n = stack.pop()
                            stack.append((p, h-1, d, n))
                        else:
                            stack.append((position, health, direction, number))
        stack = list(stack)
        stack = sorted(stack, key=lambda x: x[3])
        stack = list(map(lambda x: x[1], stack))
        return stack
        
# @lc code=end

def main():
    sol = Solution()
    positions = [50,28,19,16,47,41,4,23,3]
    healths = [30,45,19,44,45,38,5,33,46]
    directions = "LLLLLRLRL"
    ret = sol.survivedRobotsHealths(positions, healths, directions)
    print(ret)


if __name__ == "__main__":
    main()