class Solution:
    def removeVowels(self, s: str) -> str:

        vowels = ['a','e','i','o','u']

        output = [letter for letter in s if letter not in vowels]
        output = ''.join(output)
        
        return output