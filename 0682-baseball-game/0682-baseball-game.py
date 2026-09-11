class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        prev=0
        second_prev=0
        ans=[]
        for i in operations:
            if i=='C':
                ans.pop(-1)
            elif i=='D':
                ans.append(2*ans[-1])
            elif i=='+':
                ans.append(ans[-1]+ans[-2])   
            else :
                ans.append(int(i))      
        return sum(ans)           
        