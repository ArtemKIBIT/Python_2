from Menu import menu, orders, ingredients, available_ingredients, categories

def show_menu():
    print("\nМеню:")
    for dish, price in menu.items():
        print(f"{dish} - {price} грн")

def add_order():
    dish = input("Введіть назву страви: ")
    if dish in menu:
        orders.append(dish)
        print(f"Додано '{dish}' до замовлення.")
    else:
        print("Страви немає у меню.")

def show_orders():
    if orders:
        print("\nВаше замовлення:", ", ".join(orders))
    else:
        print("\nЗамовлення порожнє.")

def show_ingredients():
    dish = input("Введіть назву страви: ")
    if dish in ingredients:
        print(f"Інгредієнти {dish}: {', '.join(ingredients[dish])}")
    else:
        print("Немає інформації.")

def calculate_total():
    total = sum(menu[dish] for dish in orders)
    print(f"Загальна вартість: {total} грн")

def manage_ingredients():
    print("\nНаявні інгредієнти:", available_ingredients)
    required = {"помідор", "огірок", "олія", "часник"}
    print("Спільні:", available_ingredients & required)
    print("Відсутні:", required - available_ingredients)

def show_categories():
    idx = int(input("Введіть індекс категорії (0-3): "))
    if 0 <= idx < len(categories):
        print("Категорія:", categories[idx])
    else:
        print("Невірний індекс.")

while True:
    print("\n1-Показати меню | 2-Додати до замовлення | 3-Показати замовлення | 4-Інгредієнти страви")
    print("5-Підрахувати вартість | 6-Інгредієнти | 7-Категорії | 0-Вийти")
    choice = input("Ваш вибір: ")

    if choice == "1": show_menu()
    elif choice == "2": add_order()
    elif choice == "3": show_orders()
    elif choice == "4": show_ingredients()
    elif choice == "5": calculate_total()
    elif choice == "6": manage_ingredients()
    elif choice == "7": show_categories()
    elif choice == "0":
        print("\nДякуємо за візит!")
        break
    else:
        print("Невірний вибір.")