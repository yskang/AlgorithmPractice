import sys

if __name__ == '__main__':
    n, m = list(map(int, sys.stdin.readline().strip().split(' ')))
    nums = [x for x in range(1, n+1)]
    josephus_list = []
    while nums:
        temp = []
        while len(temp) < m:
            temp = temp + nums
        josephus_list.append(temp[m-1])
        i = nums.index(josephus_list[-1])
        nums = nums[i+1:] + nums[:i]

    print("<{}>".format(", ".join(list(map(str, josephus_list)))))