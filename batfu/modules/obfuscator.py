from batfu.modules.generator import Generator


class Obfuscator:
    def __init__(self, min_length, max_length):
        self.generator = Generator(min_length, max_length)

        self.set = self.generator.get_random_var()
        self.space = self.generator.get_random_var()
        self.equals = self.generator.get_random_var()

        self.dictionary = {}
        self.known_vars = []

    def init_dict(self, content):
        self.dictionary = self.generator.generate_dict(content)

    def create_var(self, key, value):
        if key not in self.known_vars:
            self.known_vars.append(key)
            return f"%{self.set}%%{self.space}%{key}%{self.equals}%{value}"
        return None
