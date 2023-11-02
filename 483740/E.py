def solution():
    s = input()
    t = input()
    c = 0
    n = len(s)
    m = len(t)
    i = n - 1
    j = m - 1
    while i >= 0 and j >= 0 and s[i] == t[j]:
        c += 1
        i -= 1
        j -= 1
    print(n + m - 2 * c)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
