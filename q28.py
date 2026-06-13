class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Cycle Sort - Har number ko uski sahi jagah bhejo
        # Jaise 1 ko index 0 par, 2 ko index 1 par, 3 ko index 2 par...
        # Yani number 'x' ko nums[x - 1] par hona chahiye.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swapping karke sahi jagah bhejo
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Ab check karo kaunsa number apni seat par nahi baitha hai
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # Jo apni seat par nahi hai, wahi missing hai!
                
        # Agar saare 1 se lekar n tak sahi jagah par hain, toh agla number missing hai
        return n + 1
      
