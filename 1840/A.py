import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    ans = []
    cur = s[0]
    i = 1
    while i < n:
        if s[i] == cur:
            ans.append(s[i])
            i += 1
            if i < n:
                cur = s[i]
        i += 1
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
