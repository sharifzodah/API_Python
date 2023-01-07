from Day3_Classes_and_Functions import Solution


class SubClass(Solution):
    n = 100  # class variable

    def __init__(self, a, b):
        self.a = a  # instance variable
        self.b = b  # instance variable
        Solution.__init__(self)

    def getCompleteData(self):
        return self.n + self.calc_sum(self.a, self.b)


child_obj = SubClass(50, 50)
data = child_obj.getCompleteData()
print(data)

solution = Solution()
calc_sum = solution.calc_sum(10, 10)
print(calc_sum)
