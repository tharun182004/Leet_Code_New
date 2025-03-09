#search in row wise column wise sorted matrix
'''
Given a matrix of size n x m, where every row and column is sorted in
increasing order, and a number x. Find whether element x is present in
the matrix or not. Return a boolean value true if x is present in the
matrix and false if it is not present.

Examples :
Input:  matrix[][] = [[3, 30, 38],[36, 43, 60],[40, 51, 69]], x = 62
Output: 0
Explanation: 62 is not present in the matrix, so output is 0.
Input: matrix[][] = [[18, 21, 27, 38, 55, 67]], x = 55
Output: 1
Explanation: 55 is present in the matrix.
'''


def search(self, arr, n, m, x):
    # code here
    low, high = 0, (n * m) - 1


    while low <= high:
        mid = (low + high) // 2

        # Calculate the row and column indices from the flattened matrix index
        row = mid // m  # Row index
        col = mid % m  # Column index

        # Compare the element at the calculated row and column
        if arr[row][col] == x:
            return True  # Element found
        elif arr[row][col] < x:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return False
