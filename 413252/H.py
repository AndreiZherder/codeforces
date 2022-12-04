import collections


def solution():
    s = input()
    cnt = collections.Counter(s)
    cnt['u'] //= 2
    cnt['a'] //= 2
    ans = min(cnt[c] for c in 'Bulbasr')
    print(ans)


t = 1
while t:
    solution()
    t -= 1