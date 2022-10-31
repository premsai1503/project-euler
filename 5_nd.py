def gcd_steins(a: int, b: int):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a & 1 and b & 1:
        return gcd_steins(max(a, b) % min(a, b), min(a, b))
    elif not (a & 1) and not (b & 1):
        return gcd_steins(a >> 1, b >> 1) << 1
    elif not (a & 1):
        return gcd_steins(a >> 1, b)
    return gcd_steins(a, b >> 1)

def gcd_euclid(a: int, b: int):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd_euclid(b % a, a)


def gcd_array(arr: list):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return gcd_steins(arr[0], arr[1])
    return gcd_steins(gcd_array(arr[:len(arr)//2]), gcd_array(arr[len(arr)//2:]))

def pdt_array(arr: list):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] * arr[1]
    return pdt_array(arr[:len(arr)//2]) * pdt_array(arr[len(arr)//2:])

def lcm_array(arr: list):
    return pdt_array(arr) / gcd_array(arr)

print(pdt_array(list(range(1, 4))))
print(lcm_array(list(range(1, 11))))