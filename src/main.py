
TITLE_WIDTH = 60


def get_amount():
    amount = float(input("Введите первоначальную сумму: "))

    while amount <= 0:
        print("Сумма должна быть больше нуля.")
        amount = float(input("Введите первоначальную сумму: "))

    return amount


def get_rate():
    rate = float(input("Введите годовую ставку (0-30%): "))

    while rate < 0 or rate > 30:
        print("Ставка должна быть от 0 до 30%.")
        rate = float(input("Введите годовую ставку (0-30%): "))

    return rate


def get_years():
    years = int(input("Введите срок вклада (1-5 лет): "))

    while years < 1 or years > 5:
        print("Срок должен быть от 1 до 5 лет.")
        years = int(input("Введите срок вклада (1-5 лет): "))

    return years


def get_category(rate):
    if rate < 8:
        return "Низкая"
    elif rate < 15:
        return "Средняя"
    else:
        return "Высокая"


def calculate_deposit(amount, rate, years):
    current_amount = amount

    print()
    print("ТАБЛИЦА НАЧИСЛЕНИЯ ПРОЦЕНТОВ".center(TITLE_WIDTH))
    print("=" * TITLE_WIDTH)

    print(f"{'Год':>5} {'Проценты':>24} {'Сумма':>24}")
    print("-" * TITLE_WIDTH)

    for year in range(1, years + 1):
        interest = current_amount * rate / 100
        current_amount = current_amount + interest

        print(f"{year:02d}{interest:>24.2f}{current_amount:>24.2f}")

    return current_amount


def main():
    repeat = True

    while repeat:
        print()
        print("РАСЧЁТ БАНКОВСКОГО ВКЛАДА".center(TITLE_WIDTH))
        print("=" * TITLE_WIDTH)

        amount = get_amount()
        rate = get_rate()
        years = get_years()

        category = get_category(rate)

        final_amount = calculate_deposit(amount, rate, years)
        income = final_amount - amount

        print()
        print("ИТОГОВЫЙ ОТЧЁТ".center(TITLE_WIDTH))
        print("=" * TITLE_WIDTH)

        print(f"{'Первоначальная сумма:':<30}{amount:>20.2f}")
        print(f"{'Годовая ставка:':<30}{rate:>19.1f}%")
        print(f"{'Категория ставки:':<30}{category:>20}")
        print(f"{'Конечная сумма:':<30}{final_amount:>20.2f}")
        print(f"{'Общий доход:':<30}{income:>20.2f}")

        print("=" * TITLE_WIDTH)

        answer = input("Рассчитать другой вклад? (да/нет): ")
        answer = answer.strip().lower()

        while answer != "да" and answer != "нет":
            answer = input("Введите да или нет: ")
            answer = answer.strip().lower()

        if answer == "нет":
            repeat = False

    print("Работа программы завершена.")


if __name__ == "__main__":
    main()
