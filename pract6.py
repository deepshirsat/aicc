# P6(employee).py
def employee_eval():
    print("Employee Evaluation System")
    score = int(input("Enter performance score (0-100): "))
    if score >= 85:
        print("Excellent Performance")
    elif score >= 60:
        print("Good Performance")
    elif score >= 40:
        print("Average Performance")
    else:
        print("Needs Improvement")
employee_eval()

# Output
# PS C:\Users\user> & C:/Users/user/anaconda3/python.exe "e:/AI/P6(emp).py"
# Employee Evaluation System
# Enter performance score (0-100): 70
# Good Performance

# P6(hospital).py
def hospital_expert():
    print("Hospital Expert System")
    symptom = input("Enter your symptom (fever/cough/headache): ").lower()
    if symptom == "fever":
        print("Possible illness: Viral Infection")
    elif symptom == "cough":
        print("Possible illness: Cold or Flu")
    elif symptom == "headache":
        print("Possible illness: Migraine or Stress")
    else:
        print("Consult a doctor for proper diagnosis")
hospital_expert()

# Output
# PS C:\Users\user> & C:/Users/user/anaconda3/python.exe "e:/AI/P6(hospital).py"
# Hospital Expert System
# Enter your symptom (fever/cough/headache): cough
# Possible illness: Cold or Flu

# P6(helpdesk).py
def helpdesk():
    print("Help Desk System")
    issue = input("Enter issue (login/password/network): ").lower()
    if issue == "login":
        print("Solution: Check username and password")
    elif issue == "password":
        print("Solution: Reset your password")
    elif issue == "network":
        print("Solution: Restart router or check connection")
    else:
        print("Please contact support")
helpdesk()

# Output
# PS C:\Users\user> & C:/Users/user/anaconda3/python.exe "e:/AI/P6(helpdesk).py"
# Help Desk System
# Enter issue (login/password/network): login
# Solution: Check username and password
