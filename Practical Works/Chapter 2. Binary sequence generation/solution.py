def binary(i, n, lst):
    if i == n:
        print("".join(map(str, lst)))
        return
    
    for k in (0, 1):
        lst[i] = k
        binary(i + 1, n, lst) 

n = int(input())
binary(0, n, [0] * n)
