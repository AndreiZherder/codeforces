import sys

input = sys.stdin.readline
print_row = lambda row: sys.stdout.write(" ".join(map(str, row)) + "\n")


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]


def main():
    t = int(input())
    while t:
        solution()
        t -= 1
        print()


if __name__ == '__main__':
    main()
