class Solution {
    public int[] searchRange(int[] nums, int target) {
        return new int[]{find(nums, target, true), find(nums, target, false)};
    }

    private int find(int[] nums, int target, boolean isFirst) {
        int left = 0, right = nums.length - 1, index = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                index = mid;
                if (isFirst) right = mid - 1;
                else left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return index;
    }
}
