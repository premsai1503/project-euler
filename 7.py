from itertools import count, islice

def nth_prime(k: int):
    primes = [2, 3]

    def is_prime(num: int):
        return all(num % i != 0 for i in primes)

    def generate_primes():
        yield 2
        yield 3
        for n in count(5, 2):
            if (n - 1) % 6 == 0 or (n + 1) % 6 == 0:
                if is_prime(n):
                    primes.append(n)
                    yield n

    return next(islice(generate_primes(), k - 1, None))

print(nth_prime(10001))