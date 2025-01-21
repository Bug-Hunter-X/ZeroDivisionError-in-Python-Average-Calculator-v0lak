def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers) #No Error in this line
print(f"The average is: {average}") 