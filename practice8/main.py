from Analytics import FileManager, DataLoader, ResultSaver, Report
from Analytics.analyser import TopStudentsAnalyser

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

analysers = [TopStudentsAnalyser(dl.students)]

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()
