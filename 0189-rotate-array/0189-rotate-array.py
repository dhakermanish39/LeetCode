class Solution(object):
    def rotate(self, a, k):
        n=len(a)
        k=k%n
        a[:]=a[-k:]+a[:-k]
        