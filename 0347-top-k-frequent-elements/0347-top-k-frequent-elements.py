class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        temp=[]
        for i in d.values():
            temp.append(i)
        temp.sort()
        ans=[]
        x=temp[-k]
        for i in d.keys():
            if d[i]>=x:
                ans.append(i)
        return ans                

        