#SumOfEvenPositiveNumbers
def sum_of_even_integers(n):
    if n > 0:
        sum = 0 
        adding_the_numbers = ""

#Iteration using the input of the user: Explanation - if the user will input above 0 then it will goes in
        for i in range(2, 2*n+1, 2):
            sum += i
            adding_the_numbers += str(i)

            # "+" is added only if the number is not the last number. 
            if i < 2*n-1:
                adding_the_numbers += " + "
        print("The user inputted:", n, "numbers." + "\n""The Sum of numbers:", adding_the_numbers, "=", sum)
   
#However if it is negative number or zero, it will display invalid input
    elif n < 0:
        print("Error! Only positive even integers")
    elif n == 0:
        print("Error! Invalid Input.")
    else:
        print("Invalid input!")
        
while True:
    n = int(input("Input a positive number: "))
    sum_of_even_integers(n)
