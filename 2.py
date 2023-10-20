name = input("what is your name: ")
if len(name) <3:
    print("name has to be more than five characters")
elif len(name) > 15:
    break
else:
    print ('hello Mr/Mrs ' + name)
DOB =int(input ('what is your date of birth? '))
age = (int('2022') - DOB)
print(age)
color = input('which color do you like most? ')
print (color)
home = input('which city do you come from')


