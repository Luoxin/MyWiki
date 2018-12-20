
# 常用的计算
a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

a += b
print(a)

print("*" * 40)
# 判断语句
if a == 3:
    print("a == 1")

print("*" * 40)
if a != 3:
    print("a == 1")
elif b == 2:
    print("b == 2")

print("*" * 40)
if a != 3:
    print("a == 1")
elif b != 2:
    print("b == 2")
else:
    print("other")

print("*" * 40)
# 循环语句
for index, value in enumerate(range(10)):  # range是创建一个list
    print(index, value)