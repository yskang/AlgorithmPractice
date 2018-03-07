class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        water = 0
        level = height[0]
        last_index = 0
        last_water = 0
        for i in range(1, len(height)):
            if height[i] < level:
                water += level - height[i]
            else:
                level = height[i]
                last_index = i
                last_water = water
        level = height[-1]
        water = last_water
        for i in range(len(height)-2, last_index-1, -1):
            if height[i] < level:
                water += level - height[i]
            else:
                level = height[i]

        return water



if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))