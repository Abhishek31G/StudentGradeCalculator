def get_average(scores):
    total = sum(scores)
    no_of_subjects = len(scores)
    average_result = total/no_of_subjects
    return average_result
def get_grade(average):
    if average >= 91 and average <=100:
        grade = "You are passed with grade A1"
    if average >= 81 and average <91:
        grade = "You are passed with grade A2"
    if average >= 71 and average <81:
        grade = "You are passed with grade B1"
    if average >= 61 and average <71:
        grade = "You are passed with grade B2"
    if average >= 51 and average <61:
        grade = "You are passed with grade C1"
    if average >= 41 and average <51:
        grade = "You are passed with grade C2"
    if average >= 35 and average <41:
        grade = "You are passed with grade D"
    if average >= 21 and average <35:
        grade = "You are failed with grade E1"
    if average >= 0 and average <21:
        grade = "You are failed with grade E2"

    return grade
scores_total_list = []
names_of_subjects = ["English", "Hindi", "Marathi", "Social Science", "Maths", "Science"]
for i in names_of_subjects:
    marks_of_subjects = float(input(f"Enter {i} marks: "))
    scores_total_list.append(marks_of_subjects)

subject_scores = {names_of_subjects[i]: scores_total_list[i] for i in range(len(names_of_subjects))}
#subject_scores = {"English":scores_total_list[0], "Hindi":scores_total_list[1], "Marathi":scores_total_list[2], "Social Science":scores_total_list[3], "Maths":scores_total_list[4], "Science":scores_total_list[5]}
scores_total_list.sort()
scores_total_list.pop(0)
best_five_scores = scores_total_list
average = get_average(best_five_scores)
total_marks = sum(best_five_scores)
grade_obtained = get_grade(average)

print("Note: Total marks and percentage are calculated on \"Best of 5\" rule.")
print("Marks obtained in each Subject:",subject_scores)
print("Total Marks(Out of 500):", total_marks)
print("Percentage:", average)
print("Grade Obtained(Pass/Fail):", grade_obtained)
