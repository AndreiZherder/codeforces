import sys
from typing import Tuple, List

input = sys.stdin.readline
print_list = lambda arr: sys.stdout.write(" ".join(map(str, arr)) + "\n")


def sum_of_digits(num: int) -> Tuple[int, List[int]]:
    if num == 0:
        return 0, [0]
    total = 0
    digits = []
    while num:
        digit = num % 10
        total += digit
        digits.append(digit)
        num //= 10
    return total, digits


def solution():
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2)
        return
    x = n // 2
    y = n - x
    total1, digits1 = sum_of_digits(x)
    total2, digits2 = sum_of_digits(y)
    if total2 > total1:
        digits1, digits2 = digits2, digits1
        total1, total2 = total2, total1
    delta = total1 - total2
    i = 0
    while delta > 1:
        sub = min(delta // 2, digits1[i], 9 - digits2[i])

        digits1[i] -= sub
        digits2[i] += sub
        delta -= sub * 2
        i += 1
    print(''.join(str(digit) for digit in digits1[::-1]), ''.join(str(digit) for digit in digits2[::-1]))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
