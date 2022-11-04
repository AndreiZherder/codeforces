def solution():
    n = int(input())
    ans = 0
    seq = []
    i = 1
    j = n
    while i <= j:
        ans += 1
        seq.append([i * 3 - 2, j * 3])
        i += 1
        j -= 1
    print(ans)
    for a, b in seq:
        print(a, b)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
