class Solution(object):
    def wordPattern(self, pattern, str):
        dic = {}
        dic2 = {}
        words = str.split(" ")

        if len(pattern) != len(words):
            return False

        i = 0
        for cha in pattern:
            if cha in dic.keys():
                if dic[cha] != words[i]:
                    return False

            else:
                dic[cha] = words[i]
            i += 1
        i = 0
        for word in words:
            if word in dic2.keys():
                if dic2[word] != pattern[i]:
                    return False
            else:
                dic2[word] = pattern[i]
            i += 1

        return True

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog"))
print(solution.wordPattern("abba", "dog cat cat fish"))
print(solution.wordPattern("aaaa", "dog cat cat dog"))
print(solution.wordPattern("abba", "dog dog dog dog"))