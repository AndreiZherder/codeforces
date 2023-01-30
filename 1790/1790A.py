def solution():
    pi = '314159265358979323846264338327'
    s = input()
    n = len(s)
    ans = 0
    for a, b in zip(s, pi[:n]):
        if a == b:
            ans += 1
        else:
            break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
