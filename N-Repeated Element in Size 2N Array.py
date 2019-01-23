class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = collections.Counter(A)
        for k in count:
            if count[k] >1:
                return k
