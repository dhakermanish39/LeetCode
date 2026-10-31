class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        al={}
        for ch in strs:
            sorted_word = "".join(sorted(ch))
            if sorted_word not in al:
                al[sorted_word]=[]
            al[sorted_word].append(ch)

        return list(al.values())
        