class Guitar:
    def __init__(self, strings, tuner):
        self.strings = strings
        self.tuner = tuner
    def PlayGuitar(self):
        print("Your now playing the guitar")

    def tuningGuitar(self):
        print("Your now tuning the guitar")

    def __str__(self):
        return f"Guitar with {self.strings} strings uses a {self.tuner} tuner"

g = Guitar(3, "normal")

print(g)
