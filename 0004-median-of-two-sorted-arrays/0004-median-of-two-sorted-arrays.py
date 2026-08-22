class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s=len(nums1)+len(nums2)
        a=s//2
        front=0
        back=0
        fe=0
        be=0
        
        for i in range(s):
            if front + back==a+1:
                break
            if  back >= len(nums2):
                be=fe
                fe=nums1[front]
                front+=1
            elif front >=len(nums1) :
                be=fe
                fe=nums2[back]
                back+=1   
            else:
                if nums1[front] < nums2[back]:
                    be=fe
                    fe=nums1[front]
                    front+=1
                else:
                    be=fe
                    fe=nums2[back]
                    back+=1 
        return fe if s%2!=0 else( fe+be)/2.0           







        