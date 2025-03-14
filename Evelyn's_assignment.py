# Evelyn Idogbe
# Id: A00050322

def accept_input():
    student_id = input("Student's ID or Name: ")
    coursework1 = float(input("Coursework 1 score: "))
    coursework2 = float(input("Coursework 2 score: "))
    coursework3 = float(input("Coursework 3 score: "))
    test_score = float(input("Test score: "))
    
    return student_id, coursework1, coursework2, coursework3, test_score
    #This code block accepts inputs from students 

def calculate_total_score(coursework1, coursework2, coursework3, test_score):
    overall_score = (coursework1 + coursework2 + coursework3 + test_score) / 4
    return overall_score
    # In this block the overall score for each student is calculated

def student_category (total_score):
    if total_score >= 70:
        return "First Class"
    elif total_score >= 60:
        return "Second Class Upper"
    elif total_score >= 50:
        return "Second Class Lower"
    elif total_score >= 40:
        return "Third Class"
    else:
        return "You Failed"
    # This block categorizes students

def main():
    students = []
    
    while True:
        student_data = accept_input()
        student_id, coursework1, coursework2, coursework3, test_score = student_data
        
        total_score = calculate_total_score(coursework1, coursework2, coursework3, test_score)
        category = student_category(total_score)
        # This block is the programes main loop
        
        students.append((student_id, int(total_score), category))
        break
         # This block stores data the student has entered 
            
    
    print("\nStudent Results:")
    for student in students:
        student_id, score, category = student
        print(f"Student's ID/Name: {student_id}, Score: {score} - {category}")
        # This block prints out the result

if __name__ == "__main__":
    main()
