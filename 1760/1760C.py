def solution():
    n = int(input())
    s = [(int(num), i) for i, num in enumerate(input().split())]
    s1 = list(sorted(s, reverse=True))
    first_max = s1[0][0]
    first_max_index = s1[0][1]
    second_max = s1[1][0]
    second_max_index = s1[1][1]
    ans = []
    for i in range(n):
        if i == first_max_index:
            ans.append(first_max - second_max)
        else:
            ans.append(s[i][0] - first_max)
    print(*ans)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
