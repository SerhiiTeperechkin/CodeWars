class make_looper:
    def __init__(self, string):
        self.iteration = -1
        self.string = string
    def __call__(self):
        self.iteration += 1
        return self.string[self.iteration % len(self.string)]
