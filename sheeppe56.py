#5
sheep_size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Long and these are my sheep sizes:")
print(sheep_size)
print()

month_number = int(input("How many months later do you want to see my flock? "))
print()

for j in range(month_number):
    print("MONTH ", j+1, " :")
    for i in range(len(sheep_size)):
        sheep_size[i] += 50
    print("One month has passed, now here is my flock")
    print(sheep_size)

    max = sheep_size[0]

    for i in range(len(sheep_size)):
        if max < sheep_size[i]:
            max = sheep_size[i]
    print("Now my biggest sheep has size ", max, " let's shear it")


    for i in range(len(sheep_size)):
        if sheep_size[i] == max:
            index_max = i
            break
    sheep_size[index_max] = 8
    print("After shearing, here is my flock")
    print(sheep_size)
    print()
