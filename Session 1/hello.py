a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))
print("Giai phuong trinh: ax^2 + bx + c")
delta = b ** 2 - (4 * a * c)
if delta < 0:
    print("No solutions")
elif delta == 0:
    x = -b / 2 * a
    print(x)
else:
    x1 = (-b + delta ** 0.5 / 2 * a)
    x2 = (-b - delta ** 0.5 / 2 * a)
    print("Two solutions: x1={0}, x2={1}".format(x1, x2))
