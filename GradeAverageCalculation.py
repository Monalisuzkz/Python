while True:
    print("---------------------")
    prelim=input("Prelim Grade")
    midterm=input("Midterm Grade")
    prefinal=input("Prefinal Grade")
    final=input("Final Grade")
    print("-----------------------")

    ave=(int(prelim)+int(midterm)+int(prefinal)+int(final))/4
    print("Average :",ave)


    if(ave<75):
        rem="You Failed!"
    elif(ave>=76 and ave<=79.9):
        rem="Conditional"
    elif(ave>=80 and ave<=85.9):
        rem="Conditional Grade!"
    elif(ave>=86 and ave<=89.9):
        rem="Good"
    elif(ave>=90 and ave<=95.9):
        rem="Very Good!"
    elif(ave>=96 and ave<=100.0):
        rem="Perfect!"
    else:
        rem="Invalid Grade"

    print("Remark :",rem)

    cont = input('Do you still want to do another calculation? (yes/no): ')
    if cont.lower() != 'yes':
        break