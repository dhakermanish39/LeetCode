class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in order:
            if i in friends:
                result.append(i)
        return result        