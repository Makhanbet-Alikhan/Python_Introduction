import os
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_files(self):
        if os.path.exists(self.filename):
            print("File exists")
            return True
        print("File doesn't exist")
        return False

    def create_output_folder(self, folder='output'):
        if not os.path.exists(folder):
            os.mkdir(folder)
        else:
            print("Folder already exists")