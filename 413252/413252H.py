from collections import Counter


def solution():
    s = input()
    cnt = Counter(s)
    cnt['u'] //= 2
    cnt['a'] //= 2
    print(min(cnt[c] for c in "Bulbsar"))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
