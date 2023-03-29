import sys
from typing import List

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def get_digits(num: int) -> List[int]:
        ans = []
        while num:
            ans.append(num % 10)
            num //= 10
        return ans

    a, b = [int(num) for num in input().split()]
    if a > b:
        a, b = b, a
    digits_a = get_digits(a)
    digits_b = get_digits(b)
    if len(digits_a) < len(digits_b):
        print('9' * len(digits_a))
        return
    digits_a.reverse()
    digits_b.reverse()

    x = str(digits_a[0]) * len(digits_a)
    if ''.join(map(str, digits_a)) < x < ''.join(map(str, digits_b)):
        print(str(digits_a[0]) * len(digits_a))
        return

    x = str(digits_b[0]) * len(digits_b)
    if  ''.join(map(str, digits_a)) < x < ''.join(map(str, digits_b)):
        print(str(digits_b[0]) * len(digits_b))
        return

    ans = []
    for i in range(len(digits_a)):
        if digits_a[i] <= digits_a[0]:
            ans.append(digits_a[0])
        else:
            ans.append(digits_a[i])



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
