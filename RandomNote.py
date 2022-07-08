class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            cor = False
            for j in range(len(magazine)):
                if(ransomNote[i] == magazine[j]):
                    magazine = magazine.replace(magazine[j], '', 1)
                    cor = True
                    break
            if(cor == False):
                break
        return cor
