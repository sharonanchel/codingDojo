import random

def grade(reps):
    print "Scores and Grades"
    for i in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(20)


# def scores_grades():
#   for i in range (0,10):
#     score = random.random()*40 + 60
#     if score < 70:
#       grade = "D"
#     elif score < 80:
#       grade = "C"
#     elif score < 90:
#       grade = "B"
#     else:
#       grade = "A"
#
#     print "Score: {}; Your grade is {}".format(score, grade)
#
# scores_grades()
