import csv
import random
import datetime

# 30 Student Names
names = [
    "Arjun Kumar", "Bhavana Reddy", "Charan Teja", "Divya Sri", "Eshwar Prasad",
    "Fathima Bi", "Ganesh Naik", "Harika P", "Ibrahim Khan", "Jyothi Lakshmi",
    "Karthik Raja", "Latha Mangam", "Manoj Kumar", "Navya Sree", "Omer Bin",
    "Pranathi K", "Rahul Verma", "Sai Thrinadh", "Tejaswini M", "Uday Kiran",
    "Vamsi Krishna", "Vennela R", "William Carey", "Yashwanth G", "Zoya Khan",
    "Ananya Rao", "Bharath C", "Deepak Reddy", "Indu Priya", "Kalyan Ram"
]

subjects = ["telugu", "english", "science", "math", "social"]
filename = "student_marksheet.csv"
start_date = datetime.date.today()

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing headers exactly as requested
    writer.writerow(["id", "name", "date"] + subjects)
    
    # Loop for 30 days
    for day_offset in range(30):
        current_date = start_date + datetime.timedelta(days=day_offset)
        date_str = current_date.strftime("%Y-%m-%d")
        
        # Loop for 30 students
        for i, name in enumerate(names, start=1):
            student_id = i  # Storing ID as an integer
            
            # Generates random marks between 40 and 100
            scores = [random.randint(40, 100) for _ in subjects]
            
            writer.writerow([student_id, name, date_str] + scores)

print(f"File '{filename}' generated successfully with 900 rows.")