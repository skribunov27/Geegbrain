a = list(input("введите слова через пробел>>>"))
# print(a)
length=0
for i in range(len(a)):
    if (a[i] != " ") and (length<10):
        print(a[i], end="")

    if a[i] == " ":
        print()
        length=0
    length+=1