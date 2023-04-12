

class UniversityPerson:
    
    def __init__(self, lname, fname, age):
        self.Lastname = lname
        self.Firstname = fname
        self.Age = age

    def __lt__(self, other):
        # TODO: Compare `self` with `other` in this order:
        # - lname
        # - fname
        # - age
        
        # HINT: Comparison here should take into consideration
        #       the "default" order.
        two_words_self = self.Lastname.split()
        two_words_other = other.Lastname.split()
        
        if len(two_words_self) > 1 and len(two_words_other) > 1 and two_words_self[0] == two_words_other[0]:
            # if have the same first word, but different word counts. less word count is first.
            if len(two_words_self) < len(two_words_other):
                return True
            elif len(two_words_self) > len(two_words_other): 
                return False
            
            # if have the same word count, sort by whichever is alphabetically first
            for self_word, other_word in zip(two_words_self, two_words_other):
                if self_word < other_word:
                    return True

        # if they have the same lastname, check first name
        if self.Lastname < other.Lastname:
            return True
        if self.Lastname == other.Lastname:
            if self.Firstname == other.Firstname:
                if self.Age < other.Age:
                    return True
                return False
            if self.Firstname < other.Firstname:
                return True
        return False

    @property
    def fname(self):
        # TODO: Return capitalized first name
        return ' '.join([n.capitalize for n in self.Firstname.split()])
    
    @property
    def lname(self):
        # TODO: Return capitalized last name
        return ' '.join([n.capitalize for n in self.Lastname.split()])

    def __str__(self):
        # TODO: Return UniversityPerson as a string in the specified
        #       output format
        return self.Lastname+", "+self.Firstname+"; "+self.Age

def main():
    testcases = int(input())

    for t in range(testcases):
        n_names, sort_order = input().split(' ')
        n_names = int(n_names)
        UPersons = list()
        for n in range(n_names):
            lname, fname, age = [x.strip() for x in input().split(';')]
            temp = UniversityPerson(lname, fname, age)
            UPersons.append(temp)
            # TODO: Create a UniversityPerson object with the previous information
            #       and save that object somewhere.
        
        # TODO: Sort the records
        if sort_order == "-":
            for i in range(len(UPersons)):
                for j in range(i+1, len(UPersons)):
                    if UPersons[i] < UPersons[j]:
                        UPersons[i], UPersons[j] = UPersons[j], UPersons[i]
                        
        elif sort_order == "+":
            for i in range(len(UPersons)):
                for j in range(i+1, len(UPersons)):
                    if UPersons[i] > UPersons[j]:
                        UPersons[i], UPersons[j] = UPersons[j], UPersons[i]

        # TODO: Print each person here
        print(f'Case #{t + 1}:')
        for person in UPersons:
            print(person)

if __name__ == '__main__':
    main()