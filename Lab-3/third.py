# given a list of numbers, find the sum and average

def sum_and_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return sum, average