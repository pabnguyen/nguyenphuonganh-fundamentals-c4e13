n = int(input("How many rows do you want? "))
m = int(input("How many columns do you want? "))


for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if j % 2 == 0:
                print("x", end = " ")
            else:
                print("*", end = " ")
        print()
    else:
        for j in range(m):
            if j % 2 == 0:
                print("*", end = " ")
            else:
                print("x", end = " ")
        print()
