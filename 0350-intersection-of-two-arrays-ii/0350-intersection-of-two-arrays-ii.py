class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        d1={}
        d2={}
        for i in nums1:
            d1[i]=d1.get(i,0)+1
        for i in nums2:
            d2[i]=d2.get(i,0)+1
        for i in d1.keys():
            if i in nums2:
                for j in range(min(d2[i],d1[i])):
                    res.append(i)

            

        return res