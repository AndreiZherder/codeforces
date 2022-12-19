from functools import reduce


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    print(reduce(lambda x, y: x | y, a) - reduce(lambda x, y: x & y, a))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
