import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input().lower()
    i = 0
    if s[i] != 'm':
        print('NO')
        return
    while i < n and s[i] == 'm':
        i += 1
    if i == n or s[i] != 'e':
        print('NO')
        return
    while i < n and s[i] == 'e':
        i += 1
    if i == n or s[i] != 'o':
        print('NO')
        return
    while i < n and s[i] == 'o':
        i += 1
    if i == n or s[i] != 'w':
        print('NO')
        return
    while i < n and s[i] == 'w':
        i += 1
    if i == n:
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
