class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        length = len(timeSeries)
        timeSum = 0   # 中毒的总时间
        endTime = -1  # 中毒结束的时间

        for index in range(length):
            # 新一轮攻击后，中毒结束的时间
            # newTime：表示在第newTime秒初结束攻击，注意newTime秒初是newTime-1秒末尾
            newTime = timeSeries[index] + duration

            # 情况1：上一次攻击导致的中毒已经结束
            if endTime <= timeSeries[index]:
                count = duration
            # 情况2：两次攻击的中毒时间有交集
            else:
                count = newTime - endTime
            timeSum += count

            endTime = newTime

        return timeSum