# Create a class Report that generates a report from data in a file. Provide methods to handle exceptions if the file does not exist or cannot be read.
class Report:
    def __init__(self, file_path):
        self.file_path = file_path

    def generate(self):
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
        except IOError:
            return "Error reading file."
