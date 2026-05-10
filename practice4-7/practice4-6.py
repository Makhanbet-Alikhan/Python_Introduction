import os
import csv
import json

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


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            with open(self.filename) as f:
                self.students = list(csv.DictReader(f))
        except FileNotFoundError:
            print("File doesn't exist")

    def preview(self, n=5):
        for i in range(n):
            s = self.students[i]
            print(f"Student {s['student_id']}: {s['age'], s['gender'], s['country'], s['GPA']}")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w") as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except FileNotFoundError:
            print("File doesn't exist")

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self, n=10):
        sorted_students = sorted(self.students,key=lambda x: float(x["GPA"]),reverse=True)[:n]
        top_students = []
        for s in sorted_students:
            top_students.append({"student_id": s["student_id"], "GPA": s["GPA"]})
        self.result = {
            "total_students": len(self.students),
            "top_n": n,
            "top_students": top_students
        }

    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top Students, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = [float(s["GPA"]) for s in self.students]
        self.result = {
            "total_students": len(gpas),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": sum(1 for g in gpas if g > 3.5)
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"

class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")

fm = FileManager("students.csv")
if not fm.check_files():
    exit(0)
fm.create_output_folder()

dl = DataLoader("students.csv")
dl.load()
dl.preview()

print("-" * 30)
print("Running all analysers:")
print("-" * 30)

analysers = [TopStudentsAnalyser(dl.students), GpaAnalyser(dl.students)]

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()