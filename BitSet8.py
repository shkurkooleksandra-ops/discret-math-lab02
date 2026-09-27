class BitSet8:

    def __init__(self, numbers):
        if isinstance(numbers, int):
            if numbers < 0 or numbers > 255:
                raise ValueError("Invalid BitSet8 value, accepted values between 0 and 255")
            self.bitset = numbers
        elif isinstance(numbers, list):
            self.bitset = 0
            for n in numbers:
                if not isinstance(n, int):
                    raise TypeError("BitSet8 accepts only integers")
                if n < 0 or n > 8:
                    raise ValueError("BitSet8 accepts only integers between 1 and 8")
                self.bitset = self.bitset | 1 << (n - 1)

    def __str__(self):
        return f"{self.bitset:08b}"

    def set(self):
        result = []
        for n in range(0, 8):
            if (self.bitset & 1 << n) != 0:
                result.append(n + 1)
        return result

    # Union
    def __or__(self, other):
        u = self.bitset | other.bitset
        return BitSet8(u)

    # Intersection
    def __and__(self, other):
        u = self.bitset & other.bitset
        return BitSet8(u)

    # Symmetric Difference
    def __xor__(self, other):
        u = self.bitset ^ other.bitset
        return BitSet8(u)

    # Difference
    def __sub__(self, other):
        u = self.bitset ^ (self.bitset & other.bitset)
        return BitSet8(u)

    # Invert U \ A
    def __invert__(self):
        return BitSet8(self.bitset ^ 255)  #

    # Complement A \ B
    def __truediv__(self, other):
        return BitSet8((other.bitset ^ 255) & self.bitset)

    # Cartesian
    def __mul__(self, other):
        result = []
        for x in range(0, 8):
            if (self.bitset & 1 << x) != 0:
                for y in range(0, 8):
                    if (other.bitset & 1 << y) != 0:
                        result.append((x + 1, y + 1))
        return result

    def empty(self):
        return self.bitset == 0

    def __eq__(self, other):
        return self.bitset == other.bitset

    def contains(self, other):
        return self & other == other


def input_bit_set(prompt):
    t = input(prompt).split(",")
    sn = []
    for s in t:
        ss = s.strip()
        if ss.isnumeric():
            n = int(ss)
            if n < 1 or n > 8:
                raise ValueError("Invalid value, accepted values between 1 and 8")
            sn.append(n)
    return BitSet8(sn)


def print_operation(a, op, b, c):
    print(a.set(), op, b.set(), "=", c.set())
    print(a, op)
    print(b)
    print("--------")
    print(c)


a = input_bit_set("Ведіть множину A через кому: ")
b = input_bit_set("Ведіть множину B через кому: ")

print_operation(a, "\u222A", b, a | b)
print_operation(a, "\u2229", b, a & b)
print_operation(a, "\u2216", b, a - b)
print_operation(a, "\u2206", b, a ^ b)
print_operation(a, "\\", b, a / b)
print(a.set(), "*", b.set(), "=", a * b)

