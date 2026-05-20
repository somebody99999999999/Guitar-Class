class Guitar:
    def __init__(self, guitar_type, strings, tuner):
        self.guitar_type = guitar_type
        self.strings = strings
        self.tuner = tuner

    def __str__(self):
        return f"{self.guitar_type} guitar with {self.strings} strings using a {self.tuner} tuner"
    
    def playGuitar(self):
        print("Your now playing the guitar")

    def tuningGuitar(self):
        print("Your now tuning the guitar")

    def play(self):
        print("")

guitar_type = input("What type of guitar are you using ")
strings = input("How many strings does it have ")
tuner = input("What type of tuner are you using ")

g1 = Guitar(guitar_type, strings, tuner)

print(g1)

g1.play()