def sum_even_numbers(start, end):
    even_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_sum += num
    return even_sum

result = sum_even_numbers(1, 20)
print("Sum of even numbers between 1 and 20:", result)
