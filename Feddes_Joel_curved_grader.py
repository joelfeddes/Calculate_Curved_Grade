#Joel Feddes
#This program calculates what a student's grade will be AFTER a class-curve is applied.
    

def print_title(): #Prints welcome
    print("*" * 35)
    print("CURVED GRADE CALCULATOR".center(35))
    print("*" * 35)

def initial_heading(): #Prints initial heading
    print()
    print("*Course Final Grades Report*".center(35))
    print("%-10s%15s%10s" % ("Name","Average","Grade"))
    print("-" * 35)

def summary_heading(): #Prints summary heading
    print()
    print("Summary".center(20))
    print("-" * 20)

#main
    
from statistics import * #import the stats library we created

print_title() #print title of program

fname = input("Enter the name of your full file name (include the extension): ").strip() #ask user for the file to use

initial_heading() #print the initial heading

fvar = open(fname,"r") #Read the file

names = [] #append each student name to list
avg_score = [] #append each students personal avgerage to this list
grades = [] #append each student's grade to this list.

for line in fvar: 
    line = line.strip()
    scores = line.split("\t") #Bust information into a tab-deliminted list.
    if scores[0][0] == "S": #Find lines that have test data in them. Since each line with test scores has a "Student_x" in front, use the lines that start with S.
        student = scores[0] #Identify student name
        test_1 = int(scores[1]) #Identify first test score and turn it into an int
        test_2 = int(scores[2]) #2nd test score
        test_3 = int(scores[3]) #3rd
        test_4 = int(scores[4]) #4th
        test_5 = int(scores[5]) #5th
        length = len(scores[1:]) #calculate the length (need it for the student avg score)
        student_score = test_1 + test_2 + test_3 + test_4 + test_5 #sum the student's scores
        student_avg  = student_score / length #Calculate the average for each individual student.
        avg_score.append(student_avg) #append each individual avg to the avg_score list.
        names.append(student) #append each student's name to the names list.
        
mean = find_mean(avg_score) #calculate the class mean
median = find_median(avg_score) #calculate the class median
maximum = find_max(avg_score) #calculate the max average score in the class
minimum = find_min(avg_score) #calculate the min average score in the class (loser!)
variance = find_variance(avg_score) #Find the variance between avg scores, use to find standard_dev.
standard_deviation = find_stdev(avg_score) #Find standard_deviation

for score in avg_score: #Figure out which doofus got what grade.
    if score >= (mean + 1.25 * standard_deviation):   #If the individuals score is greater than or equal to the
                                                      #mean (74.03 in this case) + 1.25 * stddev (5.39)
                                                      #than they get an A.
        grade = "A"
    elif score >= (mean + 0.25 * standard_deviation): #If these conditions are met, than the grade results in a B
        grade = "B"
    elif score >= (mean - 1 * standard_deviation):    #If these conditions are met, than the grade results in a C
        grade = "C"
    elif score >= (mean - 2 * standard_deviation):    #If these conditions are met, than the grade results in a D
        grade = "D"
    else: #They failed.
        grade = "F"
    grades.append(grade) #Append each grade to my grades list.

mode = find_mode(grades)

num_of_a = grades.count("A") #Count number of A's from grades list
num_of_b = grades.count("B") #Count number of B's from grades list
num_of_c = grades.count("C") #Count number of C's from grades list
num_of_d = grades.count("D") #Count number of D's from grades list
num_of_f = grades.count("F") #Count number of F's from grades list

for i in range(len(names)): #Prints the name, average score, and grade for each individual student.
    print("%-15s%10.2f%10s" % (names[i],avg_score[i],grades[i]))
    
summary_heading() #display summary heading

#below, print my hard earned results!
print("%-10s%10.2f" % ("Mean", mean))
print("%-10s%10.2f" % ("Median", median))
print("%-10s%10.2f" % ("StDev", standard_deviation))
print("%-10s%10.2f" % ("Min", minimum))
print("%-10s%10.2f" % ("Max", maximum))
print("%-10s%2s" % ("Most common grade:", mode[0]))
print("%-10s%10d" % ("# of A's", num_of_a))
print("%-10s%10d" % ("# of B's", num_of_b))
print("%-10s%10d" % ("# of C's", num_of_c))
print("%-10s%10d" % ("# of D's", num_of_d))
print("%-10s%10d" % ("# of F's", num_of_f))

print("Thank you for using this program.")
fvar.close()

