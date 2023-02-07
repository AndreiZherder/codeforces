

def sum_of_digits(num: int) -> int:
    ans = 0
    while num:
        ans += num % 10
        num //= 10
    return ans


def solution():

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int):
        id1 = find(i)
        id2 = find(j)
        if id1 == id2:
            return
        if rank[id1] > rank[id2]:
            parent[id2] = id1
            right[id1] = max(right[id1], right[id2])
        else:
            parent[id1] = id2
            if rank[id1] == rank[id2]:
                rank[id2] += 1
            right[id2] = max(right[id1], right[id2])

    n, q = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    parent = [i for i in range(n + 1)]
    rank = [1 for i in range(n + 1)]
    right = [i + 1 for i in range(n + 1)]
    while q:
        cmd = input().split()
        if cmd[0] == '1':
            l, r = int(cmd[1]) - 1, int(cmd[2]) - 1
            i = l
            while i <= r:
                if a[i] > 9:
                    a[i] = sum_of_digits(a[i])
                    if a[i] < 10:
                        if i > 0:
                            union(i, i - 1)
                else:
                    if i > 0:
                        union(i, i - 1)
                i = right[find(i)]
        else:
            print(a[int(cmd[1]) - 1])
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
