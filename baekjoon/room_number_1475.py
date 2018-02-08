# https://www.acmicpc.net/problem/1475

def number_of_set(room_number):
    digits = [0]*11
    for digit in room_number:
        digits[int(digit)] += 1
    digits[6] = digits[6] + digits[9]
    digits[9] = 0
    max_count = -1
    for i in range(11):
        if i != 6 and digits[i] > max_count:
            max_count = digits[i]
    if digits[6] % 2 == 0:
        need_for_6 = digits[6]/2
    else:
        need_for_6 = (digits[6]+1)/2

    if need_for_6 > max_count:
        return int(need_for_6)
    return int(max_count)


if __name__ == "__main__":
    print(number_of_set(input()))
