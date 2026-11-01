class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        widths=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={
            'a': widths[0],'b': widths[1],'c': widths[2],'d': widths[3],'e': widths[4],'f': widths[5],'g': widths[6],'h': widths[7],'i': widths[8],'j': widths[9],'k': widths[10],'l': widths[11],'m': widths[12],'n': widths[13],'o': widths[14],'p': widths[15],'q': widths[16],'r': widths[17],'s': widths[18],'t': widths[19],'u': widths[20],'v': widths[21],'w': widths[22],'x': widths[23],'y': widths[24],'z': widths[25]
        }

        ans=[]
        for i in words:
            temp=""
            for j in i:
                temp+=d[j]
            ans.append(temp)
        result ={}   
        for i in ans:
            result[i]=result.get(i,0)+1
        return len(result)    


        