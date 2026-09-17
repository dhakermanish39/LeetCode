"""class Solution(object):
    def findKthLargest(self, nums, k):
       
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        
        for i in range(1,k):
            nums.remove(max(nums))
           
        return max(nums)    
        """
import heapq
class Solution(object):
    def findKthLargest(self, a, k):
        minh=[]
        for n in a:
          heapq.heappush(minh,n)
          if len(minh) >k:
              heapq.heappop(minh)
        return minh[0]
                