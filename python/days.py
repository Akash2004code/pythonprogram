num =int(input("enetr a number ftom 1 to 7:"))
days={
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday",
   

}
if 1 <= num <=7:
    print("the day is ",days[num])
else:
    print("entewer numbetween  to 7")
