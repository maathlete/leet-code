#question: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        return(sum(list(map(lambda x: x[0]*x[1], list(zip(self.vector, vec.vector))))))
