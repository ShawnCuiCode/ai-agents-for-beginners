"""
Street Lights State Simulation
Author : Xiang Cui
Date   : 2026-05-20
light[i] = XOR(left, right) each day; boundaries treated as 0.
Cycle detection makes runtime O(2^N · N), independent of M.
Time: O(2^N · N)  Space: O(2^N · N)
"""


def solve(N, lights, M):
    """Return state of N lights after M days using cycle detection."""
    def next_state(state):
        """One-day transition: new[i] = left ^ right."""
        n = len(state)
        new = [0] * n
        for i in range(n):
            left  = state[i - 1] if i > 0     else 0
            right = state[i + 1] if i < n - 1 else 0
            new[i] = left ^ right
        return new

    seen = {}
    state = lights[:]
    for day in range(M):
        key = tuple(state)
        if key in seen:
            cycle_len = day - seen[key]
            remaining = (M - day) % cycle_len
            for _ in range(remaining):
                state = next_state(state)
            break
        seen[key] = day
        state = next_state(state)
    return state

if __name__ == "__main__":
    N = 8
    lights = list(map(int, input().split()))
    M = int(input())
    print(' '.join(map(str, solve(N, lights, M))))
