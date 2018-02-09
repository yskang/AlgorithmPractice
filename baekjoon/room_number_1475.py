# https://www.acmicpc.net/problem/1475
import math

def number_of_set(room_number):
    room_number = room_number.replace("9", "6")
    digits = [0] * 11
    for digit in room_number:
        digits[int(digit)] += 1
    digits[6] = math.ceil(digits[6]/2)
    return max(digits)


if __name__ == "__main__":
    print(number_of_set(input()))
