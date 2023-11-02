def solution():
    keyboard = input()
    word = input()
    lookup = {c: i for i, c in enumerate(keyboard)}
    prev = word[0]
    ans = 0
    for c in word:
        ans += abs(lookup[c] - lookup[prev])
        prev = c
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
