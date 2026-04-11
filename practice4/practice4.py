import os
import csv
import json

if os.path.exists('students.csv'):
    print("File exists")
else:
    print("File doesn't exist")

if os.path.exists('output/'):
    print("Folder exists")
else:
    print("Folder doesn't exist")
    os.makedirs('output')
print()
df = open('students.csv', encoding='utf-8')
reader = csv.DictReader(df)
students = list(reader)

print(f'Total students: {len(students)}')

print('First 5 rows of students:')
print('-'*30)
for row in students[:5]:
    print(row)
print('-'*30)

top10 = sorted(students, key=lambda x: float(x['final_exam_score']), reverse=True)[:10]
print("-" * 30)
print("Top 10 Students by Exam Score")
print("-" * 30)
k = []
for i in range(len(top10)):
    s = top10[i]
    k.append(f"{i + 1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {float(s['final_exam_score'])} | GPA: {s['GPA']}")
    print(k[i])

print("-" * 30)

result = {"analysis": "Top 10 Students by Exam Score", "total_students": len(students), "top_10": top10}

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)
