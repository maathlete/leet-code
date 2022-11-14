#Question: https://leetcode.com/problems/map-sum-pairs/description/

class Node:

    def __init__(self, label=None):

        self.label = label
        self.children = {}

        self.sum = 0

class MapSum:

    def __init__(self):
        
        self.trie = Node()
        self.dic = {}

    def insert(self, key: str, val: int) -> None:

        if key in self.dic:

            flag = True

        else:

            flag = False
            
        trie = self.trie

        for c in key:

            if c not in trie.children:

                trie.children[c] = Node(c)
            
            trie = trie.children[c]

            if flag:

                trie.sum -= self.dic[key]

            trie.sum += val
            
        self.dic[key] = val
    
    def sum(self, prefix: str) -> int:

        trie = self.trie

        count = 0

        for c in prefix:

            if c not in trie.children:

                return(0)

            trie = trie.children[c]

        return(trie.sum)
