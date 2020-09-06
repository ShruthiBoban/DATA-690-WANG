#Prompts a user to enter 10 integers. If the user enters anything other than integers, remind her that only integers are allowed and let her retry. Don't allow the user to enter more than 10 or less than 10 integers. Display the 10 integers back to the user at the end.
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
#https://stackoverflow.com/questions/44124059/python-program-prompts-user-to-enter-number-until-they-enter-0-then-program-add
#https://gist.github.com/AmruthPillai/77026640f8be299fd3d61e740034c1fa

NumList = []
count = 0
while True:
    if count == 10:
        break;
    x = (input(f"Please enter an integer({count + 1} of 10): "))
    print("you entered: ", x)
    try:
        x = int(x)
        NumList.append(x)
        count = count+1
    except:
        print("you have entered a non-integer. Please try again")
    
print(NumList)

#Minimum and Maximum
#https://stackoverflow.com/questions/15148491/min-and-max-of-a-list-in-python-without-using-min-max-function
def minmax1 (NumList):
    minimum = maximum = NumList[0]
    for i in NumList[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return print("minimum number = ",minimum, "and maximum number = ",maximum)
minmax1(NumList)

#Range
#https://www.tutorialgateway.org/python-program-to-sort-list-in-ascending-order/
#https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/range-statistics/

for i in range (10):
    for j in range(i + 1, 10):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
print("Element After Sorting List in Ascending Order is : ", NumList)
Range = int(NumList[9]) - int(NumList[0])
print("Range is ",Range)

#Mean
#https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
#https://www.tutorialspoint.com/converting-all-strings-in-list-to-integers-in-python#
res = [int(i) for i in NumList]
n = len(res) 
get_sum = sum((res))
mean = get_sum / n 
print("Mean is ",mean)

#Variance
#https://stackoverflow.com/questions/35583302/how-can-i-calculate-the-variance-of-a-list-in-python
#https://stackoverflow.com/questions/40930713/how-to-calculate-variance-and-std-without-import
var = sum((i-(mean)) ** 2 for i in res)/len(res)
print("the variance is ", var)

#Standard Deviation
#https://stackoverflow.com/questions/40930713/how-to-calculate-variance-and-std-without-import
standard = float(var) ** (1/2)
print("the standard deviation is ", standard)

