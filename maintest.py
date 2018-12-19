# Создать класс Cigarettes, в котором есть переменные brand — марка сигарет и cost — стоимость сигарет, а также булева(Boolean) переменная is_capsul – индикатор если True, то сигареты с капсулой, если False, то без
# Создать функцию print_cigarettes внутри класса для вывода на экран марки, стоимости сигарет и индикатор того что сигареты с капсулой или без
# По классу Cigarettes создать 7 разных объектов(разных марок сигарет) с маркой, стоимостью сигарет и индикатором того того что сигареты с капсулой или без, затем для семи объектов вызвать функцию print_cigarettes -Создать функцию который возвращает список с объединённым названием марки и стоимостью у которых есть капсула -Вывести результат на экран
# Опубликовать свой код на github.com с названием репозитория bayel2_exam и добавить ksydykbekov@gmail.com как участника

class Cigarettes:
    brand = "Winston XS"
    cost = 67
    is_capsule = False

    def print_cigaretten(self, brand, cost, is_capsule):
        self.brand = brand
        self.brand = cost
        self.is_capsule = is_capsule
        print(self.brand, self.cost, self.is_capsule)

Winston_XS = Cigarettes
print("Brand:", Winston_XS.brand)
print("Cost:",Winston_XS.cost)
print("Capsule:",Winston_XS.is_capsule)

Winston_Exchange = Cigarettes
Cigarettes.brand = "Winston Exchange"
print("\nBrand:",Winston_Exchange.brand)
Cigarettes.cost = 67
print("Cost:",Winston_Exchange.cost)
Cigarettes.is_capsule = True
print("Capsule:",Winston_Exchange.is_capsule)

Esse = Cigarettes
Cigarettes.brand = "Esse"
print("\nBrand:",Esse.brand)
Cigarettes.cost = 82
print("Cost:",Esse.cost)
Cigarettes.is_capsule = False
print("Capsule:",Esse.is_capsule)

Esse_Exchange = Cigarettes
Cigarettes.brand = "Esse Exchange"
print("\nBrand:",Esse_Exchange.brand)
Cigarettes.cost = 82
print("Cost:",Esse_Exchange.cost)
Cigarettes.is_capsule = False
print("Capsule:",Esse_Exchange.is_capsule)

Marlboro = Cigarettes
Cigarettes.brand = "Marlboro"
print("\nBrand:",Marlboro.brand)
Cigarettes.cost = 87
print("Cost:",Marlboro.cost)
Cigarettes.is_capsule = False
print("Capsule:",Marlboro.is_capsule)

Richmond = Cigarettes
Cigarettes.brand = "Richmond"
print("\nBrand:",Richmond.brand)
Cigarettes.cost = 100
print("Cost:",Richmond.cost)
Cigarettes.is_capsule = False
print("Capsule",Richmond.is_capsule)

Philip_Morris = Cigarettes
Cigarettes.brand = "Philip Morris"
print("\nBrand:",Philip_Morris.brand)
Cigarettes.cost = 95
print("Cost:",Philip_Morris.cost)
Cigarettes.is_capsule = False
print("Capsule:",Philip_Morris.is_capsule)

Polet = Cigarettes
Cigarettes.brand = "Polet"
print("\nBrand:",Polet.brand)
Cigarettes.cost = 50
print("Cost:",Polet.cost)
Cigarettes.is_capsule = False
print("Capsule:",Polet.is_capsule)

brand_dictionary = {
    "Winston_XS":False,
    "Winston_Exchange": True,
    "Esse": False,
    "Esse_Exchange": True,
    "Marlboro":False,
    "Richmond": False,
    "Philip_Morris": True,
    "Polet": False
}

for x,capsule in brand_dictionary.items():
    if capsule == True:
        print(x, capsule)


