# Узагальнення вивченого за семестр
# Проєкт "Автоматизований обмін валют
"""
Створити проєкт-прогрму для підтримки роботи пункту обміну валют, 
у якому користувач буде обирати один вид валюти для перетворення 
його у ніший вид валюти.
"""
"""
     Переглянь запропонований текст програми (вихідний код)
     Виконай вказівки у рядках коментірів (позначені символами ##)
"""

# Підготовка
## дізнайся поточний валютний курс та за необхідності внеси зміни у рядки нижче
dolar = 41.44
euro = 47.11

# Вітання
print("\n" * 100)
print("Вас вітає обмінник валют")
print("1. Перейти до обміну")
print("2. Вийти")
x = int(input("Зробіть свій вибір та введіть номер опції: "))
print("=" * 40)

# Обмін чи вихід
if x == 1 :
    # Обмін
    ## доповни програму у цьому місці вказівками, що повідомляють поточний валютний курс
    while True :
        print("Ви можете:")
        print("1. Обміняти гривні на долари")
        print("2. Обміняти долари на гривні")
        ## доповни програму у цьому місці вказівками для розширення функціоналу обмінника до роботи із євро
        print("0. Вийти")
        choise = input("робіть свій вибір та введіть номер опції: ")
        print("\n" * 100)
        # Гривні на долари
        if choise == "1" :
            uah = int(input("Введіть суму у гривнях: "))
            usd = int(uah / dolar)
            print("Отримайте Ваші долари:", usd)
            print("Обмін завершено. Ви можете продовжити")
        # Долари на гривні
        elif choise == "2" :
            usd = int(input("Введіть суму у доларах: "))
            uah = int(usd * dolar)
            print("Отримайте Ваші гривні:", uah)
            print("Обмін завершено. Ви можете продовжити")
        ## доповни програму у цьому місці для виконання операцій з обміну євро
        elif choise == "0" :
            break
        else :
            print("!" * 50)
            print("Не коректне введення. Бутьте уважнішими. Повторіть Ваш вибір...")

# Вихід
print("*" * 40)
print("Дякуємо за використання обмінника валют")
print("До побачення!")
print("*" * 40)
