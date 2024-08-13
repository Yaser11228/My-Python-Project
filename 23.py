# Create a class Config that reads configuration settings from a file and provides methods to access these settings.
class Config:
    def __init__(self, config_file):
        self.config = {}
        with open(config_file, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                self.config[key] = value

    def get(self, key):
        return self.config.get(key, None)



f1 = Config()