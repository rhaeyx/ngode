import sys

class Student():
    def __init__(self, subjects, units, funds):
        
        if(1500*units > funds):
            print("Student not enlisted. Not enough funds")
            self.subjects = []
            self.units = 0
            self.funds = funds
        else:
            self.subjects = subjects
            self.units = units
            self.funds = funds - (1500*units)
            
    def enlist(self, subject, units):
        if (self.funds - (1500 * units) < 0):
            print("Not enough funds.")
        else:
            self.subjects.append(subject)
            self.units += units
            self.funds -= (1500*units)
      
class StudentA(Student):
    def work(self, hours):
        self.funds += (60*hours)
        
###Do not edit code below. This is purely for checking.
def main():
    #create object studentA and enlist EEE 111
    studentX = Student(['Math A', 'Physics', '113', '118'], 12, 100000)
    studentX.enlist("111", 3)
    
    #create object studentB and enlist EEE 118
    studentY = StudentA(['Eng', 'Soc Sci 1', '111', '113', 'Philo 1', 'Math B'], 15, 0)
    studentY.enlist("118", 1)
    
    # print student details
    print(studentX.subjects)
    print(studentX.units)
    print(studentX.funds)	
    print(studentY.subjects)
    print(studentY.units)
    print(studentY.funds)	
    
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
    
