class Fraction:
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    def __str__(self):
        return f"{self.num}/{self.deno}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.num * other.deno + self.deno * other.num
        deno = self.deno * other.deno
        return Fraction(num, deno)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.num * other.deno - self.deno * other.num
        deno = self.deno * other.deno
        return Fraction(num, deno)

    def inverse(self):
        return Fraction(self.deno, self.num)

    def __float__(self):
        return float(self.num) / float(self.deno)

# Test case:

f1 = Fraction(3, 5)
f2 = Fraction(6, 7)
print(f1)
print(f1 + f2)
print(f1.inverse())
print(float(f1))