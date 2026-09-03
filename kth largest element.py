class Solution:
    def findKthLargest(self, arr,k) :
        
        arr.sort()
        return arr[len(arr)-k]
         
