# age = int(input("Enter ur age: "))
# a = age % 10 == 0 and age >= 50
# a = age % 10 == 0 or age >= 50
# a = age % 10 == 0 not age >= 50 ???

# print(a)
# a = int(input("enter a number "))
# if (a > 0) and 

# person = input("Status of the person")

# if person == 'student' or person == 'school 10th' or person == 'school 11th':
#     print(f'Individual is more than 15 years old, cause his/her status {person}')
# else: 
#     print(f'Individual is less than 15 years old')

# personAge = input("Enter your age: ")
# try: 
#     personAge = int(personAge)
# except:
#     print("error")
# if personAge < 18:
#     print(f'this individual is teenager cause he or she at {personAge}')
# elif personAge >= 18 and personAge < 35:
#     print(f'this individual is Adult cause age is {personAge}')
# elif personAge >= 35 and personAge < 65:
#     print(f'this individual is on Middle age cause age is {personAge}')
# else:
#     print(f'this individual is on Old age cause age is {personAge}')


# list1 = [2, 3, 4, 5]
# if 2 not in list1:
#     print("yes, he is in the list")
# else: 
#     print("he is not in the list")

num1 = input("Введите делитель ")
num2 = input("введите делимое")

try:
    num1 = int(num1) 
    num2 = int(num2)    # генерирует исключение ZeroDivisionError
    num3 = num1 / num2
    print("Результат деления:", num3)
    if num3 <= 5:
        print("num3 меньше 5")
    elif num3 > 5 and num3 < 10:
        print("num3 больше 5")
    else:
        print("num3 больше или равно 10")
except:
    print("Введите корректные числа")

finally:
    print("Блок try завершил выполнение")
print("Завершение программы")


a = 5
b = 6
sum1 = a+b
print(sum1)
# a = 5
# b = 6
# sum1 = a + b
