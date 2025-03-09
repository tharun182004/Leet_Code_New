#find row with maximum number of 1's
'''
Given a binary matrix (containing only 0 and 1) of order NxN. All rows
are sorted already, We need to find the row number with the maximum number
of 1s. Also, find the number of 1s in that row.
Note:
1. In case of a tie, print the smaller row number.
2. Row number should start from 0th index.

Example 1
Input:
N=3
mat[3][3] = {0, 0, 1,
              0, 1, 1,
              0, 0, 0}
Output:
Row number = 1
MaxCount = 2
Explanation:
Here, max number of 1s is in row number 1
and its count is 2.
Example 2
'''

def find_max_row(arr):
    count_max = -1
    row_index = -1
    for i in range(N):
        count = self.binary(mat[i], N)
        if count > count_max:
            count_max = count
            row_index = i
    return (row_index, count_max)


def binary(self, arr, N):
    low, high = 0, N - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1

    return N - low

