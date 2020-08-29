n = int(input("Enter the number? "))
boolean = int(input("Enter 1 for True and 0 for False (mean Reverse order)? "))
if boolean == 1:
    for i in range(0, n):
        for x in range(i+1):
            print("* ", end="")
        print("\n", end="")

if boolean == 0:
    for i in range(n, 0, -1):
        for x in range(i):
            print("* ", end="")
        print("\n", end="")