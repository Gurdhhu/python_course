class fibonacci_sequence:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.val_old = 1
        self.val_new = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.ret_val = self.val_old + self.val_new
            self.val_old = self.val_new
            self.val_new = self.ret_val
            self.count += 1
            return self.ret_val
        else:
            raise(StopIteration)
