def calculate_letter_grade(average):
    """Determines the letter grade based on the calculated average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_allowance(basic_income, allowance, deductions, tax_rate):
    """
    Calculates gross income, tax deduction amount, and final net earnings.
    Applies percentage-based tax logic.
    """
    gross_income = basic_income + allowance
    tax_amount = gross_income * (tax_rate / 100)
    net_earnings = gross_income - deductions - tax_amount
    return gross_income, tax_amount, net_earnings


def add_student_record(students_dict):
    """
    Inputs student marks, calculates metrics, allowance breakdown,
    and updates the main student dictionary.
    """
    print("\n--- Enter Student Details ---")
    name = input("Enter Student Name: ").strip()
    
    # Repetition structure to collect marks
    marks = []
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(1, num_subjects + 1):
        mark = float(input(f"Enter mark for Subject {i}: "))
        marks.append(mark)
    
    # Metric calculations
    average_mark = sum(marks) / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)
    grade = calculate_letter_grade(average_mark)

    # Allowance & Tax Input
    print("\n--- Enter Financial Details ---")
    basic_income = float(input("Enter Basic Income/Stipend ($): "))
    allowance = float(input("Enter Additional Allowance ($): "))
    deductions = float(input("Enter Direct Deductions ($): "))
    tax_rate = float(input("Enter Tax Percentage (%): "))

    gross, tax, net = calculate_allowance(basic_income, allowance, deductions, tax_rate)

    # Storing in Dictionary
    students_dict[name] = {
        "marks": marks,
        "average": average_mark,
        "max_mark": highest_mark,
        "min_mark": lowest_mark,
        "grade": grade,
        "financials": {
            "gross": gross,
            "tax_deducted": tax,
            "net_earnings": net
        }
    }
    print(f"\nSuccessfully added record for {name}!")


def display_all_records(students_dict):
    """Displays formatted student records and financial summaries."""
    if not students_dict:
        print("\nNo student records available.")
        return

    print("\n========================================================")
    print("              STUDENT & FINANCIAL SUMMARY              ")
    print("========================================================")
    for name, data in students_dict.items():
        print(f"\nStudent Name   : {name}")
        print(f"Marks Recorded : {data['marks']}")
        print(f"Average Score  : {data['average']:.2f}")
        print(f"Highest / Lowest: {data['max_mark']} / {data['min_mark']}")
        print(f"Letter Grade   : {data['grade']}")
        print("  --- Financial Breakdown ---")
        print(f"  Gross Income : ${data['financials']['gross']:.2f}")
        print(f"  Tax Deducted : ${data['financials']['tax_deducted']:.2f}")
        print(f"  Net Earnings : ${data['financials']['net_earnings']:.2f}")
        print("-" * 56)


def display_top_performer(students_dict):
    """Identifies and displays the student with the highest average mark."""
    if not students_dict:
        print("\nNo student records available.")
        return

    top_student = max(students_dict, key=lambda s: students_dict[s]["average"])
    top_data = students_dict[top_student]

    print("\n========================================================")
    print("                  TOP PERFORMER AWARD                   ")
    print("========================================================")
    print(f"Name         : {top_student}")
    print(f"Top Average  : {top_data['average']:.2f}")
    print(f"Grade        : {top_data['grade']}")
    print("========================================================")


def main():
    """Main program flow using selection and repetition control structures."""
    students = {}

    while True:
        print("\n=================================")
        print("   STUDENT & ALLOWANCE SYSTEM    ")
        print("=================================")
        print("1. Add Student Record")
        print("2. Display All Student Records")
        print("3. View Top Performer")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_student_record(students)
        elif choice == "2":
            display_all_records(students)
        elif choice == "3":
            display_top_performer(students)
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()
