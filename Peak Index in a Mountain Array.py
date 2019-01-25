class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if(len(A) >= 3):
            i = A.index(max(A))
        return i
