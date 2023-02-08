import sys

input = sys.stdin.readline
print_nums = lambda nums: print(' '.join(str(num) for num in nums))
print_strings = lambda strings: print(' '.join(string for string in strings))


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
