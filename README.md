# 📊 Student Attendance Calculator

A simple Python project that calculates a student's attendance percentage and checks whether it meets the required attendance criteria. If attendance is insufficient, the program calculates how many consecutive classes the student must attend to reach the required percentage.

## ✨ Features

- ✅ Accepts total classes held and classes attended.
- 📈 Calculates current attendance percentage.
- 📋 Displays total classes, attended classes, and absences.
- 🎯 Checks attendance against the required percentage.
- 🧮 Calculates the number of consecutive classes needed to meet the requirement.
- ⚠️ Validates user input and handles errors.
- 🛡️ Uses `try`, `except`, `else`, and `finally` for exception handling.

## 🛠️ Technologies Used

- **Language:** Python
- **Modules:** Built-in Python functionality
- **Concepts:** Conditional statements, loops, exception handling, user input, and mathematical calculations.

## 📂 Project Structure

```text
Student-Attendance-Calculator/
│
├── attendance.py
└── README.md
```

## 🚀 How to Run

### 1. Install Python

Download and install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.

### 2. Clone the Repository

```bash
git clone https://github.com/safamariyam1902-tech/Student-Attendance-Calculator.git
```

### 3. Open the Project Folder

```bash
cd Student-Attendance-Calculator
```

### 4. Run the Program

```bash
python attendance.py
```

## 💻 Example Output

```text
Enter total classes held: 100
Enter classes attended: 65
Enter required attendance percentage: 75

--- Attendance Report ---
Total Classes: 100
Classes Attended: 65
Classes Absent: 35
Current Attendance: 65.0 %
Required Attendance: 75.0 %
Status: Attendance shortage!
You must attend the next 40 consecutive classes without absence.

Attendance report generated successfully.
Attendance checking process completed.
```

## 🧠 How It Works

The program calculates attendance using the formula:

**Attendance Percentage**

```text
(attended classes / total classes) × 100
```

If the current attendance is below the required percentage, the program uses a `while` loop to determine how many consecutive classes must be attended without any further absences.

It also checks for invalid values, such as zero or negative total classes, attended classes exceeding total classes, and invalid attendance percentages.

## 🎯 Learning Objectives

This project helps beginners practise:

- Python variables and data types
- `if-else` conditional statements
- `while` loops
- Exception handling
- Input validation
- Percentage calculations
- Generating formatted reports

## 🔮 Future Improvements

- Add a graphical user interface (GUI).
- Save attendance reports to a file.
- Support multiple students.
- Add a monthly attendance summary.
- Allow users to calculate how many classes they can miss while maintaining the required percentage.

## 👩‍💻 Author

**Safa Mariyam**

GitHub: [safamariyam1902-tech](https://github.com/safamariyam1902-tech)

## 📄 License

This project is open-source and available for learning and educational purposes. You can add an MIT License if you want to allow others to reuse and modify the code under its terms.
