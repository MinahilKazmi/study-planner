from datetime import date, timedelta

def create_study_plan():
    print("================================")
    print("      AI STUDY PLANNER")
    print("================================\n")
    
    name = input("Enter your name: ")
    
    print("\nEnter your subjects (type 'done' when finished):")
    subjects = []
    while True:
        subject = input("Subject: ")
        if subject.lower() == "done":
            break
        subjects.append(subject)
    
    exam_date_input = input("\nEnter exam date (YYYY-MM-DD): ")
    year, month, day = exam_date_input.split("-")
    exam_date = date(int(year), int(month), int(day))
    
    today = date.today()
    days_left = (exam_date - today).days
    
    if days_left <= 0:
        print("Exam date must be in the future!")
        return
    
    print(f"\n================================")
    print(f"Study Plan for {name}")
    print(f"Days until exam: {days_left}")
    print(f"Subjects: {', '.join(subjects)}")
    print(f"================================\n")
    
    days_per_subject = days_left // len(subjects)
    current_date = today
    
    for subject in subjects:
        print(f"📚 {subject.upper()}")
        print(f"   Study from: {current_date} to {current_date + timedelta(days=days_per_subject)}")
        print(f"   Days allocated: {days_per_subject}")
        print(f"   Recommended: {days_per_subject * 2} hours total\n")
        current_date += timedelta(days=days_per_subject)
    
    print("================================")
    print("DAILY SCHEDULE RECOMMENDATION")
    print("================================")
    print("Morning   (8-10 AM):  First subject")
    print("Afternoon (2-4 PM):   Second subject") 
    print("Evening   (7-9 PM):   Review notes")
    print("\n✅ Good luck with your exams!")

create_study_plan()