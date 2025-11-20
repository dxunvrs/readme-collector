import os

# work_directory = "" - указываем свою  рабочую директорию
# По умолчанию: домашний каталог
# work_directory = os.path.expanduser("~") + "/"
work_directory = "/home/roma/Study/"

# массив с названиями предметов (как называются папки)
subjects = ["OPD", "Inf", "Prog"]

# таблицы для предметов
subjects_tables = {x: work_directory+x+"/"+x.lower()+".md" for x in subjects}

# readme.md
readme_path = work_directory + "README.md"

# шаблон (по умолчанию должен быть в рабочей директории)
# outline_path = work_directory + "Outline.md"
outline_path = "/home/roma/Projects/readme-collector/src/Outline.md"
