class Solution:
    def intToRoman(self, num: int) -> str:


        ones   = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens   = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hund   = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thou   = ["","M","MM","MMM"]
        return thou[num//1000] + hund[num//100%10] + tens[num//10%10] + ones[num%10]
