vvp = int(input("введите доход >>>"))
cost = int(input("введите издержки >>>"))

prft = vvp - cost
if prft < 0:
    print("извините, контора убыточная")
if prft > 0:
    print("прибыльная контора, рентвбельность", vvp / cost)
    men = int(input("введите количество сотрудников >>>"))
    print("рентвбельность на человека", (vvp - cost) / men)
    19
