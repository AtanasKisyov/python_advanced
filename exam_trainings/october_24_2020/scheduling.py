jobs = [int(x) for x in input().split(", ")]
wanted = jobs[int(input())]
cycles = 0

while True:
    current_job = min(jobs)
    current_job_index = jobs.index(current_job)
    if jobs.count(current_job) > 1:
        cycles += current_job
        jobs.pop(current_job_index)
        continue
    if current_job == wanted:
        cycles += current_job
        break
    cycles += current_job
    jobs.pop(current_job_index)

print(cycles)
