from typing import List
from typing import Tuple


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0:
            return False

        def hasNearbyDuplicateInBucket(
                bucketContent: Tuple[int, int],
                ind: int, num: int) -> bool:

            if bucketContent is None: return False
            return ((ind - bucketContent[0]) <= k) and \
                (abs(bucketContent[1] - num) <= t)

        # bucket (index, num) of numbers into ranges of size t+1
        #   i.e. [-t, 0) [0, t+1), [t+1, 2t+2), ...
        bucketDict = dict()

        for ind, num in enumerate(nums):
            bucket = num // (t+1)

            # diff less than t can only exist in same bucket or neighboring buckets
            if hasNearbyDuplicateInBucket(bucketDict.get(bucket), ind, num):
                return True
            if hasNearbyDuplicateInBucket(bucketDict.get(bucket-1), ind, num):
                return True
            if hasNearbyDuplicateInBucket(bucketDict.get(bucket+1), ind, num):
                return True

            bucketDict[bucket] = (ind, num)

        return False
