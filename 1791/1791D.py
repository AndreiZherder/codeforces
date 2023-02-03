from collections import Counter


def solution():
    n = int(input())
    s = input()
    cnt1 = Counter(s[0])
    cnt2 = Counter(s[1:])
    best = len(cnt1) + len(cnt2)
    for c in s[1:n - 1]:
        cnt1[c] += 1
        cnt2[c] -= 1
        if cnt2[c] == 0:
            del cnt2[c]
        best = max(best, len(cnt1) + len(cnt2))
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
