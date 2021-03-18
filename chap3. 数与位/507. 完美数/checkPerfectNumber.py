import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        count = 1
        for val in range(2, int(math.sqrt(num)) + 1):
            if num % val == 0:
                count += val
                count += int(num / val)

        if count == num:
            return True
        else:
            return False