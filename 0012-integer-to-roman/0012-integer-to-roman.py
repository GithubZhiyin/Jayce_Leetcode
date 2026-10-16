class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        如下是标准做法
        roman_map = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1),
        ]
        parts = []
        for symbol, value in roman_map:
            if num >= value:
                count, num = divmod(num, value)
                parts.append(symbol * count)
        return "".join(parts)
        '''

        ones   = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens   = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hund   = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thou   = ["","M","MM","MMM"]
        return thou[num//1000] + hund[num//100%10] + tens[num//10%10] + ones[num%10]
