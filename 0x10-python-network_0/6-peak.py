#!/usr/bin/python3
"""Module for find_peak function."""


def find_peak(nums):
    """A function that takes a list and returns the highest number."""
    count = len(nums)
    if count == 0 or nums is None:
        return (None)
    else:
        for i in range(1, count):
            if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
                return (nums[i])
            elif nums[i - 1] >= nums[i + 1] and i - 1 == 0:
                return (nums[i - 1])
            elif nums[i - 1] <= nums[i + 1] and i + 1 == count:
                return (nums[i + 1])
