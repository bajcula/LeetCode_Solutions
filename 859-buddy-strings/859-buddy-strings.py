class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        

        A = list(s)
        B = list(goal)
        
        if len(A) != len(B): return False
        
        C = [i for i in range(len(A)) if A[i] != B[i]]
        
        if len(C) == 2 and A[C[0]] == B[C[1]] and A[C[1]]==B[C[0]]: return True
        if not C:
            if len(A) > len(set(A)): return True
            
        return False
        
        