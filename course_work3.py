#Student name: Evelyn Idogbe
#Student ID: A00050322

import datetime
from tabulate import tabulate

# This function gets the student's information from the user
def get_student_data():
    # Ask the user for the student ID
    student_id = input("Enter student ID (or 'end' to stop): ")
    
    # If the user types 'end', stop the process
    if student_id.lower() == "end":
        return None
    
    # Ask for the student's name
    name = input("Enter student's name: ")
    
    # Ask for the student's date of birth
    dob = input("Enter student's D.o.B (YYYY-MM-DD): ")
    
    # Keep asking for the scores until valid numbers are entered
    while True:
        try:
            # Ask for 3 coursework scores
            coursework_scores = [
                int(input(f"Coursework {i + 1} score: ")) for i in range(3)
            ]
            # Ask for the final exam score
            final_exam = int(input("Final exam score: "))
            break  # Exit loop when all scores are valid
        except ValueError:
            # If the input isn't a valid number, tell the user and ask again
            print("Invalid input! Please enter a valid integer for the scores.")
    
    # Return all the collected information
    return student_id, name, dob, coursework_scores + [final_exam]

# This function calculates the total score (average score)
def compute_total_score(scores):
    # Simply add all scores and divide by the number of scores to get the average
    return sum(scores) / len(scores)

# This function determines which grade category the student's score falls into
def determine_category(score):
    if score >= 70:
        return "First"  # Top category
    elif score >= 60:
        return "Upper-First"  # Second-highest category
    elif score >= 50:
        return "Second"  # Middle category
    else:
        return "Third"  # Lowest category

# This function rounds the score to the nearest defined category
def round_score_to_category(score):
    if score >= 72:
        return 75, "First"
    elif score >= 68:
        return 72, "Upper-First"
    elif score >= 50:
        return 68, "Second"
    else:
        return 50, "Third"

# This function calculates the student's age based on their date of birth
def calculate_age(dob):
    # Convert the date of birth into a datetime object
    birth_date = datetime.datetime.strptime(dob, "%Y-%m-%d")
    # Calculate how many years old the student is (approximate by dividing by 365 days)
    return (datetime.datetime.now() - birth_date).days // 365

# The main function that drives everything
def main():
    students = []  # A list to store all the students' information
    
    while True:
        # Get student's data from the user
        student_info = get_student_data()
        
        # If the user typed 'end', break the loop and stop collecting data
        if student_info is None:
            break
        
        # Unpack the student data
        student_id, name, dob, scores = student_info
        
        # Calculate the student's total score
        total_score = compute_total_score(scores)
        
        # Determine which grade category the student belongs to
        category = determine_category(total_score)
        
        # Calculate the student's age
        age = calculate_age(dob)
        
        # Round the score and get the corresponding rounded category
        rounded_score, rounded_category = round_score_to_category(total_score)
        
        # Save all the student's data in a dictionary
        students.append({
            "ID": student_id,
            "Name": name,
            "D.o.B": dob,
            "Age": age,
            "Score": total_score,
            "Category": category,
            "Rounded Score": rounded_score,
            "Rounded Category": rounded_category
        })
    
    # Display all the student results in a neat table
    display_results(students)
    
    # Save the results to a file for later use
    save_results_to_file(students)

# This function displays the students' results in a table format
def display_results(students):
    # Sort the students by their ID
    sorted_students = sorted(students, key=lambda x: x["ID"])
    
    # Define the table headers
    headers = ["UID", "Name", "D.o.B", "Age", "Score", "Category", "Rounded Score", "Rounded Category"]
    
    # Prepare the table rows using the students' data
    table = [[s["ID"], s["Name"], s["D.o.B"], s["Age"], round(s["Score"], 2), s["Category"], round(s["Rounded Score"], 2), s["Rounded Category"]] for s in sorted_students]
    
    # Print the formatted table to the screen
    print(tabulate(table, headers=headers))

# This function saves the results to a text file
def save_results_to_file(students):
    # Open the file in write mode
    with open("students.txt", "w") as file:
        # Write a header row to the file
        file.write("UID Name D.o.B Age Score Category Rounded Score Rounded Category\n")
        
        # Write each student's data to the file, one student per line
        for student in students:
            file.write(f"{student['ID']} {student['Name']} {student['D.o.B']} {student['Age']} {round(student['Score'], 2)} {student['Category']} {student['Rounded Score']} {student['Rounded Category']}\n")
    
    # Let the user know that the data was saved
    print("Student data saved to students.txt")

# This is the starting point of the program
if __name__ == "__main__":
    main()
