Number = int(input("Enter value for n:"))
NumbersFoundSoFar = 0
CurrentNumber = 1
while NumbersFoundSoFar != Number:
    SumOfDigits = 0
    NumAsString = str(CurrentNumber)
    for count in range(0, len(NumAsString)):
        SumOfDigits = SumOfDigits + int(NumAsString[count])
    if CurrentNumber % SumOfDigits == 0:
        NumbersFoundSoFar += 1
        if NumbersFoundSoFar == Number:
            print(f"Harshad number for the number provided is {CurrentNumber}")
    CurrentNumber += 1


"""
FlagA = TRUE
FlagB = FALSE
FlagC = TRUE

Q3 -
 NOT FlagB AND FlagC --> TRUE
 NOT (FlagB OR FlagC) --> FALSE
 (FlagA AND FlagB) OR FlagC --> TRUE 
"""
