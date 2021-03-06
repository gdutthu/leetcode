class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 特别注意
        # 题目翻译错了哈，h_index代表有h篇论文的引用次数至少为h次。
        citations=sorted(citations)

        paperNum=len(citations)
        for index in range(paperNum):
            # 当前这篇文献的引用数量
            res=citations[index]
            if paperNum-index<=res:
                return paperNum-index
        return 0
