import random
import datetime

def merge_sort_stephen(nums):
    half = int(len(nums) / 2)
    if half:
        left, right = merge_sort_stephen(nums[:half]), merge_sort_stephen(nums[half:])
        for i in range(len(nums))[::-1]:
            if not right or left and left[-1] > right[-1]:
                nums[i] = left.pop()
            else:
                nums[i] = right.pop()
    return nums


def merge_sort_rosetta(nums):
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2
    left = nums[:middle]
    right = nums[middle:]

    left = merge_sort_rosetta(left)
    right = merge_sort_rosetta(right)
    return list(merge(left, right))


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result


def random_gen_list(count):
    nums = []
    for _ in range(count):
        nums.append(random.randrange(-10000, 10000))
    return nums


def sort(nums, merge_function):
    start_time = datetime.datetime.now()
    _ = merge_function(nums)
    end_time = datetime.datetime.now()
    diff_time = end_time - start_time
    print(diff_time)

if __name__ == "__main__":
    nums = random_gen_list(1000000)
    sort(nums, merge_sort_stephen)
    sort(nums, merge_sort_rosetta)
