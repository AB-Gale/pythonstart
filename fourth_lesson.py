# a = 5/3
# # print(round(a)) result = 2 округление крч
# print(round(a, 1)) 
import math as mt

# num1 = 5.8
# num2 = round(num1, 1)
# num3 = mt.ceil(num1)
# num4 = mt.floor(num1)
# num5 = mt.radians(30)
# num6 = mt.degrees(0.5235987755982988)
# num7 = mt.pow(3, 5)
# num8 = mt.sqrt(81)
# # print(math.ceil(num1))
# print(num7, num8)
# exit()
# print(num2, num3, num4, num5, num6, num7, num8)

# name1, name2, name3 = 'Jack', 'Alice', 'Bob'
# print(max(2, 4, 6, 1141, 55555)) выбирает самое большое число
# print(min(1, 32323, 5555, 1231, -1)) выбирает самое маленькое число

# l = 22
# w = 3.4
# h = 87
# v = l * w * h
# print(v)

# n = 20 
# r = mt.pow(7, 2)
# h = 8
# a = 3
# v = (n*r*h) / a 
# print(v)

# n = 5 
# r = mt.pow(2, 2)
# h = 2 
# v = n * r * h 
# print(v)

# a = 4 / 3 
# n = 5
# r = mt.pow(2, 3)
# v = a * n * r 
# print(v)

# student1 = ["Tom", 29, True, "male", "lawyer"] changable list
# numbers = [1, 2, 3, 4, 5]
people  = ["Tom", "John", "Alex", "Mason", "Ken"]
# nameList = [people[2]] * 10
# people[1] = "Bob"
# numbers[3] = 5
# len1 = len(people) показывает скок элементов в листе или переменной
# len1 = len(people)
# print(len1)
# people.append("Rust") 
# [:], [::] это значит slice 
# print(people[-1: 2:-2])start stop step 
# people[-1::] = "Snow"
# people.insert(0, "Clarke") добавляет по индексу (индекс, элемент)
# people2 = ["Jack", "Summer"]
# people2.extend(people)
# people2.remove("Ken")
# jackIndex = people.index("Jack")
# people[jackIndex] = "Ken"
# print(people)

# # people.clear()
# print("this is people", people)
# print("this is people2", people2)

# num1 = 1.4
# num2 = str(num1)
# print(num2)

# price = int(input("Enter the price: "))
# print(price)
# print(type(price))

age = int(input("Enter ur age: "))
a = age % 10 == 0
print(a)