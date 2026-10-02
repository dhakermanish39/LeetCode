class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        temp=[1]
        res=temp
        for i in range(rowIndex):
            t=[]    
            t.append(1)
            for i in range(1,len(temp)):
                t.append(temp[i]+temp[i-1])
            t.append(1)
            temp=t
            res=t
            
        return res    

        