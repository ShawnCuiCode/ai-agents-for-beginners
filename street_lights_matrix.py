"""
Street Lights State Simulation - Matrix Exponentiation over GF(2)
Author : Xiang Cui
Date   : 2026-05-20
Transition is linear over GF(2): state_M = T^M * state_0 (mod 2)
Fast exponentiation computes T^M in O(log M) matrix multiplications.
Time: O(N^3 · log M)   Space: O(N^2)   ← best when N large, M huge
"""


def solve(N, lights, M):
    """Return state of N lights after M days using matrix exponentiation."""

    if M == 0:
        return lights[:]

    # ── 建转移矩阵 T ────────────────────────────────────────────────────────
    # T[i][i-1] = 1（左邻居贡献）
    # T[i][i+1] = 1（右邻居贡献）
    # 其余为 0
    # 例如 N=4：
    #   T = [[0,1,0,0],
    #        [1,0,1,0],
    #        [0,1,0,1],
    #        [0,0,1,0]]
    T = [[0] * N for _ in range(N)]
    for i in range(N):
        if i > 0:
            T[i][i - 1] = 1      # 左邻居
        if i < N - 1:
            T[i][i + 1] = 1      # 右邻居

    # ── GF(2) 矩阵乘法 ─────────────────────────────────────────────────────
    # GF(2) 上：乘法 = AND，加法 = XOR（所有运算 mod 2）
    def mat_mul(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if A[i][k]:                   # 跳过 0，加速
                    for j in range(n):
                        C[i][j] ^= B[k][j]   # GF(2) 加法 = XOR
        return C

    # ── 矩阵快速幂：T^M ────────────────────────────────────────────────────
    # 原理：M = 二进制表示，例如 M=6=0b110
    #   T^6 = T^4 · T^2
    # 每次平方：T → T^2 → T^4 → T^8 …（共 log M 次）
    def mat_pow(mat, p):
        n = len(mat)
        result = [[1 if i == j else 0 for j in range(n)]  # 单位矩阵 I
                  for i in range(n)]
        base = mat
        while p > 0:
            if p & 1:               # 当前二进制位为 1
                result = mat_mul(result, base)
            base = mat_mul(base, base)   # 平方
            p >>= 1                 # 移到下一个二进制位
        return result

    TM = mat_pow(T, M)             # T^M，O(N^3 · log M)

    # ── state_M = T^M · lights (mod 2) ────────────────────────────────────
    state = [0] * N
    for i in range(N):
        for j in range(N):
            state[i] ^= TM[i][j] * lights[j]   # GF(2) 内积

    return state


# ── OJ 提交入口 ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    N      = int(input())
    lights = list(map(int, input().split()))
    M      = int(input())
    print(' '.join(map(str, solve(N, lights, M))))
