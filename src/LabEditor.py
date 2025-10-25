from Lab import Lab
from Converter import Converter
from Paths import Paths

class LabEditor():
    def __init__(self, lab : Lab, workDirectory):
        self.__lab = lab
        self.__workDirectory = workDirectory
        self.__filePath = f"{workDirectory}{Converter.changeWordEditor(self.__lab.getSubject())}/{self.__lab.getSubject()}.md"
    
    def addLab(self):
        with open(self.__filePath, "a") as f:
            newLine = f"|{self.__lab.getNumber()}|{self.__lab.getMaxPoints()}|{self.__lab.getPoints()}|{self.__lab.getPassDate()}|{self.__lab.getTheme()}|"
            f.write(newLine+"\n")

if __name__ == "__main__":
    subject = input("Название предмета: ")
    number = input("Номер лабы: ")
    maxPoints = input("Макс кол-во баллов: ")
    points = input("Мои баллы: ")
    passDate = input("Дата сдачи: ")
    theme = input("Тема: ")

    lab = Lab(subject, number, maxPoints, points, passDate, theme)
    labEditor = LabEditor(lab,Paths.workDirectory)
    labEditor.addLab()