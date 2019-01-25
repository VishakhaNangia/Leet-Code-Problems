class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        A = []
        for i in range(left,right+1):
            isSDN = True
            temp = i 
            while temp != 0:
                if temp % 10 == 0 or i % ( temp % 10) !=0:
                    isSDN = False
                    break
                temp /= 10
            if isSDN:
                A.append(i)
        return A
            
                
