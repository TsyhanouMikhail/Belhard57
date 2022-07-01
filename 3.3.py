# Пользователь вводит Имя, Возраст и Город, сформировать #
# приветственное сообщение путем форматирования 3-мя способами #

name: str = input("Имя: ")
#print(name)

age: int = input("Возраст: ")
#print(age)

city: str = input("Город: ")
#print(city)

#1
print("Привет", age, "-летний,", name, ", из города", city, ".") #1

#2
hello = "Привет " + name + ", " + age + " лет(года)" + ", из города " + city + "."
print(hello) #2

#3
name1: str = ""
name1 += name
name1 += " Привет! "
name1 += age
name1 += " лет(года), из города "
name1 += city
name1 += "."
print(name1) #3

#4
text = "Привет {name}, {age}-летний, из города {city}." .format(name=name, age=age, city=city)
print(text)#4

#5
text = f"Привет {name}, {age}-летний, из города {city}."
print(text)#5




