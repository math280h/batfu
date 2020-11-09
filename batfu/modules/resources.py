class Resource:
    def __init__(self, input_file, output_file):
        self.location = input_file
        self.output = output_file

    def load(self):
        with open(self.location, 'r') as scr:
            content = scr.readlines()
        return content

    def store(self, data):
        with open(self.output, 'w+') as scr:
            scr.writelines(data)
        return True
