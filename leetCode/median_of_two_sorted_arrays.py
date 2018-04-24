import bisect


class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        total_length = len(nums1) + len(nums2)
        even = False
        median = 0
        intersect = []

        if total_length % 2 == 0:
            even = True

        nums = []

        if nums1 and nums2 and nums1[0] > nums2[0]:
            nums1, nums2 = nums2, nums1

        if not nums1 or not nums2:
            nums = nums1 + nums2
        elif nums1[-1] <= nums2[0]:
            nums = nums1 + nums2
        elif nums1[-1] <= nums2[-1]:
            x = bisect.bisect_right(nums1, nums2[0])
            y = bisect.bisect_left(nums2, nums1[-1])

            nums1_front = nums1[:x]
            nums1_back = nums1[x:]

            nums2_front = nums2[:y]
            nums2_back = nums2[y:]

            while True:
                if nums1_back == []:
                    intersect = intersect + nums2_front
                    break
                elif nums2_front == []:
                    intersect = intersect + nums1_back
                    break
                elif nums1_back[0] <= nums2_front[0]:
                    intersect.append(nums1_back.pop(0))
                else:
                    intersect.append(nums2_front.pop(0))
            nums = nums1_front + intersect + nums2_back
        elif nums2[-1] <= nums1[-1]:
            x = bisect.bisect_right(nums1, nums2[0])
            y = bisect.bisect_left(nums1, nums2[-1])

            nums1_front = nums1[:x]
            nums1_middle = nums1[x:y]
            nums1_back = nums1[y:]

            while True:
                if nums1_middle == []:
                    intersect = intersect + nums2
                    break
                elif nums2 == []:
                    intersect = intersect + nums1_middle
                    break
                elif nums1_middle[0] <= nums2[0]:
                    intersect.append(nums1_middle.pop(0))
                else:
                    intersect.append(nums2.pop(0))

            nums = nums1_front + intersect + nums1_back

        if even:
            median = (nums[int(total_length / 2) - 1] + nums[int(total_length / 2)]) / 2
        else:
            median = nums[int(total_length / 2)]

        return float(median)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 4], [2, 3, 5]))
    print(sol.findMedianSortedArrays([], [1, 2, 3, 4, 5]))
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
