class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        c=0
        for i in range(len(hours)):
            if hours[i]>=target :
                c+=1
        return c        
        