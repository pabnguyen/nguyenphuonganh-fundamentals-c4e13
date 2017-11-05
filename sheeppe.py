#1
print("Hello, my name is Hiep and here is my sheep sizes:")

size= [5,7,300,90,24,50,75]
n= max(size)

print ("Now my biggest sheep has the size", n, "let's shear it")

#2
print("Hello, my name is Hiep and here is my sheep sizes:")

size= [5,7,300,90,24,50,75]
n= max(size)
size.remove(n)

print ("Now my biggest sheep has the size", n, "let's shear it")
print ("After shearing, here is my flock",*size)

#3
print("Hello, my name is Hiep and here is my sheep sizes:")

size= [5,7,300,90,24,50,75]
n= max(size)
size.remove(n)

print ("Now my biggest sheep has the size", n, "let's shear it")
print ("After shearing, here is my flock",*size)


#4

print("Hello, my name is Hiep and here is my sheep sizes:")

size= [5,7,300,90,24,50,75]
n= max(size)
size.remove(n)

print ("Now my biggest sheep has the size", n, "let's shear it")
print ("After shearing, here is my flock",*size)

size= [50+5,50+7,50+90,50+24,50+50,75+50]

print ("One month has passed, now my flock is:", size)
