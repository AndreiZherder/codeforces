def solution():
    # abcdabcd
    #    i   j

    s = input()
    n = len(s)
    if s[:n // 2] == s[n // 2:]:
        print('YES')
    else:
        print('NO')


t = int(input())
while t:
    solution()
    t -= 1