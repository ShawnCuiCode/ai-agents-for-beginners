# Author   : XIANG CUI
# Problem  : Remove Duplicates from List
# Approach : Hash Set - single pass, preserve first-occurrence order
# Time     : O(N) - each element visited exactly once
# Space    : O(N) - hash set stores at most N unique elements


def remove_duplicates(arr):
    """Remove duplicates while preserving the original order."""
    seen = set()     # track elements already encountered
    result = []

    for num in arr:
        if num not in seen:    # first occurrence - keep it
            seen.add(num)
            result.append(num) # add to result
        # else: duplicate - skip

    return result


# Read input
n = int(input())
arr = list(map(int, input().split()))

# Print distinct elements in original order, space-separated
print(*remove_duplicates(arr))
