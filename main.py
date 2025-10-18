from app import services, reports, utils

MENU = """
1. Добавить клиента
2. Список клиентов
3. Добавить запчасть
4. Список запчастей
5. Добавить заказ
6. Список заказов
9. Экспорт в Excel
10. Экспорт в PDF
0. Выйти
"""

def main():
    while True:
        print(MENU)
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Имя клиента: ")
            phone = input("Телефон: ")
            services.add_client(name, phone)
        elif choice == "2":
            utils.print_table(services.list_clients(), ["ID", "Имя", "Телефон"])
        elif choice == "3":
            name = input("Название запчасти: ")
            price = float(input("Цена: "))
            services.add_part(name, price)
        elif choice == "4":
            utils.print_table(services.list_parts(), ["ID", "Название", "Цена"])
        elif choice == "5":
            client_id = int(input("ID клиента: "))
            description = input("Описание ремонта: ")
            cost = float(input("Стоимость: "))
            services.add_order(client_id, description, cost)
        elif choice == "6":
            utils.print_table(
                services.list_orders(),
                ["ID", "Клиент", "Описание", "Статус", "Стоимость", "Дата"]
            )
        elif choice == "9":
            reports.export_to_excel()
        elif choice == "10":
            reports.export_to_pdf()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
