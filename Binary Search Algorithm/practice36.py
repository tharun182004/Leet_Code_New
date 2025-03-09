#search element in bitonic array
'''
Given a bitonic sequence A of N distinct elements, write a program to find
a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly
increasing then after a point strictly decreasing.

Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.

Output Format
Return a single integer denoting the position (0 index based) of the
element B in the array A if B doesn't exist in A return -1.

Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30
'''


class Solution:
    #first we have to find the peak element
    def solve(self, arr, target):
        low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        peak = high
        #binary search to find the element in increasing order of the bitonic array (first increasing half)
        low, high = 0, peak
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        #binary search to find the target element in the dereasing order of bitonic array (second half)
        low, high = peak, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

