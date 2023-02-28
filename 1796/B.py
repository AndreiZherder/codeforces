import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a = input()
    b = input()
    if a[0] == b[0]:
        print('YES')
        print(f'{a[0]}*')
        return
    if a[-1] == b[-1]:
        print('YES')
        print(f'*{a[-1]}')
        return
    if len(a) == 1 or len(b) == 1:
        print('NO')
        return
    n = len(a)
    for i in range(n - 1):
        p = a[i:i + 2]
        if p in b:
            print('YES')
            print(f'*{p}*')
            return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
