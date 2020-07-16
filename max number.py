a = int(input("введите целое число от нуля до 1000 >>>"))
m = a % 10
n = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    if a % 10 < n:
        n = a % 10
    a = a // 10
print("max=", m, "min=", n)
