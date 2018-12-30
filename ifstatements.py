#Details:
 
#Create a function that accepts 3 parameters and checks for equality between any two of them.

#Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


#Extra Credit:

#Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed 
#to your function:

#6,5,"5"

#You should modify it so that it returns true instead of false.

#Hint: there's a built in Python function called "int" that will help you convert strings to Integers.


#code snippets

def threeParameters(valueOne, valueTwo, valueThree):
    if valueOne == valueTwo:
        return True
    elif valueOne == valueThree or valueTwo == valueThree:
        return True
    else:
        return False

firstValue = input("enter the first value: " );
refinedValue = int(firstValue);
secondValue = input("enter the second value: ");
refinedValueII = int(secondValue);
thirdValue = input("enter the third value: ");
refinedValueIII = int(thirdValue);

print(threeParameters(firstValue, secondValue, thirdValue));