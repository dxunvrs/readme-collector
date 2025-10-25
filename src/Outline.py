from Converter import Converter

class Outline():
    @staticmethod
    def createSubjectTable(subject, table):
        subjectTable = [f"## {Converter.changeWordEditor(subject)}"] + table
        return subjectTable