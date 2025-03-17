import csv

# Function to calculate average score
def calculate_average(scores: list) -> float:
    return sum(scores) / len(scores) if scores else 0.0

# Function to find the highest and lowest scoring students
def find_highest_lowest(students_data: list) -> tuple:
    if not students_data:
        return None, None
    
    highest_student = max(students_data, key=lambda x: x[1])  # Max based on avg score
    lowest_student = min(students_data, key=lambda x: x[1])   # Min based on avg score
    
    return highest_student, lowest_student

# Read student scores from CSV and process the data
def process_student_scores(input_file: str, output_file: str):
    student_averages = []

    with open(input_file, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header

        for row in csv_reader:
            if len(row) < 4:  # Ensure at least ID, Name, and 1 score exist
                print(f"Skipping invalid row: {row}")
                continue

            student_id = row[0]  # Read ID but do not use it in calculations
            name = row[1]  # Read student name
            try:
                scores = list(map(float, row[2:]))  # Convert only score columns to float
                avg_score = calculate_average(scores)
                student_averages.append((name, avg_score))
            except ValueError:
                print(f"Skipping row with invalid data: {row}")  # Log invalid data
                continue

    # Find highest and lowest-scoring students
    highest, lowest = find_highest_lowest(student_averages)

    # Write results to processed_scores.txt
    with open(output_file, mode='w') as file:
        file.write("Student Name | Average Score\n")
        file.write("----------------------------\n")
        for name, avg in student_averages:
            file.write(f"{name}: {avg:.2f}\n")

        file.write("\nHighest Scoring Student:\n")
        file.write(f"{highest[0]} - {highest[1]:.2f}\n" if highest else "No valid data.\n")

        file.write("\nLowest Scoring Student:\n")
        file.write(f"{lowest[0]} - {lowest[1]:.2f}\n" if lowest else "No valid data.\n")

# Run the program
input_csv = "./students_scores.csv"
output_txt = "processed_scores.txt"
process_student_scores(input_csv, output_txt)

print(f"Processing complete. Results saved in {output_txt}.")
