 Student Result Management System

 Project Overview

The Student Result Management System is a Python-based application designed to manage student academic records in a simple and organized way.

The system allows users to:

* Add student records
* View student records
* Search for a student
* Update student information
* Delete student records
* Enter subject-wise marks
* Calculate total marks
* Calculate percentage
* Generate grades
* Check PASS/FAIL status
* Generate a result report
* Store student data permanently in a JSON file

The project is divided into three main modules:

1. **Module 1 – Student Data & Record Management**
2. **Module 2 – Result Calculation & Grading**
3. **Module 3 – Report Generation & Final Output**

---

# 📂 Modules

## Module 1: Student Data & Record Management

Module 1 is used to manage student records in a simple and organized way.

It allows the user to perform five basic operations:

* **ADD** – Add a new student
* **VIEW** – View all student records
* **SEARCH** – Search a student using Roll Number
* **UPDATE** – Update student information or marks
* **DELETE** – Delete a student record

### Student Information

The system stores:

* Roll Number
* Student Name
* Course
* Semester
* Subject-wise Marks

### Basic Logic

```text
Student Data
     ↓
Add / View / Search / Update / Delete
     ↓
Save Data
     ↓
students.json
     ↓
Retrieve Data Later
```

### Python Concepts Used

* Classes and Objects
* Variables
* Dictionaries
* Functions
* Conditional Statements
* Loops
* File Handling
* JSON

The student data is stored in **`students.json`**, so records remain available even after closing the program.

---

# Module 2: Result Calculation & Grading

Module 2 is responsible for calculating the student's academic result from the stored subject-wise marks.

The system automatically calculates:

* Total Marks
* Percentage
* Grade
* PASS/FAIL Status

### Result Calculation

The total marks are calculated by adding all subject marks.

```text
Total Marks = Sum of all Subject Marks
```

Percentage is calculated based on the total marks and number of subjects.

```text
Percentage =
(Total Marks / Maximum Marks) × 100
```

### Grade System

| Percentage | Grade |
| ---------- | ----- |
| 90 – 100   | A+    |
| 80 – 89    | A     |
| 70 – 79    | B     |
| 60 – 69    | C     |
| 50 – 59    | D     |
| 40 – 49    | E     |
| Below 40   | F     |

### PASS/FAIL Logic

The system checks every subject mark.

```text
If any subject mark < 40
        ↓
      FAIL

Otherwise
        ↓
      PASS
```

### Example

```text
Python   = 85
DBMS     = 78
Maths    = 92

Total = 255
Percentage = 85%

Grade = A
Status = PASS
```

The calculated result is displayed when the user searches for a student.

---

# Module 3: Report Generation & Final Output

Module 3 is used to generate a detailed result report for a student.

The user enters the student's **Roll Number**, and the system creates a separate text file containing the student's result.

The generated report contains:

* Roll Number
* Student Name
* Course
* Semester
* Subject-wise Marks
* Total Marks
* Percentage
* Grade
* Result Status

### Report Flow

```text
Enter Roll Number
        ↓
Find Student Record
        ↓
Calculate Result
        ↓
Generate Report
        ↓
result_<roll_no>.txt
        ↓
Display Final Result
```

For example:

```text
result_CD25083.txt
```

The generated report is saved as a **`.txt` file** and is also displayed on the screen.

---

# 🔄 Complete Project Workflow

The complete system works in the following way:

```text
                 START
                   ↓
          Load students.json
                   ↓
             Display Menu
                   ↓
        Select Operation
                   ↓
    ┌──────┬──────┬──────┬──────┬──────┬─────────┐
    ↓      ↓      ↓      ↓      ↓      ↓
   ADD    VIEW   SEARCH UPDATE DELETE REPORT
    │      │      │      │      │      │
    └──────┴──────┴──────┴──────┴──────┴─────────┘
                   ↓
             Save Data
                   ↓
          Continue Program?
             ↙          ↘
           YES           NO
            ↓             ↓
          Menu           END
```

---

# 🛠️ Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Object-Oriented Programming**

---

# 🧠 Main Python Concepts

The project demonstrates the following Python concepts:

### 1. Classes and Objects

The `Student` class is used to represent student information.

### 2. Dictionaries

Student records and subject-wise marks are stored using dictionaries.

### 3. Functions

Different functions are used for operations such as:

* Adding students
* Viewing students
* Searching students
* Updating students
* Deleting students
* Generating reports

### 4. Conditional Statements

`if`, `elif`, and `else` are used for:

* Grade calculation
* PASS/FAIL checking
* Menu selection
* Input validation

### 5. Loops

Loops are used to:

* Display menu repeatedly
* Enter multiple subjects
* Display multiple student records

### 6. JSON File Handling

JSON is used to permanently store student data.

---

# 📁 Project Structure

```text
Student-Result-Management-System/
│
├── student_result_management.py
├── students.json
├── result_<roll_no>.txt
└── README.md
```

### Files

**`student_result_management.py`**
Main Python program containing all three modules.

**`students.json`**
Stores student records permanently.

**`result_<roll_no>.txt`**
Generated result report for an individual student.

**`README.md`**
Project documentation.

---

# 📋 Main Menu

When the program starts, the following menu is displayed:

```text
===== Student Result Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Generate Result Report
7. Exit
```

---

# 🔐 Input Validation

The system also performs basic validation.

Examples:

* Duplicate Roll Number is not allowed.
* Number of subjects must be greater than 0.
* Subject name cannot be empty.
* Marks must be between **0 and 100**.
* Student must exist before searching, updating, deleting, or generating a report.
* Invalid numeric input is handled using exception handling.

---

# 💾 Data Storage

Student information is stored in:

```text
students.json
```

The program loads the JSON file when it starts and saves updated data after operations such as:

* Add
* Update
* Delete

This allows student records to remain available for future use.

---

# 📊 Result Report Example

```text
===== STUDENT RESULT REPORT =====

Roll No: CD25083
Name: Student Name
Course: Data Science
Semester: 3

Subject-wise Marks:
Python: 85
DBMS: 78
Mathematics: 92

Total Marks: 255
Percentage: 85.00%
Grade: A
Result: PASS
```

---

# ▶️ How to Run

### Step 1: Open the project folder

```bash
cd Student-Result-Management-System
```

### Step 2: Run the Python file

```bash
python student_result_management.py
```

### Step 3: Select an option from the menu

```text
1 → Add Student
2 → View Students
3 → Search Student
4 → Update Student
5 → Delete Student
6 → Generate Result Report
7 → Exit
```

---

# ✅ Advantages

* Simple and easy to use
* Reduces manual record management
* Provides organized student data
* Automatically calculates results
* Provides automatic grading
* Checks PASS/FAIL status
* Stores data permanently using JSON
* Generates individual result reports
* Demonstrates practical Python programming concepts

---

# 🎯 Project Objective

The main objective of this project is to develop a simple Python-based system for managing student academic records.

It combines **student record management, result calculation, grading, and report generation** into one application.

The project also provides practical implementation of **Python OOP, functions, dictionaries, conditional statements, loops, file handling, and JSON storage**.

---

# 🔗 Module Connection

The three modules work together:

```text
MODULE 1
Student Data & Record Management
            ↓
MODULE 2
Result Calculation & Grading
            ↓
MODULE 3
Report Generation & Final Output
```

### Overall Logic

```text
Student Information
        ↓
Manage Student Records
        ↓
Enter Subject Marks
        ↓
Calculate Total & Percentage
        ↓
Calculate Grade
        ↓
Check PASS/FAIL
        ↓
Generate Result Report
        ↓
Final Output
```

---

# 🚀 Future Improvements

The current project can be improved in the future by adding:

* Graphical User Interface (GUI)
* Database connectivity
* Login and authentication
* More advanced report formats
* Student performance charts
* Attendance management
* Automatic backup
* Web-based interface

These are **future improvements** and are not part of the current implementation.

---

# 🏁 Conclusion

The Student Result Management System is a practical Python project that manages student records and academic results in an organized way.

The project covers three important areas:
* **Module 1:** Managing student data
* **Module 2:** Calculating results and grades
* **Module 3:** Generating the final result report

The project demonstrates how Python programming concepts can be combined to solve a real-world student record and result management problem.
