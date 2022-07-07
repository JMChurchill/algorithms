class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                res =res- roman[s[i]] 
            else:
                res =res+ roman[s[i]]
        return res
    def intToRomanBasic(self, num: int) -> str:
        # ans =""
        if(num >= 900):
            if(num >= 1000):
                return "M" + self.intToRoman(num - 1000)
            else:
                return "CM" + self.intToRoman(num - 900)
        if(num >= 400):
            if(num >= 500):
                return "D" + self.intToRoman(num - 500)
            else:
                return "CD" + self.intToRoman(num - 400)
        if(num >= 90):
            if(num >= 100):
                return "C" + self.intToRoman(num - 100)
            else:
                return "XC" + self.intToRoman(num - 90)
        if(num >= 40):
            if(num >= 50):
                return "L" + self.intToRoman(num - 50)
            else:
                return "XL" + self.intToRoman(num - 40)
        if(num >= 9):
            if(num >= 10):
                return "X" + self.intToRoman(num - 10)
            else:
                return "IX" + self.intToRoman(num - 9)
        if(num >= 4):
            if(num >= 5):
                return "V" + self.intToRoman(num - 5)
            else:
                return "IV" + self.intToRoman(num - 4)
        if(num >= 1):
            return "I" + self.intToRoman(num - 1)
        return ""