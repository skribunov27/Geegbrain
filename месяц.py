mon = int(input("введите число месяца>>>"))
a = ["лето", "осень", "зима", "весна"]

if (mon<3) or (mon==12) :
    print ("это", a[2])
if 2<mon<6:
    print("это", a[3])
if 5<mon<9:
    print("это", a[0])
if 8<mon<12:
    print("это", a[1])