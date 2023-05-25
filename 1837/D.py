import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    d = {')': '(',
         '(': ')'}
    if s.count('(') != s.count(')'):
        print(-1)
        return
    a = [0 for i in range(n)]
    stack = [s[0]]
    ans = 1
    start = 0
    for i in range(1, n):
        if not stack:
            if s[i - 1] == s[i]:
                for j in range(start, i):
                    a[j] = (ans + 1) % 2 + 1
                ans += 1
                start = i
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    for j in range(start, n):
        a[j] = (ans + 1) % 2 + 1


    if ans > 2:
        ans = 2
    print(ans)
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
