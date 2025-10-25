from KeyWords import KeyWords
import re

class Converter():
    __pattern = r"[a-z]+-[a-z]+-[1-9]+"

    def __init__(self, source):
        self.source = source

    @staticmethod
    def changeWord(word):
        if word in KeyWords.keyWords.keys():
            return KeyWords.keyWords[word]
        else:
            return "err"
    
    @staticmethod
    def changeWordEditor(word):
        if word in KeyWords.keyWordsEditor.keys():
            return KeyWords.keyWordsEditor[word]
        else:
            return "err"

    def changeSource(self):
        if re.match(self.__pattern, self.source):
            res = self.source.split("-")
            return res
        else:
            return "err"