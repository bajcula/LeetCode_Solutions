#Sort the array using insertion sort

class Solution:

    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        
        for i in range(1, len(alist)):
            
            value_to_sort = alist[i]
            
            while alist[i - 1] > value_to_sort and i > 0:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
                
        return alist
        
#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends