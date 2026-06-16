# 算法面试题整理：路灯状态模拟 & 最少标记放置

---

## 第一题：路灯状态模拟（Street Lights）

### 题目描述

给定 N 盏路灯，每盏灯状态为 0 或 1。每天更新规则：
- 每盏灯的新状态 = 左邻居 XOR 右邻居
- 边界灯的不存在的邻居视为 0

给定初始状态和天数 M，求 M 天后的状态。

**示例：**
```
输入：N=8, lights=[1,1,1,0,1,1,1,1], M=2
输出：[0,0,0,0,0,1,1,0]
```

---

```python
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
```

### 核心问题 & 答案


**Q1：最朴素的解法是什么？时间复杂度是多少？**

A：逐天模拟，每天对每盏灯计算 XOR。
- 时间复杂度：O(M·N)
- 当 M=10亿、N=8 时，需要 80 亿次操作，超时。

---

**Q2：如何优化？为什么可以用循环检测？**

A：N 盏灯每盏只有 0/1 两种状态，整体状态最多有 2^N 种。根据鸽巢原理，最多走 2^N 步后必然出现重复状态，形成循环。
- 用哈希表记录每天状态首次出现的时间
- 一旦检测到重复，计算循环长度，用取模跳过剩余步骤
- 时间复杂度降为 O(2^N · N)，与 M 无关

```python
seen = {}
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
```

---

**Q3：`new[i] = left ^ right` 中 `^` 是什么？为什么不直接修改 state？**

A：`^` 是按位异或（XOR）运算符，规则是"相同为0，不同为1"。
不能直接修改 state 是因为所有灯的新状态要**同时**基于旧状态计算，若边算边改，后面的灯会读到已更新的值，导致结果错误。因此先算入临时列表 `new`，全部算完再返回。

---

**Q4：`state = lights[:]` 是什么语法？**

A：Python 切片复制语法，创建一个新列表（内容与 lights 相同但相互独立）。
等价写法：`lights.copy()` 或 `list(lights)`。
目的是保护原始输入不被函数内部修改。

---

**Q5：时间复杂度 O(2^N · N) 怎么推导的？**

A：
- 状态总数：N 盏灯，每盏 0/1，共 2^N 种状态
- 鸽巢原理：最多走 2^N 步必然检测到循环
- 每步 `next_state` 遍历 N 盏灯，耗时 O(N)
- 总计：O(2^N · N)

---

### 延伸问题 & 答案

**Q6：这道题一共有哪些解法？各自适用场景？**

| 解法 | 时间 | 空间 | 适用场景 |
|------|------|------|---------|
| 暴力模拟 | O(M·N) | O(N) | M 很小（<10万） |
| 哈希表循环检测 | O(2^N·N) | O(2^N·N) | N≤12，首选 |
| 龟兔算法 | O(2^N·N) | O(N) | N≤17，内存受限 |
| 位运算+哈希表 | O(2^N) | O(2^N) | N≤17，追求速度 |
| 矩阵快速幂 | O(N³·logM) | O(N²) | N>17，通用最优 |

**N 的选择建议：**
```
N ≤ 12   →  哈希表（代码最简洁）
N ≤ 17   →  位运算（每步 O(1)）
N > 17   →  矩阵快速幂（唯一不超时方案）
内存极紧  →  龟兔算法（O(N) 空间）
```

---

**Q7：龟兔算法（Floyd's）如何应用到这道题？**

A：Floyd's 用快慢两个"指针"代替哈希表，空间从 O(2^N·N) 降至 O(N)。

四个阶段：
1. **找相遇点**：tort 走1步，hare 走2步，在环内相遇
2. **找环长 λ**：hare 从相遇点继续走，走回原处的步数
3. **找环起点 μ**：tort 回起点，hare 先走 λ 步，同速走至相遇
4. **算答案**：
   - 若 M < μ：直接模拟 M 步
   - 若 M ≥ μ：走到 μ，再走 (M-μ) % λ 步

```python
# 第一阶段
tort = next_state(lights)
hare = next_state(next_state(lights))
while tort != hare:
    tort = next_state(tort)
    hare = next_state(next_state(hare))

# 第二阶段
lam = 1
hare = next_state(tort)
while tort != hare:
    hare = next_state(hare)
    lam += 1

# 第三阶段
tort, hare = lights[:], lights[:]
for _ in range(lam):
    hare = next_state(hare)
mu = 0
while tort != hare:
    tort = next_state(tort)
    hare = next_state(hare)
    mu += 1
```

---

**Q8：位运算如何一条指令算完所有灯？**

A：将 N 盏灯状态压缩为一个整数，利用 CPU 并行处理多个 bit：

```python
mask = (1 << N) - 1
new_state = ((s >> 1) ^ (s << 1)) & mask
# s >> 1：每个 bit i 得到右邻居（bit i+1）
# s << 1：每个 bit i 得到左邻居（bit i-1）
# 边界自动补 0（移出去的位为 0）
```

每步从 O(N) 降至 O(1)，总时间 O(2^N)。

---

**Q9：矩阵快速幂的原理是什么？**

A：这道题的状态转换是 GF(2)（二进制域）上的线性变换，可以表示为矩阵乘法：

$$\text{state}_M = T^M \cdot \text{state}_0 \pmod{2}$$

转移矩阵 T（N=4 示例）：
```
T = [[0,1,0,0],
     [1,0,1,0],
     [0,1,0,1],
     [0,0,1,0]]
```

用快速幂计算 T^M：将 M 写成二进制，只需 O(log M) 次矩阵乘法，每次矩阵乘法 O(N³)，总时间 **O(N³·log M)**，与 2^N 完全无关。

**当 N=30 时对比：**
- 哈希表/位运算：2^30 ≈ 10亿步 → 超时
- 矩阵快速幂：30³ × 30 ≈ 81万步 → 瞬间完成

---

**Q10：龟兔算法算"指针"吗？**

A：是双指针思想的经典应用。在链表中 tort/hare 是真正的内存地址指针；在本题中是状态变量，逻辑完全相同——一快一慢，在环内必然相遇。

**为什么一定相遇？**
设环长 λ，两者进入环后，距离差每步增加1，当差值 ≡ 0 (mod λ) 时相遇，即最晚 k=λ 步必然相遇。

---

**Q11：为什么原始代码选哈希表而不选位运算？**

A：N=8 时两者时间差不到 0.001 秒，绝对差距可忽略。
- 列表循环：代码直接对应题目描述，可读性强，调试方便
- 位运算：需要额外理解移位方向，容易写错，调试需要 bin() 转换

**原则：在性能差异无实际影响时，优先选可读性更好的写法。**（Knuth："过早优化是万恶之源"）

---

---

## 第二题：最少标记放置（Minimum Marker Placements）

### 题目描述

数轴上有 N 个路段，每个路段用 [startX, endX] 表示。在数轴上放置最少数量的标记点，使每个路段上至少有一个标记点。

**示例：**
```
输入：
N=3
starts=[0, 4, 1]
ends=  [4, 0, 3]
→ 区间：[0,4], [0,4], [1,3]
输出：1（在 x=3 处放一个标记即可覆盖全部）
```

---

```python
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
```

### 核心问题 & 答案

**Q1：题目本质是什么问题？**

A：**区间刺穿问题（Interval Stabbing）**：用最少的点，使每个区间内至少含一个点。

---

**Q2：贪心策略是什么？为什么放右端点最优？**

A：**按右端点升序排序，每次在当前未被覆盖的最早结束区间的右端点放标记。**

放右端点而非左端点或中间，是因为标记尽量靠右能最大化覆盖后续区间的概率，同样覆盖当前区间的前提下"向右探出"最远，使下一个标记需要的时机尽可能晚。

```python
intervals = sorted([(min(s,e), max(s,e)) for s,e in zip(starts,ends)],
                   key=lambda x: x[1])   # 按右端点排序
count, marker = 0, float('-inf')
for left, right in intervals:
    if marker < left:        # 当前标记未覆盖此区间
        marker = right       # 在右端点放标记
        count += 1
```

---

**Q3：`min(s,e), max(s,e)` 为什么要做这个处理？**

A：题目中路段有方向（起点可能大于终点），需要统一为 left ≤ right 的标准形式，否则排序和覆盖判断会出错。

---

**Q4：`marker = float('-inf')` 的作用？**

A：初始时还没有放任何标记，用负无穷代表"当前标记在所有区间左边"，确保第一个区间一定触发放标记的逻辑（`marker < left` 必然成立）。

---

**Q5：时间和空间复杂度？**

A：
- 时间：O(N log N)——排序主导
- 空间：O(N)——存储区间列表

---

### 延伸问题 & 答案

**Q6：这道题有哪些解法？**

| 解法 | 时间 | 说明 |
|------|------|------|
| 暴力枚举 | 指数级 | 枚举所有端点组合，不可行 |
| **贪心（当前代码）** | O(N log N) | 最优，简洁高效 |
| 动态规划 | O(N²) | 可处理带权重的变体题 |
| 扫描线 | O(N log N) | 逻辑更直观，复杂度相同 |

---

**Q7：为什么这道题可以用贪心，而不需要 DP？**

A：贪心成立需要满足两个条件：
1. **局部最优 = 全局最优**：每次放在最右边，不会让后续情况变差
2. **贪心选择不可撤销**：放了标记就已覆盖当前区间，无需反悔

本题两个条件都满足。若每个标记有不同代价（带权区间刺穿），局部最优不再等于全局最优，才需要 DP。

---

**Q8：和第一题相比，两题算法选择的差异是什么？**

| | 第一题（路灯） | 第二题（标记）|
|--|-------------|------------|
| 核心思想 | 循环检测 | 贪心 |
| 解法数量 | 5种（各有优劣） | 4种（贪心明显最优）|
| 能用贪心吗 | ❌ 状态转换非单调 | ✅ 右端点单调排序 |
| 关键约束 | M 极大 | 区间覆盖 |

---

**Q9：手算验证（需要2个标记的案例）**

```
路段：[0,1]  [2,3]  [0,3]

数轴：0    1    2    3
      ████              [0,1]
                ████   [2,3]
      ████████████     [0,3]

放 x=1：覆盖[0,1]✓  [2,3]✗  → 不够
放 x=1 和 x=2：
  [0,1]：1在内✓
  [2,3]：2在内✓
  [0,3]：1在内✓
→ 答案=2
```

贪心执行：
1. 排序后：[0,1], [0,3], [2,3]
2. 处理[0,1]：marker=-∞ < 0 → 放标记到1，count=1
3. 处理[0,3]：marker=1 在[0,3]内 → 跳过
4. 处理[2,3]：marker=1 < 2 → 放标记到3，count=2
5. 答案=2 ✓

---

## 面试高频追问

**Q：如果面试官问"还有其他解法吗？"怎么回答？**

第一题：
> "对于 N 较小的情况，哈希表循环检测已经足够；若 N 较大，可以考虑矩阵快速幂，将状态转换表示为 GF(2) 上的线性变换，时间复杂度降至 O(N³·logM)；内存受限时可用 Floyd's 龟兔算法将空间从 O(2^N) 降至 O(N)；此外还可以用位运算将每步从 O(N) 优化至 O(1)。"

第二题：
> "贪心是最优解。如果每个标记有不同权重（带权区间刺穿），则需要改用动态规划；如果区间是二维的（矩形覆盖），则变成 NP-hard 问题，需要近似算法。"

**Q：如何向面试官描述复杂度分析的思路？**

> "我先考虑暴力解的复杂度，找到瓶颈在哪里（第一题是 M 太大，第二题是需要穷举），然后思考能否利用问题的数学结构来降低复杂度——第一题利用了状态空间有限的周期性，第二题利用了区间端点的单调排序性质。"
