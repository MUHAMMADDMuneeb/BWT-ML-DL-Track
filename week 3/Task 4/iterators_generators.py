import random

# Countdown iterator
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current

# Fibonacci generator
def fibonacci_generator(limit):
    a = 0 
    b = 1
    while a <= limit:
        yield a
        a=b
        b =  a + b

# Random number generator
def random_number_generator(start, end, count):
    for i in range(count):
        yield random.randint(start, end)

# Demonstration
def main():
    # Demonstrate Countdown
    print("Countdown from 5:")
    for number in Countdown(5):
        print(number)

    # Demonstrate Fibonacci Generator
    print("\nFibonacci numbers up to 50:")
    for number in fibonacci_generator(50):
        print(number)

    # Demonstrate Random Number Generator
    print("\nRandom numbers between 1 and 10 (5 numbers):")
    for number in random_number_generator(1, 10, 5):
        print(number)

if __name__ == "__main__":
    main()
