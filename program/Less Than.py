"""
You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k.

Input: arr[] = [54, 43, 2, 1, 5], k = 6
Output: 2 1 5
Explanation: 2 1 5 are less than 6.
"""

def lessThan(arr, k):
    ans = []  #ans is an empty list that will be used to store the numbers from arr that are less than k.
    for num in arr:
        if num < k:
            ans.append(num) #If the condition is true (i.e., num < k), then the number is added to the ans list.
    return ans
arr = [54, 43, 2, 1, 5]
k = 6
print(lessThan(arr, k))