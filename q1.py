class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()  # Sorting toh zaroori hai boss
        
        n = len(nums)
        
        for base_idx in range(n - 2):
            # Pichle number se match kare toh aage badho (pehle element ka duplicate check)
            if base_idx > 0 and nums[base_idx] == nums[base_idx - 1]:
                continue
            
                
            # Do pointers set kiye: ek aage se, ek peeche se
            low = base_idx + 1
            high = n - 1                                         
            
            while low < high:
                current_sum = nums[base_idx] + nums[low] + nums[high]
                
                if current_sum == 0:
                    # Sahi triplet mil gaya
                    triplets.append([nums[base_idx], nums[low], nums[high]])
                    
                    # 'low' pointer ke duplicates skip karo
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    # 'high' pointer ke duplicates skip karo
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                        
                    # Dono pointers ko agle naye numbers par le jao
                    low += 1
                    high -= 1
                    
                elif current_sum < 0:
                    low += 1  # Sum badhane ke liye low ko aage badhao
                else:
                    high -= 1  # Sum ghatane ke liye high ko peeche lao
                    
        return triplets