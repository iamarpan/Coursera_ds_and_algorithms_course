# python3
import heapq
from collections import namedtuple



def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = []
    for index in range(n_workers):
        next_free_time.append([0,index])
    heapq.heapify(next_free_time)
    for job in jobs:
        next_worker = heapq.heappop(next_free_time)
        result.append((next_worker[1],next_worker[0]))
        next_worker[0]+=job
        heapq.heappush(next_free_time,next_worker)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0],job[1])


if __name__ == "__main__":
    main()
