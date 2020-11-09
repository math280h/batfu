import random
import string


class Generator:
    def __init__(self, min_length, max_length):
        self.used = []

        self.min = min_length
        self.max = max_length

    def generate_dict(self, content):
        d = {}
        for line in content:
            for char in line:
                d[char] = self.get_random_var()
        return d

    def get_random_var(self):
        while True:
            rand = "".join([random.choice(string.ascii_letters) for _ in range(random.randrange(self.min, self.max))])
            if rand not in self.used:
                self.used.append(rand)
                return rand
