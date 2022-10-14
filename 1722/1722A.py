from collections import Counter


def solution():
    n = int(input())
    s = input()
    if Counter(s) == Counter('Timur'):
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
