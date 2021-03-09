# left triangle

print("enter the number")
n = int(input())

for i in range(n):
    for j in range(n-i):       # n-1 is printing stars

        print("*", end=" ")

    print()