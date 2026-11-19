class StockItem:
    def __init__(self, article, name, size, price, available):
        if available < 0:
            raise ValueError("Invalid quantity")
        self.name = name
        self.article = article
        self.size = size
        self.price = price
        self._available = available
        self._reserved = 0
    @property
    def available(self):
        return self._available
    @property
    def reserved(self):
        return self._reserved

    def reserve(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity")
        if quantity <= self._available:
            self._reserved += quantity
            self._available -= quantity
        else:
            raise ValueError("Invalid quantity")

    def cancel_reservation(self, quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid quantity")
        if quantity > self._reserved:
            raise ValueError("Invalid quantity")
        else:
            self._reserved -= quantity
            self._available += quantity

# res = StockItem(12311, "шапка", "one size", 3500, 3)
# res.reserve(2)
# print(res.available)
# try:
#     res.reserve(2)
# except ValueError:
#     print("ошибка")
# print(res.available)
# res.cancel_reservation(1)
# print(res.available)

catalog = [
    StockItem("K01", "Кеды", 39, 3000, 3),
    StockItem("K01", "Кеды", 40, 3000, 2),
    StockItem("B01", "Ботинки", 42, 5000, 1),
    StockItem("B01", "Ботинки", 43, 5000, 0),
]

def show_stocks():
    for item in catalog:
        print(f"{item.article}; Название: {item.name}; размер: {item.size}; цена: {item.price} руб; доступно: {item.available}")
# show_stocks()

def find_stock(catalog, article, size):
    for item in catalog:
        if item.article == article and item.size == size:
            return item
    return None


def show_reservations():
    total = 0
    reserv_position = False
    for item in catalog:
        if item.reserved > 0:
            cost = item.price * item.reserved
            print(f"{item.reserved} стоимоть: {cost} руб")
            total += cost
            reserv_position = True
    if not reserv_position:
        print("не зарезервировано")
    else:
        print(total)
# show_reservations()

def main():
    while True:
        print("0. Выход")
        print("1. Показать каталог")
        print("2. Зарезервировать пары")
        print("3. Отменить резерв")
        print("4. Показать резерв")
        choice = input("выберите команду: ")

        if choice == "0":
            print("до свидания!")
            break
        elif choice == "1":
            show_stocks()
        elif choice == "2":
            article = input("введите артикул: ")
            try:
                size = int(input("введите размер: "))
                quantity = int(input("введите количество: "))
            except ValueError:
                print("ошибка. размер и количество не числа")
                continue

            item = find_stock(catalog, article, size)
            if item is None:
                print("Товар не найден.")
            else:
                try:
                    item.reserve(quantity)
                    print(f"зарезервировано {quantity} кол-во")
                except ValueError:
                    print(f"ошибка")

        elif choice == "3":
            article = input("введите артикул: ")
            try:
                size = int(input("Введите размер: "))
                quantity = int(input("Введите количество: "))
            except ValueError:
                print("ошибка. размер и количество не числа")
                continue

            item = find_stock(catalog, article, size)
            if item is None:
                print("товар не найден")
            else:
                try:
                    item.cancel_reservation(quantity)
                    print(f"отменено {quantity}")
                except ValueError:
                    print(f"ошибка")

        elif choice == "4":
            show_reservations()
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()




