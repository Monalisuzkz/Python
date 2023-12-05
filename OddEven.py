"""
SumOfEven = 0
SumOfOdd = 0

i = 0
for i in range(10):
    num = int(input("Enter Number: "))

    if num % 2 == 0:
         SumOfEven += num

    else:
         SumOfOdd += num

print("Even Numbers: ", SumOfEven)
print("Odd Numbers: ", SumOfOdd) 
"""

Biggest = -1
Smallest = 0

i = 0
for i in range(10):
    num = int(input("Enter Number: "))
        
    if num > Biggest:
         num = Biggest

    else:
         num = Smallest

print("Biggest Number: ", Biggest)
print("Smallest Number: ", Smallest)    


