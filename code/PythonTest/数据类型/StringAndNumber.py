#rock_band = "Al Carl Mike Brian"
#(rhyth,, lead, vocals, bass) = rock_band.split() #
'''
highest_score = 0
result_f = open("results.txt")
for line in result_f:
    (name,score) = line.split()
    if score.isalpha() == True:
        print(score,"is not string.")
    else:
        if float(score) > highest_score:
            highest_score = float(score)
result_f.close()
print("The highest score was: %f" %highest_score)
#print(highest_score)
'''
'''
a = '9.12'
if a.isdigit() == True:
    print(a)
'''
highest_score = 0
second_highest = 0
third_highest = 0
result_f = open("results.txt")
for line in result_f:
    (name,score) = line.split()
    if score.isalpha() == True:
        print(score,"is not string.")
    else:
        if float(score) > highest_score:
            third_highest = second_highest
            second_highest = highest_score
            highest_score = float(score)
        elif float(score) > second_highest:
            third_highest = second_highest
            second_highest = float(score)
        elif float(score) > third_highest:
            third_highest = float(score)
        else:
            None
result_f.close()
float("+inf")   #正无穷
float("-inf")   #负无穷
print("The highest score was: %f" %highest_score)
print("The second score was:  %f" %second_highest)
print("The third score was:   %f" %third_highest)