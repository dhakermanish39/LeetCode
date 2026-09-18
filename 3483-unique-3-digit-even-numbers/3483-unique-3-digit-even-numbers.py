class Solution(object):
    def totalNumbers(self, digits):

        """
        :type digits: List[int]
        :rtype: int
        """
        """
        if len(set(digits))==1:
            return 1
        def fact(n):
            if n==1 or n==0:
                return 1
            return n*fact(n-1)
        x=len(digits)  
        d={}
        for i in digits:
            d[i]=d.get(i,0)+1
        c=0
        ans=[]
        for i in d.keys():
            if i%2==0:
                c+=1
            if d[i]>1:
                if i%2!=0:
                    ans.append(d[i])
        m=1
        for i in ans:
            m*=fact(i)
        x=x-digits.count(0)    
        return (c*(x-1)*(x-2) )/m if x>=3 else  c     """
        l=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                if j==i:
                    continue
                else:    
                    for k in range(len(digits)):
                        if k==i or j==k:
                            continue
                        else:
                            temp =(((digits[i]*10)+digits[j])*10)+digits[k]
                    
                            if temp >99 and temp%2==0:
                                l.add(temp)
        print(l)                
        return len(l)                




        