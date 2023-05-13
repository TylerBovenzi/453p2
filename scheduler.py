from job import Job
class Scheduler:
    def __init__(self, filename):
        self.jobs = []
        self.jobs_pending = []
        self.jobs_completed = []
        self.run_time = 0
        self.elaboration = ""
        index = 0
        with open(filename, 'r') as f:
            for line in f:
                burst_time, arrival_time = line.strip().split()
                job = Job(int(arrival_time), int(burst_time), int(index))
                index = index + 1
                self.jobs_pending.append(job)
        self.jobs_pending = sorted(self.jobs_pending, key=lambda x: x.get_id())
        self.jobs_pending = sorted(self.jobs_pending, key=lambda x: x.get_arrival_time())
        for i in range(len(self.jobs_pending)):
            self.jobs_pending[i].set_id(i)
        #for job in self.jobs_pending:
        #    print(f"Job {job.get_id():3d} -- Arrival {job.get_arrival_time():3.2f}  Burst {job.get_burst_time():3.2f}")
        self.jobs_pending = sorted(self.jobs_pending, key=lambda x: -x.get_id())

    def print_sched(self):
        for job in self.jobs:
            print("Job arrival time:", job.get_arrival_time())
            print("Job burst time:", job.get_burst_time())

    def run(self):
        while(len(self.jobs) + len(self.jobs_pending) > 0):
            for i in range(len(self.jobs_pending)-1,-1,-1):
                job = self.jobs_pending[i]
                if job.arrival_time == self.run_time:
                    self.jobs.append(job)
                    self.jobs_pending.remove(job)

            self.run_time = self.run_time + 1

            job_scheduled = self.get_next()
            add_string = "--"
            if(len(self.jobs)>0): add_string = "P" + str(self.jobs[job_scheduled].id2)
            self.elaboration = self.elaboration + "[" + add_string + "]"

            for i in range(0, len(self.jobs)):
                job = self.jobs[i]
                if i == job_scheduled:
                    job.execute()
                else:
                    job.wait()

            if(len(self.jobs) > 0):
                job = self.jobs[job_scheduled]
                if (job.get_remaining_time() == 0):
                    self.jobs_completed.append(self.jobs[job_scheduled])
                    self.jobs.pop(job_scheduled)

    def get_next(self):
        pass


class SRTN(Scheduler):
    def __init__(self, filename):
        super().__init__(filename)

    def get_next(self):
        index = 0
        srt = -1
        for i in range(len(self.jobs)):
            if(srt < 0) or (self.jobs[i].get_remaining_time() < srt):
                index = i
                srt = self.jobs[i].get_remaining_time()
        return index

class FIFO(Scheduler):
    def __init__(self, filename):
        super().__init__(filename)

    def get_next(self):
        return 0

class RR(Scheduler):
    def __init__(self, filename, quantum):
        super().__init__(filename)
        self.max_quantum = quantum

    def get_next(self):
        if(len(self.jobs) > 0):
            if(self.jobs[0].get_quantum_timer() == self.max_quantum):
                job = self.jobs.pop(0)
                job.clear_quantum()
                self.jobs.append(job)
            self.jobs[0].increment_quantum()
        return 0

