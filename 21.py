# Create a class FileManager with methods to read from and write to a file.
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except Exception as e:
            return f"error : {e}"

    def write_file(self, content, mode="w"):
        try:
            with open(self.file_path, mode) as file:
                file.write(content)
                return "Write Successful"
        except Exception as e:
            return f"Error: {e}"