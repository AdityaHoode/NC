class Solution:
    def binarySearchMatrix(self, matrix: List[List[int]], target: int) -> int:
        l,r=0,len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[m][-1]:
                l=m+1
            elif target<matrix[m][0]:
                r=m-1
            else:
                return m
        return -1

    def binarySearchRow(self, row: List[int], target: int) -> int:
        l,r=0,len(row)-1
        while l<=r:
            m=(l+r)//2
            if target>row[m]:
                l=m+1
            elif target<row[m]:
                r=m-1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index=self.binarySearchMatrix(matrix, target)
        if index!=-1:
            return self.binarySearchRow(matrix[index], target)
        else: 
            return False