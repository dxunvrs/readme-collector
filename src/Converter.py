from KeyWords import KeyWords
import re

class Converter():
    __pattern = r"[a-z]+-[a-z]+-[1-9]+"

    @staticmethod
    def changeWordConverter(word):
        if word in KeyWords.keyWordsConverter.keys():
            return KeyWords.keyWordsConverter[word]
        else:
            return "err"
    
    @staticmethod
    def changeWordEditor(word):
        if word in KeyWords.keyWordsEditor.keys():
            return KeyWords.keyWordsEditor[word]
        else:
            return "err"

    @staticmethod
    def changeSource(source):
        if re.match(Converter.__pattern, source):
            res = source.split("-")
            return f"{Converter.changeWordConverter(res[0])} {Converter.changeWordConverter(res[1])} {res[2]}"
        else:
            return "err"