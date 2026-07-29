def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        return
    if n == 2:
        print(max(a[0], a[1]))
        return

    prev2 = a[0]
    prev1 = max(a[0], a[1])

    for i in range(2, n):
        current = max(prev1, a[i] + prev2)
        prev2 = prev1
        prev1 = current
    print(prev1)

if __name__ == '__main__':
    solve()
