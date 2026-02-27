t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] <= max(2*i, 2*(n-i-1)):
            print("NO")
            break
    else:
        print("YES")