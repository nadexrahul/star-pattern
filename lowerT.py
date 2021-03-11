print("enter the number")
n = int(input())

for i in range(n):
    for j in range(n*2-1):
        if j >= i and j <= 2*n-2-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()