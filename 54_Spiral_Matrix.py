class Solution(object):
    def spiralOrder(self, matrix):
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        op = []

        while top <= bottom and left <= right:

            # Top row
            for i in range(left, right+1):
                op.append(matrix[top][i])
            top += 1

            # Right column
            for i in range(top, bottom+1):
                op.append(matrix[i][right])
            right -= 1

            # Bottom row
            if bottom >= top:
                for i in range(right, left-1, -1):
                    op.append(matrix[bottom][i])
                bottom -= 1

            # Left column
            if right >= left:
                for i in range(bottom, top-1, -1):
                    op.append(matrix[i][left])
                left += 1

        return op
