weight = int(input("what is your weight? "))
unit=input("kg or l: ").lower()
if unit.lower() == "l":
    converted=weight*0.5
    print(f"you are {converted} kilos")
elif unit == "kg":
    converted = weight / 0.5
    print(f"you are {converted} pounds")
else:
    print(" I don't understand this commmand please")