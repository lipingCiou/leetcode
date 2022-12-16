# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
#  Note that you must do this in-place without making a copy of the array.
#
#
#  Example 1:
#  Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#  Example 2:
#  Input: nums = [0]
# Output: [0]
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁴
#  -2³¹ <= nums[i] <= 2³¹ - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#
#  Related Topics Array Two Pointers 👍 12031 👎 302


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Searching the non-zero element and record its location, we use the variable j to record it.
        So we can imagine that when we found a non-zeros , we can exchange their location.
        for example, the non-zeors is found at nums[i]
        and we can assign nums[j]=nums[i]
        Because the j is the correct location.
        When it has done,j = j + 1 .
        So th J is the next location and waiting you found the next none-zeros element.
        After moving nums[i] to location j, we need to assign nums[i] the zero value(nums[i]=0)
        But we need the exclude the situation ,i== j
        so we can do as below:
        """
        j = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[j] = nums[index]
                if index != j:
                    nums[index]=0
                j = j + 1

if __name__ == "__main__":
    a=Solution()
    k=[1,1,0,3,0]
    a.moveZeroes(k)
    print(k)
# leetcode submit region end(Prohibit modification and deletion)
