class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        rule = {'type' : 0, 'color' : 1, 'name' : 2}

        cnt, index = 0, rule[ruleKey]
        
        for item in items:
            if item[index] == ruleValue:
                cnt += 1
                
        return cnt