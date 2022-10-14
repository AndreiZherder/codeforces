

def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    s = set(a)
    if len(a) == len(s):
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
