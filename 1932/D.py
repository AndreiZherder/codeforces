from collections import defaultdict
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    trump = input()
    cards = input().split()
    d = defaultdict(list)
    for card in cards:
        d[card[1]].append(card[0])
    x = sum(len(d[suit]) % 2 for suit in d if suit != trump)
    if len(d[trump]) < x or (len(d[trump]) - x) % 2 != 0:
        print('IMPOSSIBLE')
        return
    for suit in d:
        d[suit].sort()
    ans = []
    for suit in d:
        if suit != trump:
            i = 0
            j = len(d[suit]) - 1
            while j - i + 1 > 1:
                ans.append(f'{d[suit][i]}{suit} {d[suit][j]}{suit}')
                i += 1
                j -= 1
            if j - i + 1 == 1:
                ans.append(f'{d[suit][i]}{suit} {d[trump].pop()}{trump}')
    suit = trump
    i = 0
    j = len(d[suit]) - 1
    while j - i + 1 > 1:
        ans.append(f'{d[suit][i]}{suit} {d[suit][j]}{suit}')
        i += 1
        j -= 1
    print('\n'.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
