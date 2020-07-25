# Kamesh Vedula
# Problem: Search in Rotated Sorted Array


def search(self, nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
            hi = mid - 1
        else:
            lo = mid + 1
            
    return -1


# def search(self, nums: List[int], target: int) -> int:
#     start, end = 0, len(nums) - 1
#     while start <= end:
#         mid = start + (end - start) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] >= nums[start]:
#             if target >= nums[start] and target < nums[mid]:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             if target <= nums[end] and target > nums[mid]: 
#                 start = mid + 1
#             else:
#                 end = mid - 1
#     return -1