# Author   : XIANG CUI
# Problem  : Shortest Job First (SJF) Average Waiting Time
# Approach : Greedy simulation - pick shortest available job each step
# Time     : O(N^2) - linear scan per task
# Space    : O(N) - store all tasks

def sjf_avg_waiting(req, dur):
    """
    Non-preemptive SJF scheduling.
    Returns average waiting time across all tasks.
    Tie-break: smallest duration first, then earliest request time.
    """
    tasks = list(zip(req, dur))  # pair each task: (request_time, duration)
    n = len(tasks)
    done = [False] * n           # track completed tasks
    current_time = tasks[0][0]  # start clock at first task arrival
    total_waiting = 0

    for _ in range(n):
        # Collect all tasks that have arrived and not yet executed
        available = [
            (tasks[j][1], tasks[j][0], j)
            for j in range(n)
            if not done[j] and tasks[j][0] <= current_time
        ]

        if not available:
            # CPU idle - jump to next task arrival
            current_time = min(tasks[j][0] for j in range(n) if not done[j])
            available = [
                (tasks[j][1], tasks[j][0], j)
                for j in range(n)
                if not done[j] and tasks[j][0] <= current_time
            ]

        # Pick shortest job, tie-break by earliest request time
        available.sort()
        duration, req_time, idx = available[0]

        total_waiting += current_time - req_time  # waiting = start - arrival
        current_time += duration                  # advance clock
        done[idx] = True

    return total_waiting / n


# Read input
req_size = int(input())
req = list(map(int, input().split()))
dur_size = int(input())
dur = list(map(int, input().split()))

# Print average waiting time rounded to 2 decimal places
print("{:.2f}".format(sjf_avg_waiting(req, dur)))
