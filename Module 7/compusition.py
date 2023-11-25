class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size
    
class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity

#computer has a cpu
#computer has a ram
#computer has a hardrive
class Computer:
    def __init__(self,cores,size,capacity) -> None:
        self.cpu_cores = CPU(cores)
        self.ram_size = RAM(size)
        self.hardrive = HardDrive(capacity)


mac = Computer(8,8,1)