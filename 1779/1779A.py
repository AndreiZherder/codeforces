def solution():
    n = int(input())
    s = input()
    if 'RL' in s:
        print(0)
        return
    i = s.find('LR')
    if i != -1:
        print(i + 1)
    else:
        print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
