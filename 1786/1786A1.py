def solution():
    n = int(input())
    players = [1, 0]
    n -= 1
    i = 2
    j = 1
    while n >= 2 * i + 1:
        players[j] += 2 * i + 1
        n -= 2 * i + 1
        i += 2
        j ^= 1
    players[j] += n
    print(*players)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
