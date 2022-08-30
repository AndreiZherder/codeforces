


def solution():
    n = int(input())
    s = input()
    total = 0
    for i, c in enumerate(s):
        if c == 'L':
            total += i
        else:
            total += n - i - 1
    ans = []
    i = 0
    j = 0
    for k in range(1, n + 1):
        while i < n // 2 and s[i] == 'R':
            i += 1
        while j < n // 2 and s[n - j - 1] == 'L':
            j += 1
        if i == n // 2 and j == n // 2:
            ans.append(total)
            continue
        if i <= j:
            total -= i
            total += n - i - 1
            ans.append(total)
            i += 1
        else:
            total -= j
            total += n - j - 1
            ans.append(total)
            j += 1
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
