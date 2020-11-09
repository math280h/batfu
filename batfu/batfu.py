from batfu.modules.resources import Resource
from batfu.modules.obfuscator import Obfuscator


class Batfu:
    def __init__(self, input_file, output_file, min_length, max_length):
        self.resource = Resource(input_file, output_file)
        self.obfuscator = Obfuscator(min_length, max_length)

    def run(self):
        print("Obfuscating...")
        script = self.resource.load()

        self.obfuscator.init_dict(script)

        prologue = [
            f"@echo off\n",
            f"set {self.obfuscator.set}=set\n",
            f"%{self.obfuscator.set}% {self.obfuscator.space}= \n",
            f"%{self.obfuscator.set}%%{self.obfuscator.space}%{self.obfuscator.equals}==\n",
        ]

        settings = []
        for line in script:
            for char in line:
                var = self.obfuscator.create_var(self.obfuscator.dictionary[char], char)
                if var is not None:
                    settings.append(var + "\n")

        obs = []
        for line in script:
            for char in line:
                obs.append(f"%{self.obfuscator.dictionary[char]}%")
            obs.append("\n")

        code = [] + prologue + settings + obs

        self.resource.store(code)
        print("Done...")
