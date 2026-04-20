import os
import csv
import json


def check_files():
    t = False
    if os.path.exists('students.csv'):
        print("File exists")
        t = True
    else:
        print("File doesn't exist")

    if os.path.exists('output/'):
        print("Folder exists")
    else:
        print("Folder doesn't exist")
        os.mkdir('output')
    return t

def load_data(name):
    try:
        df = open(name, encoding='utf-8')
        reader = csv.DictReader(df)
        return list(reader)
    except FileNotFoundError:
        print("File doesn't exist")
    except Exception as e:
        print("ERROR", e)

def preview_data(students, n=5):

    print(f'First {n} rows of students:')
    print('-' * 30)
    for row in students[:n]:
        print(row)
    print('-' * 30)

def get_top_students(students, n=10):
    valid_students = []

    for row in students:
        try:
            row["final_exam_score"] = float(row["final_exam_score"])
            valid_students.append(row)
        except ValueError:
            print(f"Warning: skipping row with invalid final_exam_score: {row['final_exam_score']}")
            continue

    top = sorted(valid_students, key=lambda x: x["final_exam_score"], reverse=True)[:n]
    print("-" * 30)
    print(f'Top {n} Students by Exam Score')
    print("-" * 30)
    for i in range(len(top)):
        print(top[i])
    print("-" * 30)
    return top
check_files()
students = load_data('students.csv')

print(preview_data(students))
print(get_top_students(students))
print('-'*30)
print("Lambda / Map / Filter")
print("-"*30)
print("final exam score > 95:", len(list(filter(lambda x: float(x["final_exam_score"]) >= 95, students))))
print("GPA values: ", list(map(lambda x: x["GPA"], students))[:5])
print("assignment_score > 90: ", len(list(filter(lambda x: float(x["assignment_score"]) >= 90, students))))


load_data("adw.csv")
