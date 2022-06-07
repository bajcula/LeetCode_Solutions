class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == '':
            return -1

        for item in s:
            if s.count(item) == 1:
                return s.index(item)
            
        return -1