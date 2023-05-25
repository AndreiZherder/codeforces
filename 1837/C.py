import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    cur = '0'
    ans = []
    for c in s:
        if c != '?':
            ans.append(c)
            cur = c
        elif cur == '1':
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
