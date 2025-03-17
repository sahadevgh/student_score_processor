# student_score_processor

## Overview
This Python program reads student scores from a CSV file (`students_scores.csv`), calculates the average score for each student, and determines the highest and lowest-scoring students. The processed results are saved in a text file (`processed_scores.txt`).

### **Key Features**
- Reads student records from a CSV file.
- Calculates the average score for each student.
- Identifies the highest and lowest-scoring students.
- Handles missing or incorrect data gracefully.
- Saves processed results in a structured text file.

---

## **Technologies Used**
- **Python**: Core programming language.
- **CSV Module**: For reading structured student data.
- **Built-in Functions**: `sum()`, `len()`, `max()`, `min()` for calculations.
- **File Handling**: Reads from and writes to files.

---

## **Program Structure**
### **1. `calculate_average(scores: list) -> float`**
Computes the average of a list of numerical scores.

#### **Usage**
```python
scores = [85, 90, 78]
avg = calculate_average(scores)
print(avg)  # Output: 84.33
```

### **2. `find_highest_lowest(students_data: list) -> tuple`**
Finds the student with the highest and lowest average scores.

#### **Usage**
```python
students = [("Alice", 92.5), ("Bob", 76.3), ("Charlie", 88.9)]
highest, lowest = find_highest_lowest(students)
print(highest, lowest)  # Output: ('Alice', 92.5), ('Bob', 76.3)
```

### **3. `process_student_scores(input_file: str, output_file: str)`**
Reads scores from `students_scores.csv`, processes data, and writes the results to `processed_scores.txt`.

#### **Usage**
```python
process_student_scores("students_scores.csv", "processed_scores.txt")
```

---

## **Installation & Setup**
### **Prerequisites**
- **Python 3.x** installed

### **1. Clone the Repository (if applicable)**
```bash
git clone <repository_url>
cd student_score_processor
```

### **2. Create and Activate a Virtual Environment (Recommended)**
```bash
python3 -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate    # Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt  # If a requirements file exists
```

*Note: This script relies only on Python’s built-in modules, so no external dependencies are required.*

---

## **CSV File Format (`students_scores.csv`)**
Ensure the file follows this structure:
```
ID,Name,Math,Science,English
1,Michael White,56,78,38
2,Daniel Young,89,75,61
3,Emily Davis,66,72,67
4,Sarah Green,80,79,70
5,Isabella Allen,72,65,57
6,Alice Brown,99,96,93
```

### **How the CSV is Processed**
- The **ID column is ignored** during calculations.
- The **Name column is used for identifying students**.
- All other columns are **converted to float** for calculation.

---

## **Running the Program**
### **1. Ensure the CSV file is in the same directory**
```bash
ls students_scores.csv  # Check if the file exists
```

### **2. Run the Python Script**
```bash
python student_score_processor.py
```

### **3. View Processed Results**
The output is saved in `processed_scores.txt`.
```bash
cat processed_scores.txt  # View results
```

---

## **Expected Output (`processed_scores.txt`)**
```
Student Name | Average Score
----------------------------
Michael White: 57.33
Daniel Young: 75.00
Emily Davis: 68.33
Sarah Green: 76.33
Isabella Allen: 64.67
Alice Brown: 96.00

Highest Scoring Student:
Alice Brown - 96.00

Lowest Scoring Student:
Michael White - 57.33
```

---

## **Error Handling**
✔ Skips invalid rows automatically and prints a warning.
✔ Ensures **only numeric columns** are processed.
✔ Handles **empty or malformed files** gracefully.

---

## **Troubleshooting**
| Issue | Solution |
|--------|----------|
| `FileNotFoundError` | Ensure `students_scores.csv` exists in the same directory. |
| `ValueError: could not convert string to float` | Check if the file format is correct (No missing/misplaced data). |
| `PermissionError` | Ensure Python has write access to the output file. |

---

## **License**
This project is open-source and available for personal and educational use.

---

## **Author**
**Sahabia Yakubu**  
📧 **Email**: yakubukarim12@gmail.com  
🐙 **GitHub**: [sahadevgh](https://github.com/sahadevgh)  
🐦 **Twitter/X**: @sahadevgh

---

🚀 *Happy Coding!*

