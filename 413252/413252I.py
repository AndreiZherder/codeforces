from collections import defaultdict


def solution():
    def dfs(node: int) -> bool:
        if not tree[node]:
            return True
        cnt = 0
        ok = False
        for child in tree[node]:
            if not tree[child]:
                cnt += 1
                if cnt > 2:
                    ok = True
                    break
        if not ok:
            return False
        else:
            return all(dfs(child) for child in tree[node])


    n = int(input())
    tree = defaultdict(list)
    for child in range(2, n + 1):
        parent = int(input())
        tree[parent].append(child)
    if dfs(1):
        print('YES')
    else:
        print('NO')



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
