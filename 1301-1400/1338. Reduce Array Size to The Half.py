from collections import Counter
from math import ceil
class Solution:
    def minSetSize(self, arr):
            
        # In Python, we can use the built-in Counter class.
        counts = Counter(arr)
        max_value = max(counts.values())
                
        # Put the counts into buckets.
        buckets = [0] * (max_value + 1)
        
        for count in counts.values():
            buckets[count] += 1
            
        # Determine set_size.
        set_size = 0
        arr_numbers_to_remove = len(arr) // 2
        bucket = max_value
        while arr_numbers_to_remove > 0:
            max_needed_from_bucket = ceil(arr_numbers_to_remove / bucket)
            set_size_increase = min(buckets[bucket], max_needed_from_bucket)
            set_size += set_size_increase
            arr_numbers_to_remove -= set_size_increase * bucket
            bucket -= 1
            
        return set_size
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))
        