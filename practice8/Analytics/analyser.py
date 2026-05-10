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
            top_students.append(s)
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