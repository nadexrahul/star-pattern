# left triangle
print("enter the number")
n = int(input())
for i in range(n):
    for j in range(n+1):
        if j >= n-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()