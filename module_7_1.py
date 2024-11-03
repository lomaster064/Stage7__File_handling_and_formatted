class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__filename = 'products.txt'

    def get_products(self):
        file_name = self.__filename
        file = open(file_name, 'r')
        res = file.read()
        file.close()
        return res

    def add(self, *products):
        file_name = self.__filename
        file = open(file_name, 'a')
        for i in products:
            file_str = self.get_products()
            value = str(i)
            if value not in file_str:
                file.write(value + '\n')
            else:
                print(f'Продукт {value} уже есть в магазине')

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
print()

s1.add(p1, p2, p3)

print(s1.get_products())
