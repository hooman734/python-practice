"""
Question18 - Simple CGPA calculator

Write a program to read a CSV file of student IDs, names, and scores, and for each student, output their name, ID, average score and CGPA in the following format:

<name> (<id>): <average-score> <cgpa>
"""


import csv 
import numbers 


def simple_cgpa_calc():
    def cgpa(array_of_scores):
        total: numbers = 0

        try:
            for score in array_of_scores:
                total += float(score)

            average = total / len(array_of_scores)

            if average <= 1.7:
                return average, "C-"
            elif average <= 2.0:
                return average, "C"
            elif average <= 2.3:
                return average, "C+"
            elif average <= 2.7:
                return average, "B-"
            elif average <= 3.0:
                return average, "B"
            elif average <= 3.3:
                return average, "B+"
            elif average <= 3.7:
                return average, "A-"
            elif average <= 3.9:
                return average, "A"
            else:
                return average, "A+"
        except:
            return "average-Score", " CGPA"

    with open('sample.csv', newline='') as csvfile:
        score_list = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in score_list:
            each_student = row[0].split(",")
            gpa_info = cgpa(each_student[2:])
            print(f"{each_student[1]} ({each_student[0]}): {gpa_info[0]} {gpa_info[1]}")


if __name__ == '__main__':
    simple_cgpa_calc()

