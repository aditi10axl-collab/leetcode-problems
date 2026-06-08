class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            // If we found the target, return its index
            if (nums[mid] == target) {
                return mid;
            }
            
            // Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                // Check if target lies within the sorted left half
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1; // Search left
                } else {
                    left = mid + 1;  // Search right
                }
            } 
            // Otherwise, the right half must be sorted
            else {
                // Check if target lies within the sorted right half
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;  // Search right
                } else {
                    right = mid - 1; // Search left
                }
            }
        }
        
        // Target was not found in the array
        return -1;
    }
}//class Solution {
    //public int search(int[] nums, int target) {
     //   for (int i = 0; i < nums.length; i++) {
      //      if (nums[i] == target) {
        //        return i;
      //      }
//}
   ////     return -1;
   // }//
//}