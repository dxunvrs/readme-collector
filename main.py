from src.Collector import Collector
from src.Lab import Lab

def main():
    subject = input("Название предмета: ")
    number = input("Номер лабы: ")
    maxPoints = input("Макс кол-во баллов: ")
    points = input("Мои баллы: ")
    passDate = input("Дата сдачи: ")
    theme = input("Тема: ")


    lab = Lab(subject, number, maxPoints, points, passDate, theme)

    collector = Collector("test.md", lab)
    collector.changeReadme()

if __name__ == "__main__":
    main()