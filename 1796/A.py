import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    k = int(input())
    s = input()
    f = []
    for i in range(1, 61):
        if i % 3 == 0:
            f.append('F')
        if i % 5 == 0:
            f.append('B')
    f = ''.join(f)
    if s in f:
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
