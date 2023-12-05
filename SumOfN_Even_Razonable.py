def sum_of_even(n):
    if n < 0:
        return None
    even_integers = [2 * i for i in range(1, n + 1)]
    sum_of_even_integers = sum(even_integers)

    return even_integers, sum_of_even_integers

while True:
    try:
        number = int(input("Enter a value of N:"))

        if number == 0:
            print(f"You've entered a {number} integer. Please try other integer.")
        elif number < 0:
            print(f"You've entered a negative integer: {number}. Please try another integer.")

        else:
            result_of_sum = sum_of_even(number)

            if result_of_sum is not None:
                even_integers, sum_of_even = result_of_sum

                if number > 1:
                    print(f"{'+'.join(map(str, even_integers))}={sum_of_even}")
                else:
                    print(f"{even_integers[0]}={sum_of_even}")

    except ValueError:
        print("Invalid Input. Please enter a valid integer.")
        break
