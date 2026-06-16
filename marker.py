"""
Minimum Marker Placements (Interval Stabbing)
Author : Xiang Cui
Date   : 2026-05-20
Find the minimum number of points that pierce every interval [startX, endX].
Greedy: sort by right endpoint, always stab at the right end of earliest interval.
Time: O(N log N)  Space: O(N)
"""


def solve():
    """Read input, compute and print minimum marker placements."""
    N      = int(input())
    starts = list(map(int, input().split()))
    _      = int(input())               # numE, always equals N
    ends   = list(map(int, input().split()))

    # normalise direction: ensure left <= right
    intervals = sorted(
        [(min(s, e), max(s, e)) for s, e in zip(starts, ends)],
        key=lambda x: x[1]             # sort by right endpoint
    )

    count  = 0
    marker = float('-inf')
    for left, right in intervals:
        if marker < left:              # current marker misses this interval
            marker = right             # place new marker at right endpoint
            count += 1

    print(count)


# ── OJ 提交入口 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    solve()
