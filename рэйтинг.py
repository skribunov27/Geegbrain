my_list = [8, 5, 3, 2, 1]
l = int(input("введите число>>>"))

maxx = 0
ind = 0
for i in range(len(my_list)):
    if my_list[i] > l:
        ind = i
my_list.insert(ind + 1, l)
print(my_list)
