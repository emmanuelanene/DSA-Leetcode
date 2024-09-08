class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        divisor = 1
        while x > divisor * 10:
            divisor *= 10

        while x:
            left = x // divisor
            right = x % 10

            if left != right:
                return False

            x = (x % divisor) // 10
            divisor = divisor / 100

        return True
        