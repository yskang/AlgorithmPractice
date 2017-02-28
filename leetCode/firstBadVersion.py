# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def isBadVersion(version):
    if version >= 100:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n

        while True:
            if isBadVersion(start - 1 + int((end-start) / 2)) == False and isBadVersion(start + int((end-start)/2)) == True:
                return start + int((end-start)/2)

            if isBadVersion(start + int((end - start) / 2)):
                end = start + int((end-start)/2)
            else:
                start += int((end - start) / 2)

            if start == n-1 and end == n:
                return n





sol = Solution()
print(sol.firstBadVersion(100))