class Solution:
    def intToRoman(self, num: int) -> str:


        roman_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        l = []
        for k, v in roman_map.items():
            while num >= v:
                l.append(k)
                num -= v 
     
        return "".join(l)

