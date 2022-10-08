class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        print(words)
        empDic = {}
        sentence = ""
        for word in words:
            empDic[word[-1]] = word[:-1]
        for i in sorted(empDic.keys()):
            sentence += empDic[i] + " "
        return sentence.strip()
