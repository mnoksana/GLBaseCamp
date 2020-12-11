# Вызов функции: count_holes('08824')
# Возвращает: 5

def is_number(value):
    """
    Check if is value is decimal number
    """
    str_value = str(value)
    if str_value and str_value[0] in ['+', '-']:
        return str_value[1::].isdecimal()
    else:
        return str_value.isdecimal()


def count_holes(value):
    """
    Count holes in number
    """

    if is_number(value):
        number = abs(int(value))
        count = 0
        while number:
            remainder = number % 10
            if remainder in [0, 4, 6, 9]:
                count += 1
            elif remainder in [8]:
                count += 2
            number //= 10
    else:
        return "error"

    return count


if __name__ == "__main__":
    numbers = ['08824', '088.24', '000001234567890', '', -123654]
    for num in numbers:
        print(f"{num}: {count_holes(num)}")
    