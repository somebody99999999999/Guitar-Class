class Guitar:
    def __init__(self, strings, tuner):
        self.strings = strings
        self.tuner = tuner

    def __str__(self):
        return f"Guitar with {self.strings} strings uses a {self.tuner} tuner"

g = Guitar(3, "normal")

print(g)
