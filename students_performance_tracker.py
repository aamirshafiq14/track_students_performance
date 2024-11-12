# Step 1: Defining the Student class
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def calculate_average(self):
        # Calculating the average score of the student
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self):
        # Checking if the student is passing all subjects (assuming passing score is 40)
        return all(score >= 40 for score in self.scores)

# Step 2: Defining the PerformanceTracker class
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        # Adding a new student to the tracker
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        # Calculating the average score for the entire class
        total_sum = sum(student.calculate_average() for student in self.students.values())
        return total_sum / len(self.students)

    def display_student_performance(self):
        # Printing each student's performance
        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name}, Average Score: {average:.2f}, Status: {status}")

# Step 3: Handling user input
def input_student_data():
    tracker = PerformanceTracker()
    
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        scores = []
        for subject in ['Math', 'Science', 'English']:
            while True:
                try:
                    score = int(input(f"Enter score for {subject}: "))
                    scores.append(score)
                    break
                except ValueError:
                    print("Please enter a valid integer for the score.")
        
        tracker.add_student(name, scores)
    
    return tracker

# Main program
if __name__ == "__main__":
    tracker = input_student_data()
    print("\nStudent Performance:")
    tracker.display_student_performance()
    print(f"\nClass Average Score: {tracker.calculate_class_average():.2f}")
