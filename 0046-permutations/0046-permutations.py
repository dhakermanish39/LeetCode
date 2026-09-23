class Solution(object):
    def permute(self, nums):
        re = []
        def result(num):
            if len(num) == 1:
                return [num]
            ans = []
            for i in range(len(num)):
                x = num[i]
                remaining = num[:i] + num[i+1:]
                for p in result(remaining):
                    ans.append([x] + p)
            return ans
        return result(nums)