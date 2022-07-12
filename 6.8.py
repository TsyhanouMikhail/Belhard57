# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

belarus_: list = ["Minsk", "Bobrujsk", "Grodno", "1", "5", "4"]
russia_: list = ["Omsk", "Moskau", "1"]
usa_: list = ["NY", "Boston", "3", "88", "99"]

users = {
    "Belarus": belarus_,
    "Russia": russia_,
    "USA": usa_
}

print(users)

gorod = str(input("Введите город "))
gorod_: str = str()
for key, user in users.items():
    if gorod in user:
        gorod_ = gorod_ + ", " + key

    else:
        pass

if gorod_:
    print("Введенный город из стран(ы): ", gorod_)
else:
    print("Введенный город отсутствует в списке")


