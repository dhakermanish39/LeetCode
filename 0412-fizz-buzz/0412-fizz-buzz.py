class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num=[]
        i=1
        while i<=n:

            if i%15==0:
                num.append("FizzBuzz")
            elif    i%3==0 :
                num.append("Fizz")
            elif  i%5==0:
                num.append("Buzz")
            else:
                num.append(str(i))
            i+=1        
        return num        



        