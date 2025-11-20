import Paths

# добавляем лабы в одну из рабочих папок, в зависимости от предмета
def main() -> None:
    name: str = input("Название предмета: ")
    number: str = input("Номер лабы: ")
    max_points: str = input("Макс. кол-во баллов: ")
    points: str = input("Мои баллы: ")
    pass_date: str = input("Дата сдачи: ")
    theme: str = input("Тема: ")

    # проверяем на что похоже введенное название и записываем лабу в md-таблицу
    if name.lower() in ["opd", "опд"]:
        write_lab("OPD", number, max_points, points, pass_date, theme)

    elif name.lower() in ["prog", "прога", "java", "программирование"]:
        write_lab("Prog", number, max_points, points, pass_date, theme)

    elif name.lower() in ["inf", "инфа", "информатика"]:
        write_lab("Inf", number, max_points, points, pass_date, theme)

    else:
        print("Пока нет такого предмета")

def write_lab(subject: str, number: str, max_points: str, points: str, pass_date: str, theme: str) -> None:
    empty_table: str = "|Номер|Макс. баллов|Баллы|Дата сдачи|Тема|" + "\n" + "|:-:|:-:|:-:|:-:|:-:|" + "\n" # шаблон пустой таблицы

    try:
        with open(Paths.subjects_tables[subject], "a+") as file:
            new_line: str = f"|{number}|{max_points}|{points}|{pass_date}|{theme}|" + "\n" # добавляем инфу о лабе

            if file.read():
                file.write(new_line)

            else:
                file.write(empty_table)
                file.write(new_line)

    except FileNotFoundError:
        print("В рабочей директории нет нужных каталогов")

    except PermissionError:
        print("Нет доступа")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()