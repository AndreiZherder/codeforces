import sys


def solution():
    row = '\n'
    while row == '\n':
        row = sys.stdin.readline()
    a = [row.strip()]
    for i in range(7):
        row = sys.stdin.readline().strip()
        a.append(row)
    for i in range(8):
        if a[i] == 'RRRRRRRR':
            print('R')
            return
    print('B')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
