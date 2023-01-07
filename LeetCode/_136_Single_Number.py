class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for number in nums:
            if number in s:
                s.remove(number)
            else:
                s.add(number)
        return list(s)[0]


solution = Solution()
numbers = [1, 5, 2, 5, 2]
print(solution.singleNumber(numbers))
