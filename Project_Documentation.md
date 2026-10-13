# Project Documentation: Student Performance Analytics System

## 1. Project Title

**Student Performance Analytics System**

Student Name: Rizwan Ustad
Student ID: 3GN23AI041 
Department: Artificial Intelligence and Machine Learning  
Course: Python with AI

## 2. Objective

Analyze student marks and attendance using Python, Pandas, and NumPy. The program calculates totals, averages, grades, pass/fail results, class statistics, subject-wise averages, and top performers.

## 3. Technologies Used

- **Python:** Program logic, conditions, and reusable functions.
- **Pandas:** Reads and analyzes student records in a DataFrame.
- **NumPy:** Supports numerical calculations and rounding averages.
- **CSV:** Stores the sample dataset.

## 4. Dataset Description

`students.csv` contains 20 sample records with `Student_ID`, `Name`, `Department`, `Python`, `Mathematics`, `Statistics`, and `Attendance`. Marks and attendance range from 0 to 100.

## 5. Implementation

1. **Load data:** Pandas reads `students.csv`.
2. **Validate data:** Checks required columns, missing values, marks, and attendance.
3. **Calculate performance:** A reusable function calculates total and average marks.
4. **Assign grades:** Conditional statements assign grades based on averages.
5. **Determine pass/fail:** A function checks whether every subject mark is at least 40.
6. **Analyze class performance:** Calculates class average, highest and lowest student averages, pass/fail counts, and subject-wise averages.
7. **Find top performers:** Sorts students by average in descending order and displays full details for the top five, including subject marks, total, average, grade, and result.
8. **Save top-five details:** Exports the top five students' full performance details to `top_five_students.csv`.\n9. **Save results:** Exports all processed student data to `student_performance_results.csv`.

## 6. Key Features

- CSV loading using Pandas.
- Total and average calculations.
- Grade assignment and pass/fail classification.
- Class and subject-wise performance summary.
- Best and lowest-performing subject identification.
- Detailed top-five student performance table.
- Input-data validation and CSV export of all results and the top five student performances.

## 7. Output / Screenshots

After running `python main.py`, capture screenshots of the student results table, class summary, subject-wise averages, and the full top-five student performance table. You may also capture `student_performance_results.csv` and `top_five_students.csv`.

## 8. Final Outcome

The program generates student-level and class-level performance statistics and displays a detailed top-five student performance table. It demonstrates a practical use of Python, NumPy, and Pandas without requiring machine learning or charts.

## 9. Challenges & Learning

Update these points after testing:
- Learned to load CSV data into a Pandas DataFrame.
- Practiced functions, conditions, and loops.
- Learned to calculate totals, averages, and subject-wise statistics.
- Learned the importance of validating data.
- Learned to sort records to identify top-performing students.

Add any actual errors faced and how you solved them.

## 10. GitHub Repository

**Repository Name: "student-performance-analytics"

**Repository URL: https://github.com/rustad470-u/student-performance-analytics.git

The repository contains the Python source code, student dataset, generated CSV results, project documentation, requirements file, and screenshots.

The project was tested successfully before submission.