n = int(input("Enter a number: "))

for i in range(n):
    if (i % 2) == 0:
        print("Fizz")
    elif (i % 3) == 0:
        print("Buzz")
