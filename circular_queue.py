class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.a = [None] * size
        self.head = 0 
        self.tail = 0
        self.sum = self.counter = 0
    def __repr__(self):
        return f'{self.a}'

    def enqueue(self, n):
        self.sum += n
        self.tail = self.tail % len(self.a)
        self.a[self.tail] = n
        self.tail += 1
        self.counter += 1

        if self.count() == len(self.a):
            arr = [None] * (len(self.a)*2-len(self.a))
            self.a = [*self.a[self.head:]] + [*self.a[0:self.head]] + arr
            self.head = 0
            self.tail = self.count()
            print(f'Resized to {len(self.a)} elements')

    def dequeue(self):
        val = self.a[self.head%len(self.a)]
        self.counter -= 1
        self.sum -= val
        self.a[self.head%len(self.a)] = None
        self.head = (self.head + 1) % len(self.a)
        return val

    def count(self):
        return self.counter

    def avg(self):
        return self.sum/self.count()

def sample2():
    q = CircularQueue(20)
    for x in range(10):
        q.enqueue(x)
    for x in range(5):
        q.dequeue()
    for x in range(100):
        q.enqueue(x)
    print('count =', q.count())
    print('average =', q.avg())
    print(q.dequeue())

def sample3():
    q = CircularQueue(3)
    q.enqueue(1)
    for x in range(3):
        q.enqueue(x)
        q.dequeue()
    print('avg is', q.avg())
    print(q.dequeue())

def sample4():
    q = CircularQueue(1)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())

def sample5():
    q = CircularQueue(3)
    for x in range(3):
        q.enqueue(x)
    print('count is', q.count())
    sum = 0
    while q.count() > 0:
        sum += q.dequeue()
    print('sum is', sum)

def sample6():
    q = CircularQueue(1)
    for x in range(5):
        q.enqueue(x)
        q.enqueue(2 * x)
        q.dequeue()
    print('count is', q.count())
    print('avg is', q.avg())