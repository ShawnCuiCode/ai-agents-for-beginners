"""
SJF test harness - verify logic before submitting
"""
import heapq


def sjf(req, dur):
    """Non-preemptive SJF: returns average waiting time."""
    tasks = list(zip(req, dur))  # [(request_time, duration), ...]
    n = len(tasks)
    if n == 0:
        return 0.0

    current_time = tasks[0][0]  # start at first task arrival
    total_waiting = 0
    heap = []  # min-heap: (duration, request_time)
    i = 0

    while i < n or heap:
        # Push all tasks that have arrived by current_time
        while i < n and tasks[i][0] <= current_time:
            heapq.heappush(heap, (tasks[i][1], tasks[i][0]))
            i += 1

        if not heap:
            # Queue empty - jump to next task arrival
            current_time = tasks[i][0]
            continue

        # Pick shortest job; tie-break: earliest request time
        duration, req_time = heapq.heappop(heap)
        total_waiting += current_time - req_time
        current_time += duration

    return total_waiting / n


# ---- Tests ----

# Test 1: classic SJF textbook example
# Tasks: (req=0,dur=6),(req=0,dur=8),(req=0,dur=7),(req=0,dur=3)
# All arrive at t=0; SJF order: dur=3,6,7,8
# Start times: 0,3,9,16  Waiting: 0,3,9,16  avg=7.0
req1 = [0, 0, 0, 0]
dur1 = [6, 8, 7, 3]
result1 = sjf(req1, dur1)
assert abs(result1 - 7.0) < 0.01, f"Test1 failed: {result1}"
print(f"Test 1 passed: {result1:.2f}")

# Test 2: tasks arrive at different times
# (req=0,dur=8),(req=1,dur=4),(req=2,dur=9),(req=3,dur=5)
# t=0: only task0 available -> run dur=8. current=8
# t=8: tasks 1,2,3 all arrived. heap:[(4,1),(5,3),(9,2)]
#       pick (4,1). wait=8-1=7. current=12
# t=12: heap[(5,3),(9,2)]. pick(5,3). wait=12-3=9. current=17
# t=17: heap[(9,2)]. pick(9,2). wait=17-2=15. current=26
# waiting: 0+7+9+15=31. avg=7.75
req2 = [0, 1, 2, 3]
dur2 = [8, 4, 9, 5]
result2 = sjf(req2, dur2)
assert abs(result2 - 7.75) < 0.01, f"Test2 failed: {result2}"
print(f"Test 2 passed: {result2:.2f}")

# Test 3: single task
req3 = [5]
dur3 = [3]
result3 = sjf(req3, dur3)
assert abs(result3 - 0.0) < 0.01, f"Test3 failed: {result3}"
print(f"Test 3 passed: {result3:.2f}")

# Test 4: tasks arrive one-by-one, never overlap
# (0,5),(6,3),(10,4)  each starts right after prev finishes
# t=0: run(0,5). wait=0. current=5
# t=5: only task1 not yet(req=6). jump to 6.
# t=6: run(6,3). wait=0. current=9
# t=9: run(10,4)? req=10, jump to 10.
# t=10: run(10,4). wait=0. current=14
# avg=0.0
req4 = [0, 6, 10]
dur4 = [5, 3, 4]
result4 = sjf(req4, dur4)
assert abs(result4 - 0.0) < 0.01, f"Test4 failed: {result4}"
print(f"Test 4 passed: {result4:.2f}")

print("\nAll tests passed!")
