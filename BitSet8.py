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

    def list(self):
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

    # Symmetric Difference
    def __sub__(self, other):
        u = self.bitset ^ (self.bitset & other.bitset)
        return BitSet8(u)

    # Invert U \ A
    def __invert__(self):
        return BitSet8(self.bitset ^ 255)

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


x = BitSet8([3, 4,5])
y = BitSet8([3, 4])
