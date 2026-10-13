# Student Performance Analytics System

A beginner-friendly Python data-analysis project using **Python, Pandas, and NumPy**.

## Features

- Loads `students.csv` using Pandas.
- Calculates each student's total and average marks.
- Assigns grades and pass/fail results.
- Shows class average, highest and lowest averages, and pass/fail counts.
- Calculates subject-wise averages and identifies the best and lowest-performing subjects.
- Displays the **top five student performances**, including subject marks, total, average, grade, and result.
- Checks required columns, missing values, marks, and attendance.
- Saves calculated results to `student_performance_results.csv`.\n- Saves the top five students' full performance details to `top_five_students.csv`.

## Technologies

- Python 3
- Pandas
- NumPy

## Dataset

The sample dataset contains 20 records with `Student_ID`, `Name`, `Department`, marks in Python, Mathematics and Statistics, and `Attendance`. Marks and attendance are on a scale of 0 to 100.

## Grading rule

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–<90 | A |
| 70–<80 | B |
| 60–<70 | C |
| 40–<60 | D |
| Below 40 | F |

## Pass/fail rule

A student passes only if they score at least 40 in all three subjects. Attendance is displayed but does not affect pass/fail in this version.

## Setup and run

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The program prints the student results, class summary, subject-wise analysis, and detailed top-five performance table. It also creates `student_performance_results.csv` and `top_five_students.csv`.

## Files

- `main.py` — main program and reusable functions.
- `students.csv` — sample dataset.
- `Project_Documentation.md` — project documentation.
- `requirements.txt` — required libraries.\n- `student_performance_results.csv` — complete calculated results generated when the program runs.\n- `top_five_students.csv` — the top five students' performance details generated when the program runs.

## GitHub submission

Upload the code, dataset, README, requirements, and documentation to a GitHub repository. Verify the program runs, then submit the repository URL using your course provider's Google Form.
