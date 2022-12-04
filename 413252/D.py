def solution():
    s = input()
    n = len(s)
    s += 'A'
    ans = 0
    j = -1
    for i in range(n + 1):
        if s[i] in 'AEIOUY':
            ans = max(ans, i - j)
            j = i
    print(ans)


t = 1
while t:
    solution()
    t -= 1