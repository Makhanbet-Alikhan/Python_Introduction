import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_files(self):
        t = False
        if os.path.exists(self.filename):
            print("File exists")
            t = True
        else:
            print("File doesn't exist")
        return t

    def create_output_folder(self, folder='output'):
        if not os.path.exists(folder):
            os.mkdir(folder)
        else:
            print("Folder already exists")

class DataLoader:
    def __init__(self,filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            df = open(self.filename)
            self.students = list(csv.DictReader(df))
            return self.students
        except FileNotFoundError:
            print("File doesn't exist")

    def preview(self, n = 5):
        for i in range(n):
            print(f'Student {self.students[i]['student_id']}: {self.students[i]["age"], self.students[i]["gender"], self.students[i]["country"] ,self.students[i]["GPA"]}')

class DataAnalyzer:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self, n=10):
        self.result = (sorted(self.students, key=lambda x: x["final_exam_score"], reverse=True)[:n])
        return self.result
    def print_results(self):
        for i in self.result:
            print(i)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f, indent=4)
                print("Results saved")
        except FileNotFoundError:
            print("File doesn't exist")

fm = FileManager("students.csv")

if not fm.check_files():
    print("File doesn't exist")
    exit(0)
fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analyser = DataAnalyzer(dl.students)
analyser.analyse(10)
analyser.print_results()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()

