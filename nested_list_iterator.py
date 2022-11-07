class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.nestedList = []

        self.n = len(nestedList)

        def dfs(item):

            if item.isInteger():

                self.nestedList.append(item.getInteger())
            
            else:

                objList = item.getList()

                for subobj in objList:

                    dfs(subobj)

        for item in nestedList:

            dfs(item)                

    def next(self) -> int:
        
        return(self.nestedList.pop(0))
    
    def hasNext(self) -> bool:

        return(True if self.nestedList else False)
