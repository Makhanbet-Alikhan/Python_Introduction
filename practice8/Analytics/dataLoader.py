import csv

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