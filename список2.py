l = int(input("введите длину списка>>>"))
print(l)
a = [0] * l
for i in range(len(a)):
    a[i] = int(input("введите элемент списка>>>"))

# print(a)

for i in range(len(a)):
    if i % 2==1:
        a[i], a[i - 1] = a[i - 1], a[i]

print(a)
