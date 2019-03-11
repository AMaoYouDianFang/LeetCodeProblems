class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        def dfs(nestedList):
            for item in nestedList:
                if item.isInteger():
                    self.stack.append(item)
                else:
                    dfs(item.getList())  #封装好的函数
        dfs(nestedList)
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack!=[]