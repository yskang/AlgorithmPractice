class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0

        ms = {}

        for n in nums:
            ms[n] = 1

        count = 0
        max_count = 0
        keys = list(ms.keys())
        key = keys.pop()
        check_down = True
        start = key

        while keys != []:
            if check_down:
                if key-1 in ms:
                    key = key-1
                    del ms[key]
                    count += 1
                    if count > max_count:
                        max_count = count
                else:
                    check_down = False
                    key = start
            else:
                if key+1 in ms:
                    key = key+1
                    del ms[key]
                    count += 1
                    if count > max_count:
                        max_count = count
                else:
                    check_down = True
                    key = keys.pop()
                    start = key
                    count = 0
                    
        return max_count+1
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive([]))
    print(sol.longestConsecutive([0, -1]))
    print(sol.longestConsecutive([0]))