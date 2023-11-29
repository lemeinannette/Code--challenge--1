def exactly_two_positive(a, b, c):
   
    count_positive = 0
    if a > 0:
        count_positive += 1
    if b > 0:
        count_positive += 1
    if c > 0:
        count_positive += 1
    
   
    return count_positive == 2

# Examples:
print(exactly_two_positive(2, 4, -3))  # Output: True
print(exactly_two_positive(-4, 6, 8))  # Output: True
print(exactly_two_positive(4, -6, 9))  # Output: True
print(exactly_two_positive(-4, 6, 0))  # Output: False
print(exactly_two_positive(4, 6, 10))  # Output: False
print(exactly_two_positive(-14, -3, -4))  # Output: False
