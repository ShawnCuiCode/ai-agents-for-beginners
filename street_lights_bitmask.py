"""
Street Lights State Simulation - Bitmask Optimisation
Author : Xiang Cui
Date   : 2026-05-20
Compress the entire N-light state into one integer.
Each step uses two shift+XOR operations instead of a Python loop.
Time: O(2^N)   Space: O(2^N)   ← each step is O(1) instead of O(N)
"""


def solve(N, lights, M):
    """Return state of N lights after M days using bitmask + cycle detection."""

    mask = (1 << N) - 1          # N个1，例如 N=8 → 0b11111111 = 255

    # 把列表转成整数，bit i = lights[i]
    state = 0
    for i, v in enumerate(lights):
        if v:
            state |= (1 << i)

    def next_state(s):
        # (s >> 1)：每个 bit i 得到旧 bit(i+1) = 右邻居
        # (s << 1)：每个 bit i 得到旧 bit(i-1) = 左邻居
        # XOR 两者，边界自动补 0（移出去的位就是 0）
        return ((s >> 1) ^ (s << 1)) & mask

    # 循环检测（与哈希表版本逻辑相同，但状态是整数，比较更快）
    seen = {}
    for day in range(M):
        if state in seen:
            cycle_len = day - seen[state]
            remaining = (M - day) % cycle_len
            for _ in range(remaining):
                state = next_state(state)
            break
        seen[state] = day
        state = next_state(state)

    # 把整数还原为列表
    return [(state >> i) & 1 for i in range(N)]


# ── OJ 提交入口 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    N      = int(input())
    lights = list(map(int, input().split()))
    M      = int(input())
    print(' '.join(map(str, solve(N, lights, M))))
