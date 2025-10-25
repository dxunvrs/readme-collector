from Paths import Paths
from Outline import Outline

class Collector():
    def addLabsToReadme(self):
        newLines = []
        for labsFilePath in Paths.labsFilesPaths:
            with open(labsFilePath[0], "r") as f:
                labsFile = f.read().splitlines()
            newLines += Outline.createSubjectTable(labsFilePath[1], labsFile)
        with open(Paths.mainOutline, "r") as f:
            newLines = f.read().splitlines() + newLines
        with open(Paths.readmePath, "w") as f:
            for newLine in newLines:
                f.write(newLine + "\n")

if __name__ == "__main__":
    collector = Collector()
    collector.addLabsToReadme()