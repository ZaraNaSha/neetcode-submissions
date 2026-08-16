class MinStack:

    def __init__(self):
        self.s = []
        self.minv = 2^31 - 1

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.minv = val
        else:
            self.s.append(val-self.minv)
            if val < self.minv:
                self.minv = val
        print(self.s)

    def pop(self) -> None:
        if not self.s:
            return 
        pop = self.s.pop()
        if pop < 0:
            self.minv = self.minv - pop  

    def top(self) -> int:
        if not self.s:
            return 
        pop = self.s[-1]
        if pop>0:
            return pop + self.minv  
        else:
            return self.minv

    def getMin(self) -> int:
        return self.minv
        
