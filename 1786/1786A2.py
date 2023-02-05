from itertools import chain


def solution():
    n = int(input())
    players = [[1, 0], [0, 0]]
    n -= 1
    i = 2
    j = 1
    color = 1
    while n >= 2 * i + 1:
        k = (2 * i + 1) // 2
        players[j][color] += k + 1
        players[j][color ^ 1] += k
        n -= 2 * i + 1
        i += 2
        j ^= 1
        color ^= 1
    if n % 2 == 1:
        k = n // 2
        players[j][color] += k + 1
        players[j][color ^ 1] += k
    else:
        k = n // 2
        players[j][color] += k
        players[j][color ^ 1] += k
    print(*chain.from_iterable(players))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
