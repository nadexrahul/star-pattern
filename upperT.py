print("enter the number")
n = int(input())

for i in range(n):
    for j in range(n*2-1):
        if j >= n-i+1 and j <= n+i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()