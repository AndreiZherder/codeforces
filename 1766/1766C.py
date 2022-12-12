from copy import deepcopy


def solution():
    def paint(i: int) -> bool:
        j = 0
        while j < n:
            if s[i][j] == 'B':
                s[i][j] = 'W'
                if s[i ^ 1][j] == 'B':
                    i ^= 1
                    continue
                else:
                    j += 1
            else:
                return False
        return True

    n = int(input())
    s1 = [list(input()), list(input())]
    s = deepcopy(s1)
    if paint(0):
        print('YES')
        return
    s = deepcopy(s1)
    if paint(1):
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
