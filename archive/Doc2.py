import sys

class Student():
    def __init__(self, subjects, units, funds):
        self.discount = 0
        tuitionfee = 1500 * units 
        if(tuitionfee > funds):
            print("Student not enlisted. Not enough funds.")
            self.subjects = []
            self.units = 0
            self.funds = funds
        else:
            self.subjects = subjects
            self.units = units
            self.funds = funds - tuitionfee
      
    def enlist(self, subject, units):
        tuitionfee = (units*1500) - (units*1500*self.discount)
        if (self.funds - tuitionfee < 0):
            print("Not enough funds.")
        else:
            self.subjects.append(subject)
            self.units += units
            self.funds = self.funds - tuitionfee
      
class StudentA(Student):
    def work(self, hours):
        self.funds += (60*hours)

class STscholar(Student):
    def __init__(self, subjects, units, funds, bracket):
        discount_rate = 0
        if bracket == 'A':
            discount_rate = 0
        elif bracket == 'B':
            discount_rate = 0.33
        elif bracket == 'C':
            discount_rate = 0.60
        elif bracket == 'D':
            discount_rate = 0.80
        elif bracket == 'E':
            discount_rate = 1
        discount_tuition = units*1500*discount_rate
        super().__init__(subjects, units, funds + discount_tuition)    
        self.discount = discount_rate
        self.bracket = bracket

class SAscholar(STscholar, StudentA):
    def overtime(self, hours):
        overtime_pay = (1+float(self.discount))*60
        self.funds += hours*overtime_pay

###Do not edit code below. This is purely for checking.
def main():
    
    #initialize list of students
    mystudents=[]
    
    #enlist students of different types
    mystudents.append(Student(['Math 2', 'Physics 7', 'EEE 3', 'EEE 8'], 12, 100000))
    mystudents[0].enlist("EEE 1", 3)
    
    mystudents.append(StudentA(['Eng 3', 'Soc Sci 1', 'EEE 1', 'EEE 3', 'Philo 1', 'Math 20'], 15, 50000))
    mystudents[1].enlist("EEE 8", 1)
    mystudents[1].work(10)
    
    mystudents.append(STscholar(['Math 2', 'Physics 7', 'EEE 3', 'EEE 8'], 12, 100000,"B"))
    mystudents[2].enlist("EEE 1", 3)
    
    mystudents.append(SAscholar(['Math 2', 'Physics 7', 'EEE 3', 'EEE 8'], 12, 100000,"B"))
    mystudents[3].enlist("EEE 1", 3)
    mystudents[3].work(10)
    mystudents[3].overtime(10)
    
    # print student details    
    for i in mystudents:
        print(i.subjects)
        print(i.units)
        print(i.discount)	
        print(round(i.funds, 2), "\n")
    
    #### Remove the following 10 lines if not coding in HackerRank
    # execute additional test cases, if any
    inplist = []
    for line in sys.stdin:
        inplist.append(line.replace("\n",""))
    
    if inplist[0] == "0":
        pass
    else:
        for i in range(1, len(inplist)):
            exec(inplist[i])

if __name__ == '__main__':
    main()