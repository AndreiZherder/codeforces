def solution():
    n = 10 - int(input())
    input()
    d = {2: 1,
         3: 3,
         4: 6,
         5: 10,
         6: 15,
         7: 21,
         8: 28,
         9: 36}
    print(d[n] * 6)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
