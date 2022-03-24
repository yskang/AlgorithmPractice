# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


def is_bad_version(version):
    if version >= 100:
        return True
    else:
        return False


class Solution(object):
    def first_bad_version(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n

        while True:
            if not is_bad_version(start - 1 + int((end-start) / 2)) \
               and is_bad_version(start + int((end-start)/2)):
                return start + int((end-start)/2)

            if is_bad_version(start + int((end - start) / 2)):
                end = start + int((end-start)/2)
            else:
                start += int((end - start) / 2)

            if start == n-1 and end == n:
                return n


sol = Solution()
print(sol.first_bad_version(100))
