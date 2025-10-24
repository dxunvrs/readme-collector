from src.Lab import Lab

class Collector():
    def __init__(self, readme, lab : Lab):
        self.__readme = readme
        self.__lab : Lab = lab
    
    def changeReadme(self):
        with open(self.__readme, "r") as readmeFile:
            lines = readmeFile.read().splitlines()
        for i in range(len(lines)):
            if f"## {self.__lab.getSubject()}" in lines[i]:
                for j in range(i,len(lines)):
                    if "..." == lines[j]:
                        lines[j] = f"|{self.__lab.getNumber()}|{self.__lab.getMaxPoints()}|{self.__lab.getPoints()}|{self.__lab.getPassDate()}|{self.__lab.getTheme()}|  "
                        lines.insert(j+1,"...")
                        break
        with open(self.__readme, "w") as readmeFile:
            for line in lines:
                readmeFile.write(line + "\n")
