class Solution(object):

    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        x_reversed = 0
        while num > 0:
            x_reversed = (x_reversed * 10) + num % 10
            num = num // 10
        return x_reversed == x

    def isPalindrome2(self, x):
        return str(x) == str(x)[::-1]


solution = Solution()
palindrome = solution.isPalindrome(121)
print(palindrome)
print(solution.isPalindrome2(0))
