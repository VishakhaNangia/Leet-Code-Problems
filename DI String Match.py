class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        A =[]
        for i in S:
            if i == 'I':
                A.append(lo)
                lo += 1
            else:
                A.append(hi)
                hi -=1
        return A+[lo]
