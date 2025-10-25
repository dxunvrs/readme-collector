# Описание
Сборщик файла README.md  
Поддерживает две функции: добавление лабы в таблицу предмета и сборка README.md  
В README.md добавляет все таблицы и обновляет список  веток  в разделе "В работе"
# Инструкция
1. Добавить свои пути в файле src/Paths.py
```class Paths():
    workDirectory = "/home/roma/Study/" # Рабочая директория
    # Пути до файлов с таблицами
    labsFilesPaths = [ 
        (f"{workDirectory}Inf/inf.md", "inf"),
        (f"{workDirectory}Prog/prog.md", "prog"),
        (f"{workDirectory}OPD/opd.md", "opd")
    ]
    mainOutline = "/home/roma/Projects/readme-collector/src/mainOutline.md" # Макет для README.md
    readmePath = "/home/roma/Study/README.md" # путь к файлу README.me который нужно изменить
```
2. Можно запустить скрипт addlab.sh и добавить лабу в заданную предметную таблицу
```
bash addlab.sh
Название: prog
Макс.баллов: 100
Мои баллы: 100
Дата сдачи: xx.xx.xxxx
Тема: Указываем тему
```

3. Скриптом readmecollect.sh пересобрать README.md  

Список заменяемых слов лежит в src/KeyWords.py  
Именовать ветки нужно следующим образом  
> inf-lab-4  
> название предмета из ключевых слов-lab-номер лабы 
