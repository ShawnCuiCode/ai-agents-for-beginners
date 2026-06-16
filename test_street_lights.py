from street_lights import solve


def test(name, N, lights, M, expected):
    result = solve(N, lights, M)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {name}")
    if result != expected:
        print(f"       got:      {result}")
        print(f"       expected: {expected}")


# OJ Case 1
test("OJ Case1 M=1",
     N=8, lights=[1,0,0,0,0,1,0,0], M=1,
     expected=[0,1,0,0,1,0,1,0])

# OJ Case 2
test("OJ Case2 M=2",
     N=8, lights=[1,1,1,0,1,1,1,1], M=2,
     expected=[0,0,0,0,0,1,1,0])

# 中间步骤 M=1
test("中间步骤 M=1",
     N=8, lights=[1,1,1,0,1,1,1,1], M=1,
     expected=[1,0,1,0,1,0,0,1])

# M=0 不变
test("M=0 不变",
     N=8, lights=[1,1,1,0,1,1,1,1], M=0,
     expected=[1,1,1,0,1,1,1,1])

# 全0
test("全0状态 M=5",
     N=8, lights=[0,0,0,0,0,0,0,0], M=5,
     expected=[0,0,0,0,0,0,0,0])

# 全1 M=1
test("全1状态 M=1",
     N=8, lights=[1,1,1,1,1,1,1,1], M=1,
     expected=[1,0,0,0,0,0,0,1])

# 大 M 环检测（用暴力结果交叉验证）
brute = [1,1,1,0,1,1,1,1]
for _ in range(1_000_000):
    n = len(brute)
    brute = [(brute[i-1] if i > 0 else 0) ^ (brute[i+1] if i < n-1 else 0)
             for i in range(n)]
test("大M环检测 M=1000000",
     N=8, lights=[1,1,1,0,1,1,1,1], M=1_000_000,
     expected=brute)

# 单灯
test("单灯 M=10",
     N=1, lights=[1], M=10,
     expected=[0])
