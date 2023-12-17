class Adder:
    def __init__(self, value=0):
        self.value = value

    def __call__(self, x=None):
        if x is not None:
            return Adder(int(self.value + x))
        else:
            return int(self.value)

    def __repr__(self):
        return str(int(self.value))

# How to use class in python
add = Adder()

result1 = add(1)
print(result1)       