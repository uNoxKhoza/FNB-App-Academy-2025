#Control statements

age = 21

if age < 16:
    print('this user is under age')
else:
    print('User Accepted')

#Inputs

num1 = int(input('Enter first number:  '))
num2 = int(input('Enter the second number:  '))

if num1 > num2:
    print(num1,'It is greater', num2)
elif num2 > num1:
    print(num2, 'is greater than' , num1)  
else:
    print('Both numbers are equal')