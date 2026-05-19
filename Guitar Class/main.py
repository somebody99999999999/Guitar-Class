class Guitar:
    def __init__(self, strings, tuner ):
        self.strings = strings
        self.tuner = tuner

    def __str__(self):
        return f"{self.strings} is"