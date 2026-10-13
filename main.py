"""

Student Performance Analytics System
A beginner-friendly Python project using Pandas and NumPy.
"""

import pandas as pd
import numpy as np


def load_data(file_name):
    """Read student records from a CSV file."""
    students = pd.read_csv(file_name)
    return students


def calculate_performance(students):
    """Calculate total and average marks for every student."""
    subjects = ["Python", "Mathematics", "Statistics"]

    students["Total"] = students[subjects].sum(axis=1)
    students["Average"] = np.round(students[subjects].mean(axis=1), 2)

    return students


def assign_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def assign_pass_fail(row):
    """A student passes only when every subject mark is at least 40."""
    if (
        row["Python"] >= 40
        and row["Mathematics"] >= 40
        and row["Statistics"] >= 40
    ):
        return "Pass"
    else:
        return "Fail"


def add_results(students):
    """Add grade and pass/fail columns to the student table."""
    students["Grade"] = students["Average"].apply(assign_grade)
    students["Result"] = students.apply(assign_pass_fail, axis=1)
    return students


def show_class_summary(students):
    """Display overall class statistics."""
    subjects = ["Python", "Mathematics", "Statistics"]

    print("\n========== CLASS SUMMARY ==========")
    print("Number of students:", len(students))
    print("Class average:", round(students["Average"].mean(), 2))
    print("Highest student average:", students["Average"].max())
    print("Lowest student average:", students["Average"].min())
    print("Students passed:", (students["Result"] == "Pass").sum())
    print("Students failed:", (students["Result"] == "Fail").sum())

    print("\nSubject-wise average marks:")
    print(students[subjects].mean().round(2).to_string())

    best_subject = students[subjects].mean().idxmax()
    lowest_subject = students[subjects].mean().idxmin()
    print("\nBest-performing subject:", best_subject)
    print("Lowest-performing subject:", lowest_subject)


def show_top_students(students):
    """Display and save the full performance details of the top five students."""
    top_students = students.sort_values(
        by="Average", ascending=False
    ).head(5)

    top_student_columns = [
        "Student_ID", "Name", "Department", "Python", "Mathematics",
        "Statistics", "Attendance", "Total", "Average", "Grade", "Result"
    ]
    top_students = top_students[top_student_columns]

    print("\n========== TOP 5 STUDENT PERFORMANCES ==========")
    print(top_students.to_string(index=False))

    # Save the top five records to a separate CSV file.
    top_students.to_csv("top_five_students.csv", index=False)
    print("\nTop five student details saved to top_five_students.csv")


def main():
    """Run the complete student performance analysis."""
    students = load_data("students.csv")

    # Check that the expected columns are present.
    required_columns = [
        "Student_ID", "Name", "Department",
        "Python", "Mathematics", "Statistics", "Attendance"
    ]

    for column in required_columns:
        if column not in students.columns:
            print("Error: Required column is missing:", column)
            return

    # Basic checks for missing values and marks outside the valid range.
    if students[required_columns].isnull().any().any():
        print("Error: The dataset contains missing values. Please check students.csv.")
        return

    subjects = ["Python", "Mathematics", "Statistics"]
    for subject in subjects:
        if not students[subject].between(0, 100).all():
            print("Error: Marks in", subject, "must be between 0 and 100.")
            return

    if not students["Attendance"].between(0, 100).all():
        print("Error: Attendance must be between 0 and 100.")
        return

    students = calculate_performance(students)
    students = add_results(students)

    print("========== STUDENT PERFORMANCE ANALYTICS ==========")
    print("\nStudent results:")
    print(
        students[
            ["Student_ID", "Name", "Department", "Total",
             "Average", "Grade", "Result", "Attendance"]
        ].to_string(index=False)
    )

    show_class_summary(students)
    show_top_students(students)

    # Save the calculated results to a new CSV file.
    students.to_csv("student_performance_results.csv", index=False)
    print("\nDetailed results saved to student_performance_results.csv")


if __name__ == "__main__":
    main()
