class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.arr = nums
        if not N:
            return
        self.tree = [0] * (4 * N)
        self.__buildTree(self.arr, self.tree, 0, 0, N-1)


    def __buildTree(self, arr, tree, treeIdx, lo, hi):
        if lo == hi:
            tree[treeIdx] = arr[lo]
            return
        mid = (lo + hi) // 2
        leftIdx = 2 * treeIdx + 1
        rightIdx = 2 * treeIdx + 2
        self.__buildTree(arr, tree, leftIdx, lo, mid)
        self.__buildTree(arr, tree, rightIdx, mid+1, hi)
        tree[treeIdx] = self.__merge(tree[leftIdx], tree[rightIdx])
    

    def __merge(self, left, right):
        return left + right


    def __query(self, tree, treeIdx, lo, hi, i, j):
        if i > hi or j < lo:
            return 0
        if i <= lo and hi <= j:
            return tree[treeIdx]

        mid = (lo + hi) // 2
        leftIdx = 2 * treeIdx + 1
        rightIdx = 2 * treeIdx + 2

        if mid < i:
            return self.__query(tree, rightIdx, mid+1, hi, i, j)
        elif mid >= j:
            return self.__query(tree, leftIdx, lo, mid, i, j)

        left = self.__query(tree, leftIdx, lo, mid, i, mid)
        right = self.__query(tree, rightIdx, mid+1, hi, mid+1, j)

        return self.__merge(left, right)


    def __update(self, tree, treeIdx, lo, hi, arrIdx, val):
        if arrIdx < lo or arrIdx > hi:
            return
        if lo == hi:
            tree[treeIdx] = val
            return
        mid = (lo + hi) // 2

        leftIdx = 2 * treeIdx + 1
        rightIdx = 2 * treeIdx + 2
        if mid < arrIdx:
            self.__update(tree, rightIdx, mid+1, hi, arrIdx, val)
        else:
            self.__update(tree, leftIdx, lo, mid, arrIdx, val)

        tree[treeIdx] = self.__merge(tree[leftIdx], tree[rightIdx])


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if not self.arr:
            return
        self.__update(self.tree, 0, 0, len(self.arr)-1, i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.arr:
            return 0
        return self.__query(self.tree, 0, 0, len(self.arr)-1, i, j)


if __name__ == '__main__':
    obj = NumArray([9, -8])
    print(obj.tree)
    obj.update(0,3)
    print(obj.tree)
    print(obj.sumRange(1,1))
    print(obj.sumRange(0,1))
    obj.update(1,-3)
    print(obj.tree)
    print(obj.sumRange(0,1))
