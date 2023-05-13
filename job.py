class Job:
    def __init__(self, arrival_time: int, burst_time: int, id: int):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.wait_time = 0
        self.turn_around = 0
        self.id = id
        self.id2 = id
        self.quantum_timer = 0

    def get_arrival_time(self) -> int:
        return self.arrival_time

    def get_turnaround_time(self) -> int:
        return self.turn_around

    def get_burst_time(self) -> int:
        return self.burst_time

    def get_remaining_time(self) -> int:
        return self.remaining_time

    def get_id(self) -> int:
        return self.id

    def get_wait_time(self) -> int:
        return self.wait_time

    def execute(self) -> int:
        self.remaining_time = self.remaining_time - 1
        self.turn_around = self.turn_around + 1

    def wait(self):
        self.wait_time = self.wait_time + 1
        self.turn_around = self.turn_around + 1

    def get_quantum_timer(self):
        return self.quantum_timer

    def increment_quantum(self):
        self.quantum_timer = self.quantum_timer + 1

    def clear_quantum(self):
        self.quantum_timer = 0

    def set_id(self, id):
        self.id = id