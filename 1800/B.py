import string
import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = (int(num) for num in input().split())
    s = input()
    cnt = {c: [0, 0] for c in string.ascii_lowercase}
    for c in s:
        if c.islower():
            cnt[c.lower()][0] += 1
        else:
            cnt[c.lower()][1] += 1
    ans = 0
    for c in cnt:
        ans += min(cnt[c][0], cnt[c][1])
        x = (max(cnt[c][0], cnt[c][1]) - min(cnt[c][0], cnt[c][1])) // 2
        y = min(x, k)
        ans += y
        k -= y
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
