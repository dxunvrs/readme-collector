from src.Converter import Converter

class Lab(): 
    def __init__(self, subject, number, maxPoints, points, passDate, theme):
        self.__subject = subject
        self.__number = number
        self.__maxPoints = maxPoints
        self.__points = points
        self.__passDate = passDate
        self.__theme = theme
    
    def getSubject(self):
        return Converter.changeWord(self.__subject)
    
    def getNumber(self):
        return self.__number
    
    def getMaxPoints(self):
        return self.__maxPoints
    
    def getPoints(self):
        return self.__points
    
    def getPassDate(self):
        return self.__passDate
    
    def getTheme(self):
        return self.__theme