import Paths

def main() -> None:
    # проходимся по предметам и создаем таблицы для них
    new_lines: str = "# Баллы за лабы" + "\n"
    for subject in Paths.subjects:
        match subject:
            case "OPD":
                new_lines += create_table("ОПД", Paths.subjects_tables[subject])
            case "Prog":
                new_lines += create_table("Программирование", Paths.subjects_tables[subject])
            case "Inf":
                new_lines += create_table("Информатика", Paths.subjects_tables[subject])

    # открываем шаблон
    try:
        with open(Paths.outline_path, "r") as outline: 
            new_lines = outline.read() + "\n" + new_lines

    except FileNotFoundError:
        print("В рабочей директории нет нужных таблиц")

    except PermissionError:
        print("Нет доступа")

    except Exception as e:
        print(e)

    # записываем результат
    with open(Paths.readme_path, "w") as output:
        output.write(new_lines)

def create_table(subject: str, path: str) -> str:
    table: str = subject + "\n"
    try:
        with open(path, "r") as file: 
            table += file.read() + "\n"
            return table

    except FileNotFoundError:
        print("В рабочей директории нет нужных таблиц")

    except PermissionError:
        print("Нет доступа")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()