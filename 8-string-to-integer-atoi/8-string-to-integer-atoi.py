class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        i = 0
        sign = 1
        res = 0
        maxNum = 2 ** 31 - 1
        minNum = - maxNum - 1
        
        while i < l and s[i] == " ":
            i += 1
            
        if i < l and s[i] == '+':
            sign = 1
            i += 1
        elif i < l and s[i] == '-':
            sign = -1
            i += 1
            
        while i < l and s[i].isdigit():
            res = res * 10 + int(s[i])
            if (res > maxNum):
                if sign == -1:
                    return minNum
                else:
                    return maxNum
            i += 1
        
        return res * sign