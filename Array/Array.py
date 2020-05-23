# @Time : 2020/5/22 20:24 
# -- coding: utf-8 --
# @Author : like

# @File : Array.py 

# @Description: xx

class Solution:
    # 189
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def swap(l, r):
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1
                r = r - 1

        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)

    # 41
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 1
        n = len(nums)
        for i in range(n):
            while (0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]):
                # 这里不需要考虑交换后的元素，因为只要有对应桶的元素最后一定会被放到正确的位置上
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if (nums[i] != i + 1):
                return i + 1
        return n + 1

    # 299
    def getHint(self, secret, guess):
        A, B = 0, 0
        dic1, dic2 = {}, {}
        siz = len(secret)
        for i in range(siz):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in dic1:
                    dic1[secret[i]] = 1
                else:
                    dic1[secret[i]] += 1
                if guess[i] not in dic2:
                    dic2[guess[i]] = 1
                else:
                    dic2[guess[i]] += 1
        for x in dic1:
            if x in dic2:
                B += min(dic1[x], dic2[x])
        return str(A) + 'A' + str(B) + 'B'

    # 134
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    # 118
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            #zip list=[(1, 4), (2, 5), (3, 6)]
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res
    #119
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex = rowIndex + 1
        if rowIndex == 0:
            return []
        res = [[1]]
        while len(res) < rowIndex:
            # zip list=[(1, 4), (2, 5), (3, 6)]
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res[-1]
    #169
    
if __name__ == '__main__':
    sol = Solution
    sol.
