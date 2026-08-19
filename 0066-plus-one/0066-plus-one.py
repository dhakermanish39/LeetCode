class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num="".join(map(str,digits))
        num=int(num)+1
        num=list(map(int,str(num)))
        return num
        