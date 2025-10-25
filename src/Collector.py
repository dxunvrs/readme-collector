from Paths import Paths
from Outline import Outline
from Converter import Converter
import sys

class Collector():
    __newLines = []
    def __init__(self, branches):
        self.__branches = branches

    def addLabsToReadme(self):
        self.__newLines += ["# Баллы за лабы"]
        for labsFilePath in Paths.labsFilesPaths:
            with open(labsFilePath[0], "r") as f:
                labsFile = f.read().splitlines()
            self.__newLines += Outline.createSubjectTable(labsFilePath[1], labsFile)
        
    def updateInWorks(self):
        self.__newLines += ["# В работе"]
        for branch in self.__branches:
            res = Converter.changeSource(branch)
            if res != "err":
                self.__newLines += [f"[{res}](https://github.com/dxunvrs/ITMO/tree/{branch}/)  "]

    def updateReadme(self):
        with open(Paths.mainOutline, "r") as f:
            self.__newLines = f.read().splitlines()
        self.updateInWorks()
        self.addLabsToReadme()
        with open(Paths.readmePath, "w") as f:
            for newLine in self.__newLines:
                f.write(newLine + "\n")

if __name__ == "__main__":
    collector = Collector(sys.argv[1:])
    collector.updateReadme()