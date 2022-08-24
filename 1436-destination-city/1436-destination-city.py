class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        visited = []
        
        for i in range(len(paths)):
            visited.append(paths[i][0])
        
        for i in range(len(paths)):
            if paths[i][1] not in visited:
                return paths[i][1]
        