"""
Street Lights State Simulation - Floyd's Tortoise & Hare
Author : Xiang Cui
Date   : 2026-05-20
light[i] = XOR(left, right) each day; boundaries treated as 0.
Floyd's cycle detection: no hash table needed.
Time: O(2^N · N)  Space: O(N)   ← space improved from O(2^N·N)
"""


def solve(N, lights, M):
    """Return state of N lights after M days using Floyd's algorithm."""

    def next_state(state):
        """One-day transition: new[i] = left ^ right."""
        n = len(state)
        new = [0] * n
        for i in range(n):
            left  = state[i - 1] if i > 0     else 0
            right = state[i + 1] if i < n - 1 else 0
            new[i] = left ^ right
        return new

    # ── 特殊情况：M=0 直接返回 ─────────────────────────────────────────────
    if M == 0:
        return lights[:]

    # ── 第一阶段：龟兔赛跑，找相遇点 ──────────────────────────────────────
    #   tort 每次走 1 步（慢）
    #   hare 每次走 2 步（快）
    #   在环里必然相遇
    tort = next_state(lights)           # 第1步
    hare = next_state(next_state(lights))  # 第2步
    while tort != hare:
        tort = next_state(tort)                    # 走1步
        hare = next_state(next_state(hare))        # 走2步

    # ── 第二阶段：求环长 λ ──────────────────────────────────────────────────
    #   让 hare 继续从相遇点走，走回原处的步数即为环长
    lam = 1
    hare = next_state(tort)
    while tort != hare:
        hare = next_state(hare)
        lam += 1

    # ── 第三阶段：求环起点 μ ────────────────────────────────────────────────
    #   tort 回到起点，hare 先走 λ 步
    #   然后两者同速走，相遇时走过的步数即为 μ
    tort = lights[:]
    hare = lights[:]
    for _ in range(lam):
        hare = next_state(hare)
    mu = 0
    while tort != hare:
        tort = next_state(tort)
        hare = next_state(hare)
        mu += 1

    # ── 第四阶段：计算答案 ─────────────────────────────────────────────────
    #   M 步之前环还没开始 → 直接模拟
    #   M 步落在环内      → 走到环起点，再取模跳步
    if M < mu:
        state = lights[:]
        for _ in range(M):
            state = next_state(state)
        return state
    else:
        state = lights[:]
        for _ in range(mu):                   # 走到环起点
            state = next_state(state)
        for _ in range((M - mu) % lam):       # 环内取模跳步
            state = next_state(state)
        return state


# ── OJ 提交入口 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    N      = int(input())
    lights = list(map(int, input().split()))
    M      = int(input())
    print(' '.join(map(str, solve(N, lights, M))))
