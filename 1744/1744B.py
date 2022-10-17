

def solution():
    n, q = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    queries = []
    for i in range(q):
        queries.append([int(num) for num in input().split()])
    even = 0
    odd = 0
    s = 0
    for num in a:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        s += num
    ans = []
    for type, x in queries:
        if type == 0:
            s += even * x
            ans.append(s)
            if x % 2 == 1:
                odd += even
                even = 0
        else:
            s += odd * x
            ans.append(s)
            if x % 2 == 1:
                even += odd
                odd = 0
    for num in ans:
        print(num)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
