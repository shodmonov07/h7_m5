class Fibonacci:
    def __init__(self, max_value: int):
        self.max_value = max_value

    def __iter__(self):
        self.current = 0
        self.next_value = 1
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        value_to_return = self.current
        self.current, self.next_value = self.next_value, self.current + self.next_value
        return value_to_return

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for number in self:
                f.write(f"{number}\n")


fib = Fibonacci(77)

for num in fib:
    print(num)

fib.save_to_file('fibonacci.txt')
