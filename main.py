import eel

eel.init("web")

@eel.expose
def col(number):
    try:
        number = int(number)
        l = []
        if number <= 0:
            return "Можно использовать только положительные числа"
        else:
            while number != 1:
                if number % 2 == 0:
                    result = number // 2
                    number = result
                    l.append(result)
                else:
                    result = 3 * number + 1
                    number = result
                    l.append(result)
            return l
    except ValueError:
        return "Ошибка ввода данных"

eel.start("index.html", size=(500, 500))